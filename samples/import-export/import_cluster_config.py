import json
import pickle
import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('import_cluster_config', 'cluster_ip'),
                                 username=configparser.get('import_cluster_config', 'username'),
                                 password=configparser.get('import_cluster_config', 'password'),
                                 domain= configparser.get('import_cluster_config', 'domain'))

cluster_dict = pickle.load(open("cluster_config.txt", "rb"))

with open("template.json", "r") as file_obj:
    template_dict = json.load(file_obj)



def create_protection_policy():
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    protection_policy_list = cluster_dict.get("policies", [])
    try:
        if not protection_policy_list:
            print("No existing protection policies available.")
            protection_policy = template_dict["policy"]
        else:
            protection_policy = protection_policy_list[0]
            protection_policy.name = "TestPolicy"

        result = cohesity_client.protection_policies.create_protection_policy(
            protection_policy)
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
            storage_domain = template_dict["storage_domain"]
            cluster_partition_id = cohesity_client.cluster_partitions.\
                get_cluster_partitions()[0].id
            storage_domain["name"] = "TestSD"
            storage_domain["id"] = cluster_partition_id
        else:
            # If the view box if available, modified name.
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
            view = template_dict["view"]
            view_box_id = cohesity_client.view_boxes.get_view_boxes()[0].id
            view["viewBoxId"] = view_box_id
        else:
            view = view_list[0]
            view.name = "TestView"
        cohesity_client.views.create_view(view)
    except RequestErrorErrorException as e: 
        print(e)
    except APIException as e: 
        print(e)
    except Exception as err:
        print(err)



# create_protection_policy()
# create_storage_domain()
create_view()