# Copyright 2020 Cohesity Inc.
#
# Python utility to import the cluster config.
# Expects input config file to be present in the current directory.
# Usage: python import_cluster_config.py <path/to/file>

import argparse
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
    from cohesity_management_sdk.models.append_hosts_parameters import AppendHostsParameters
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
    print("Please install Cohesity Python SDK and try again.")
    print(
        "To install Python SDK, run 'pip install cohesity-management-sdk "
        "configparser requests'"
    )
    sys.exit()

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

from configparser import NoSectionError, NoOptionError, MissingSectionHeaderError

# Custom module import
import library
from library import RestClient

# Disable python warnings.
requests.packages.urllib3.disable_warnings()


logger = logging.getLogger("import_app")
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
ERROR_LIST = []
KCASSANDRA = "kCassandra"
configparser = configparser.ConfigParser()
parser = argparse.ArgumentParser(
    description="Import Config Arguments"
)
parser.add_argument(
    "--config",
    "-c",
    default="config.ini",
    action="store",
    help="Config file to import the resources.")
parser.add_argument('file', nargs='*')
args = parser.parse_args()
config_file = args.config


# Validate the configuration file content.
try:
    configparser.read(config_file)
except MissingSectionHeaderError as err:
    print(
        "Given configuration file is invalid, please make sure %s is "
        "decrypted" % config_file)
    sys.exit()


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
    print("Error while fetching value from '%s' file, err_msg" " '%s'" %  (config_file,err))
    sys.exit()

# Read the imported cluster configurations from file.
if not args.file:
    logger.error("Please specify the exported config file.")
    sys.exit(1)
else:
    try:
        cluster_dict = pickle.load(open(args.file[0], "rb"))
    except IOError:
        print("Import file does not exist")
        sys.exit(1)


# Variables to store resources and corresponding ids.

view_mapping = {}
policy_mapping = {}
source_mapping = {}
remote_cluster_mapping = {}
exported_remote_cluster_mapping = {}
storage_domain_mapping = {}

imported_res_dict = defaultdict(list)
export_config = cluster_dict["cluster_config"]
import_config = library.get_cluster_config(cohesity_client)
env_list = [
    env_enum.KGENERICNAS,
    env_enum.KISILON,
    env_enum.KPHYSICAL,
    env_enum.KPHYSICALFILES,
    env_enum.KVIEW,
    env_enum.K_VMWARE,
    env_enum.KSQL,
    env_enum.KCASSANDRA,
    env_enum.KAD,
    env_enum.KORACLE,
    env_enum.K_HYPERV_VSS,
    env_enum.K_HYPERV,
    env_enum.KNETAPP,
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
                if resp and resp.client_subnets:
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
    external_targets = dict()
    available_vaults_dict = {}
    vaults = cluster_dict.get("external_targets")
    available_vaults = library.get_external_targets(cohesity_client)

    for vault in available_vaults:
        available_vaults_dict[vault.name] = vault.id

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
                "%s, err is %s" % (vault.name, config_file, err)
            )


def check_register_status(name, environment, sleep_count=6):
    """
    Fetch registration status after specific sleep time.
    """
    try:
        status = None
        while sleep_count != 0:
            sources = cohesity_client.protection_sources.list_protection_sources(
                environment=environment
            )
            if environment in [env_enum.K_HYPERV, KCASSANDRA]:
                for source in sources:
                    if source.registration_info.access_info.endpoint == name:
                        status = source.registration_info.authentication_status
                        break
            else:
                nodes = sources[0].nodes
                for node in nodes:
                    reg_info = node["registrationInfo"]
                    if reg_info["accessInfo"]["endpoint"] == name:
                        status = reg_info["authenticationStatus"]
                        break
            # Check for the registration status, if the process is
            # pending, sleep for 10sec and poll again.
            if status in ["kScheduled", "kPending"]:
                time.sleep(sleep_time * 5)
                sleep_count = sleep_count - 1
            else:
                # If the status is either success/failed return.
                return
    except Exception as err:
        ERROR_LIST.append(err)


def recursive_mapping(resources, result):
    """
    Function to recursively iterate over the response and create mapping of
    datastore name and id.
    : return datastore name and id mapping.
    """
    if isinstance(resources, dict):
        if "nodes" in resources:
            recursive_mapping(resources["nodes"], result)
        elif (
            resources["protectionSource"]["hypervProtectionSource"]["type"]
            == "kDatastore"
        ):
            result[resources["protectionSource"]["name"]] = resources[
                "protectionSource"
            ]["id"]
    elif isinstance(resources, list):
        for node in resources:
            recursive_mapping(node, result)
    else:
        recursive_mapping(resources.nodes, result)


def fetch_hyperv_datastore_mapping(source_id):
    """
    Function to get the HyperV source objects and create a dictionary of
    datastore names and datastore ids.
    : return dict
    """
    try:
        result = {}
        resources = cohesity_client.protection_sources.list_protection_sources(
            id=source_id, include_datastores=True
        )
        recursive_mapping(resources, result)
        return result

    except Exception as err:
        ERROR_LIST.append(err)


def create_sources(source, environment, node):
    """ """
    try:
        update_source = False
        body = RegisterProtectionSourceParameters()
        body.environment = environment
        source_id = source.protection_source.id
        if environment in [env_enum.KAD, env_enum.KSQL, env_enum.KORACLE]:
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
            check_register_status(name, environment)
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

        elif environment == env_enum.KNETAPP:
            protect_source = source.protection_source
            section = name = protect_source.name
            source_id = protect_source.id
            registration_info = source.registration_info
            endpoint = body.endpoint = registration_info.access_info.endpoint
            body.username = registration_info.username
            body.netapp_type = protect_source.netapp_protection_source.mtype
            body.allowed_ip_addresses = registration_info.allowed_ip_addresses
            body.denied_ip_addresses = registration_info.denied_ip_addresses

            # Check the config file for section with endpoint or source name.
            if configparser.has_section(endpoint):
                body.password = configparser.get(endpoint, "password")
                section = endpoint
            elif configparser.has_section(name):
                body.password = configparser.get(name, "password")
            else:
                ERROR_LIST.append(
                    "Section %s or %s not available in the config file" % (
                        name, endpoint))
                return

            if registration_info.nas_mount_credentials and \
                registration_info.nas_mount_credentials.nas_protocol != \
                    nas_enum.KNFS3:
                exported_creds = registration_info.nas_mount_credentials
                password = configparser.get(section, "smb_password")
                mount_creds = NasMountCredentialParams()
                mount_creds.password = password
                mount_creds.username = exported_creds.username
                mount_creds.domain = exported_creds.domain
                mount_creds.nas_protocol = exported_creds.nas_protocol
                body.nas_mount_credentials = mount_creds


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
                    password = configparser.get(name, "smb_password")
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

        elif environment == KCASSANDRA:
            name = source.protection_source.name
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
            body = dict(environment=KCASSANDRA, cassandraParams=cassandra_params)
            api = "data-protect/sources/registrations"
            status_code, resp = rest_obj.post(api, version="v2", data=json.dumps(body))
            if status_code == 201:
                json_resp = json.loads(resp)
                source_mapping[source_id] = json_resp["id"]
                check_register_status(name, environment, sleep_count=10)
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

        elif environment == env_enum.K_HYPERV:
            # In case of standalone server, source is not registered.
            protect_source = source.protection_source
            source_type = protect_source.hyperv_protection_source.mtype
            # Only HyperV SCVMM host type is supported, checking the type
            # before source registration.
            if source_type != "kSCVMMServer":
                return
            name = protect_source.name
            register_info = source.registration_info
            body = RegisterProtectionSourceParameters()
            body.endpoint = name
            body.hyperv_type = source_type
            body.environment = env_enum.K_HYPERV
            body.username = register_info.username
            body.password = configparser.get(name, "password")
            if register_info.throttling_policy:
                body.throttling_policy = register_info.throttling_policy
            result = register_sources(body, name, source_id)
            # Get the imported source id.
            imported_source_id = source_mapping.get(source_id, None)
            if imported_source_id and register_info.throttling_policy_overrides:
                # Check for source registration status.
                check_register_status(name, environment)

                # Create the datastore name and id mapping.
                datastores = fetch_hyperv_datastore_mapping(imported_source_id)
                body = UpdateProtectionSourceParameters()
                overrides = []
                for datastore in register_info.throttling_policy_overrides:
                    datastore_id = datastores.get(datastore.datastore_name, "")
                    if not datastore_id:
                        ERROR_LIST.append(
                            "Failed to find datastore '%s' in the source '%s'"
                            % (datastore.datastore_name, name)
                        )
                    datastore.datastore_id = datastore_id
                    overrides.append(datastore)
                body.throttling_policy_overrides = overrides
                try:
                    result = (
                        cohesity_client.protection_sources.update_protection_source(
                            source_mapping[source_id], body
                        )
                    )
                # Ignoring the timeout error, since the source updation API updates the
                # source yet the response is delayed than expected.
                except TimeoutError as e:
                    pass
            return
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
    oracle_sources = cohesity_client.protection_sources.list_protection_sources(
        environment=env_enum.KORACLE
    )
    if oracle_sources:
        oracle_sources = [
            source["protectionSource"]["physicalProtectionSource"]["name"]
            for source in oracle_sources[0].nodes
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
                env_enum.K_HYPERV,
                env_enum.KISILON,
                env_enum.K_VMWARE,
                env_enum.KNETAPP,
                KCASSANDRA,
            ]:
                registered_source_list[name] = id
                continue

            res = library.get_protection_source_by_id(cohesity_client, id, env)
            nodes = res.nodes if res.nodes else []
            for node in nodes:
                registered_source_list[node["protectionSource"]["name"]] = node[
                    "protectionSource"
                ]["id"]

        for source in sources:
            environment = source.protection_source.environment
            if environment not in env_list:
                continue
            name = source.protection_source.name
            id = source.protection_source.id

            if environment == env_enum.KVIEW:
                # Views are not created as a part of sources.
                continue
            nodes = cluster_dict.get("source_dct")[id]

            if environment in [
                env_enum.K_HYPERV,
                env_enum.K_VMWARE,
                env_enum.KISILON,
                env_enum.KNETAPP,
                KCASSANDRA,
            ]:
                if name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[name]
                    imported_res_dict["Protection Sources"].append(name)
                    if override:
                        cohesity_client.protection_sources.create_refresh_protection_source_by_id(
                            registered_source_list[name]
                        )
                    continue
                elif environment != env_enum.K_VMWARE:
                    nodes = nodes[0] if nodes else None
                    create_sources(source, environment, nodes)
                    continue
            if not nodes:
                continue
            for node in nodes:
                id = node["protectionSource"]["id"]
                name = node["protectionSource"]["name"]
                if (
                    (environment == env_enum.KSQL and name in sql_sources)
                    or (environment == env_enum.KAD and name in ad_sources)
                    or (environment == env_enum.KORACLE and name in oracle_sources)
                ):
                    # Check the Sql/AD source is already registered, if already
                    # registered no changes are made.
                    continue
                elif (
                    environment not in [env_enum.KAD, env_enum.KSQL, env_enum.KORACLE]
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
                        "Storage domain not avaialble for view %s" % view.name
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
    protection_policy_list = cluster_dict.get("policies", [])
    existing_policies = library.get_protection_policies(cohesity_client)
    for policy in existing_policies:
        existing_policy_list[policy.name] = policy.id

    for policy in protection_policy_list:
        is_policy_available = False
        try:
            # If policy with same name is already available.
            if policy.name in existing_policy_list.keys():
                is_policy_available = True
                imported_res_dict["Protection Policies"].append(policy.name)
                policy_id = existing_policy_list[policy.name]
                policy_mapping[policy.id] = policy_id
                # Override the existing policy if override is set to True.
                if not override:
                    continue

            if not policy.incremental_scheduling_policy.daily_schedule:
                policy.incremental_scheduling_policy.daily_schedule = {}

            if not policy.incremental_scheduling_policy.monthly_schedule:
                policy.incremental_scheduling_policy.monthly_schedule = {}
            if policy.full_scheduling_policy:
                if not policy.full_scheduling_policy.daily_schedule:
                    policy.full_scheduling_policy.daily_schedule = {"days": []}

            body = ProtectionPolicyRequest()
            _construct_body(body, policy)
            if policy.snapshot_replication_copy_policies:
                for remote_cluster in policy.snapshot_replication_copy_policies:
                    cluster_name = remote_cluster.target.cluster_name
                    cluster_ip = exported_remote_cluster_mapping.get("cluster_name", "")
                    cluster_id = remote_cluster_mapping.get("cluster_ip", None)
                    if cluster_id:
                        remote_cluster.target.cluster_id = cluster_id

            if (
                policy.snapshot_archival_copy_policies
                and len(policy.snapshot_archival_copy_policies) != 0
            ):
                for ext_target in policy.snapshot_archival_copy_policies:
                    vault_id = ext_target.target.vault_id
                    if external_targets.get(vault_id, None):
                        ext_target.target.vault_id = external_targets[vault_id]
                    try:
                        del ext_target._names["id"]
                    except KeyError:
                        pass
            if is_policy_available:
                cohesity_client.protection_policies.update_protection_policy(
                    policy, policy_id
                )
                continue
            result = cohesity_client.protection_policies.create_protection_policy(body)
            imported_res_dict["Protection Policies"].append(policy.name)
            policy_mapping[policy.id] = result.id
            time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy.name, e)
            )
        except APIException as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy.name, e)
            )
        except Exception as e:
            ERROR_LIST.append(
                "Error creating Policy: %s, failed with error: " "%s" % (policy.name, e)
            )


def get_parent_source_id(environment):
    parent_source = None
    sources = cohesity_client.protection_sources.list_protection_sources(
        environment=environment
    )
    if sources:
        parent_source = sources[0].protection_source.id
    return parent_source


def create_protection_jobs():
    """
    Creates protection job.
    """
    existing_job_list = {}
    active_protection_jobs = []
    imported_job_prefix = configparser.get(
        "import_cluster_config", "imported_job_prefix"
    )
    imported_job_suffix = configparser.get(
        "import_cluster_config", "imported_job_suffix"
    )
    active_protection_jobs = cluster_dict.get("protection_jobs", [])

    # Fetch Sql parent source id.
    sql_parent_source = get_parent_source_id(env_enum.KSQL)

    # Fetch AD parent source id.
    ad_parent_source = get_parent_source_id(env_enum.KAD)

    # Fetch Oracle parent source id.
    oracle_parent_source = get_parent_source_id(env_enum.KORACLE)

    existing_jobs = library.get_protection_jobs(cohesity_client)
    for job in existing_jobs:
        existing_job_list[job.name] = job.id

    try:
        selected_jobs = configparser.get("import_cluster_config", "selected_jobs")
        jobs_to_import = [
            job.strip() for job in selected_jobs.split(",") if selected_jobs
        ]
        for protection_job in active_protection_jobs:
            source_list = []
            _parent_id = None
            is_job_available = False
            job_name = protection_job.name
            if jobs_to_import and job_name not in jobs_to_import:
                # Check job is available in the json, if no jobs is added all
                # the jobs are protected, or else only selected jobs are
                # protected.
                continue
            if imported_job_prefix or imported_job_suffix:
                job_name = imported_job_prefix + job_name + imported_job_suffix
                protection_job.name = job_name
            environment = protection_job.environment

            # During source registration we provide environment type as kHyperV
            # and as kHyperVVSS during Protection Group related CRUD functions.
            if environment == env_enum.K_HYPERV_VSS:
                environment = env_enum.K_HYPERV
            parent_id = protection_job.parent_source_id
            if environment not in env_list:
                continue
            if environment == env_enum.KVIEW:
                if protection_job.view_box_id not in storage_domain_mapping.keys():
                    continue
                # In earlier cluster versions, View jobs can created using
                # View name alone, whereas in later versions View jobs require
                # source ids.
                source_ids = protection_job.source_ids
                protection_job.source_ids = list()
                protection_job.parent_source_id = None
                nodes = cluster_dict.get("protection_sources")
                for node in nodes[0].nodes:
                    if node["protectionSource"]["id"] in source_ids:
                        source_id = view_mapping.get(
                            node["protectionSource"]["name"], None
                        )
                        if source_id:
                            protection_job.source_ids.append(source_id)
                            protection_job.view_name = node["protectionSource"]["name"]
            elif (
                environment
                not in [
                    env_enum.KAD,
                    env_enum.KORACLE,
                    env_enum.KGENERICNAS,
                    env_enum.KSQL,
                    env_enum.KPHYSICAL,
                    env_enum.KPHYSICALFILES,
                ]
                and source_mapping.get(parent_id, None) is None
            ):
                err_msg = "Protection Source not available for job %s" % job_name
                ERROR_LIST.append(err_msg)
                continue

            # Check if the protection source is already available.
            if job_name in existing_job_list.keys():
                imported_res_dict["Protection Jobs"].append(job_name)
                is_job_available = True
                current_job_id = existing_job_list[job_name]
                if not override:
                    continue

            source_id_list = (
                protection_job.source_ids if protection_job.source_ids else []
            )
            tag_id_list = []
            if protection_job.vm_tag_ids:
                for tag in protection_job.vm_tag_ids:
                    tag_id_list.extend(tag)
                if protection_job.exclude_vm_tag_ids:
                    for tag in protection_job.exclude_vm_tag_ids:
                        tag_id_list.extend(tag)

            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            # UUID list for VMware resources.
            uuid_list = []
            tag_uuid_list = []

            if source_mapping.get(parent_id, None):
                protection_job.parent_id = source_mapping[parent_id]

            list_len = len(source_id_list + tag_id_list)
            protection_job.view_box_id = storage_domain_mapping.get(
                protection_job.view_box_id, None
            )
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id, None
            )
            if not protection_job.view_box_id:
                ERROR_LIST.append("Viewbox not available for job %s" % job_name)
                continue

            if not protection_job.policy_id:
                ERROR_LIST.append(
                    "Protection policy not available for job %s" % job_name
                )
                continue
            sources = cluster_dict["source_dct"].get(parent_id, [])

            nodes = []
            if environment == env_enum.KNETAPP:
                nodes = sources if isinstance(sources, list) else []
            for source in sources:
                nodes.extend(source.get("nodes", []))

            copy_env_list = copy.deepcopy(env_list)
            for env in [
                env_enum.KISILON,
                env_enum.K_VMWARE,
                env_enum.KSQL,
                KCASSANDRA,
                env_enum.K_HYPERV,
                env_enum.KNETAPP,
                env_enum.KAD,
                env_enum.KORACLE,
            ]:
                copy_env_list.pop(copy_env_list.index(env))

            to_proceed = True

            if not nodes and environment in copy_env_list:
                for each_source in sources:
                    id = each_source["protectionSource"]["id"]
                    if id in source_id_list:
                        if environment in [
                            env_enum.KPHYSICAL,
                            env_enum.KPHYSICALFILES,
                            env_enum.KGENERICNAS,
                        ]:
                            env = (
                                env_enum.KPHYSICAL
                                if "Physical" in environment
                                else env_enum.KGENERICNAS
                            )
                            obj = library.get_protection_source_by_id(
                                cohesity_client, _id=None, env=env
                            )
                            if not obj or source_mapping.get(id, None) is None:
                                ERROR_LIST.append(
                                    "Protection Source not available for job %s"
                                    % job_name
                                )
                                to_proceed = False
                                break
                            _parent_id = obj.protection_source.id

                            source_list.append(source_mapping[id])
                            protection_job.parent_source_id = _parent_id
                            if protection_job.source_special_parameters:
                                for (
                                    ps_source
                                ) in protection_job.source_special_parameters:
                                    if ps_source.source_id == id:
                                        ps_source.source_id = source_mapping[id]
                        else:
                            protection_job.view_name = each_source["protectionSource"][
                                "name"
                            ]
            # Check to break from loop if protection source for job is not
            # available.
            if not to_proceed:
                continue
            missing_objects = []
            tag_id_mapping = {}
            uuid_source_mapping = {}
            resource_list = source_id_list + tag_id_list
            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                # Fetch the UUID list from with available source ids from
                # exported cluster. VMware resources are provided with UUID
                # and mapping is based on uuid.
                _id = node["protectionSource"]["id"]
                if environment == env_enum.K_VMWARE and _id in resource_list:
                    uuid = node["protectionSource"]["vmWareProtectionSource"]["id"].get(
                        "uuid"
                    )
                    if _id in source_id_list:
                        uuid_list.append(uuid)
                    elif _id in tag_id_list:
                        tag_uuid_list.append(uuid)
                    uuid_source_mapping[uuid] = node["protectionSource"]["id"]
                elif (
                    environment == env_enum.KISILON
                    and node["protectionSource"]["id"] in source_id_list
                ):
                    uuid_source_mapping[node["protectionSource"]["name"]] = node[
                        "protectionSource"
                    ]["isilonProtectionSource"]["mountPoint"]["accessZoneName"]
                elif (
                    environment == KCASSANDRA
                    and node["protectionSource"]["id"] in source_id_list
                ):
                    uuid_list.append(
                        node["protectionSource"]["cassandraProtectionSource"]["uuid"]
                    )
                elif (
                    environment == env_enum.KNETAPP
                    and node["protectionSource"]["id"] in source_id_list
                ):
                    uuid_list.append(
                        node["protectionSource"]["netappProtectionSource"]["uuid"]
                    )
                elif (
                    environment == env_enum.K_HYPERV
                    and node["protectionSource"]["id"] in source_id_list
                ):
                    uuid_source_mapping[node["protectionSource"]["name"]] = node[
                        "protectionSource"
                    ]["id"]
                if len(uuid_list + tag_uuid_list) == list_len:
                    break
            nodes = []

            if source_mapping.get(parent_id, None):
                nodes = library.get_protection_source_by_id(
                    cohesity_client, source_mapping[parent_id], environment
                )

                nodes = [] if not nodes else nodes.nodes
            source_spl_params = protection_job.source_special_parameters
            source_object_dct = {}
            tag_list = []
            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                if environment == env_enum.K_VMWARE:
                    uuid = node["protectionSource"]["vmWareProtectionSource"]["id"].get(
                        "uuid"
                    )
                    if (
                        node["protectionSource"]["parentId"]
                        != source_mapping[parent_id]
                    ):
                        continue
                    _id = node["protectionSource"]["id"]
                    if uuid in uuid_list:
                        source_list.append(_id)
                        source_object_dct[uuid_source_mapping[uuid]] = _id
                    elif uuid in tag_uuid_list:
                        # Tag id mapping.
                        tag_id_mapping[uuid_source_mapping[uuid]] = _id
                        tag_list.append(_id)
                elif environment == env_enum.KISILON:
                    name = node["protectionSource"]["name"]
                    if (
                        node["protectionSource"]["isilonProtectionSource"].get(
                            "mountPoint", None
                        )
                        is None
                    ):
                        mount_point = node["protectionSource"][
                            "isilonProtectionSource"
                        ]["accessZone"]["name"]
                    else:
                        mount_point = node["protectionSource"][
                            "isilonProtectionSource"
                        ]["mountPoint"]["accessZoneName"]
                    if (
                        name in uuid_source_mapping.keys()
                        and mount_point == uuid_source_mapping[name]
                    ):
                        name = node["protectionSource"]["name"]
                        protocol = node["protectionSource"]["isilonProtectionSource"][
                            "mountPoint"
                        ]["protocols"]
                        if "kNfs" in protocol:
                            source_list.append(node["protectionSource"]["id"])
                        else:
                            # flag set to skip protection job creation which contains
                            # objects with SMB protocol.
                            to_proceed = False
                            ERROR_LIST.append(
                                "Protection job '%s' contain objects %s of "
                                "following protocol %s. Supported protocol is kNfs."
                                % (job_name, name, ", ".join(protocol))
                            )
                            break
                elif environment == KCASSANDRA:
                    uuid = node["protectionSource"]["cassandraProtectionSource"].get(
                        "uuid"
                    )
                    if (
                        uuid in uuid_list
                        and node["protectionSource"]["parentId"]
                        == source_mapping[parent_id]
                    ):
                        id = node["protectionSource"]["id"]
                        source_list.append(id)
                elif environment == env_enum.KNETAPP:
                    uuid = node["protectionSource"]["netappProtectionSource"].get(
                        "uuid"
                    )
                    if (
                        uuid in uuid_list
                        and node["protectionSource"]["parentId"]
                        == source_mapping[parent_id]
                    ):
                        id = node["protectionSource"]["id"]
                        source_list.append(id)
                elif environment == env_enum.K_HYPERV:
                    name = node["protectionSource"]["name"]
                    if (
                        name in uuid_source_mapping.keys()
                        and node["protectionSource"]["parentId"]
                        == source_mapping[parent_id]
                    ):
                        source_list.append(node["protectionSource"]["id"])
                        del uuid_source_mapping[name]
                if len(source_list + tag_list) == list_len:
                    break
            # Check to break from loop.
            if not to_proceed:
                continue
            if tag_list:
                vm_tag_ids = protection_job.vm_tag_ids
                protection_job.vm_tag_ids = list()
                for tag_ids in vm_tag_ids:
                    tags = list()
                    for tag_id in tag_ids:
                        tags.append(tag_id_mapping[tag_id])
                    protection_job.vm_tag_ids.append(tags)

            if environment in [env_enum.KAD, env_enum.KSQL, env_enum.KORACLE]:
                exported_entity_mapping = (
                    cluster_dict["sql_entity_mapping"]
                    if environment == env_enum.KSQL
                    else cluster_dict["ad_entity_mapping"]
                    if environment == env_enum.KAD
                    else cluster_dict["oracle_entity_mapping"]
                )
                source_list = [
                    source_mapping[_id]
                    for _id in protection_job.source_ids
                    if source_mapping.get(_id, None)
                ]
                if not source_list:
                    ERROR_LIST.append(
                        "Protection Source not available for job %s" % job_name
                    )
                    continue
                if source_spl_params:
                    for param in source_spl_params:
                        instance_list = []
                        entity_mapping = {}
                        _source_id = param.source_id  # exported source id.
                        source_id = source_mapping[param.source_id]
                        sources = (
                            cohesity_client.protection_sources.list_protection_sources(
                                id=source_id
                            )
                        )
                        application_nodes = sources[0].application_nodes or []
                        for nodes in application_nodes:
                            if environment in [env_enum.KORACLE, env_enum.KAD]:
                                entity_mapping[
                                    nodes["protectionSource"]["name"]
                                ] = nodes["protectionSource"]["id"]
                            for node in nodes.get("nodes", []):
                                entity_mapping[node["protectionSource"]["name"]] = node[
                                    "protectionSource"
                                ]["id"]
                        param.source_id = source_id

                        # Fetch list of databases protected through job.
                        entity_ids = (
                            param.sql_special_parameters.application_entity_ids
                            if environment == env_enum.KSQL
                            else param.ad_special_parameters.application_entity_ids
                            if environment == env_enum.KAD
                            else param.oracle_special_parameters.application_entity_ids
                        )
                        for _id in entity_ids:
                            instance_name = exported_entity_mapping[_source_id][_id]
                            if entity_mapping.get(instance_name, None):
                                instance_list.append(entity_mapping[instance_name])
                            else:
                                missing_objects.append(instance_name)
                        if environment == env_enum.KSQL:
                            param.sql_special_parameters = (
                                ApplicationSpecialParameters()
                            )
                            param.sql_special_parameters.application_entity_ids = (
                                instance_list
                            )
                        elif environment == env_enum.KAD:
                            param.ad_special_parameters = ApplicationSpecialParameters()
                            param.ad_special_parameters.application_entity_ids = (
                                instance_list
                            )
                        elif environment == env_enum.KORACLE:
                            param.oracle_special_parameters = (
                                ApplicationSpecialParameters()
                            )
                            param.oracle_special_parameters.application_entity_ids = (
                                instance_list
                            )
                protection_job.parent_source_id = (
                    sql_parent_source
                    if environment == env_enum.KSQL
                    else ad_parent_source
                    if environment == env_enum.KAD
                    else oracle_parent_source
                )
            if missing_objects:
                ERROR_LIST.append(
                    "Following list of objects '%s' are not available in the "
                    "source for job '%s'" % (
                        ",".join(missing_objects), job_name))
                missing_objects.clear()
                if not instance_list or source_list:
                    continue

            if source_spl_params and environment == env_enum.K_VMWARE:
                for param in source_spl_params:
                    if param.source_id in source_object_dct.keys():
                        param.source_id = source_object_dct[param.source_id]

            if source_list:
                protection_job.source_ids = source_list

            if source_mapping.get(parent_id, ""):
                protection_job.parent_source_id = source_mapping[parent_id]

            # For Physical sources, Update source side deduplication excluded
            # source ids.
            if (
                environment in [env_enum.KPHYSICALFILES, env_enum.KPHYSICAL]
                and protection_job.perform_source_side_dedup
            ):
                if protection_job.dedup_disabled_source_ids:
                    disabled_sources = list()
                    for source_id in protection_job.dedup_disabled_source_ids:
                        if source_mapping.get(source_id, None):
                            disabled_sources.append(source_mapping[source_id])
                    protection_job.dedup_disabled_source_ids = disabled_sources

            try:
                if override and is_job_available:
                    cohesity_client.protection_jobs.update_protection_job(
                        protection_job, current_job_id
                    )
                else:
                    result = cohesity_client.protection_jobs.create_protection_job(
                        protection_job
                    )
                    current_job_id = result.id
                    imported_res_dict["Protection Jobs"].append(job_name)

                if pause_jobs:
                    body = ChangeProtectionJobStateParam()
                    body.pause = True
                    cohesity_client.protection_jobs.change_protection_job_state(
                        current_job_id, body
                    )
                    time.sleep(2 * sleep_time)
            except Exception as e:
                ERROR_LIST.append(
                    "Creating Protection Job '%s' failed with error: %s" % (job_name, e)
                )

    except RequestErrorErrorException as e:
        ERROR_LIST.append(e)
    except APIException as e:
        ERROR_LIST.append(e)
    except Exception as err:
        ERROR_LIST.append(err)


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
                    "in %s" % (cluster.name, config_file)
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
                        import_config.id, remote_body
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
    from config input(.ini) file.
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
            code, resp = library.gflag(
                cluster_ip, username, password, domain, json.dumps(body), "put"
            )
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


def create_host_mapping():
    """
    Function to import host mapping.
    """
    try:
        body = AppendHostsParameters()
        exported_hosts = cluster_dict["host_mappings"]
        existing_hosts = library.get_host_mapping(cohesity_client)
        body.hosts = existing_hosts
        host_ips = [host.ip for host in existing_hosts]
        newly_added_ips = []
        for host in exported_hosts:
            # If host is already added, skip else create an entry.
            if host.ip not in host_ips:
                body.hosts.append(host)
                newly_added_ips.append(host.ip)
            else:
                imported_res_dict["Host Mappings"].append(host.ip)
        if newly_added_ips:
            cohesity_client.network.create_append_hosts(body)
            imported_res_dict["Host Mappings"].extend(newly_added_ips)
    except Exception as err:
        ERROR_LIST.append(
            "Error occurred while creating host mapping entry. Error details %s" % err
        )

def add_routes():
    """
    Function to import routes.
    """
    try:
        exported_routes = cluster_dict["routes"]
        existing_routes = library.get_routes(cohesity_client)
        existing_route_ifaces = [route.iface_group_name for route in existing_routes]
        for route in exported_routes:
            # If route is already added, skip else create an entry.
            if route.iface_group_name not in existing_route_ifaces:
                cohesity_client.routes.add_route(route)
            imported_res_dict["Routes"].append(route.iface_group_name)
    except Exception as err:
        ERROR_LIST.append(
            "Error occurred while adding routes. Error details %s" % err
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
    logger.info("Importing Host mapping\n\n")
    create_host_mapping()
    logger.info("Importing Routes\n\n")
    add_routes()
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
