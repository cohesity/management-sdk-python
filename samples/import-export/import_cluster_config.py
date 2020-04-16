import json
import time
import pickle
import library
import logging
import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

# Fetch the Cluster credentials from config file.
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
cluster_dict = pickle.load(open("cluster_config.txt", "rb"))

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


def create_source(source, environment, node):
    """
    """
    try:
        body = RegisterProtectionSourceParameters()
        body.environment = environment
        if environment == "kGenericNas":
            from cohesity_management_sdk.models.nas_mount_credential_params import NasMountCredentialParams
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            res_type = protect_source["nasProtectionSource"]["type"]
            host_type = protect_source["nasProtectionSource"]["protocol"]
            body.endpoint = endpoint
            body.nas_type = res_type
            body.nas_mount_credentials = NasMountCredentialParams()
            body.nas_mount_credentials.nas_protocol = host_type
            body.nas_mount_credentials.nas_type = res_type
            logger.info("Registering source %s" % (endpoint))
            result = register_source(body, source)

        elif environment == "kPhysical":
            protect_source = node["protectionSource"]
            endpoint = protect_source["name"]
            environ = protect_source["environment"]
            res_type = protect_source["physicalProtectionSource"]["type"]
            host_type = protect_source["physicalProtectionSource"]["hostType"]
            body.endpoint = endpoint
            body.environment = environment
            body.physical_type = res_type
            body.host_type = host_type
            logger.info("Registering source %s" % (endpoint))
            result = register_source(body, source)

        elif environment in ["kVMware", "kView"]:
            source_name = source.protection_source.name
            logger.info("Registering source %s" % (source_name))
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
                #password = configparser.get(source.protection_source.name, "password")
                #body.password = password
                body.password = "Cohe$1ty"
            if env_type == "kvCloudDirector":
                return
            if env == "view":
                body.view_type = "kViewBox"
            result = register_source(body, source)
            time.sleep(sleep_time)
    except Exception as e:
        logger.info(e)

def register_source(body, source):
    """
    Registers the protection source.
    """
    try:
        result = cohesity_client.protection_sources.create_register_protection_source(
            body)
        source_mapping[source.protection_source.id] = result.id
        source_ids.append(result.id)
        logger.info("Source registration '%s' is successful." %
                    (body.endpoint))
        return result
    except RequestErrorErrorException as e:
        logger.info(e)
    except APIException as e:
        logger.info(e)
    except Exception as e:
        logger.info(e)


def create_storage_domain():
    """
    Fetches existing storage domain list. Create new domain if the exported
    domain is not available.
    """
    existing_storage_domain_list = {}
    logger.info("Importing Storage domains")
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
                logger.info("Creating storage domain '%s'" %
                            (storage_domain.name))
                result = cohesity_client.view_boxes.create_view_box(
                    storage_domain)
                sds.append(result.id)
                storage_domain_mapping[storage_domain.id] = result.id
            except RequestErrorErrorException as e:
                logger.info(e)
            except APIException as e:
                logger.info(e)
    except Exception as err:
        logger.info(err)


def create_protection_source():
    """
    Creates protection source
    """
    registered_source_list = {}
    sources = cluster_dict.get("sources", [])
    logger.info("Importing protection sources")
    try:
        existing_sources = library.get_protection_sources(cohesity_client)

        for source in existing_sources:
            env = (source.protection_source.environment)
            if env not in ["kPhysical", "kVMware", "KView", "kGenericNas"]:
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

        logger.info(registered_source_list)
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
                    logger.info("Source '%s' already registered, ignoring." % (source_name))
                    continue
                #else:
                #    nodes = nodes[-1]

            for node in nodes:
                name = node["protectionSource"]["name"]
                id = node["protectionSource"]["id"]
                if name in registered_source_list.keys():
                    source_mapping[id] = registered_source_list[name]
                    logger.info("Source '%s' already registered, ignoring." % (name))
                    continue

                create_source(source, environment, node)

    except Exception as err:
        logger.info(err)


def create_view():
    """
    Fetches list of views available in the cluster, adds new view if the
    view is not available in exported list.
    """
    logger.info("Importing protection views")
    view_list = cluster_dict.get("views", [])
    existing_views = library.get_views(cohesity_client)
    existing_view_dict = {}
    for view in existing_views:
        existing_view_dict[view.name] = view.view_id

    for view in view_list:
        logger.info("Creating protection view '%s'" % (view.name))
        try:
            if view.name in existing_view_dict.keys():
                logger.info("Protection view '%s' already available." %
                            (view.name))
                view_mapping[view.name] = existing_view_dict[view.name]
                continue
            view.view_box_id = storage_domain_mapping[view.view_box_id]
            result = cohesity_client.views.create_view(view)
            view_mapping[view.name] = result.name
            view_ids.append(result.name)
            time.sleep(sleep_time)
        except RequestErrorErrorException as e:
            logger.info(e)
        except APIException as e:
            logger.info(e)
        except Exception as err:
            logger.info(err)


def create_protection_policy():
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
                policy_mapping[policy.id] = existing_policy_list[policy.name]
                continue

            if not policy.incremental_scheduling_policy.daily_schedule:
                policy.incremental_scheduling_policy.daily_schedule = {}

            if not policy.incremental_scheduling_policy.monthly_schedule:
                policy.incremental_scheduling_policy.monthly_schedule = {}

            result = cohesity_client.protection_policies.create_protection_policy(
                policy)
            policy_ids.append(result.id)
            policy_mapping[policy.id] = result.id
            time.sleep(sleep_time)

        except RequestErrorErrorException as e:
            logger.info(e)
        except APIException as e:
            logger.info(e)
        except Exception as err:
            logger.info(err)


def create_protection_job():
    """
    Creates protection job.
    """
    existing_job_list = []
    active_protection_jobs = []

    protection_job_list = cluster_dict.get("protection_jobs", [])
    exported_protection_source_objects = cluster_dict.get(
        "protection_objects", {})
    existing_jobs = library.get_protection_jobs(cohesity_client)

    for job in existing_jobs:
        existing_job_list.append(job.name)

    try:
        for each_job in protection_job_list:
            name = each_job.name

            if not each_job.is_deleted:
                active_protection_jobs.append(each_job)

        for protection_job in active_protection_jobs:
            source_list = []
            exported_sources_list = {}

            if protection_job.parent_source_id not in source_mapping.keys():
                continue
            name = protection_job.name
            logger.info("Creating protection job '%s'" % name)
            # Check if the protection source is already available.
            if protection_job.name in existing_job_list:
                logger.debug("Protection job '%s' already available." % name)
                continue

            source_id_list = protection_job.source_ids
            parent_id = protection_job.parent_source_id

            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            if protection_job.environment in ["kPhysical"]:
                pass

            # UUID list for VMware resources.
            uuid_list = []
            # logger.info(exported_protection_source_objects)
            count = 0
            list_len = len(source_id_list)

            # logger.info(exported_protection_source_objects)
            res = (exported_protection_source_objects[parent_id])
            for res in exported_protection_source_objects[parent_id]:
                if res.id in source_id_list:
                    if res.environment == "kVMware":
                        uuid_list.append(res.vmware_protection_source.id.uuid)
                    exported_sources_list[res.name] = res.parent_id
                    count += 1
                if count == list_len:
                    break

            for res in library.get_protection_source_object_by_id(cohesity_client, source_mapping[parent_id]):
                if res.environment == "kVMware" and res.vmware_protection_source.id.uuid in uuid_list:
                    source_list.append(res.id)

                elif res.name in exported_sources_list.keys() or res.parent_id == source_mapping[parent_id]:
                    # For protection views, view name is required.
                    if protection_job.environment == "kView":
                        protection_job.view_name = res.name
                    source_list.append(res.id)
            protection_job.view_box_id = storage_domain_mapping[protection_job.view_box_id]
            protection_job.source_ids = source_list
            protection_job.parent_source_id = source_mapping[parent_id]
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id)

            if not (source_list and protection_job.policy_id and protection_job.view_box_id):
                continue
            if not (protection_job.policy_id):
                logger.info("protection policy not available")
                continue
            try:
                result = cohesity_client.protection_jobs.create_protection_job(
                    protection_job)
                logger.info("Protection job '%s' is created successfully" % (
                    protection_job.name))
                jobs.append(result.id)
                time.sleep(2 * sleep_time)
            except Exception as e:
                logger.info(e)

    except RequestErrorErrorException as e:
        logger.info(e)
    except APIException as e:
        logger.info(e)
    except Exception as err:
        logger.info(err)


def update_ids():
    with open("del_res.json", "r") as f:
        j = json.load(f)
        logger.info(j)
        j["policies"].extend(policy_ids)
        j["storage_domains"].extend(sds)
        j["views"].extend(view_ids)
        j["sources"].extend(source_ids)
        j["jobs"].extend(jobs)
    with open("del_res.json", "w") as f:
        logger.info(j)
        json.dump(j, f)

if __name__ == "__main__":
    create_protection_source()
    create_protection_policy()
    create_storage_domain()
    create_view()
    create_protection_job()
    update_ids()
