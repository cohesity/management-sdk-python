# Copyright 2020 Cohesity Inc.
#
# Python utility to import the cluster config.
# Expects config.ini to be present in the current directory.
# Usage: python import_cluster_config.py <path/to/file>

import sys
import json
import time
import pickle
import random
import library
import logging
from os import path
import configparser
from collections import defaultdict
from cohesity_management_sdk.models.vault import Vault
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.view_box_pair_info import ViewBoxPairInfo
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
from cohesity_management_sdk.models.register_remote_cluster import RegisterRemoteCluster
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.nas_mount_credential_params import NasMountCredentialParams
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters
from cohesity_management_sdk.models.change_protection_job_state_param import ChangeProtectionJobStateParam


logger = logging.getLogger('import_app')
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
ERROR_LIST = []
configparser = configparser.ConfigParser()
configparser.read('config.ini')
sleep_time = int(configparser.get("import_cluster_config", "api_pause_time"))

cohesity_client = CohesityClient(cluster_vip=configparser.get('import_cluster_config', 'cluster_ip'),
                                 username=configparser.get(
                                     'import_cluster_config', 'username'),
                                 password=configparser.get(
                                     'import_cluster_config', 'password'),
                                 domain=configparser.get('import_cluster_config', 'domain'))


override = configparser.get("import_cluster_config", "override")
# Read the imported cluster configurations from file.
if len(sys.argv) != 2:
    logger.error("Please specify the exported config file.")
    sys.exit(1)
else:
    try:
        cluster_dict = pickle.load(open(sys.argv[1], "rb"))
    except IOError:
        print('Import file does not exist')
        sys.exit(1)


# TODO Delete
view_ids = []
policy_ids = []
sds = []
jobs = []
source_ids = []


policy_mapping = {}
source_mapping = {}
storage_domain_mapping = {}
view_mapping = {}
remote_cluster_mapping = {}
imported_res_dict = defaultdict(list)


export_config = cluster_dict["cluster_config"]
import_config = library.get_cluster_config(cohesity_client)
exported_cluster_partitions = cluster_dict["partitions"]
exported_host_names = [partition.host_name for partition in exported_cluster_partitions]


import_cluster_ip = configparser.get('import_cluster_config', 'cluster_ip')
export_cluster_ip = configparser.get('export_cluster_config', 'cluster_ip')


def import_cluster_config():
    try:
        config = cluster_dict.get("cluster_config")
        existing_config = import_config
        config.name = existing_config.name
        cohesity_client.cluster.update_cluster(config)
        time.sleep(sleep_time)
    except Exception as e:
        logger.error(e)


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

        if vault.config.amazon: # Amazon s3 and Generic s3 targets
            try:
                body = Vault()

                _construct_body(body, vault)
                secret_key = configparser.get(vault.name, "secret_access_key")
                body.config.amazon.secret_access_key = secret_key

                cohesity_client.vaults.create_vault(body)
                imported_res_dict["External Targets"].append(body.name)
                time.sleep(sleep_time)
            except RequestErrorErrorException as e:
                logger.error(e)
            except APIException as e:
                ERROR_LIST.append("Error Adding S3 Target %s, Failed with error %s" % (vault.name, e))
            except Exception as err:
                ERROR_LIST.append("Please add correct config for %s in "
                                  "config.ini" % vault.name)
        if vault.config.nas:
            body = Vault()
            _construct_body(body, vault)
            try:
                cohesity_client.vaults.create_vault(body)
                imported_res_dict["External Targets"].append(body.name)
            except RequestErrorErrorException as e:
                logger.error(e)
            except APIException as e:
                ERROR_LIST.append(
                    "Error Adding S3 Target %s, Failed with error %s" % (
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
        if environment == "kGenericNas":
            source_id = node["protectionSource"]["id"]
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            is_local_mount = False
            if export_cluster_ip in endpoint:
                endpoint = endpoint.replace(export_cluster_ip, import_cluster_ip)
                is_local_mount = True
            else:
                for host in exported_host_names:
                    if host in endpoint:
                        endpoint = endpoint.replace(host, import_cluster_ip)
                        is_local_mount = True
                        break

            res_type = protect_source["nasProtectionSource"]["type"]
            host_type = protect_source["nasProtectionSource"]["protocol"]

            body.endpoint = endpoint
            body.nas_type = res_type
            body.nas_mount_credentials = NasMountCredentialParams()
            body.nas_mount_credentials.nas_protocol = host_type
            body.nas_mount_credentials.nas_type = res_type
            if host_type != "kNfs3":
                # Nfs file system doesn't require credentials
                username = node["registrationInfo"]["nasMountCredentials"].get(
                    "username", None)
                if is_local_mount:
                    password = configparser.get("import_cluster_config", "password")
                else:
                    password = configparser.get(endpoint , "password")
                body.nas_mount_credentials.username = username
                body.nas_mount_credentials.password = password

        elif environment == "kPhysical":
            source_id = node["protectionSource"]["id"]
            body.force_register = True
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            res_type = protect_source["physicalProtectionSource"]["type"]
            host_type = protect_source["physicalProtectionSource"]["hostType"]
            body.endpoint = endpoint
            body.environment = environment
            body.physical_type = res_type
            body.host_type = host_type

        elif environment in ["kVMware", "kView"]:
            env = environment[1:].lower()
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
            body.vmware_type = env_type
            if env_type not in ["kViewBox"]:
                password = configparser.get(source.protection_source.name, "password")
                body.password = password
            if env_type == "kvCloudDirector":
                return
            if env == "view":
                body.view_type = "kViewBox"
        register_sources(body, source_id)
        time.sleep(sleep_time)
    except Exception as e:
        ERROR_LIST.append("Error adding source: %s" % e)

def register_sources(body, source_id):
    """
    Registers the protection source.
    """
    try:
        result = cohesity_client.protection_sources.create_register_protection_source(
            body)
        source_mapping[source_id] = result.id
        source_ids.append(result.id)
        imported_res_dict["Protection Sources"].append(body.endpoint)
        return result

    except Exception as e:
        ERROR_LIST.append("Error occured while creating resource %s" % body.endpoint)
        ERROR_LIST.append(e)


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
                if override:
                    cohesity_client.view_boxes.update_view_box(new_storage_domain_id, storage_domain)
                continue

            try:
                result = cohesity_client.view_boxes.create_view_box(
                    storage_domain)
                sds.append(result.id)
                storage_domain_mapping[storage_domain.id] = result.id
            except RequestErrorErrorException as e:
                ERROR_LIST.append(e)
            except APIException as e:
                ERROR_LIST.append(e)
    except Exception as err:
        logger.info(err)


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
            if env not in ["kPhysical", "kPhysicalFiles", "kVMware", "kView", "kGenericNas"]:
                continue

            id = (source.protection_source.id)
            name = source.protection_source.name
            if env == "kVMware":
                registered_source_list[name] = id
                continue
            
            
            res = library.get_protection_source_by_id(cohesity_client, id, env)
            nodes = res.nodes if res.nodes else []
            for node in nodes:
                registered_source_list[node["protectionSource"]
                                       ["name"]] = node["protectionSource"]["id"]

        for source in sources:
            environment = source.protection_source.environment
            if environment not in ["kPhysical", "kPhysicalFiles", "kVMware", "KView", "kGenericNas"]:
                continue
            source_name = source.protection_source.name
            id = source.protection_source.id

            nodes = cluster_dict.get("source_dct")[id]
            if environment == "kVMware":
                if source_name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[source_name]
                    imported_res_dict["Protection Sources"].append(source_name)
                    continue
            if not nodes:
                continue
            for node in nodes:
                name = node["protectionSource"]["name"]
                if environment == "kGenericNas":
                    for host in exported_host_names:
                        if host in name:
                            name = name.replace(host, import_cluster_ip)

                id = node["protectionSource"]["id"]

                if name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[name]
                    imported_res_dict["Protection Sources"].append(name)
                    #logger.info("Source '%s' already registered, ignoring." % (name))
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
    #logger.info("Importing protection views")
    view_list = cluster_dict.get("views", [])
    existing_views = library.get_views(cohesity_client)
    existing_view_dict = {}
    for view in existing_views:
        existing_view_dict[view.name] = view.view_id
    for view in view_list:
        try:
            if view.name in existing_view_dict.keys():
                imported_res_dict["Protection Views"].append(view.name)
                #logger.info("Cohesity View '%s' already available." %
                #            (view.name))
                if override:
                    cohesity_client.views.update_view(view)
                view_mapping[view.name] = existing_view_dict[view.name]
            else:
                view.view_box_id = storage_domain_mapping[view.view_box_id]
                result = cohesity_client.views.create_view(view)
                view_mapping[view.name] = result.view_id
                view_ids.append(result.name)
                imported_res_dict["Protection Views"].append(view.name)
                time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            logger.error(e)
        except APIException as e:
            logger.error(e)
        except Exception as err:
            logger.error(err)


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
                cohesity_client.protection_policies.update_protection_policy(policy, policy_id)
                continue
            body = ProtectionPolicyRequest()
            _construct_body(body, policy)
            if policy.snapshot_archival_copy_policies and len(\
                    policy.snapshot_archival_copy_policies) != 0:
                for ext_target in policy.snapshot_archival_copy_policies:
                    try:
                        del ext_target._names['id']
                    except KeyError:
                        pass
            result = cohesity_client.protection_policies.create_protection_policy(
                body)
            imported_res_dict["Protection Policies"].append(policy.name)
            policy_ids.append(result.id)
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
    physical_parent_id = None
    active_protection_jobs = []
    protection_job_list = cluster_dict.get("protection_jobs", [])

    existing_jobs = library.get_protection_jobs(cohesity_client)
    for job in existing_jobs:
        existing_job_list[job.name] = job.id

    try:
        for each_job in protection_job_list:
            if not each_job.is_deleted:
                active_protection_jobs.append(each_job)

        for protection_job in active_protection_jobs:
            source_list = []
            is_job_available = False
            name = protection_job.name
            environment = protection_job.environment
            if environment not in ["kPhysical", "kPhysicalFiles", "kVMware", "kView", "kGenericNas"]:
                continue

            if environment == "kView":
                if protection_job.view_box_id not in storage_domain_mapping.keys():
                    continue
                
            elif environment == "kVMware" and  protection_job.parent_source_id not in source_mapping.keys():
                continue

            # Check if the protection source is already available.
            if protection_job.name in existing_job_list.keys():
                imported_res_dict["Protection Jobs"].append(protection_job.name)
                is_job_available = True
                current_job_id = existing_job_list[protection_job.name]
                if not override:
                    continue

            source_id_list = protection_job.source_ids
            parent_id = protection_job.parent_source_id
            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            # UUID list for VMware resources.
            uuid_list = []
            if source_mapping.get(parent_id, None):
                protection_job.parent_id = source_mapping[parent_id]
            list_len = len(source_id_list)
            source = cluster_dict.get("source_dct")[parent_id]

            nodes = source[0].get("nodes", [])
            if not nodes and environment in ["kPhysical", "kPhysicalFiles", "kView"]:
                for each_source in source:
                    id = each_source["protectionSource"]["id"]
                    if id in source_id_list:
                        if environment in ["kPhysical", "kPhysicalFiles"]:
                            if not physical_parent_id:
                                physical_parent_id = library.get_protection_source_by_id(
                                    cohesity_client, id=None, env="kPhysical").protection_source.id
                            source_list.append(source_mapping[id])
                            protection_job.parent_source_id = physical_parent_id
                            if protection_job.source_special_parameters:
                                for ps_source in protection_job.source_special_parameters:
                                    if ps_source.source_id == id:
                                        ps_source.source_id = source_mapping[id]
                        else:
                            protection_job.view_name = each_source["protectionSource"]["name"]


            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                # Fetch the UUID list from with available source ids from exported cluster. VMware
                # resources are provided with UUID and mapping is based on uuid.
                if environment == "kVMware" and node["protectionSource"]["id"] in source_id_list:
                    uuid_list.append(node["protectionSource"]["vmWareProtectionSource"]["id"].get("uuid"))
                if len(uuid_list) == list_len:
                    break

            nodes = []
            if source_mapping.get(parent_id, None):
                nodes = library.get_protection_source_by_id(cohesity_client, source_mapping[parent_id], environment).nodes

            for node in nodes:
                if node.get("nodes", []):
                    nodes.extend(node["nodes"])
                if environment == "kVMware":
                    uuid = node["protectionSource"]["vmWareProtectionSource"]["id"].get("uuid")
                    if uuid in uuid_list and node["protectionSource"]["parentId"] == source_mapping[parent_id]:
                        source_list.append(node["protectionSource"]["id"])
                if len(source_list) == list_len:
                    break

            if environment not in ["kPhysical", "kPhysicalFiles", "kView"] and source_mapping.get(parent_id, None) == None:
                err_msg = "Protection Source not available for job %s" % name
                ERROR_LIST.append(err_msg)
                continue


            protection_job.view_box_id = storage_domain_mapping[protection_job.view_box_id]
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id, None)

    
            if not protection_job.view_box_id:
                ERROR_LIST.append("Viewbox not available for job %s" % name)
                continue

            if not protection_job.policy_id:
                ERROR_LIST.append("Protection policy not available for job %s" % name)
                continue

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
                    jobs.append(current_job_id)
                    imported_res_dict["Protection Jobs"].append(protection_job.name)

                if bool(configparser.get('import_cluster_config',
                                         'pause_jobs')):
                    body = ChangeProtectionJobStateParam()
                    body.pause = True
                    cohesity_client.protection_jobs\
                        .change_protection_job_state(current_job_id, body)
                    time.sleep(2 * sleep_time)
            except Exception as e:
                ERROR_LIST.append("Creating Protection Job failed: %s" % e)

    except RequestErrorErrorException as e:
        logger.info(e)
    except APIException as e:
        logger.info(e)
    except Exception as err:
        logger.info(err)


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
                                    "Remote Cluster pairing not successful" % view_box.local_view_box_name)
                continue

            local_view_box_pair.local_view_box_id = remote_view_box_pair.remote_view_box_id = local_view_box_id
            local_view_box_pair.local_view_box_name = remote_view_box_pair.remote_view_box_name = view_box.local_view_box_name
            local_view_box_pair.remote_view_box_id = remote_view_box_pair.local_view_box_id = view_box.remote_view_box_id
            local_view_box_pair.remote_view_box_name = remote_view_box_pair.local_view_box_name = view_box.remote_view_box_name

            body.view_box_pair_info.append(local_view_box_pair)
            remote_body.view_box_pair_info.append(remote_view_box_pair)
        return body, remote_body

    except Exception as err:
        ERROR_LIST.append(err)


def create_remote_clusters():

    repl_list = {}
    remote_cluster_list = cluster_dict.get("remote_clusters", [])
    existing_cluster_list = library.get_remote_clusters(cohesity_client)

    for cluster in existing_cluster_list:
        repl_list[cluster.name] = cluster.cluster_id

    # if the remote cluster exists then get the ID
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
            #Add the remote cluster first
            if cluster.name not in configparser:
                ERROR_LIST.append("Please add password for remote cluster: %s "
                                  "in config.ini" % cluster.name)
                continue

            remote_cluster_password = configparser.get(cluster.name, 'password')
            cluster.password = remote_cluster_password
            body = RegisterRemoteCluster()
            remote_body = RegisterRemoteCluster()
            _construct_body(body, cluster)
            _construct_body(remote_body, cluster)
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

                interfaces = remote_cohesity_client.remote_cluster.get_remote_cluster_by_id(id=export_config.id)
                if interfaces:
                    interface_group = interfaces[0].network_interface_group
                    remote_body.network_interface_group = interface_group
                else:
                    # Get the interfaces available in remote cluster.
                    interfaces = c2.interface_group.get_interface_groups()
                    if interfaces:
                        remote_body.network_interface_group = interfaces[0].name

                if is_remote_cluster_available:
                    remote_cohesity_client.remote_cluster.update_remote_cluster(import_config.id, remote_body)
                else:
                    remote_cohesity_client.remote_cluster.create_remote_cluster(remote_body)
            except APIException as err:
                if "already been registered" in err.args[0]:
                    pass
                else:
                    raise err

            c2 = CohesityClient(cluster_vip=configparser.get('import_cluster_config', 'cluster_ip'),
                                username=configparser.get('import_cluster_config', 'username'),
                                password=configparser.get('import_cluster_config', 'password'),
                                domain=configparser.get('import_cluster_config', 'domain'))

            interfaces = cohesity_client.interface_group.get_interface_groups()
            if interfaces:
                ifaces = [iface.name for iface in interfaces]
            iface_grp = body.network_interface_group
            body.network_interface_group = ifaces.pop() if iface_grp not in ifaces else iface_grp

            if is_remote_cluster_available:
                cohesity_client.remote_cluster.update_remote_cluster(cluster_id, body)
            cohesity_client.remote_cluster.create_remote_cluster(body)
            imported_res_dict["Remote Clusters"].append(cluster.name)

        except RequestErrorErrorException as e:
            logger.info(e)
        except APIException as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(
                cluster_vip=configparser.get('import_cluster_config',
                                             'cluster_ip'),
                username=configparser.get('import_cluster_config', 'username'),
                password=configparser.get('import_cluster_config', 'password'),
                domain=configparser.get('import_cluster_config', 'domain'))
            if "already been registered" in e.args[0]:
                continue
            ERROR_LIST.append("Remote_cluster registration failed with error: %s" % e.args[0])
        except Exception as e:
            # Since the client is singleton, we are re-initing the class object
            c2 = CohesityClient(
                cluster_vip=configparser.get('import_cluster_config',
                                             'cluster_ip'),
                username=configparser.get('import_cluster_config', 'username'),
                password=configparser.get('import_cluster_config', 'password'),
                domain=configparser.get('import_cluster_config', 'domain'))
            ERROR_LIST.append("Please provide passwords for the remote "
                              "cluster in config.ini, Failed to import remote cluster with error: %s" % e.args[0])


def _construct_body(body, entity):
    items = [item for item in dir(entity)if not item.startswith('__') and not
             item.startswith('_')]
    for item in items:
        if hasattr(getattr(entity, item), 'id'):
            continue
        setattr(body, item, getattr(entity, item))

def _get_sd_id(view_box_name):
    existing_storage_domains = library.get_storage_domains(cohesity_client)
    for sd in existing_storage_domains:
        if sd.name == view_box_name:
            return sd.id
    return -1

def debug():
    with open("del_res.json", "r") as f:
        json_dict = json.load(f)
        json_dict["policies"].extend(policy_ids)
        json_dict["storage_domains"].extend(sds)
        json_dict["views"].extend(view_ids)
        json_dict["sources"].extend(source_ids)
        json_dict["jobs"].extend(jobs)
    with open("del_res.json", "w") as f:
        json.dump(json_dict, f)

if __name__ == "__main__":
    logger.info("Importing cluster config \n\n")
    import_cluster_config()
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
    # debug()


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
