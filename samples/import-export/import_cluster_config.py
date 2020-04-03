import json
import pickle
import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_management_sdk.models.create_view_request import CreateViewRequest
from cohesity_management_sdk.models.create_view_box_params import CreateViewBoxParams
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

cluster_dict = pickle.load(open("cluster_config.txt", "rb"))


def create_protection_policy():
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    protection_policy_list = cluster_dict.get("policies", [])
    try:
        if not protection_policy_list or protection_policy_list[0].mtype == "kRPO":
            protection_policy = ProtectionPolicyRequest()
            scheduling_policy = {"periodicity": "kMonthly",
                                 "monthlySchedule": {
                                     "dayCount": "kFirst",
                                     "day": "kSunday"
                                 }}
            protection_policy.incremental_scheduling_policy = scheduling_policy
        else:
            protection_policy = protection_policy_list[0]
        protection_policy.name = "TestPolicy"

        result = cohesity_client.protection_policies.create_protection_policy(
            protection_policy)
        print(result)
    except RequestErrorErrorException as e:
        print(e)
    except APIException as e:
        print(e)
    except Exception as err:
        print(err)


def create_storage_domain():
    try:
        storage_domain_list = cluster_dict.get("storage_domains", [])
        if not storage_domain_list:
            storage_domain = CreateViewBoxParams()
            cluster_partition_id = cohesity_client.cluster_partitions.\
                get_cluster_partitions()[0].id
            storage_domain.cluster_partition_id = cluster_partition_id
        else:
            storage_domain = storage_domain_list[0]
        storage_domain.name = "TestSD"
        result = cohesity_client.view_boxes.create_view_box(storage_domain)
        print(result)
    except RequestErrorErrorException as e:
        print(e)
    except APIException as e:
        print(e)
    except Exception as err:
        print(err)


def create_view():
    view_list = cluster_dict.get("views", [])
    try:
        if not view_list:
            view = CreateViewRequest()
            view_box_id = cohesity_client.view_boxes.get_view_boxes()[0].id
            view.view_box_id = view_box_id
        else:
            view = view_list[0]
        view.name = "TestView"
        result = cohesity_client.views.create_view(view)
        print(result)
    except RequestErrorErrorException as e:
        print(e)
    except APIException as e:
        print(e)
    except Exception as err:
        print(err)


# create_protection_policy()
# create_storage_domain()
# create_view()
