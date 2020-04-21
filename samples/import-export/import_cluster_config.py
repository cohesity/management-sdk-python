# Copyright 2020 Cohesity Inc.
#
# Python utility to import the cluster config.
# Expects config.ini to be present in the current directory.
# Usage: python import_cluster_config.py <path/to/file>

import sys
from os import path

import json
import time
import pickle
import random
import library
import logging
import configparser
from cohesity_management_sdk.models.vault import Vault
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
from cohesity_management_sdk.models.register_remote_cluster import RegisterRemoteCluster
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
ERROR_LIST = []
configparser = configparser.ConfigParser()
configparser.read('config.ini')
sleep_time = int(configparser.get("sleep", "time"))
cohesity_client = CohesityClient(cluster_vip=configparser.get('import_cluster_config', 'cluster_ip'),
                                 username=configparser.get(
                                     'import_cluster_config', 'username'),
                                 password=configparser.get(
                                     'import_cluster_config', 'password'),
                                 domain=configparser.get('import_cluster_config', 'domain'))

# Read the imported cluster configurations from file.
if len(sys.argv) != 2:
    logger.error("Please specify the exported config file.")
    sys.exit(1)
if not path.exists(sys.argv[1]):
    logger.error("Exported Config file does not exist")
    sys.exit(1)

else:
    cluster_dict = pickle.load(open(sys.argv[1], "rb"))

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
from collections import defaultdict
imported_res_dict = defaultdict(list)

cluster_name = ""
node_ips = []
export_config = cluster_dict["cluster_config"]
import_config = library.get_cluster_config(cohesity_client)
import_cluster_ip = configparser.get('import_cluster_config', 'cluster_ip')
export_cluster_ip = configparser.get('export_cluster_config', 'cluster_ip')

def import_cluster_config():
    try:
        config = cluster_dict["cluster_config"]
        cluster_name = config.name
        node_ips = config.node_ips
        #cohesity_client.cluster.update_cluster(config)
    except Exception as e:
        logger.error(e)



def create_vaults():
    available_vaults_dict = {}
    vaults = cluster_dict.get("external_targets")
    available_vaults = library.get_external_targets(cohesity_client)

    for vault in available_vaults:
        available_vaults_dict[vault.name] = vault.id
    
    for vault in vaults:
        if not vault.config.nas:
            continue
        body = Vault()
        vault_name =  vault.name# + "_" + "1"
        if vault_name in available_vaults_dict.keys():
            imported_res_dict["External Targets"].append(vault.name)
            continue
        _construct_body(body, vault)
        if vault.config.nas and vault.config.nas.mount_path: 
            try:
                body.name = vault.name #str(random.choice(range(100)))
                if vault.config.nas.host == export_cluster_ip:
                    body.config.nas.host = import_cluster_ip
                res = cohesity_client.vaults.create_vault(body)
                imported_res_dict["External Targets"].append(body.name)
            except Exception as e:
                logger.info(e)


def create_sources(source, environment, node):
    """
    """
    try:
        body = RegisterProtectionSourceParameters()
        body.environment = environment
        if environment == "kGenericNas":
            from cohesity_management_sdk.models.nas_mount_credential_params import NasMountCredentialParams
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            # share_list = []

            # for i in cohesity_client.views.get_views_by_share_name().shares_list:
            #     share_list.append(i.nfs_mount_path)

            # for val in filter(None, share_list):
            #     if endpoint.split(":")[-1] == val.split(":"):
            #         endpoint = val

            #endpoint = cluster_ip + ":" + endpoint.split(":")[-1]
            
            if export_config.name in endpoint:
                endpoint = endpoint.replace(export_config.name, import_cluster_ip)#import_config.name)
            elif export_cluster_ip in endpoint:
                endpoint = endpoint.replace(export_cluster_ip, import_cluster_ip)
            res_type = protect_source["nasProtectionSource"]["type"]
            host_type = protect_source["nasProtectionSource"]["protocol"]
            body.endpoint = endpoint
            body.nas_type = res_type
            body.nas_mount_credentials = NasMountCredentialParams()
            body.nas_mount_credentials.nas_protocol = host_type
            body.nas_mount_credentials.nas_type = res_type
            #logger.info("Registering source %s" % (endpoint))

        elif environment == "kPhysical":
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            res_type = protect_source["physicalProtectionSource"]["type"]
            host_type = protect_source["physicalProtectionSource"]["hostType"]
            body.endpoint = endpoint
            body.environment = environment
            body.physical_type = res_type
            body.host_type = host_type
            #logger.info("Registering source %s" % (endpoint))

        elif environment in ["kVMware", "kView"]:
            #source_name = source.protection_source.name
            #logger.info("Registering source %s" % (source_name))
            env = environment[1:].lower()
            body.username = source.registration_info.username
            body.environment = environment

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
        register_sources(body, source)
        time.sleep(sleep_time)
    except Exception as e:
        logger.info(e)

def register_sources(body, source):
    """
    Registers the protection source.
    """
    try:
        result = cohesity_client.protection_sources.create_register_protection_source(
            body)
        source_mapping[source.protection_source.id] = result.id
        source_ids.append(result.id)
        imported_res_dict["Protection Sources"].append(body.endpoint)
        #logger.info("Source registration '%s' is successful." %
        #            (body.endpoint))
        return result
    except RequestErrorErrorException as e:
        ERROR_LIST.append(e)
    except APIException as e:
        ERROR_LIST.append(e)
    except Exception as e:
        ERROR_LIST.append(e)


def create_storage_domains():
    """
    Fetches existing storage domain list. Create new domain if the exported
    domain is not available.
    """
    existing_storage_domain_list = {}
    #logger.info("Importing Storage domains")
    try:
        existing_storage_domains = library.get_storage_domains(cohesity_client)

        for storage_domain in existing_storage_domains:
            existing_storage_domain_list[storage_domain.name] = storage_domain.id
        storage_domain_list = cluster_dict.get("storage_domains", [])

        for storage_domain in storage_domain_list:
            if storage_domain.name in existing_storage_domain_list.keys():
                storage_domain_mapping[storage_domain.id] = existing_storage_domain_list[storage_domain.name]
                continue
            try:
                #logger.info("Creating storage domain '%s'" %
                #            (storage_domain.name))
                result = cohesity_client.view_boxes.create_view_box(
                    storage_domain)
                sds.append(result.id)
                storage_domain_mapping[storage_domain.id] = result.id
            except RequestErrorErrorException as e:
                logger.error(e)
            except APIException as e:
                logger.error(e)
    except Exception as err:
        logger.info(err)


def create_protection_sources():
    """
    Creates protection source
    """
    registered_source_list = {}
    sources = cluster_dict.get("sources", [])
    #logger.info("Importing protection sources")
    try:
        existing_sources = library.get_protection_sources(cohesity_client)

        for source in existing_sources:
            env = (source.protection_source.environment)
            if env not in ["kPhysical", "kVMware", "kView", "kGenericNas"]:
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
            if environment not in ["kPhysical", "kVMware", "KView", "kGenericNas"]:
                continue
            source_name = source.protection_source.name
            id = source.protection_source.id

            nodes = cluster_dict.get("source_dct")[id]
            if environment == "kVMware":
                if source_name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[source_name]
                    imported_res_dict["Protection Sources"].append(source_name)
                    #logger.info("Source '%s' already registered, ignoring." % (source_name))
                    continue
                #else:
                #    nodes = nodes[-1]
            if not nodes:
                continue
            for node in nodes:
                name = node["protectionSource"]["name"]
                id = node["protectionSource"]["id"]
                if name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[name]
                    imported_res_dict["Protection Sources"].append(name)
                    #logger.info("Source '%s' already registered, ignoring." % (name))
                    continue

                create_sources(source, environment, node)

    except Exception as err:
        logger.info(err)


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
        try:
            # If policy with same name is already available.
            if policy.name in existing_policy_list.keys():
                imported_res_dict["Protection Policies"].append(policy.name)
                policy_mapping[policy.id] = existing_policy_list[policy.name]
                continue
            
            if not policy.incremental_scheduling_policy.daily_schedule:
                policy.incremental_scheduling_policy.daily_schedule = {}

            if not policy.incremental_scheduling_policy.monthly_schedule:
                policy.incremental_scheduling_policy.monthly_schedule = {}
            body = ProtectionPolicyRequest()
            _construct_body(body, policy)
            result = cohesity_client.protection_policies.create_protection_policy(
                body)
            imported_res_dict["Protection Policies"].append(policy.name)
            policy_ids.append(result.id)
            policy_mapping[policy.id] = result.id
            time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            logger.info(e)
        except APIException as e:
            logger.info(e)
        except Exception as err:
            logger.info(err)


def create_protection_jobs():
    """
    Creates protection job.
    """
    existing_job_list = []
    active_protection_jobs = []

    protection_job_list = cluster_dict.get("protection_jobs", [])

    existing_jobs = library.get_protection_jobs(cohesity_client)
    for job in existing_jobs:
        existing_job_list.append(job.name)

    try:
        for each_job in protection_job_list:
            if not each_job.is_deleted:
                active_protection_jobs.append(each_job)

        for protection_job in active_protection_jobs:
            name = protection_job.name
            environment = protection_job.environment
            source_list = []
            if environment not in ["kPhysical", "kVMware", "kView", "kGenericNas"]:
                continue

            if environment == "kView":
                if protection_job.view_box_id not in storage_domain_mapping.keys():
                    continue
                
            elif environment == "kVMware" and  protection_job.parent_source_id not in source_mapping.keys():
                continue

            # Check if the protection source is already available.
            if protection_job.name in existing_job_list:
                imported_res_dict["Protection Jobs"].append(protection_job.name)
                # logger.debug("Protection job '%s' already available." % name)
                continue

            source_id_list = protection_job.source_ids
            parent_id = protection_job.parent_source_id
            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            # UUID list for VMware resources.
            uuid_list = []

            # logger.info(exported_protection_source_objects)

            list_len = len(source_id_list)
            source = cluster_dict.get("source_dct")[parent_id]

            nodes = source[0].get("nodes", [])
            if not nodes and environment == "kView":
                for each_source in source:
                    if each_source["protectionSource"]["id"] in source_id_list:
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

            if environment != "kView" and source_mapping.get(parent_id, None) == None:
                err_msg = "Protection Source not available for job %s" % name
                ERROR_LIST.append(err_msg)
                continue

            protection_job.view_box_id = storage_domain_mapping[protection_job.view_box_id]
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id, None)

            if not protection_job.view_box_id: #source_list and
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
                result = cohesity_client.protection_jobs.create_protection_job(
                    protection_job)

                #logger.info("Protection job '%s' is created successfully" % (
                #    protection_job.name))
                jobs.append(result.id)
                imported_res_dict["Protection Jobs"].append(protection_job.name)
                time.sleep(2 * sleep_time)
            except Exception as e:
                logger.info(e)

    except RequestErrorErrorException as e:
        logger.info(e)
    except APIException as e:
        logger.info(e)
    except Exception as err:
        logger.info(err)

def create_remote_clusters():

    repl_list = {}
    remote_cluster_list = cluster_dict.get("remote_clusters", [])
    existing_cluster_list = library.get_remote_clusters(cohesity_client)

    for cluster in existing_cluster_list:
        repl_list[cluster.name] = cluster.cluster_id

    # if the remote cluster exists then get the ID
    for cluster in remote_cluster_list:
        if cluster.name in repl_list.keys():
            continue
        try:
            #Add the remote cluster first
            if cluster.name not in configparser:
                ERROR_LIST.append("Please add password for remote cluster %s" % cluster.name)
            remote_cluster_password = configparser.get(cluster.name, 'password')
            # c2 = CohesityClient(cluster_vip=cluster.local_ips[0],
            #                     username=cluster.user_name,
            #                     password=remote_cluster_password)
            cluster.password = remote_cluster_password
            body = RegisterRemoteCluster()
            _construct_body(body, cluster)
            body.cluster_id = None
            for view_box in body.view_box_pair_info:
                local_view_box_id = _get_sd_id(view_box.local_view_box_name)
                if local_view_box_id < 0:
                    ERROR_LIST.append("Failed to find Storage domain %s, "
                                      "Remote Cluster pairing not successful" % view_box.local_view_box_name)
                    continue
                view_box.local_view_box_id = storage_domain_mapping[local_view_box_id]
            body.password = remote_cluster_password
            cohesity_client.remote_cluster.create_remote_cluster(body)
        except RequestErrorErrorException as e:
            logger.info(e)
        except APIException as e:
            logger.info(e)
            ERROR_LIST.append(e)
        except Exception as err:
            logger.info(err)

    # for policy in protection_policy_list:
    #     try:
    #         # If policy with same name is already available.
    #         if policy.name in existing_policy_list.keys():
    #             policy_mapping[policy.id] = existing_policy_list[policy.name]
    #             continue
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
        j = json.load(f)
        #logger.info(j)
        j["policies"].extend(policy_ids)
        j["storage_domains"].extend(sds)
        j["views"].extend(view_ids)
        j["sources"].extend(source_ids)
        j["jobs"].extend(jobs)
    with open("del_res.json", "w") as f:
        #logger.info(j)
        json.dump(j, f)


if __name__ == "__main__":
    # import_cluster_config()
    create_storage_domains()
    create_remote_clusters()
    create_views()
    create_vaults()
    create_protection_sources()
    create_protection_policies()
    create_protection_jobs()
    debug()

logger.info("Please find the imported resources summary.")
for key, val in imported_res_dict.items():
    logger.info("Successfully registered/created the following %s:\n%s\n" % (key, ", ".join(val)))

if ERROR_LIST:
    ERROR_LIST = [str(err) for err in ERROR_LIST]
    logger.error("Please find the error messages,")
    logger.error("\n".join(ERROR_LIST))