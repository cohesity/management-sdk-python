# Copyright 2020 Cohesity Inc.
#
# Python utility to export the cluster config.
# Usage: python export_cluster_config.py

import argparse
import datetime
import json
import logging
import pickle
import os
import requests
import sys
import library

# Custom module import
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.environment_register_protection_source_parameters_enum \
    import EnvironmentRegisterProtectionSourceParametersEnum as env_enum
from library import RestClient


# Disable python warnings.
requests.packages.urllib3.disable_warnings()

# Check for python version
if float(sys.version[:3]) >= 3:
    import configparser as configparser
else:
    import ConfigParser as configparser

logger = logging.getLogger('export_app')

# Fetch command line arguments.
parser = argparse.ArgumentParser(
    description="Please provide export file location and filename")
parser.add_argument("--file_location", default=os.getcwd(), action="store")
parser.add_argument("--file_name", default='',  action="store")
args = parser.parse_args()
file_location = args.file_location
file_name = args.file_name

# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

try:
    cluster_vip=configparser.get('export_cluster_config', 'cluster_ip')
    username=configparser.get('export_cluster_config', 'username')
    password=configparser.get('export_cluster_config', 'password')
    domain=configparser.get('export_cluster_config', 'domain')

    cohesity_client = CohesityClient(cluster_vip=cluster_vip,
                                     username=username,
                                     password=password,
                                     domain=domain)
    # Make a function call to validate the credentials.
    cohesity_client.principals.get_user_privileges()
except APIException as err:
    print("Authentication error occurred, error details: %s" % err)
    exit(1)
except Exception as err:
    print("Authentication error occurred, error details: %s" % err)
    exit(1)


logger.setLevel(logging.INFO)

logger.info("Exporting resources from cluster '%s'" % (
    configparser.get('export_cluster_config', 'cluster_ip')))

# Skip paused jobs and failover ready jobs by setting this flag to true in config file.
skip_jobs = configparser.getboolean('export_cluster_config', 'skip_jobs')

cluster_dict = {
    "cluster_config": library.get_cluster_config(cohesity_client),
    "views": library.get_views(cohesity_client),
    "storage_domains": library.get_storage_domains(cohesity_client),
    "policies": library.get_protection_policies(cohesity_client),
    "protection_jobs": library.get_protection_jobs(cohesity_client, skip_jobs),
    "protection_sources": library.get_protection_sources(cohesity_client),
    "external_targets": library.get_external_targets(cohesity_client),
    "sources": library.get_protection_sources(cohesity_client),
    "remote_clusters": library.get_remote_clusters(cohesity_client),
    "sql_entity_mapping": library.get_sql_entity_mapping(cohesity_client,
                                                         env_enum.KSQL)
}

exported_res = library.debug()
source_dct = {}
KCASSANDRA = "kCassandra"

# List of support environments.
env_list = [env_enum.KGENERICNAS, env_enum.KISILON, env_enum.KPHYSICAL,
            env_enum.KPHYSICALFILES, env_enum.KVIEW, env_enum.K_VMWARE,
            env_enum.KSQL, KCASSANDRA]


for source in cluster_dict["sources"]:
    id = source.protection_source.id
    env = source.protection_source.environment
    rest_obj = RestClient(cluster_vip, username, password, domain)
    if env == "kCassandra":
        api = "public/protectionSources?id={}&environment={}".format(id, env)
        _, resp = rest_obj.get(api=api)
        resp = json.loads(resp)
        source_dct[id] = resp
    else:
        res = library.get_protection_source_by_id(cohesity_client, id, env)
        source_dct[id] = res.nodes
    if env in [env_enum.KVIEW, env_enum.K_VMWARE, env_enum.KISILON, 'kCassandra']:
        name = source.protection_source.name
        exported_res["Protection Sources"].append(name)
    else:
        if res.nodes:
            for nodes in res.nodes:
                name = nodes["protectionSource"]["name"]
                if name not in exported_res["Protection Sources"]:
                    exported_res["Protection Sources"].append(name)
cluster_dict["source_dct"] = source_dct

# Fetch all the gflags from the cluster.
code, resp = library.gflag(cluster_vip, username, password, domain)

if code == 200:
    cluster_dict["gflag"] = resp.decode("utf-8")
else:
    # Incase of cluster versions less than 6.3, API for fetching gflags is not
    # available.
    cluster_dict["gflag"] = []

# File path is created using location and filename provided. If location and
# filename is not provided by user, default location and filename is used.
exported_config_file = "export-config-%s-%s" % (
        cluster_dict['cluster_config'].name,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
if file_location and file_name:
    exported_config_file = os.path.join(file_location, file_name)
elif file_location:
    exported_config_file = os.path.join(file_location, exported_config_file)
elif file_name:
    exported_config_file = file_name

# Fetch all the resources and store the data in file.
pickle.dump(cluster_dict, open(exported_config_file, "wb"))

logger.info("Please find the exported resources summary.\n")
for key, val in exported_res.items():
    logger.info("Successfully exported the following %s:\n%s\n" %
                (key, ", ".join(val)))


logger.info("Exported config file: %s" % exported_config_file)
