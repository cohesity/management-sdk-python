import pickle
import library
import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('export_cluster_config', 'cluster_ip'),
                                 username=configparser.get('export_cluster_config', 'username'),
                                 password=configparser.get('export_cluster_config', 'password'),
                                 domain= configparser.get('export_cluster_config', 'domain'))


cluster_dict = {
    "cluster_config": library.get_cluster_config(cohesity_client),
    "views": library.get_views(cohesity_client),
    "storage_domains": library.get_storage_domains(cohesity_client),
    "policies": library.get_protection_policies(cohesity_client),
    "protection_jobs": library.get_protection_jobs(cohesity_client),
    "protection_sources": library.get_protection_sources(cohesity_client),
    "external_targets": library.get_external_targets(cohesity_client),
    "sources": library.get_protection_sources(cohesity_client)#,
    #"all_protection_sources": library.get_all_protection_sources(cohesity_client)
    }
dct = {}
for source in cluster_dict["sources"]:
    dct[source.protection_source.id] = library.get_all_protection_sources(cohesity_client, source.protection_source.id)
cluster_dict["all_protection_sources"] = dct

# Fetch all the resources and store the data in file.
pickle.dump(cluster_dict, open("cluster_config.txt", "wb"))