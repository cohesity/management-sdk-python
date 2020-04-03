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
cluster_dict = {
    "views": [],
    "storage_domains": [],
    "policies": [],
    "protection_jobs": [],
    "protection_sources": [],
    "external_targets": []
}

def get_protection_policies():
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    cluster_dict['policies'] = policy_list


def get_storage_domains():
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    cluster_dict["storage_domains"] = storage_domain_list


def get_views():
    views_list = cohesity_client.views.get_views().views
    cluster_dict["views"] = views_list


def get_protection_jobs():
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    cluster_dict["protection_jobs"] = protection_job_list


def get_protection_sources():
    protection_source_list = cohesity_client.protection_sources.list_protection_sources()
    cluster_dict["protection_sources"] = protection_source_list


def get_external_targets():
    external_target_list = cohesity_client.vaults.get_vaults()
    cluster_dict["external_targets"] = external_target_list

get_storage_domains()
get_protection_policies()
get_protection_jobs()
get_protection_sources()
get_external_targets()
get_views()
# Fetch all the resources and store the data in file.
pickle.dump(cluster_dict, open("cluster_config.txt", "wb"))