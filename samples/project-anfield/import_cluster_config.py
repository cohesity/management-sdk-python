# Copyright 2020 Cohesity Inc.
#
# Python utility to import the cluster config.
# Expects config.ini to be present in the current directory.
# Usage: python import_cluster_config.py <path/to/file>

import copy
import json
import logging
import pickle
import sys
import time

from collections import defaultdict
from os import path

# Third party module import.
try:
    from cohesity_management_sdk.cohesity_client import CohesityClient
    from cohesity_management_sdk.exceptions.request_error_error_exception import (
        RequestErrorErrorException,
    )
    from cohesity_management_sdk.exceptions.api_exception import APIException
    from cohesity_management_sdk.models.application_special_parameters import (
        ApplicationSpecialParameters,
    )
    from cohesity_management_sdk.models.change_protection_job_state_param import (
        ChangeProtectionJobStateParam,
    )
    from cohesity_management_sdk.models.environment_register_protection_source_parameters_enum import (
        EnvironmentRegisterProtectionSourceParametersEnum as env_enum,
    )
    from cohesity_management_sdk.models.exclude_type_enum import ExcludeTypeEnum
    from cohesity_management_sdk.models.external_target_type_enum import (
        ExternalTargetTypeEnum,
    )
    from cohesity_management_sdk.models.external_client_subnets import (
        ExternalClientSubnets,
    )
    from cohesity_management_sdk.models.latency_thresholds import LatencyThresholds
    from cohesity_management_sdk.models.nas_mount_credential_params import (
        NasMountCredentialParams,
    )
    from cohesity_management_sdk.models.nas_protocol_enum import (
        NasProtocolEnum as nas_enum,
    )
    from cohesity_management_sdk.models.protection_policy_request import (
        ProtectionPolicyRequest,
    )
    from cohesity_management_sdk.models.register_application_servers_parameters import (
        RegisterApplicationServersParameters,
    )
    from cohesity_management_sdk.models.register_remote_cluster import (
        RegisterRemoteCluster,
    )
    from cohesity_management_sdk.models.register_protection_source_parameters import (
        RegisterProtectionSourceParameters,
    )
    from cohesity_management_sdk.models.throttling_policy_override import (
        ThrottlingPolicyOverride,
    )
    from cohesity_management_sdk.models.throttling_policy_parameters import (
        ThrottlingPolicyParameters,
    )
    from cohesity_management_sdk.models.update_protection_source_parameters import (
        UpdateProtectionSourceParameters,
    )
    from cohesity_management_sdk.models.vault import Vault
    from cohesity_management_sdk.models.view_box_pair_info import ViewBoxPairInfo
    from cohesity_management_sdk.models.vmware_type_enum import (
        VmwareTypeEnum as vmware_enum,
    )
    from cohesity_management_sdk.models.type_view_protection_source_enum import (
        TypeViewProtectionSourceEnum as view_enum,
    )
except ImportError as err:
    import sys

    print("Please install Cohesity Python SDK and try again.")
    print(
        "To install Python SDK, run 'pip install cohesity-management-sdk "
        "configparser requests'"
    )
    sys.exit()

# Custom module import
import library
from library import RestClient

try:
    import requests

    # Check for python version
    if float(sys.version[:3]) >= 3:
        import configparser as configparser
    else:
        import ConfigParser as configparser
except ImportError as err:
    print("Please install dependency packages and try again.")
    print("To run dependencies, run 'sh setup.sh'.")
    sys.exit()

from configparser import NoSectionError, NoOptionError

# Disable python warnings.
requests.packages.urllib3.disable_warnings()

logger = logging.getLogger("import_app")
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
ERROR_LIST = []
configparser = configparser.ConfigParser()
configparser.read("config.ini")

try:
    cluster_ip = configparser.get("import_cluster_config", "cluster_ip")
    username = configparser.get("import_cluster_config", "username")
    password = configparser.get("import_cluster_config", "password")
    domain = configparser.get("import_cluster_config", "domain")

    cohesity_client = CohesityClient(
        cluster_vip=cluster_ip, username=username, password=password, domain=domain
    )
    # Make a function call to validate the credentials.
    cohesity_client.principals.get_user_privileges()
    rest_obj = RestClient(cluster_ip, username, password, domain)
    global ng_cluster
    ng_cluster = library.is_ngce(rest_obj)
except APIException as err:
    print("Authentication error occurred, error details: %s" % err)
    sys.exit(1)
except Exception as err:
    print("Authentication error occurred, error details: %s" % err)
    sys.exit(1)

# Check for the flags for pause jobs and override.
try:
    override = configparser.getboolean("import_cluster_config", "override")
    pause_jobs = configparser.getboolean("import_cluster_config", "pause_jobs")
    gflag_import = configparser.getboolean("import_cluster_config", "gflag")
    access_mgmnt = configparser.getboolean(
        "export_cluster_config", "export_access_management"
    )
    sleep_time = configparser.getint("import_cluster_config", "api_pause_time")
    global_whitelists = configparser.getboolean(
        "import_cluster_config", "global_whitelists"
    )
    vlans = configparser.getboolean("import_cluster_config", "vlans")
except (NoOptionError, NoSectionError) as err:
    print("Error while fetching value from config.ini file, err_msg" " '%s'" % err)
    sys.exit()

# Read the imported cluster configurations from file.
if len(sys.argv) != 2:
    logger.error("Please specify the exported config file.")
    sys.exit(1)
else:
    try:
        cluster_dict = pickle.load(open(sys.argv[1], "rb"))
    except IOError:
        print("Import file does not exist")
        sys.exit(1)


# Variables to store resources and corresponding ids.

sd_vault_list = []
view_mapping = {}
policy_mapping = {}
source_mapping = {}
external_targets = {}
registering_sources = []
remote_cluster_mapping = {}
job_parent_id_mapping = {}
exported_remote_cluster_mapping = {}
storage_domain_mapping = {}

imported_res_dict = defaultdict(list)
export_config = cluster_dict["cluster_config"]
import_config = library.get_cluster_config(cohesity_client)
env_list = [
    env_enum.KHDFS,
    env_enum.KHIVE,
    env_enum.KGENERICNAS,
    env_enum.KISILON,
    env_enum.KPHYSICAL,
    env_enum.KPHYSICALFILES,
    env_enum.KVIEW,
    env_enum.K_VMWARE,
    env_enum.KSQL,
    env_enum.KCASSANDRA,
    env_enum.KAD,
    env_enum.KGCP,
    env_enum.KGCPNATIVE,
]


def update_whitelist_settings():
    try:
        settings = cluster_dict["whitelist_settings"]
        if settings["subnets"]:
            try:
                body = ExternalClientSubnets()
                body.client_subnets = list()
                existing_subnets = list()
                # Fetch existing subnets available in the cluster, to avoid
                # overwriting existing subnets.
                resp = cohesity_client.clusters.get_external_client_subnets()
                if resp.client_subnets:
                    # Existing subnets are not updated.
                    body.client_subnets.extend(resp.client_subnets)
                    existing_subnets = [subnet.ip for subnet in resp.client_subnets]
                for subnet in settings["subnets"]:
                    if subnet.ip not in existing_subnets:
                        body.client_subnets.append(subnet)
                if len(body.client_subnets) > 0:
                    cohesity_client.clusters.update_external_client_subnets(body)
                imported_res_dict["Subnet whitelist"] = [
                    subnet.ip for subnet in settings["subnets"]
                ]
            except Exception as e:
                ERROR_LIST.append(
                    "Error while updating subnet whitelists, err msg: %s" % e
                )

        if settings["nis_providers"]:
            NIS_PROVIDERS_API = "nis-providers"
            _, resp = rest_obj.get(NIS_PROVIDERS_API, version="v2")
            nisproviders = json.loads(resp)["nisProviders"]
            nis_servers = (
                [nis["masterServerHostname"] for nis in nisproviders]
                if nisproviders
                else []
            )
            for nis in settings["nis_providers"]:
                if nis["masterServerHostname"] in nis_servers:
                    continue
                code, resp = rest_obj.post(
                    NIS_PROVIDERS_API, version="v2", data=json.dumps(nis)
                )
                if code != 201:
                    ERROR_LIST.append(
                        "Error while adding NIS provider, err msg: %s" % resp
                    )

        if settings["netgroups"]:
            NIS_NETGROUPS_API = "nis-netgroups"
            _, resp = rest_obj.get(NIS_NETGROUPS_API, version="v2")
            groups = json.loads(resp)["nisNetgroups"]
            existing_groups = [group["name"] for group in groups] if groups else []
            for group in settings["netgroups"]:
                if group["name"] in existing_groups:
                    imported_res_dict["Nis Netgroups"].append(group["name"])
                    continue
                code, resp = rest_obj.post(
                    NIS_NETGROUPS_API, version="v2", data=json.dumps(group)
                )
                if code != 201:
                    ERROR_LIST.append(
                        "Error while adding Netgroup %s, err msg: %s"
                        % (group["name"], resp)
                    )
                imported_res_dict["Nis Netgroups"].append(group["name"])

    except Exception as err:
        ERROR_LIST.append("Error occured while importing whitelists, err msg: %s" % err)


def import_cluster_config():
    try:
        config = cluster_dict.get("cluster_config")
        existing_config = import_config
        config.name = existing_config.name
        cohesity_client.cluster.update_cluster(config)
        time.sleep(sleep_time)
    except Exception as e:
        ERROR_LIST.append("Error while importing cluster config %s" % e)


def create_vaults():
    global external_targets
    available_vaults_dict = {}
    vaults = cluster_dict.get("external_targets")
    available_targets = library.get_external_targets(cohesity_client)
    for each_vault in available_targets:
        available_vaults_dict[each_vault.name] = each_vault.id

    for vault in vaults:
        if vault.name in available_vaults_dict.keys():
            external_targets[vault.id] = available_vaults_dict[vault.name]
            imported_res_dict["External Targets"].append(vault.name)
            continue
        try:
            body = Vault()
            _construct_body(body, vault)
            if vault.config.qstar:  # Qstar target.
                password = configparser.get(vault.name, "password")
                body.config.qstar.password = password
            elif vault.config.azure:  # Azure Hot Blob target.
                storage_access_key = configparser.get(vault.name, "storage_access_key")
                body.external_target_type = ExternalTargetTypeEnum.KAZURE
                body.config.azure.storage_access_key = storage_access_key
            elif vault.config.amazon:  # Amazon s3 targets
                secret_key = configparser.get(vault.name, "secret_access_key")
                body.config.amazon.secret_access_key = secret_key
            elif vault.config.google:
                private_key = (
                    configparser.get(vault.name, "client_private_key")
                    .encode()
                    .decode("unicode-escape")
                )
                body.config.google.client_private_key = private_key
            resp = cohesity_client.vaults.create_vault(body)
            external_targets[vault.id] = resp.id
            imported_res_dict["External Targets"].append(body.name)
            time.sleep(sleep_time)
        except (APIException, RequestErrorErrorException) as e:
            ERROR_LIST.append(
                "Error Adding Target: %s, Failed with error: %s" % (vault.name, e)
            )
        except Exception as err:
            ERROR_LIST.append(
                "Please add correct config for %s in "
                "config.ini, err is %s" % (vault.name, err)
            )


def check_register_status(name=None, environment=None, sleep_count=6):
    """
    Fetch registration status after specific sleep time.
    """
    try:
        global registering_sources
        while len(registering_sources) > 0:
            sources = cohesity_client.protection_sources.list_protection_sources_registration_info(
                    ids=registering_sources).root_nodes
            for source in sources:
                status = None
                environment = source.root_node.environment
                if environment not in [env_enum.KCASSANDRA, env_enum.KHDFS, env_enum.KHIVE, env_enum.KSQL]:
                    continue
                if source.registration_info.access_info.endpoint == name:
                    status = source.registration_info.authentication_status
                # Check for the registration status, if the process is
                # pending, sleep for 10sec and poll again.
                if status in ["kScheduled", "kPending"]:
                    time.sleep(sleep_time * 5)
                else:
                    # If the status is either success/failed update list.
                    registering_sources.pop(registering_sources.index(source.root_node.id))
        time.sleep(sleep_time * 5)
    except Exception as err:
        ERROR_LIST.append(err)


def create_sources(source, environment, node):
    """ """
    try:
        update_source = False
        global registering_sources
        body = RegisterProtectionSourceParameters()
        body.environment = environment
        if environment == env_enum.KHDFS:
            source_id = source.protection_source.id
            hdfs_params = source.registration_info.hdfs_params
            name = source.registration_info.access_info.endpoint
            config_dir = configparser.get(name, "hdfs_config")
            username = configparser.get(name, "username")
            password = configparser.get(name, "password")
            if not (username or password or config_dir):
                raise Exception(
                    "Missing Credentials or HDFSConfig path in config.ini file"
                )
            body = {
                "environment": env_enum.KHDFS,
                "hdfsParams": {
                    "host": source.registration_info.access_info.endpoint,
                    "configurationDirectory": config_dir,
                    "sshPasswordCredentials": {
                        "username": username,
                        "password": password,
                    },
                    "sshPrivateKeyCredentials": None,
                    "hadoopDistribution": hdfs_params.hadoop_distribution,
                    "hadoopVersion": hdfs_params.hadoop_version,
                    "kerberosPrincipal": hdfs_params.kerberos_principal,
                    "namenodeAddress": hdfs_params.namenode,
                    "webhdfsPort": hdfs_params.port,
                },
            }
            api = "data-protect/sources/registrations"
            status_code, resp = rest_obj.post(api, version="v2", data=json.dumps(body), timeout=30)
            if status_code == 201:
                json_resp = json.loads(resp)
                source_mapping[source_id] = json_resp["id"]
            else:
                ERROR_LIST.append(
                    "Error adding source: %s Failed with error %s" % (name, resp)
                )
            return
        elif environment == env_enum.KHIVE:
            source_id = source.protection_source.id
            hive_params = source.registration_info.hive_params
            name = source.registration_info.access_info.endpoint
            hdfs_entity_id = hive_params.hdfs_entity_id
            config_dir = configparser.get(name, "hive_config")
            username = configparser.get(name, "username")
            password = configparser.get(name, "password")
            if not (username or password or config_dir):
                raise Exception(
                    "Missing Credentials or HiveConfig path in config.ini file"
                )
            if not source_mapping.get(hdfs_entity_id, ""):
                raise Exception(
                    "HDFS source '%s' is not available, skipping Hive "
                    "registration" % name
                )
            body = {
                "environment": env_enum.KHIVE,
                "hiveParams": {
                    "host": name,
                    "configurationDirectory": config_dir,
                    "sshPasswordCredentials": {
                        "username": username,
                        "password": password,
                    },
                    "sshPrivateKeyCredentials": None,
                    "hdfsSourceRegistrationID": source_mapping[hdfs_entity_id],
                    "metastoreAddress": hive_params.metastore,
                    "metastorePort": hive_params.thrift_port,
                    "kerberosPrincipal": hive_params.kerberos_principal,
                },
            }
            api = "data-protect/sources/registrations"
            status_code, resp = rest_obj.post(api, version="v2", data=json.dumps(body))
            if status_code == 201:
                json_resp = json.loads(resp)
                source_mapping[source_id] = json_resp["id"]
                #check_register_status(name, environment, sleep_count=10)
                registering_sources.append(json_resp["id"])
            else:
                ERROR_LIST.append(
                    "Error adding source: %s Failed with error %s" % (name, resp)
                )
            return
        elif environment in [env_enum.KAD, env_enum.KSQL]:
            name = node["protectionSource"]["name"]
            body = RegisterApplicationServersParameters()
            body.applications = [environment]
            id = node["protectionSource"]["id"]
            if not source_mapping.get(id, None):
                ERROR_LIST.append(
                    "Skipping %s registration, since Physical Source '%s' "
                    "registration failed." % (environment[1:], name)
                )
                return
            body.protection_source_id = source_mapping[id]
            resp = (
                cohesity_client.protection_sources.create_register_application_servers(
                    body
                )
            )
            registering_sources.append(resp.id)
            return

        elif environment == env_enum.KGENERICNAS:
            source_id = node["protectionSource"]["id"]
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            is_local_mount = False

            res_type = protect_source["nasProtectionSource"]["type"]
            host_type = protect_source["nasProtectionSource"]["protocol"]
            name = endpoint
            body.endpoint = endpoint
            body.nas_type = res_type
            body.nas_mount_credentials = NasMountCredentialParams()

            body.nas_mount_credentials.nas_protocol = host_type
            body.nas_mount_credentials.nas_type = res_type
            body.nas_mount_credentials.skip_validation = True

            if host_type != nas_enum.KNFS3:
                # Nfs file system doesn't require credentials
                username = node["registrationInfo"]["nasMountCredentials"].get(
                    "username", None
                )
                if is_local_mount:
                    password = configparser.get("import_cluster_config", "password")
                else:
                    password = configparser.get(endpoint, "password")
                    domain = "LOCAL"
                    if configparser.has_option(endpoint, "domain"):
                        # If the NAS user belongs to different domain other
                        # than LOCAL, update domain field in config file.
                        domain = configparser.get("domain")
                    body.nas_mount_credentials.domain = domain
                body.nas_mount_credentials.username = username
                body.nas_mount_credentials.password = password

        elif environment == env_enum.KPHYSICAL:
            source_id = node["protectionSource"]["id"]
            body.force_register = True
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            name = endpoint
            res_type = protect_source["physicalProtectionSource"]["type"]
            host_type = protect_source["physicalProtectionSource"]["hostType"]
            body.endpoint = endpoint
            body.environment = environment
            body.physical_type = res_type
            body.host_type = host_type

        elif environment == env_enum.KGCP:
            source_id = source.protection_source.id
            name = source.protection_source.name
            gcp_protection_source = source.protection_source.gcp_protection_source
            gcp_credentials = dict(
                clientEmailAddress=gcp_protection_source.owner_id,
                gcpType=gcp_protection_source.mtype,
                projectId=gcp_protection_source.project_id,
                vpcNetwork=gcp_protection_source.vpc_network,
                vpcSubnetwork=gcp_protection_source.vpc_subnetwork,
            )
            gcp_credentials["clientPrivateKey"] = (
                configparser.get(name, "password").encode().decode("unicode-escape")
            )
            body = dict(environment=env_enum.KGCP, gcpCredentials=gcp_credentials)
            # Registering GCP source is time-consuming and returns 500. Need to
            # make a get API call and fetch the source id.
            api = "public/protectionSources/register"

            start_time = time.time()
            try:
                status_code, resp = rest_obj.post(
                    api, version="public_v1", data=json.dumps(body), timeout=30
                )
                if status_code not in [200, 201]:
                    raise Exception(json.loads(resp)["message"])
            except Exception as err:
                raise Exception(err)
            return

        elif environment == env_enum.KISILON:
            # Since public API is not available for Isilon source registration
            # registering source using private API call.
            # entity type 14 is reserved for Isilon source.
            body = {
                "entity": {"type": 14, "isilonEntity": {"type": 0}},
                "entityInfo": {
                    "endpoint": "",
                    "type": 14,
                    "credentials": {"password": "", "username": ""},
                },
            }
            source_id = source.protection_source.id
            username = source.registration_info.username
            endpoint = source.registration_info.access_info.endpoint
            name = source.protection_source.isilon_protection_source.name
            password = configparser.get(name, "password")
            body["entityInfo"]["endpoint"] = endpoint
            body["entityInfo"]["credentials"]["username"] = username
            body["entityInfo"]["credentials"]["password"] = password
            if source.registration_info.nas_mount_credentials:
                mount_creds = source.registration_info.nas_mount_credentials
                protocol = mount_creds.nas_protocol
                if protocol == nas_enum.KCIFS1:
                    # Update SMB credentials, for protecting SMB endpoints
                    # credential is required.
                    username = mount_creds.username
                    password = configparser.get(endpoint, "smb_password")
                    body["entityInfo"]["credentials"]["nasMountCredentials"] = {
                        "protocol": 2,
                        "username": username,
                        "password": password,
                    }
            # Private api to register protection sources.
            api = "backupsources"
            code, resp = rest_obj.post(api, data=json.dumps(body))
            if code != 200:
                ERROR_LIST.append(
                    "Error adding source : %s failed with error : %s" % (name, resp)
                )
            else:
                result = json.loads(resp.decode("utf-8"))
                source_mapping[source_id] = result["entity"]["id"]
                imported_res_dict["Protection Sources"].append(name)
            return

        elif environment == env_enum.KCASSANDRA:
            name = source.protection_source.name
            source_id = source.protection_source.id
            if not configparser.has_section(name):
                ERROR_LIST.append(
                    "Please provide SSH and database credentials for "
                    "Caassandra source %s" % name
                )
                return
            ssh_username = configparser[name].get("username", None)
            ssh_password = configparser[name].get("password", None)
            db_username = configparser[name].get("db_username", None)
            db_password = configparser[name].get("db_password", None)

            if not (ssh_password and ssh_username):
                ERROR_LIST.append("Please provide ssh credentials for %s" % name)
                return

            if not (db_password and db_username):
                ERROR_LIST.append("Please provide database credentials for %s" % name)
                return
            imported_params = node["registrationInfo"]["cassandraParams"]
            cassandra_params = dict(
                configDirectory=imported_params["configDirectory"],
                sshPrivateKeyCredential=None,
                jmxCredentials=None,
                dataCenterNames=imported_params["dataCenters"],
                dseConfigurationDirectory=imported_params["dseConfigDirectory"],
                isDseAuthenticator=imported_params["isDseAuthenticator"],
                isDseTieredStorage=imported_params["isDseTieredStorage"],
                dseSolrInfo=None,
                kerberosPrincipal=None,
            )
            cassandra_params["seedNode"] = source.registration_info.access_info.endpoint
            cassandra_params["sshPasswordCredentials"] = dict(
                username=ssh_username, password=ssh_password
            )
            cassandra_params["cassandraCredentials"] = dict(
                username=db_username, password=db_password
            )
            body = dict(
                environment=env_enum.KCASSANDRA, cassandraParams=cassandra_params
            )
            api = "data-protect/sources/registrations"
            status_code, resp = rest_obj.post(api, version="v2", data=json.dumps(body))
            if status_code == 201:
                json_resp = json.loads(resp)
                source_mapping[source_id] = json_resp["id"]
                # check_register_status(name, environment, sleep_count=10)
                registering_sources.append(json_resp["id"])
            else:
                ERROR_LIST.append(
                    "Error adding source: %s Failed with error %s" % (name, resp)
                )
            return

        elif environment in [env_enum.K_VMWARE, env_enum.KVIEW]:
            env = environment[1:].lower()
            name = source.protection_source.name
            body.username = source.registration_info.username
            body.environment = environment
            source_id = source.protection_source.id
            if source.registration_info:
                endpoint = source.registration_info.access_info.endpoint
                body.endpoint = endpoint
            for attr in dir(source.protection_source):
                if env in attr:
                    attribute = attr
                    break
            registration_info = source.registration_info
            if registration_info.throttling_policy:
                body.throttling_policy = registration_info.throttling_policy
            if registration_info.subnets:
                body.subnets = registration_info.subnets
            # Option to add minimum free space and throttling policy override
            # is not available during source registration. Sources are updated.
            if (
                registration_info.minimum_free_space_gb
                or registration_info.throttling_policy_overrides
            ):
                update_source = True
            env_type = getattr(source.protection_source, attribute).mtype
            if env_type.lower() == vmware_enum.K_VCLOUD_DIRECTOR.lower():
                # Since environment type returns kvCloudDirector and enum
                # returns kVCloudDirector, both are converted to lowercase.
                return
            body.vmware_type = env_type
            if env_type not in [view_enum.KVIEWBOX]:
                password = configparser.get(name, "password")
                body.password = password
            if env == "view":
                body.view_type = view_enum.KVIEWBOX
        register_sources(body, name, source_id)
        time.sleep(sleep_time)

        # Update source is only for VMware Vcenter, to update source settings.
        if update_source:
            update_protection_source(registration_info, name, source_mapping[source_id])
    except NoSectionError as e:
        ERROR_LIST.append(
            "Error while fetching data from config file"
            " for source %s, err msg %s " % (name, e)
        )
    except Exception as e:
        ERROR_LIST.append("Error adding source : %s failed with error : %s" % (name, e))


def datastore_mapping(source_id):
    """
    Fetch datastores available in the Vcenter source and create a mapping of
    datastore name and id.
    """
    try:
        result = dict()
        response = cohesity_client.protection_sources.list_protection_sources(
            id=source_id,
            include_datastores=True,
            exclude_types=ExcludeTypeEnum.KVIRTUALMACHINE,
        )
        if not response:
            ERROR_LIST.append("Vcenter with id %s not available" % source_id)
            return
        nodes = response[0].nodes
        for node in nodes:
            if "nodes" in node.keys():
                nodes.extend(node["nodes"])
            elif (
                node["protectionSource"]["vmWareProtectionSource"].get("type", None)
                == "kDatastore"
            ):
                vm_source = node["protectionSource"]["vmWareProtectionSource"]
                result[vm_source["name"]] = node["protectionSource"]["id"]
        return result
    except Exception as err:
        ERROR_LIST.append(
            "Error while fetching datastores for Vcenter "
            "with id: %s, err msg %s." % (source_id, err)
        )


def update_protection_source(registration_info, name, source_id):
    """
    Update the protection source.
    """
    try:
        body = UpdateProtectionSourceParameters()
        if registration_info.throttling_policy_overrides:
            body.throttling_policy = registration_info.throttling_policy
            body.throttling_policy_overrides = list()
            datastore_dict = datastore_mapping(source_id)
            for policy in registration_info.throttling_policy_overrides:
                override = ThrottlingPolicyOverride()
                datastore_name = policy.datastore_name
                override.datastore_id = datastore_dict[datastore_name]
                override.datastore_name = datastore_name
                throttling_policy = ThrottlingPolicyParameters()
                throttling_policy.enforce_max_streams = True
                throttling_policy.max_concurrent_streams = (
                    policy.throttling_policy.max_concurrent_streams
                )
                throttling_policy.latency_thresholds = LatencyThresholds()
                throttling_policy.latency_thresholds.active_task_msecs = 30
                throttling_policy.latency_thresholds.new_task_msecs = 30
                override.throttling_policy = throttling_policy
                body.throttling_policy_overrides.append(override)
        if registration_info.subnets:
            subnets = registration_info.subnets
        if registration_info.minimum_free_space_gb:
            body.minimum_free_space_gb = registration_info.minimum_free_space_gb
        result = cohesity_client.protection_sources.update_protection_source(
            source_id, body
        )
    except Exception as e:
        ERROR_LIST.append(
            "Error while updating source : %s, failed with error : %s" % (name, e)
        )


def register_sources(body, name, source_id):
    """
    Registers the protection source.
    """
    try:
        result = cohesity_client.protection_sources.create_register_protection_source(
            body
        )
        source_mapping[source_id] = result.id
        imported_res_dict["Protection Sources"].append(body.endpoint)
        return result

    except Exception as e:
        ERROR_LIST.append(
            "Error adding source : %s, failed with error : %s" % (name, e)
        )


def create_storage_domains():
    """
    Fetches existing storage domain list. Create new domain if the exported
    domain is not available.
    """
    global sd_vault_list
    existing_storage_domain_list = {}
    try:
        existing_storage_domains = library.get_storage_domains(cohesity_client)

        for storage_domain in existing_storage_domains:
            existing_storage_domain_list[storage_domain.name] = storage_domain.id
        storage_domain_list = cluster_dict.get("storage_domains", [])

        cluster_partitions = cohesity_client.cluster_partitions.get_cluster_partitions()
        partition_id_mapping = {
            partition.id: partition.name for partition in cluster_partitions
        }
        partition_id, partition_name = partition_id_mapping.popitem()
        # Using V2 API, find list of vaults with are mapped to storage domains.
        code, resp = rest_obj.get("storage-domains", "v2")
        if code != 200:
            raise Exception("Error while fetching Storage domains using V2 API")
        json_resp = json.loads(resp)["storageDomains"] or []
        sd_vault_list = [ domain["vaultId"] for domain in json_resp if "vaultId" in domain.keys()]
        for storage_domain in storage_domain_list:
            # For storage domain creation, cluster partition id is mandatory.
            # Check partition is is available in the cluster id, if available
            # use the same or else use available partition.
            if storage_domain.cluster_partition_id not in partition_id_mapping.keys():
                storage_domain.cluster_partition_id = partition_id
                storage_domain.cluster_partition_name = partition_name

            if storage_domain.name in existing_storage_domain_list.keys():
                new_storage_domain_id = existing_storage_domain_list[
                    storage_domain.name
                ]
                storage_domain_mapping[storage_domain.id] = new_storage_domain_id
                imported_res_dict["Storage Domains"].append(storage_domain.name)
                if override:
                    cohesity_client.view_boxes.update_view_box(
                        new_storage_domain_id, storage_domain
                    )
                continue
            continue
            try:
                result = cohesity_client.view_boxes.create_view_box(storage_domain)
                storage_domain_mapping[storage_domain.id] = result.id
                imported_res_dict["Storage Domains"].append(storage_domain.name)
            except RequestErrorErrorException as e:
                ERROR_LIST.append(
                    "Error adding storage domain %s, Failed with error %s"
                    % (storage_domain.name, e)
                )
            except APIException as e:
                ERROR_LIST.append(
                    "Error adding storage domain %s, Failed with error %s"
                    % (storage_domain.name, e)
                )
    except Exception as err:
        ERROR_LIST.append(
            "Error adding storage domain %s, Failed with error %s"
            % (storage_domain.name, err)
        )


def create_protection_sources():
    """
    Creates protection source
    """
    registered_source_list = {}

    sources = cluster_dict.get("sources", [])
    # Fetch list of Sql servers available in the cluster.
    sql_sources = cohesity_client.protection_sources.list_protection_sources(
        environment=env_enum.KSQL
    )
    if sql_sources:
        sql_sources = [
            source["protectionSource"]["physicalProtectionSource"]["name"]
            for source in sql_sources[0].nodes
            if source["protectionSource"].get("physicalProtectionSource", None)
        ]

    ad_sources = cohesity_client.protection_sources.list_protection_sources(
        environment=env_enum.KAD
    )
    if ad_sources:
        ad_sources = [
            source["protectionSource"]["physicalProtectionSource"]["name"]
            for source in ad_sources[0].nodes
        ]

    try:
        existing_sources = library.get_protection_sources(cohesity_client)
        for source in existing_sources:
            env = source.protection_source.environment
            if env not in env_list:
                continue
            id = source.protection_source.id
            name = source.protection_source.name
            if env in [
                env_enum.KISILON,
                env_enum.K_VMWARE,
                env_enum.KCASSANDRA,
                env_enum.KGCP,
                env_enum.KHDFS,
                env_enum.KHIVE,
            ]:
                if env == env_enum.KHIVE:
                    registered_source_list[name + "_hive"] = id
                else:
                    registered_source_list[name] = id
                continue

            res = library.get_protection_source_by_id(cohesity_client, id, env)
            nodes = res.nodes if res.nodes else []
            for node in nodes:
                registered_source_list[node["protectionSource"]["name"]] = node[
                    "protectionSource"
                ]["id"]
        # Check source is already registered.
        resp = cohesity_client.protection_sources.list_protection_sources_registration_info(
            environments=env_enum.KHIVE
        )
        root_nodes = resp.root_nodes if resp.root_nodes else []
        hive_sources = [
            source.registration_info.access_info.endpoint for source in root_nodes
        ]
        for source in sources:
            environment = source.protection_source.environment
            if environment not in env_list:
                continue
            source_name = source.protection_source.name
            name = source.protection_source.name
            id = source.protection_source.id

            if environment == env_enum.KVIEW:
                # Views are not created as a part of sources.
                continue
            nodes = []
            if cluster_dict["source_dct"].get(id, None):
                nodes = cluster_dict.get("source_dct")[id]

            if environment in [
                env_enum.K_VMWARE,
                env_enum.KISILON,
                env_enum.KCASSANDRA,
                env_enum.KGCP,
                env_enum.KHDFS,
                env_enum.KHIVE,
            ]:
                if source_name in registered_source_list.keys():
                    if environment == env_enum.KHIVE:
                        if source_name not in hive_sources:
                            create_sources(source, environment, nodes)
                            continue
                        else:
                            # HDFS and HIVE sources have same source name
                            # but different ids.
                            source_mapping[id] = registered_source_list[
                                source_name + "_hive"
                            ]
                            imported_res_dict["Protection Sources"].append(source_name)
                            continue
                    source_mapping[id] = registered_source_list[source_name]
                    imported_res_dict["Protection Sources"].append(source_name)
                    if override:
                        try:
                            cohesity_client.protection_sources.create_refresh_protection_source_by_id(
                                registered_source_list[source_name]
                            )
                        except Exception as err:
                            ERROR_LIST.append(
                                "Error while refreshing source '%s', err msg '%s'"
                                % (source_name, err)
                            )
                    continue
                elif environment in [
                    env_enum.KISILON,
                    env_enum.KCASSANDRA,
                    env_enum.KGCP,
                    env_enum.KHDFS,
                    env_enum.KHIVE,
                ]:
                    nodes = nodes[0] if nodes else None
                    create_sources(source, environment, nodes)
                    continue
            if not nodes:
                continue
            for node in nodes:
                id = node["protectionSource"]["id"]
                name = node["protectionSource"]["name"]
                if (environment == env_enum.KSQL and name in sql_sources) or (
                    environment == env_enum.KAD and name in ad_sources
                ):
                    # Check the Sql/AD source is already registered, if already
                    # registered no changes are made.
                    continue
                elif (
                    environment not in [env_enum.KAD, env_enum.KSQL]
                    and name in registered_source_list.keys()
                ):
                    source_mapping[id] = registered_source_list[name]
                    imported_res_dict["Protection Sources"].append(name)
                    if override:
                        cohesity_client.protection_sources.create_refresh_protection_source_by_id(
                            registered_source_list[name]
                        )
                    continue
                create_sources(source, environment, node)

    except Exception as err:
        ERROR_LIST.append(
            "Error adding source: %s, failed with error: %s" % (name, err)
        )


def create_views():
    """
    Fetches list of views available in the cluster, adds new view if the
    view is not available in exported list.
    """
    existing_view_dict = {}
    view_list = cluster_dict.get("views", [])
    existing_views = library.get_views(cohesity_client)
    for view in existing_views:
        existing_view_dict[view.name] = view.view_id
    for view in view_list:
        try:
            if view.name in existing_view_dict.keys():
                imported_res_dict["Protection Views"].append(view.name)
                if override:
                    cohesity_client.views.update_view(view)
                view_mapping[view.name] = existing_view_dict[view.name]
            else:
                view_box_id = storage_domain_mapping.get(view.view_box_id, None)
                if not view_box_id:
                    ERROR_LIST.append(
                        "Storage domain not available for view %s" % view.name
                    )
                    continue
                view.view_box_id = view_box_id
                result = cohesity_client.views.create_view(view)
                view_mapping[view.name] = result.view_id
                imported_res_dict["Protection Views"].append(view.name)
                time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            ERROR_LIST.append(
                "Error adding view %s, Failed with error %s" % (view.name, e)
            )
        except APIException as e:
            ERROR_LIST.append(
                "Error adding view %s, Failed with error %s" % (view.name, e)
            )
        except Exception as err:
            ERROR_LIST.append(
                "Error adding view %s, Failed with error %s" % (view.name, err)
            )


def create_protection_policies():
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    existing_policy_list = {}
    protection_policies = cluster_dict.get("policies", [])
    existing_policies = library.get_protection_policies(cohesity_client, rest_obj)

    global cad_policies
    cad_policies = list()
    available_policies = dict()
    API = "data-protect/policies"
    for policy in existing_policies:
        available_policies[policy["name"]] = policy["id"]
        if policy["backupPolicy"]["regular"].get("primaryBackupTarget", None):
            cad_policies.append(policy["id"])
    for policy in protection_policies:
        try:
            is_cad_policy = False
            policy_name = policy["name"]
            if policy_name in available_policies:
                imported_res_dict["Protection Policies"].append(policy_name)
                policy_mapping[policy["id"]] = available_policies[policy_name]
                continue
            exported_policy_id = policy["id"]

            if policy["backupPolicy"]["regular"].get("primaryBackupTarget", None):
                is_cad_policy = True
                vault = policy["backupPolicy"]["regular"]["primaryBackupTarget"][
                    "archivalTargetSettings"
                ]
                vault_id = vault["targetId"]
                if not external_targets.get(vault_id, None):
                    raise Exception(
                        "Primary Backup External target '%s' not available for Policy %s"
                        % (vault["targetName"], policy["name"])
                    )
                if vault_id not in sd_vault_list:
                    raise Exception("For NextGen CE, the primary backup target needs to have an associated storage domain. Skipping Policy creation.")
                policy["backupPolicy"]["regular"]["primaryBackupTarget"][
                    "archivalTargetSettings"
                ]["targetId"] = external_targets[vault_id]
            if policy_name in available_policies:
                if not override:
                    imported_res_dict["Protection Policies"].append(policy_name)
                    policy_id = available_policies[policy_name]
                    policy_mapping[exported_policy_id] = policy_id
                    continue
            if not is_cad_policy:
                raise Exception(
                    "Local backup policies are not supported in NextGen CE, Skipping Policy creation.")

            # ConfigId field is created during the policy creation and hence removed
            # from payload.
            if policy.get("extendedRetention", []):
                for item in policy.get("extendedRetention", []):
                    if item.get("configId", ""):
                        del item["configId"]
            remote_target = policy.get("remoteTargetPolicy", None)
            if remote_target:
                for r_target in remote_target["replicationTargets"]:
                    del r_target["configId"]
                for a_target in remote_target["archivalTargets"]:
                    target_id = a_target["targetId"]
                    target_name = a_target["targetName"]
                    del a_target["configId"]
                    if not external_targets.get(target_id, None):
                        raise Exception(
                            "External target %s not available." % target_name
                        )
                    a_target["targetId"] = external_targets[target_id]
            code, resp = rest_obj.post(API, "v2", data=json.dumps(policy))
            json_resp = json.loads(resp)
            if code != 201:
                raise Exception(json_resp)
            imported_res_dict["Protection Policies"].append(policy_name)
            policy_mapping[policy["id"]] = json_resp["id"]

            # CAD policies does not required storage domain Id while creating
            # protection jobs.
            if is_cad_policy:
                cad_policies.append(json_resp["id"])

        except RequestErrorErrorException as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy_name, e)
            )
        except APIException as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy_name, e)
            )
        except Exception as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy_name, e)
            )


def get_parent_source_id(environment):
    parent_source = None
    sources = cohesity_client.protection_sources.list_protection_sources(
        environment=environment
    )
    if sources:
        parent_source = sources[0].protection_source.id
    return parent_source


def generate_sql_mapping():
    """ """
    nodes = list()
    app_nodes = list()
    sql_entity_mapping = {}
    sql_objects = cohesity_client.protection_sources.list_protection_sources(
        environment=env_enum.KSQL
    )
    if not sql_objects:
        return sql_entity_mapping
    for obj in sql_objects[0].nodes:
        app_nodes.extend(
            [
                i["nodes"]
                for i in obj.get("applicationNodes", [])
                if type(i["nodes"]) == list
            ]
        )
    for node in app_nodes:
        if type(node) == list:
            nodes.extend(node)
        else:
            nodes.append(node)
    for node in nodes:
        sql_entity_mapping[node["protectionSource"]["name"]] = node["protectionSource"][
            "id"
        ]
    return sql_entity_mapping


def recursion(cont, nodes):
    if type(cont) == list:
        for node in cont:
            recursion(node, nodes)
    elif type(cont) == dict:
        if "nodes" in cont:
            nodes.append(cont)
            recursion(cont["nodes"], nodes)
        else:
            nodes.append(cont)


def create_protection_jobs():
    """
    Creates protection job.
    """
    existing_job_list = {}
    active_protection_jobs = []
    active_protection_jobs, exported_jobs = cluster_dict.get("protection_jobs", [])

    _, existing_jobs = library.get_protection_jobs(cohesity_client, rest_obj)

    for job in existing_jobs:
        existing_job_list[job["name"]] = job["id"]

    for job in active_protection_jobs:
        if job.environment == env_enum.KSQL and job.source_special_parameters:
            mapping = dict()
            for params in job.source_special_parameters:
                mapping[
                    params.source_id
                ] = params.sql_special_parameters.application_entity_ids
            job_parent_id_mapping[job.name] = mapping
        else:
            job_parent_id_mapping[job.name] = {job.parent_source_id: job.source_ids}

        selected_jobs = configparser.get("import_cluster_config", "selected_jobs")
        jobs_to_import = [
            job.strip() for job in selected_jobs.split(",") if selected_jobs
        ]
        sql_mapping = generate_sql_mapping()

    for job in exported_jobs:
        update_job = False
        try:
            job_name = job["name"]
            environment = job["environment"]
            if jobs_to_import and job_name not in jobs_to_import:
                continue
            if job_name in existing_job_list:
                if not override:
                    imported_res_dict["Protection Jobs"].append(job_name)
                    continue
                update_job = True
            # For CAD policies, storage domains are mapped to external targets and
            # targets are mapped to policies.
            policy_id = policy_mapping[job["policyId"]]
            job["policyId"] = policy_id
            if policy_id in cad_policies:
                del job["storageDomainId"]
            else:
                job["storageDomainId"] = storage_domain_mapping[job["storageDomainId"]]

            if job["environment"] == "kPhysical":
                if job["physicalParams"]["protectionType"] == "kFile":
                    objects = job["physicalParams"]["fileProtectionTypeParams"][
                        "objects"
                    ]
                else:
                    objects = job["physicalParams"]["volumeProtectionTypeParams"][
                        "objects"
                    ]
                for p_obj in objects:
                    if p_obj["id"] in source_mapping:
                        p_obj["id"] = source_mapping[p_obj["id"]]
                    else:
                        del p_obj
                if not objects:
                    raise Exception(
                        "Physical sources not available for job '%s' creation."
                        % job_name
                    )
            elif job["environment"] == "kGCP":
                # Get instance details based on parent source.
                parent_id = list(job_parent_id_mapping[job["name"]].keys())[0]
                source_ids = job_parent_id_mapping[job["name"]][parent_id]
                source_id = source_mapping.get(parent_id, None)
                if not source_id:
                    raise Exception("Source not available for job %s" % job["name"])
                objects = cluster_dict["source_dct"][parent_id]
                nodes = list()
                resp = recursion(objects, nodes)
                object_names = list()
                object_list = list()
                for _id in nodes:
                    node_id = _id["protectionSource"]["id"]
                    if node_id in source_ids:
                        object_names.append(_id["protectionSource"]["name"])
                        source_ids.pop(source_ids.index(node_id))
                    if not source_ids:
                        break
                objects = library.get_protection_source_by_id(
                    cohesity_client, source_id, environment
                )
                m_nodes = list()
                recursion(objects.nodes[0], m_nodes)
                for _id in nodes:
                    name = _id["protectionSource"]["name"]
                    obj_id = _id["protectionSource"]["id"]
                    if name in object_names:
                        object_list.append(obj_id)
                        object_names.pop(object_names.index(name))
                    if len(object_names) == 0:
                        break
                if object_names:
                    ERROR_LIST.append(
                        "Following list of GCP object(s) are not found %s"
                        % ", ".join(object_names)
                    )
                mtype = job["gcpParams"]["protectionType"]
                key = mtype[1:].lower() + "ProtectionTypeParams"
                job["gcpParams"][key]["objects"] = [{"id": _id} for _id in object_list]

            elif job["environment"] == env_enum.KSQL:
                db_objects = list()
                entity_mapping = generate_sql_mapping()
                mtype = job["mssqlParams"]["protectionType"][1:]
                key = mtype.lower() + "ProtectionTypeParams"
                object_ids = [obj["id"] for obj in job["mssqlParams"][key]["objects"]]
                if mtype == "Volume":
                    # If SQL source is fully backed up as Volume-Based, Job is
                    # created using Physical Source Id.
                    for object_id in object_ids:
                        if source_mapping.get(object_id, None):
                            db_objects.append(dict(id=source_mapping[object_id]))
                for source_id, objects in cluster_dict["sql_entity_mapping"].items():
                    for object_id in object_ids:
                        if object_id in objects:
                            obj_name = cluster_dict["sql_entity_mapping"][source_id][
                                object_id
                            ]
                            if entity_mapping.get(obj_name, None):
                                db_objects.append(dict(id=entity_mapping[obj_name]))
                if not db_objects:
                    raise Exception("Protection Source not available")
                job["mssqlParams"][key]["objects"] = db_objects

            elif job["environment"] == env_enum.KHDFS:
                parent_id = job["hdfsParams"]["hdfsSourceId"]
                source_id = source_mapping.get(parent_id, None)
                if not source_id:
                    raise Exception(
                        "Protection Source not available"
                    )
                job["hdfsParams"]["hdfsSourceId"] = source_id
                job["hdfsParams"]["sourceId"] = source_id

            elif job["environment"] == env_enum.KHIVE:
                missing_sources = 0
                objects = job["hiveParams"]["objects"]
                hive_objects = list()
                parent_id = job["hiveParams"]["sourceId"]
                name = job["hiveParams"]["sourceName"]
                nodes = list()
                if not source_mapping.get(parent_id, None):
                    raise Exception("Protection Source '%s' not registered" % name)

                # Create Uuid and object Id mapping for both clusters..
                import_parent_id = source_mapping.get(parent_id, None)
                sources = library.get_protection_source_by_id(
                    cohesity_client, import_parent_id, environment
                )
                if not sources:
                    raise Exception("Source %s not available" % name)
                sources = sources.nodes
                recursion(sources, nodes)
                hive_object_mapping = dict()
                for node in nodes:
                    hive_object_mapping[
                        node["protectionSource"]["hiveProtectionSource"]["uuid"]
                    ] = node["protectionSource"]["id"]
                nodes = list()
                recursion(cluster_dict["source_dct"][parent_id], nodes)
                ex_hive_object_mapping = dict()
                for node in nodes:
                    ex_hive_object_mapping[node["protectionSource"]["id"]] = node[
                        "protectionSource"
                    ]["hiveProtectionSource"]["uuid"]

                for h_object in objects:
                    source_id = source_mapping.get(h_object["id"], None)
                    # Check for objects.
                    uuid = ex_hive_object_mapping.get(h_object["id"], None)
                    uuid = hive_object_mapping.get(uuid, None)
                    object_id = uuid or source_id
                    if not object_id:
                        missing_sources += 1
                        break
                    hive_objects.append(dict(id=object_id))
                if missing_sources > 0:
                    raise Exception(
                        "No Hive Objects are available to proceed."
                    )
                job["hiveParams"]["objects"] = hive_objects
                job["hiveParams"]["hdfsSourceId"] = source_id

            API = "data-protect/protection-groups"
            if update_job:
                API = API + "/" + existing_job_list[job_name]
                code, resp = rest_obj.put(API, "v2", data=json.dumps(job))
            else:
                code, resp = rest_obj.post(API, "v2", data=json.dumps(job))
            if code in [200, 201]:
                imported_res_dict["Protection Jobs"].append(job_name)
            else:
                raise Exception(resp)
        except Exception as error:
            ERROR_LIST.append(
                "Error while creating job '%s', err msg '%s'" % (job_name, error)
            )


def construct_view_box_pair(view_box_pair_info, body, remote_body):
    try:
        body.view_box_pair_info = []
        remote_body.view_box_pair_info = []
        for view_box in view_box_pair_info:
            local_view_box_id = _get_sd_id(view_box.local_view_box_name)
            local_view_box_pair = ViewBoxPairInfo()
            remote_view_box_pair = ViewBoxPairInfo()
            if local_view_box_id < 0:
                ERROR_LIST.append(
                    "Failed to find Storage domain %s, "
                    "Remote Cluster pairing not successful"
                    % view_box.local_view_box_name
                )
                continue

            local_view_box_pair.local_view_box_id = (
                remote_view_box_pair.remote_view_box_id
            ) = local_view_box_id
            local_view_box_pair.local_view_box_name = (
                remote_view_box_pair.remote_view_box_name
            ) = view_box.local_view_box_name
            local_view_box_pair.remote_view_box_id = (
                remote_view_box_pair.local_view_box_id
            ) = view_box.remote_view_box_id
            local_view_box_pair.remote_view_box_name = (
                remote_view_box_pair.local_view_box_name
            ) = view_box.remote_view_box_name

            body.view_box_pair_info.append(local_view_box_pair)
            remote_body.view_box_pair_info.append(remote_view_box_pair)
        return body, remote_body

    except Exception as err:
        ERROR_LIST.append(err)


def create_remote_clusters():
    """ """
    repl_list = {}
    remote_cluster_list = cluster_dict.get("remote_clusters", [])
    existing_cluster_list = library.get_remote_clusters(cohesity_client)
    import_cluster_ip = configparser.get("import_cluster_config", "cluster_ip")
    for cluster in existing_cluster_list:
        repl_list[cluster.name] = cluster.cluster_id
        remote_cluster_mapping[cluster.remote_ips[0]] = cluster.cluster_id
    # If the remote cluster exists then get the ID.
    for cluster in remote_cluster_list:
        exported_remote_cluster_mapping[
            remote_cluster_list[0].name
        ] = remote_cluster_list[0].remote_ips[0]
        # Check the remote cluster registered is not the current cluster.
        if cluster.remote_ips[0] == import_cluster_ip:
            continue
        is_remote_cluster_available = False
        if cluster.name in repl_list.keys():
            if not override:
                imported_res_dict["Remote Clusters"].append(cluster.name)
                continue
            is_remote_cluster_available = True
        try:
            # Add the remote cluster first
            if cluster.name not in configparser.sections():
                ERROR_LIST.append(
                    "Please add password for remote cluster: %s "
                    "in config.ini" % cluster.name
                )
                continue
            remote_cluster_password = configparser.get(cluster.name, "password")
            cluster_password = configparser.get("import_cluster_config", "password")
            body = RegisterRemoteCluster()
            remote_body = RegisterRemoteCluster()
            _construct_body(body, cluster)
            _construct_body(remote_body, cluster)
            remote_body.password = cluster_password
            body.password = remote_cluster_password
            cluster_id = cluster.cluster_id
            body.cluster_id = None
            remote_body.cluster_id = None
            local_ips = [import_cluster_ip]
            remote_ips = cluster.remote_ips
            if cluster.view_box_pair_info:
                body, remote_body = construct_view_box_pair(
                    cluster.view_box_pair_info, body, remote_body
                )
            body.local_ips = remote_body.remote_ips = local_ips
            body.remote_ips = remote_body.local_ips = remote_ips
            try:
                remote_cohesity_client = CohesityClient(
                    cluster_vip=remote_ips[0],
                    username=cluster.user_name,
                    password=remote_cluster_password,
                )

                interfaces = (
                    remote_cohesity_client.remote_cluster.get_remote_cluster_by_id(
                        id=export_config.id
                    )
                )

                if interfaces:
                    try:
                        interface_group = interfaces[0].network_interface_group
                    except Exception as err:
                        interface_group = interfaces[0].network_interface
                    remote_body.network_interface_group = interface_group
                else:
                    # Get the interfaces available in remote cluster.
                    interfaces = cohesity_client.interface_group.get_interface_groups()
                    if interfaces:
                        remote_body.network_interface_group = interfaces[0].name

                if is_remote_cluster_available:
                    remote_cohesity_client.remote_cluster.update_remote_cluster(
                        cluster_id, remote_body
                    )
                else:
                    remote_cohesity_client.remote_cluster.create_remote_cluster(
                        remote_body
                    )
            except APIException as err:
                if "already been registered" in err.args[0]:
                    pass
                else:
                    raise err

            c2 = CohesityClient(
                cluster_vip=configparser.get("import_cluster_config", "cluster_ip"),
                username=configparser.get("import_cluster_config", "username"),
                password=configparser.get("import_cluster_config", "password"),
                domain=configparser.get("import_cluster_config", "domain"),
            )

            interfaces = cohesity_client.interface_group.get_interface_groups()
            if interfaces:
                ifaces = [iface.name for iface in interfaces]

            # In newer cluster versions, network_interface_group is renamed as
            # network_interface.
            if "network_interface" in dir(body):
                iface_grp = body.network_interface
            else:
                iface_grp = body.network_interface_group
            body.network_interface_group = (
                ifaces.pop() if iface_grp not in ifaces else iface_grp
            )

            if is_remote_cluster_available:
                cohesity_client.remote_cluster.update_remote_cluster(cluster_id, body)
            else:
                cohesity_client.remote_cluster.create_remote_cluster(body)
            imported_res_dict["Remote Clusters"].append(cluster.name)
            remote_cluster_mapping[cluster.remote_ips[0]] = cluster.cluster_id

        except RequestErrorErrorException as e:
            ERROR_LIST.append(e)
        except APIException as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(
                cluster_vip=configparser.get("import_cluster_config", "cluster_ip"),
                username=configparser.get("import_cluster_config", "username"),
                password=configparser.get("import_cluster_config", "password"),
                domain=configparser.get("import_cluster_config", "domain"),
            )
            if "already been registered" in e.args[0]:
                continue
            ERROR_LIST.append(
                "Registering remote cluster %s failed with "
                "error: %s" % (cluster.name, e.args[0])
            )
        except Exception as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(
                cluster_vip=configparser.get("import_cluster_config", "cluster_ip"),
                username=configparser.get("import_cluster_config", "username"),
                password=configparser.get("import_cluster_config", "password"),
                domain=configparser.get("import_cluster_config", "domain"),
            )
            ERROR_LIST.append(
                "Registering remote cluster %s failed with "
                "error: %s" % (cluster.name, e.args[0])
            )


def add_active_directory():
    """
    Function to add active directory to the cluster. AD credentials are fetched
    from config.ini file.
    """
    existing_ad_list = list()
    ad_resp = library.get_ad_entries(cohesity_client)
    if ad_resp:
        existing_ad_list = [ad.domain_name for ad in ad_resp]
    for domain in cluster_dict.get("ad", []):
        try:
            domain_name = domain.domain_name
            if not configparser.has_section(domain_name):
                ERROR_LIST.append(
                    "Please update credentials for active directory '%s'" % domain_name
                )
                continue
            if domain_name not in existing_ad_list:
                domain.user_name = configparser[domain_name]["username"]
                domain.password = configparser[domain_name]["password"]
                if configparser[domain_name].get("machine_accounts", None):
                    domain.machine_accounts = configparser[domain_name][
                        "machine_accounts"
                    ].split(",")
                domain.overwrite_existing_accounts = True
                cohesity_client.active_directory.create_active_directory_entry(domain)
            imported_res_dict["Active Directory"].append(domain_name)
        except APIException as err:
            ERROR_LIST.append(
                "Error while adding active directory '%s', err msg %s"
                % (domain_name, err)
            )


def create_roles():
    """
    Function to create roles.
    """
    existing_roles = [role.label for role in cohesity_client.roles.get_roles()]
    for role in cluster_dict.get("roles", []):
        name = role.label
        try:
            if name not in existing_roles:
                cohesity_client.roles.create_role(role)
            imported_res_dict["Roles"].append(name)
        except APIException as err:
            ERROR_LIST.append("Error while adding Role '%s', err msg %s" % (name, err))


def create_vlans():
    """
    Function to import Vlans.
    """
    # Importing interface groups before importing Vlans.
    iface_groups = library.get_interface_groups(cohesity_client)
    existing_iface_groups = [group.name for group in iface_groups]
    for group in cluster_dict.get("iface_groups", []):
        if group.name in existing_iface_groups:
            continue
        try:
            cohesity_client.interface_group.create_interface_group(group)
        except Exception as err:
            ERROR_LIST.append(
                "Error while creating interface group %s, err msg: %s"
                % (group.name, err)
            )
    existing_vlans = [
        vlan.iface_group_name for vlan in library.get_vlans(cohesity_client)
    ]
    exported_vlans = cluster_dict.get("vlans", [])
    for vlan in exported_vlans:
        try:
            vlan_name = vlan.iface_group_name
            if vlan_name not in existing_vlans:
                # Subnet mask bits and subnet mask IP4 cannot be
                # specified at the same time.
                if vlan.subnet.netmask_ip_4 and vlan.subnet.netmask_bits:
                    vlan.subnet.netmask_ip_4 = None
                cohesity_client.vlan.create_vlan(vlan)
            imported_res_dict["Vlans"].append(vlan_name)
        except Exception as err:
            ERROR_LIST.append(
                "Error while creating Vlan %s, err msg %s" % (vlan_name, err)
            )


def create_ad_objects():
    """ """
    resp = library.get_ad_objects(
        cohesity_client, cluster_dict.get("ad_objects", {}).keys()
    )
    if not resp:
        return
    for domain, objects in cluster_dict.get("ad_objects").items():
        users = objects["users"]
        groups = objects["groups"]

        # Fetch active directory users and groups available in the cluster.
        avl_objects = resp[domain]
        existing_users = [user.username for user in avl_objects.get("users", [])]
        existing_groups = [group.name for group in avl_objects.get("groups", [])]

        for user in users:
            try:
                if user.username not in existing_users:
                    cohesity_client.principals.create_user(user)
            except APIException as err:
                ERROR_LIST.append(
                    "Error while creating AD user '%s', err msg %s"
                    % (user.username, err)
                )
        for group in groups:
            try:
                if group.name not in existing_groups:
                    cohesity_client.groups.create_group(group)
            except APIException as err:
                ERROR_LIST.append(
                    "Error while creating AD group '%s', err msg %s" % (group.name, err)
                )


def _construct_body(body, entity):
    items = [
        item
        for item in dir(entity)
        if not item.startswith("__") and not item.startswith("_")
    ]
    for item in items:
        if hasattr(getattr(entity, item), "id"):
            continue
        setattr(body, item, getattr(entity, item))


def _get_sd_id(view_box_name):
    existing_storage_domains = library.get_storage_domains(cohesity_client)
    for sd in existing_storage_domains:
        if sd.name == view_box_name:
            return sd.id
    return -1


def update_gflags():
    # Update the Gflag values for services.
    try:
        cluster_ip = configparser.get("import_cluster_config", "cluster_ip")
        username = configparser.get("import_cluster_config", "username")
        password = configparser.get("import_cluster_config", "password")
        domain = configparser.get("import_cluster_config", "domain")
        # Update the flags from exported cluster.
        exported_gflags = json.loads(cluster_dict["gflag"])
        for body in exported_gflags:
            code, resp = library.gflag(json.dumps(body), "put")
            if code not in [200, 204]:
                ERROR_LIST.append(
                    "Failed to update gflag for service %s" % (body["serviceName"])
                )
                continue
            imported_res_dict["Gflag services"].append(body["serviceName"])
    except Exception as err:
        ERROR_LIST.append(
            "Error occurred while updating gflags. Error details %s" % err
        )


if __name__ == "__main__":
    logger.info("Importing cluster config \n\n")
    import_cluster_config()
    # Gflags are imported from cluster based on flag value.
    if gflag_import:
        logger.info("Importing gflags \n\n")
        update_gflags()
    if access_mgmnt:
        logger.info("Importing Active directories  \n\n")
        add_active_directory()
        logger.info("Importing roles  \n\n")
        create_roles()
        logger.info("Importing AD groups and users \n\n")
        create_ad_objects()
    if vlans:
        logger.info("Importing Vlans\n\n")
        create_vlans()
    logger.info("Importing Targets  \n\n")
    create_vaults()
    if global_whitelists:
        logger.info("Update Global whitelist settings \n\n")
        update_whitelist_settings()
    logger.info("Importing Storage domains \n\n")
    create_storage_domains()
    logger.info("Importing remote clusters  \n\n")
    create_remote_clusters()
    logger.info("Importing Views  \n\n")
    create_views()
    logger.info("Importing Sources  \n\n")
    create_protection_sources()
    logger.info("Importing Policies  \n\n")
    create_protection_policies()
    logger.info("Importing Jobs  \n\n")
    # Before importing jobs, check for Source registration status.
    check_register_status()
    create_protection_jobs()

logger.info("Imported resources summary.")
for key, val in imported_res_dict.items():
    logger.info("%s:\n%s\n" % (key, ", ".join(val)))

if ERROR_LIST:
    ERROR_LIST = [str(err) for err in ERROR_LIST]
    logger.error("Please find the error list/corrective actions:")
    i = 1
    for E in ERROR_LIST:
        logger.error("\t  %s: %s\n" % (i, E))
        i = i + 1
