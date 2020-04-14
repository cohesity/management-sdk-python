import json
import pickle
import library
import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
from cohesity_management_sdk.models.register_protection_source_parameters import RegisterProtectionSourceParameters
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

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

view_box_mapping = {}

def create_storage_domain():
    existing_storage_domain_list = {}
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
                result = cohesity_client.view_boxes.create_view_box(storage_domain)
                sds.append(result.id)
                storage_domain_mapping[storage_domain.id] = result.id
            except RequestErrorErrorException as e:
                print(e)
            except APIException as e:
                print(e)
    except Exception as err:
        print(err)


def create_protection_source():
    registered_source_list = {}
    sources = cluster_dict.get("sources", [])

    try:
        existing_sources = library.get_protection_sources(cohesity_client)

        for source in existing_sources:
            registered_source_list[source.protection_source.name] = source.protection_source.id

        for source in sources:
            source_name = source.protection_source.name
            # Check whether the source is already registered
            if source_name in registered_source_list.keys():
                source_mapping[source.protection_source.id] = registered_source_list[source_name]
                continue

            body = RegisterProtectionSourceParameters()
            environment = source.protection_source.environment
            body.endpoint = source_name
            env = environment[1:].lower()
            if environment in ["kPhysical"]:
                continue
            body.username = source.registration_info.username
            body.environment = environment
            for attr in dir(source.protection_source):
                if env in attr:
                    attribute = attr
                    break
            env_type = getattr(source.protection_source, attribute).mtype

            if env_type not in ["kViewBox"]:
                password = configparser.get(source.protection_source.name, "password")
                body.password = password
                #body.password = "Cohe$1ty"
            # Set the environment type
            setattr(body, env + "_type", env_type)

            if env == "view": 
                body.view_type = "kViewBox"

            try:
                result = cohesity_client.protection_sources.create_register_protection_source(
                    body)
                source_mapping[source.protection_source.id] = result.id
                source_ids.append(result.id)
            except RequestErrorErrorException as e:
                print(e)
            except APIException as e:
                print(e)
    except Exception as err:
        print(err)


def create_view():
    view_list = cluster_dict.get("views", [])
    existing_views = library.get_views(cohesity_client)
    existing_view_dict = {}
    for view in existing_views:
        existing_view_dict[view.name] = view.view_id
    for view in view_list:
        try:
            if view.name in existing_view_dict.keys():
                view_mapping[view.name] = existing_view_dict[view.name]
                continue
            result = cohesity_client.views.create_view(view)
            view_mapping[view.name] = result.name
            view_ids.append(result.name)

        except RequestErrorErrorException as e:
            print(e)
        except APIException as e:
            print(e)
        except Exception as err:
            print(err)


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

        except RequestErrorErrorException as e:
            print(e)
        except APIException as e:
            print(e)
        except Exception as err:
            print(err)


def create_protection_job():

    existing_job_list = []
    active_protection_jobs = []

    protection_job_list = cluster_dict.get("protection_jobs", [])
    exported_protection_source_objects = cluster_dict.get("protection_objects", {})
    existing_jobs = library.get_protection_jobs(cohesity_client)

    for job in existing_jobs:
        existing_job_list.append(job.name)

    try:
        for each_job in protection_job_list:
            if not each_job.is_deleted:
                active_protection_jobs.append(each_job)

        for protection_job in active_protection_jobs:

            source_list = []
            exported_sources_list = {}
 
            # Check if the protection source is already available.
            if protection_job.name in existing_job_list:
                continue

            source_id_list = protection_job.source_ids
            parent_id = protection_job.parent_source_id

            excluded_source_ids = protection_job.exclude_source_ids
            if not excluded_source_ids:
                exclude_source_ids = []

            print(protection_job.environment)
            if protection_job.environment in ["kPhysical"]:
                continue

            # UUID list for VMware resources.
            uuid_list = []
            for res in exported_protection_source_objects[parent_id]:
                if res.id in source_id_list:
                    if res.environment == "kVMware":
                        uuid_list.append(res.vmware_protection_source.id.uuid)
                    exported_sources_list[res.name] = res.parent_id

            for res in library.get_protection_source_objects(cohesity_client, source_mapping[parent_id]):
                if res.environment == "kVMware" and res.vmware_protection_source.id.uuid in uuid_list:
                    # if protection_job.environment == "kView":
                    #     protection_job.view_name = res.name
                    source_list.append(res.id)

                elif res.name in exported_sources_list.keys() and res.parent_id == source_mapping[parent_id]:
                    # For protection views, view name is required.
                    if protection_job.environment == "kView":
                        protection_job.view_name = res.name
                    source_list.append(res.id)

                #if res.id in excluded_source_ids:
                #    exclude_source_ids.append(res.id)
            if not source_list:
                continue
            protection_job.view_box_id = storage_domain_mapping[protection_job.view_box_id]
            protection_job.source_ids = source_list
            protection_job.parent_source_id = source_mapping[parent_id]
            protection_job.policy_id = policy_mapping.get(
                protection_job.policy_id)

            try:
                result = cohesity_client.protection_jobs.create_protection_job(
                    protection_job)
                print(result)
            except Exception as e:
                print(e)
                
            print(result)
            jobs.append(result.id)
    except RequestErrorErrorException as e:
        print(e)
    except APIException as e:
        print(e)
    except Exception as err:
        print(err)


def update_ids():
    with open("del_res.json", "r") as f:
        j = json.load(f)
        print(j)
        j["policies"].extend(policy_ids)
        j["storage_domains"].extend(sds)
        j["views"].extend(view_ids)
        j["sources"].extend(source_ids)
        j["jobs"].extend(jobs)
    with open("del_res.json", "w") as f:
        print(j)
        json.dump(j, f)


create_protection_source()
create_protection_policy()
create_storage_domain()
create_view()
create_protection_job()
update_ids()