# Copyright 2020 Cohesity Inc.
#
# Python utility to import the cluster config.
# Expects config.ini to be present in the current directory.
# Usage: python import_cluster_config.py <path/to/file>

import copy
import json
import logging
import pickle
import random
import requests
import sys
import time

from collections import defaultdict
from os import path

# Custom module import
import library
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.change_protection_job_state_param import ChangeProtectionJobStateParam
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
from cohesity_management_sdk.models.environment_register_protection_source_parameters_enum \
    import EnvironmentRegisterProtectionSourceParametersEnum as env_enum
from cohesity_management_sdk.models.nas_mount_credential_params import NasMountCredentialParams
from cohesity_management_sdk.models.nas_protocol_enum import NasProtocolEnum as nas_enum
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.register_remote_cluster import RegisterRemoteCluster
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters
from cohesity_management_sdk.models.vault import Vault
from cohesity_management_sdk.models.view_box_pair_info import ViewBoxPairInfo
from cohesity_management_sdk.models.vmware_type_enum import VmwareTypeEnum as vmware_enum
from cohesity_management_sdk.models.type_view_protection_source_enum import TypeViewProtectionSourceEnum as view_enum
from library import RestClient

# Check for python version
if float(sys.version[:3]) >= 3:
    import configparser as configparser
    from configparser import NoSectionError
else:
    import ConfigParser as configparser
    from ConfigParser import NoSectionError
# Disable python warnings.
requests.packages.urllib3.disable_warnings()


logger = logging.getLogger("import_app")
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
ERROR_LIST = []
configparser = configparser.ConfigParser()
configparser.read("config.ini")

sleep_time = int(configparser.get("import_cluster_config", "api_pause_time"))
try:
    cluster_ip = configparser.get("import_cluster_config", "cluster_ip")
    username = configparser.get("import_cluster_config", "username")
    password = configparser.get("import_cluster_config", "password")
    domain = configparser.get("import_cluster_config", "domain")

    cohesity_client = CohesityClient(cluster_vip=cluster_ip,
                                     username=username,
                                     password=password,
                                     domain=domain)
    # Make a function call to validate the credentials.
    cohesity_client.principals.get_user_privileges()
    rest_obj = RestClient(cluster_ip, username, password, domain)
except APIException as err:
    print("Authentication error occurred, error details: %s" % err)
    exit(1)
except Exception as err:
    print("Authentication error occurred, error details: %s" % err)
    exit(1)

# Check for the flags for pause jobs and override.
override = configparser.get(
    "import_cluster_config", "override").capitalize() == "True"
pause_jobs = configparser.get(
    "import_cluster_config", "pause_jobs").capitalize() == "True"
gflag_import = configparser.get(
    "import_cluster_config", "gflag").capitalize() == "True"

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
view_mapping = {}
policy_mapping = {}
source_mapping = {}
remote_cluster_mapping = {}
storage_domain_mapping = {}

imported_res_dict = defaultdict(list)
export_config = cluster_dict["cluster_config"]
import_config = library.get_cluster_config(cohesity_client)
env_list = [env_enum.KGENERICNAS, env_enum.KISILON, env_enum.KPHYSICAL,
            env_enum.KPHYSICALFILES, env_enum.KVIEW, env_enum.K_VMWARE]


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
    available_vaults_dict = {}
    vaults = cluster_dict.get("external_targets")
    available_vaults = library.get_external_targets(cohesity_client)

    for vault in available_vaults:
        available_vaults_dict[vault.name] = vault.id

    for vault in vaults:
        if vault.name in available_vaults_dict.keys():
            imported_res_dict["External Targets"].append(vault.name)
            continue

        if vault.config.amazon:  # Amazon s3 targets
            try:
                body = Vault()
                _construct_body(body, vault)
                secret_key = configparser.get(vault.name, "secret_access_key")
                body.config.amazon.secret_access_key = secret_key
                cohesity_client.vaults.create_vault(body)
                imported_res_dict["External Targets"].append(body.name)
                time.sleep(sleep_time)
            except RequestErrorErrorException as e:
                ERROR_LIST.append(
                    "Error Adding Amazon S3 Target: %s, Failed with error: %s" % (
                        vault.name, e))
            except APIException as e:
                ERROR_LIST.append(
                    "Error Adding Amazon S3 Target: %s, Failed with error: %s" % (
                        vault.name, e))
            except Exception as err:
                ERROR_LIST.append("Please add correct config for %s in "
                                  "config.ini" % vault.name)
        if vault.config.nas:  # Generic s3 targets
            body = Vault()
            _construct_body(body, vault)
            try:
                cohesity_client.vaults.create_vault(body)
                imported_res_dict["External Targets"].append(body.name)
            except RequestErrorErrorException as e:
                ERROR_LIST.append(
                    "Error Adding S3 Target: %s, Failed with error: %s" % (
                        vault.name, e))
            except APIException as e:
                ERROR_LIST.append(
                    "Error Adding S3 Target: %s, Failed with error: %s" % (
                        vault.name, e))
            except Exception as err:
                ERROR_LIST.append("Please add correct config for %s in "
                                  "config.ini" % vault.name)


def create_sources(source, environment, node):
    """
    """
    try:
        body = RegisterProtectionSourceParameters()
        body.environment = environment
        if environment == env_enum.KGENERICNAS:
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
            if host_type != nas_enum.KNFS3:
                # Nfs file system doesn't require credentials
                username = node["registrationInfo"]["nasMountCredentials"].get(
                    "username", None)
                if is_local_mount:
                    password = configparser.get(
                        "import_cluster_config", "password")
                else:
                    password = configparser.get(endpoint, "password")
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

        elif environment == env_enum.KISILON:
            # Since public API is not available for Isilon source registration
            # registering source using private API call.
            # entity type 14 is reserved for Isilon source.
            body = {
                "entity": {
                    "type": 14,
                    "isilonEntity": {
                        "type": 0
                    }
                },
                "entityInfo": {
                    "endpoint": "",
                    "type": 14,
                    "credentials": {
                        "password": "",
                        "username": ""
                    }
                }
            }
            source_id = source.protection_source.id
            username = source.registration_info.username
            endpoint = source.registration_info.access_info.endpoint
            name = source.protection_source.isilon_protection_source.name
            password = configparser.get(name, "password")
            body["entityInfo"]["endpoint"] = endpoint
            body["entityInfo"]["credentials"]["username"] = username
            body["entityInfo"]["credentials"]["password"] = password
            # Private api to register protection sources.
            api = "backupsources"
            code, resp = rest_obj.post(api, data=json.dumps(body))
            if code != 200:
                ERROR_LIST.append(
                    "Error adding source : %s failed with error : %s" % (
                        name, resp))
            else:
                result = json.loads(resp.decode("utf-8"))
                source_mapping[source_id] = result["entity"]["id"]
                imported_res_dict["Protection Sources"].append(name)
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
    except NoSectionError as e:
        ERROR_LIST.append("Please provide password for source %s " % (
            name))
    except Exception as e:
        ERROR_LIST.append("Error adding source : %s failed with error : %s" % (
            name, e))


def register_sources(body, name, source_id):
    """
    Registers the protection source.
    """
    try:
        result = cohesity_client.protection_sources.create_register_protection_source(
            body)
        source_mapping[source_id] = result.id
        imported_res_dict["Protection Sources"].append(body.endpoint)
        return result

    except Exception as e:
        ERROR_LIST.append(
            "Error adding source : %s, failed with error : %s" % (
                name, e))


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

        for storage_domain in storage_domain_list:
            if storage_domain.name in existing_storage_domain_list.keys():
                new_storage_domain_id = existing_storage_domain_list[storage_domain.name]
                storage_domain_mapping[storage_domain.id] = new_storage_domain_id
                imported_res_dict["Storage Domains"].append(storage_domain.name)
                if override:
                    cohesity_client.view_boxes.update_view_box(
                        new_storage_domain_id, storage_domain)
                continue

            try:
                result = cohesity_client.view_boxes.create_view_box(
                    storage_domain)
                storage_domain_mapping[storage_domain.id] = result.id
                imported_res_dict["Storage Domains"].append(storage_domain.name)
            except RequestErrorErrorException as e:
                ERROR_LIST.append(
                    "Error adding storage domain %s, Failed with error %s" % (
                        storage_domain.name, e))
            except APIException as e:
                ERROR_LIST.append(
                    "Error adding storage domain %s, Failed with error %s" % (
                        storage_domain.name, e))
    except Exception as err:
        ERROR_LIST.append("Error while adding storage domains")


def create_protection_sources():
    """
    Creates protection source
    """
    registered_source_list = {}
    sources = cluster_dict.get("sources", [])

    try:
        existing_sources = library.get_protection_sources(cohesity_client)

        for source in existing_sources:
            env = (source.protection_source.environment)
            if env not in env_list:
                continue

            id = source.protection_source.id
            name = source.protection_source.name
            if env in [env_enum.KISILON, env_enum.K_VMWARE]:
                registered_source_list[name] = id
                continue

            res = library.get_protection_source_by_id(cohesity_client, id, env)
            nodes = res.nodes if res.nodes else []
            for node in nodes:
                registered_source_list[node["protectionSource"]
                                       ["name"]] = node["protectionSource"]["id"]

        for source in sources:
            environment = source.protection_source.environment
            if environment not in env_list:
                continue
            source_name = source.protection_source.name
            id = source.protection_source.id

            if environment == env_enum.KVIEW:
                # Views are not created as a part of sources.
                continue
            nodes = cluster_dict.get("source_dct")[id]
            if environment in [env_enum.K_VMWARE, env_enum.KISILON]:
                if source_name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[source_name]
                    imported_res_dict["Protection Sources"].append(source_name)
                    if override:
                        cohesity_client.protection_sources.create_refresh_protection_source_by_id(
                            registered_source_list[source_name])
                    continue
                elif environment == env_enum.KISILON:
                    create_sources(source, environment, None)
                    continue
            if not nodes:
                continue
            for node in nodes:
                id = node["protectionSource"]["id"]
                name = node["protectionSource"]["name"]
                if name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[name]
                    imported_res_dict["Protection Sources"].append(name)
                    if override:
                        cohesity_client.protection_sources.create_refresh_protection_source_by_id(
                            registered_source_list[name])
                    continue
                create_sources(source, environment, node)

    except Exception as err:
        ERROR_LIST.append("Error adding source: %s, failed with error: %s" %
                          (name, err))


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
                view_box_id = storage_domain_mapping.get(
                    view.view_box_id, None)
                if not view_box_id:
                    ERROR_LIST.append(
                        "Storage domain not avaialble for view %s" % view.name)
                    continue
                view.view_box_id = view_box_id
                result = cohesity_client.views.create_view(view)
                view_mapping[view.name] = result.view_id
                imported_res_dict["Protection Views"].append(view.name)
                time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            ERROR_LIST.append("Error adding view %s, Failed with error %s" % (
                view.name, e))
        except APIException as e:
            ERROR_LIST.append("Error adding view %s, Failed with error %s" % (
                view.name, e))
        except Exception as err:
            ERROR_LIST.append("Error adding view %s, Failed with error %s" % (
                view.name, err))


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

            if is_policy_available:
                cohesity_client.protection_policies.update_protection_policy(
                    policy, policy_id)
                continue
            body = ProtectionPolicyRequest()
            _construct_body(body, policy)
            if policy.snapshot_archival_copy_policies and len(
                    policy.snapshot_archival_copy_policies) != 0:
                for ext_target in policy.snapshot_archival_copy_policies:
                    try:
                        del ext_target._names["id"]
                    except KeyError:
                        pass
            result = cohesity_client.protection_policies.create_protection_policy(
                body)
            imported_res_dict["Protection Policies"].append(policy.name)
            policy_mapping[policy.id] = result.id
            time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            ERROR_LIST.append("Error creating Policy: %s, failed with error: "
                              "%s" % (policy.name, e))
        except APIException as e:
            ERROR_LIST.append("Error creating Policy: %s, failed with error: "
                              "%s" % (policy.name, e))
        except Exception as e:
            ERROR_LIST.append("Error creating Policy: %s, failed with error: "
                              "%s" % (policy.name, e))


def create_protection_jobs():
    """
    Creates protection job.
    """
    existing_job_list = {}
    active_protection_jobs = []
    active_protection_jobs = cluster_dict.get("protection_jobs", [])

    existing_jobs = library.get_protection_jobs(cohesity_client)
    for job in existing_jobs:
        existing_job_list[job.name] = job.id

    try:
        for protection_job in active_protection_jobs:
            source_list = []
            _parent_id = None
            is_job_available = False
            job_name = protection_job.name
            environment = protection_job.environment
            parent_id = protection_job.parent_source_id

            if environment not in env_list:
                continue
            if environment == env_enum.KVIEW:
                if protection_job.view_box_id not in storage_domain_mapping.keys():
                    continue
            elif environment not in [env_enum.KPHYSICAL, env_enum.KPHYSICALFILES, env_enum.KVIEW] and source_mapping.get(parent_id, None) == None:
                err_msg = "Protection Source not available for job %s" % job_name
                ERROR_LIST.append(err_msg)
                continue

            # Check if the protection source is already available.
            if protection_job.name in existing_job_list.keys():
                imported_res_dict["Protection Jobs"].append(
                    protection_job.name)
                is_job_available = True
                current_job_id = existing_job_list[protection_job.name]
                if not override:
                    continue

            source_id_list = protection_job.source_ids
            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            # UUID list for VMware resources.
            uuid_list = []

            if source_mapping.get(parent_id, None):
                protection_job.parent_id = source_mapping[parent_id]

            list_len = len(source_id_list)
            protection_job.view_box_id = storage_domain_mapping.get(
                protection_job.view_box_id, None)
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id, None)

            if not protection_job.view_box_id:
                ERROR_LIST.append(
                    "Viewbox not available for job %s" % job_name)
                continue

            if not protection_job.policy_id:
                ERROR_LIST.append(
                    "Protection policy not available for job %s" % job_name)
                continue
            sources = cluster_dict["source_dct"].get(parent_id, [])
            nodes = []
            for source in sources:
                nodes.extend(source.get("nodes", []))

            copy_env_list = copy.deepcopy(env_list)
            copy_env_list.pop(copy_env_list.index(env_enum.K_VMWARE))
            copy_env_list.pop(copy_env_list.index(env_enum.KISILON))
            to_proceed = True

            if not nodes and environment in copy_env_list:
                for each_source in sources:
                    id = each_source["protectionSource"]["id"]
                    if id in source_id_list:
                        if environment in [
                                env_enum.KPHYSICAL, env_enum.KPHYSICALFILES, env_enum.KGENERICNAS]:
                            env = env_enum.KPHYSICAL if "Physical" in environment else env_enum.KGENERICNAS
                            obj = library.get_protection_source_by_id(
                                cohesity_client, id=None, env=env)
                            if not obj or source_mapping.get(id, None) == None:
                                ERROR_LIST.append(
                                    "Protection Source not available for job %s" % job_name)
                                to_proceed = False
                                break
                            _parent_id = obj.protection_source.id

                            source_list.append(source_mapping[id])
                            protection_job.parent_source_id = _parent_id
                            if protection_job.source_special_parameters:
                                for ps_source in protection_job.source_special_parameters:
                                    if ps_source.source_id == id:
                                        ps_source.source_id = source_mapping[id]
                        else:
                            protection_job.view_name = each_source[
                                "protectionSource"]["name"]
            # Check to break from loop if protection source for job is not
            # available.
            if not to_proceed:
                continue
            uuid_source_mapping = {}
            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                # Fetch the UUID list from with available source ids from
                # exported cluster. VMware resources are provided with UUID
                # and mapping is based on uuid.
                if environment == env_enum.K_VMWARE and node["protectionSource"][
                        "id"] in source_id_list:
                    uuid_list.append(node["protectionSource"][
                        "vmWareProtectionSource"]["id"].get("uuid"))
                    uuid_source_mapping[uuid_list[-1]] = node[
                        "protectionSource"]["id"]
                if environment == env_enum.KISILON and node["protectionSource"][
                        "id"] in source_id_list:
                    uuid_source_mapping[node["protectionSource"]["name"]] = \
                        node["protectionSource"]["isilonProtectionSource"][
                        "mountPoint"]["accessZoneName"]
                if len(uuid_list) == list_len:
                    break
            nodes = []

            if source_mapping.get(parent_id, None):
                nodes = library.get_protection_source_by_id(
                    cohesity_client, source_mapping[parent_id], environment).nodes
            source_spl_params = protection_job.source_special_parameters
            source_object_dct = {}
            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                if environment == env_enum.K_VMWARE:
                    uuid = node["protectionSource"]["vmWareProtectionSource"][
                        "id"].get("uuid")
                    if uuid in uuid_list and node["protectionSource"][
                            "parentId"] == source_mapping[parent_id]:
                        id = node["protectionSource"]["id"]
                        source_list.append(id)
                        source_object_dct[uuid_source_mapping[uuid]] = id
                if environment == env_enum.KISILON:
                    name = node["protectionSource"]["name"]
                    if node["protectionSource"]["isilonProtectionSource"].get(
                            "mountPoint", None) == None:
                        mount_point = node["protectionSource"]["isilonProtectionSource"][
                            "accessZone"]["name"]
                    else:
                        mount_point = node["protectionSource"]["isilonProtectionSource"][
                            "mountPoint"]["accessZoneName"]
                    if name in uuid_source_mapping.keys() and mount_point == \
                            uuid_source_mapping[name]:
                        name = node["protectionSource"]["name"]
                        protocol = node["protectionSource"]["isilonProtectionSource"][
                            "mountPoint"]["protocols"]
                        if "kNfs" in protocol:
                            source_list.append(node["protectionSource"]["id"])
                        else:
                            # flag set to skip protection job creation which contains
                            # objects with SMB protocol.
                            to_proceed = False
                            ERROR_LIST.append(
                                "Protection job '%s' contain objects %s of "
                                "following protocol %s. Supported protocol is kNfs." % (
                                    job_name, name, ", ".join(protocol)))
                            break
                if len(source_list) == list_len:
                    break
            # Check to break from loop.
            if not to_proceed:
                continue
            if source_spl_params and environment == env_enum.K_VMWARE:
                for param in source_spl_params:
                    if param.source_id in source_object_dct.keys():
                        param.source_id = source_object_dct[param.source_id]

            if source_list:
                protection_job.source_ids = source_list

            if source_mapping.get(parent_id, ""):
                protection_job.parent_source_id = source_mapping[parent_id]

            try:
                if override and is_job_available:
                    cohesity_client.protection_jobs.update_protection_job(
                        protection_job, current_job_id)
                else:
                    result = cohesity_client.protection_jobs.create_protection_job(
                        protection_job)
                    current_job_id = result.id
                    imported_res_dict["Protection Jobs"].append(job_name)

                if pause_jobs:
                    body = ChangeProtectionJobStateParam()
                    body.pause = True
                    cohesity_client.protection_jobs\
                        .change_protection_job_state(current_job_id, body)
                    time.sleep(2 * sleep_time)
            except Exception as e:
                ERROR_LIST.append(
                    "Creating Protection Job '%s' failed with error: %s" % (
                        job_name, e))

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
                ERROR_LIST.append("Failed to find Storage domain %s, "
                                  "Remote Cluster pairing not successful" %
                                  view_box.local_view_box_name)
                continue

            local_view_box_pair.local_view_box_id = \
                remote_view_box_pair.remote_view_box_id = local_view_box_id
            local_view_box_pair.local_view_box_name = \
                remote_view_box_pair.remote_view_box_name = view_box.local_view_box_name
            local_view_box_pair.remote_view_box_id = \
                remote_view_box_pair.local_view_box_id = view_box.remote_view_box_id
            local_view_box_pair.remote_view_box_name = \
                remote_view_box_pair.local_view_box_name = view_box.remote_view_box_name

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

    # If the remote cluster exists then get the ID.
    for cluster in remote_cluster_list:
        # Check the remote cluster registered is not the current cluster.
        if cluster.remote_ips[0] == import_cluster_ip:
            continue

        is_remote_cluster_available = False
        if cluster.name in repl_list.keys():
            if not override:
                continue
            is_remote_cluster_available = True
        try:
            # Add the remote cluster first
            if cluster.name not in configparser.sections():
                ERROR_LIST.append("Please add password for remote cluster: %s "
                                  "in config.ini" % cluster.name)
                continue
            remote_cluster_password = configparser.get(
                cluster.name, "password")
            cluster_password = configparser.get(
                "import_cluster_config", "password")
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
                    cluster.view_box_pair_info, body, remote_body)
            body.local_ips = remote_body.remote_ips = local_ips
            body.remote_ips = remote_body.local_ips = remote_ips
            try:
                remote_cohesity_client = CohesityClient(
                    cluster_vip=remote_ips[0],
                    username=cluster.user_name,
                    password=remote_cluster_password)

                interfaces = remote_cohesity_client.remote_cluster.get_remote_cluster_by_id(
                    id=export_config.id)

                if interfaces:
                    interface_group = interfaces[0].network_interface_group
                    remote_body.network_interface_group = interface_group
                else:
                    # Get the interfaces available in remote cluster.
                    interfaces = cohesity_client.interface_group.get_interface_groups()
                    if interfaces:
                        remote_body.network_interface_group = interfaces[0].name

                if is_remote_cluster_available:
                    remote_cohesity_client.remote_cluster.update_remote_cluster(
                        import_config.id, remote_body)
                else:
                    remote_cohesity_client.remote_cluster.create_remote_cluster(
                        remote_body)
            except APIException as err:
                if "already been registered" in err.args[0]:
                    pass
                else:
                    raise err

            c2 = CohesityClient(cluster_vip=configparser.get(
                "import_cluster_config", "cluster_ip"),
                username=configparser.get(
                "import_cluster_config", "username"),
                password=configparser.get(
                "import_cluster_config", "password"),
                domain=configparser.get(
                "import_cluster_config", "domain"))

            interfaces = cohesity_client.interface_group.get_interface_groups()
            if interfaces:
                ifaces = [iface.name for iface in interfaces]
            iface_grp = body.network_interface_group
            body.network_interface_group = ifaces.pop() if iface_grp not in \
                ifaces else iface_grp

            if is_remote_cluster_available:
                cohesity_client.remote_cluster.update_remote_cluster(
                    cluster_id, body)
            else:
                cohesity_client.remote_cluster.create_remote_cluster(body)
            imported_res_dict["Remote Clusters"].append(cluster.name)

        except RequestErrorErrorException as e:
            ERROR_LIST.append(e)
        except APIException as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(cluster_vip=configparser.get(
                "import_cluster_config", "cluster_ip"),
                username=configparser.get(
                    "import_cluster_config", "username"),
                password=configparser.get(
                    "import_cluster_config", "password"),
                domain=configparser.get(
                    "import_cluster_config", "domain"))
            if "already been registered" in e.args[0]:
                continue
            ERROR_LIST.append("Registering remote cluster %s failed with "
                              "error: %s" % (cluster.name, e.args[0]))
        except Exception as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(
                cluster_vip=configparser.get(
                    "import_cluster_config", "cluster_ip"),
                username=configparser.get(
                    "import_cluster_config", "username"),
                password=configparser.get(
                    "import_cluster_config", "password"),
                domain=configparser.get(
                    "import_cluster_config", "domain"))
            ERROR_LIST.append("Registering remote cluster %s failed with "
                              "error: %s" % (cluster.name, e.args[0]))


def _construct_body(body, entity):
    items = [item for item in dir(entity)if not item.startswith("__") and not
             item.startswith("_")]
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
        cluster_ip = configparser.get('import_cluster_config', 'cluster_ip')
        username = configparser.get('import_cluster_config', 'username')
        password = configparser.get('import_cluster_config', 'password')
        domain = configparser.get('import_cluster_config', 'domain')
        # Update the flags from exported cluster.
        exported_gflags = json.loads(cluster_dict["gflag"])
        for body in exported_gflags:
            code, resp = library.gflag(
                cluster_ip, username, password, domain, json.dumps(body), "put")
            if code not in [200, 204]:
                ERROR_LIST.append("Failed to update gflag for service %s" % (
                    body["serviceName"]))
                continue
            imported_res_dict["Gflag services"].append(body["serviceName"])
    except Exception as err:
        ERROR_LIST.append(
            "Error occurred while updating gflags. Error details %s" % err)


if __name__ == "__main__":
    logger.info("Importing cluster config \n\n")
    import_cluster_config()
    # Gflags are imported from cluster based on flag value.
    if gflag_import:
        logger.info("Importing gflags \n\n")
        update_gflags()
    logger.info("Importing Storage domains \n\n")
    create_storage_domains()
    logger.info("Importing remote clusters  \n\n")
    create_remote_clusters()
    logger.info("Importing Views  \n\n")
    create_views()
    logger.info("Importing Targets  \n\n")
    create_vaults()
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
