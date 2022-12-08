# Copyright 2020 Cohesity Inc.
#
# Python utility to export the cluster config.
# Usage: python export_cluster_config.py

"""
Module to contain functions.
"""

try:
    import argparse
    import datetime
    import json
    import logging
    import os
    import pickle
    import socket
    import requests
    import sys
    import library

    # Custom module import
    from cohesity_management_sdk.cohesity_client import CohesityClient
    from cohesity_management_sdk.exceptions.api_exception import APIException
    from cohesity_management_sdk.models.environment_register_protection_source_parameters_enum import \
        EnvironmentRegisterProtectionSourceParametersEnum as env_enum
    from cohesity_management_sdk.models.netapp_type_enum import NetappTypeEnum
    from library import RestClient
except ImportError as err:
    import sys

    print(
        "Please ensure Cohesity Python SDK and dependency packages are installed to continue."
    )
    print(
        "To install Python SDK, run 'pip install cohesity-management-sdk "
        "configparser requests'"
    )
    print("To install dependencies, run 'sh setup.py'")
    sys.exit()

# Disable python warnings.
requests.packages.urllib3.disable_warnings()

# Check for python version
if float(sys.version[:3]) >= 3:
    import configparser
else:
    import ConfigParser as configparser

from configparser import NoSectionError, NoOptionError, MissingSectionHeaderError

logger = logging.getLogger("export_app")

# Fetch command line arguments.
parser = argparse.ArgumentParser(
    description="Please provide export file location and filename"
)
parser.add_argument(
    "--file_location",
    default=os.getcwd(),
    action="store",
    help="Directory to store the exported config file.",
)
parser.add_argument(
    "--file_name",
    default="",
    action="store",
    help="File name to store the exported config.",
)
parser.add_argument(
    "--auto_fill_config",
    default="",
    action="store_true",
    help="Enable this flag to auto populate the config file sections and fields",
)
parser.add_argument(
    "--config",
    "-c",
    default="config.ini",
    action="store",
    help="Config file to export the resources.",
)

args = parser.parse_args()
file_location = args.file_location
file_name = args.file_name
auto_fill_config = args.auto_fill_config
config_file = args.config

# Validate the configuration file content.
try:
    configparser = configparser.ConfigParser()
    configparser.read(config_file)
except MissingSectionHeaderError as err:
    print(
        "Given configuration file is invalid, please make sure %s is "
        "decrypted" % config_file)
    sys.exit()


# Fetch the Cluster credentials from config file.
try:
    cluster_vip = configparser.get("export_cluster_config", "cluster_ip")
    username = configparser.get("export_cluster_config", "username")
    password = configparser.get("export_cluster_config", "password")
    domain = configparser.get("export_cluster_config", "domain")
    # Check Cluster IP/FQDN is reachable.
    try:
        socket.create_connection((cluster_vip, 80), timeout=2)
    except ConnectionRefusedError as err:
        # Source is reachable, but port is not opened.
        pass
    except socket.timeout as err:
        raise Exception(
            "Cluster IP %s is not reachable, please check network "
            "connectivity" % cluster_vip)
    cohesity_client = CohesityClient(
        cluster_vip=cluster_vip, username=username, password=password, domain=domain
    )
    # Make a function call to validate the credentials.
    cohesity_client.principals.get_user_privileges()
    rest_obj = RestClient(cluster_vip, username, password, domain)
except APIException as err:
    print("Authentication error occurred, error details: %s" % err)
    sys.exit(1)
except Exception as err:
    print("Authentication error occurred, error details: %s" % err)
    sys.exit(1)

logger.setLevel(logging.INFO)

logger.info(
    "Exporting resources from cluster '%s'",
    (configparser.get("export_cluster_config", "cluster_ip")),
)

try:
    # Skip paused jobs and failover ready jobs by setting this flag to true
    # in config file.
    skip_jobs = configparser.getboolean("export_cluster_config", "skip_jobs")
    export_access_mgmnt = configparser.getboolean(
        "export_cluster_config", "export_access_management"
    )
except (NoSectionError, NoOptionError) as err:
    print("Error while fetching '%s' content, error msg %s" % (config_file, err))

cluster_dict = {
    "cluster_config": library.get_cluster_config(cohesity_client),
    "views": library.get_views(cohesity_client),
    "storage_domains": library.get_storage_domains(cohesity_client),
    "policies": library.get_protection_policies(cohesity_client),
    "protection_jobs": library.get_protection_jobs(cohesity_client, skip_jobs),
    "protection_sources": library.list_protection_sources(cohesity_client),
    "external_targets": library.get_external_targets(cohesity_client),
    "sources": library.get_protection_sources(cohesity_client),
    "remote_clusters": library.get_remote_clusters(cohesity_client),
    "sql_entity_mapping": library.get_sql_entity_mapping(
        cohesity_client, env_enum.KSQL
    ),
    "ad_entity_mapping": library.get_ad_entity_mapping(cohesity_client, env_enum.KAD),
    "oracle_entity_mapping": library.get_ad_entity_mapping(
        cohesity_client, env_enum.KORACLE
    ),
    "whitelist_settings": library.get_whitelist_settings(cohesity_client, rest_obj),
    "vlans": library.get_vlans(cohesity_client),
    "iface_groups": library.get_interface_groups(cohesity_client),
    "routes": library.get_routes(cohesity_client),
    "host_mappings": library.get_host_mapping(cohesity_client),
}

# Export Active directory entries and AD users and groups along with roles.
if export_access_mgmnt:
    cluster_dict["ad"] = library.get_ad_entries(cohesity_client)
    cluster_dict["ad_objects"] = library.get_ad_objects(cohesity_client)
    cluster_dict["roles"] = cohesity_client.roles.get_roles()

exported_res = library.debug()

source_dct = {}
KCASSANDRA = "kCassandra"

# List of support environments.
env_list = [
    env_enum.KGENERICNAS,
    env_enum.KISILON,
    env_enum.KPHYSICAL,
    env_enum.KPHYSICALFILES,
    #env_enum.KVIEW,
    env_enum.K_VMWARE,
    env_enum.KSQL,
    KCASSANDRA,
    env_enum.KAD,
    env_enum.KORACLE,
    env_enum.K_HYPERV,
    env_enum.KNETAPP,
]


for source in cluster_dict["sources"]:
    _id = source.protection_source.id
    env = source.protection_source.environment
    if env not in env_list:
        continue

    if env == "kCassandra":
        API = "public/protectionSources?id={}&environment={}".format(_id, env)
        _, resp = rest_obj.get(api=API)
        resp = json.loads(resp)
        source_dct[_id] = resp
    else:
        res = library.get_protection_source_by_id(cohesity_client, _id, env)
        source_dct[_id] = res.nodes

    if env in [
        env_enum.KVIEW,
        env_enum.K_VMWARE,
        env_enum.KISILON,
        "kCassandra",
        env_enum.K_HYPERV,
        env_enum.KNETAPP,
    ]:
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
    cluster_dict["cluster_config"].name,
    datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"),
)
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
    if not val:continue
    logger.info("Successfully exported the following %s:\n%s\n", key, ", ".join(val))


logger.info("Exported config file: %s", exported_config_file)

# Auto populate config.ini file based on flag.
if auto_fill_config:
    logger.info("Auto populating sections in '%s' file." % config_file)
    result = library.auto_populate_config(config_file)
    if not result:
        logger.error("Error while updating '%s' file" % config_file)
    else:
        logger.info("Successfully updated '%s' file" % config_file)
