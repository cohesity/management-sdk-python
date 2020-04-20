import pickle
import library
import logging
import configparser
import datetime
from cohesity_management_sdk.cohesity_client import CohesityClient

logger = logging.getLogger(__file__)

# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('export_cluster_config', 'cluster_ip'),
                                 username=configparser.get('export_cluster_config', 'username'),
                                 password=configparser.get('export_cluster_config', 'password'),
                                 domain= configparser.get('export_cluster_config', 'domain'))

logger.setLevel(logging.INFO)


logger.info("Exporting resources from cluster '%s'" % (
    configparser.get('export_cluster_config', 'cluster_ip')))


cluster_dict = {
    "cluster_config": library.get_cluster_config(cohesity_client),
    "views": library.get_views(cohesity_client),
    "storage_domains": library.get_storage_domains(cohesity_client),
    "policies": library.get_protection_policies(cohesity_client),
    "protection_jobs": library.get_protection_jobs(cohesity_client),
    "protection_sources": library.get_protection_sources(cohesity_client),
    "external_targets": library.get_external_targets(cohesity_client),
    "sources": library.get_protection_sources(cohesity_client),
    "remote_clusters": library.get_remote_clusters(cohesity_client)
    }


exported_res = library.debug()

obj_dct = {}
source_dct = {}

for source in cluster_dict["sources"]:
    id = source.protection_source.id
    env = source.protection_source.environment
    res = library.get_protection_source_by_id(cohesity_client, id, env)
    source_dct[id] = res.nodes
    if env in ["kView", "kVMware"]:
        name = source.protection_source.name
        exported_res["Protection Sources"].append(name)
    else:
        for nodes in res.nodes:
            name =  nodes["protectionSource"]["name"]
            if name not in exported_res["Protection Sources"]:
                exported_res["Protection Sources"].append(name)
    obj_dct[id] = \
        library.get_protection_source_object_by_id(cohesity_client, id)
cluster_dict["protection_objects"] = obj_dct
cluster_dict["source_dct"] = source_dct

# Fetch all the resources and store the data in file.

pickle.dump(cluster_dict,
            open("export-config-%s" %
                 datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"), "wb"))

logger.info("Please find the imported resources summary.\n")
for key, val in exported_res.items():
    logger.info("Successfully exported the following %s:\n%s\n" % (key, ", ".join(val)))