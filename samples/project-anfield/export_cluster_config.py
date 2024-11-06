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
parser.add_argument(
    '--verbose', '-v',
    action='store_true',
    help='Enable verbose logging to console. By default log file is doing verbose logging. This one should be used only if live console verbosity is desired.'
)
parser.add_argument(
    '--log_file',
    default='export_script.log',
    help='File to write logs to.'
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
    # try:
    #     socket.create_connection((cluster_vip, 80), timeout=2)
    # except ConnectionRefusedError as err:
    #     # Source is reachable, but port is not opened.
    #     pass
    # except socket.timeout as err:
    #     raise Exception(
    #         "Cluster IP %s is not reachable, please check network "
    #         "connectivity" % cluster_vip)
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

logger = logging.getLogger("export_app")
logger.setLevel(logging.DEBUG)  # Capture all levels

# Console logging handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG if args.verbose else logging.INFO)
logger.propagate = False

# File logging handler
file_handler = logging.FileHandler(args.log_file, mode='w')  # Ensure 'write' mode
file_handler.setLevel(logging.DEBUG)

# Defining logging formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Clear all existing handlers before adding new ones
if logger.hasHandlers():
    logger.handlers.clear()

# Clear existing handlers to avoid duplication
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# Starting the export process
logger.info(
    "Starting export process for cluster: '%s'",
    (configparser.get("export_cluster_config", "cluster_ip")),
)

try:
    # Skip paused jobs and failover ready jobs by setting this flag to true
    # in config file.
    logger.info("Preparing boolean value to determine if jobs must be skipped.")
    skip_jobs = configparser.getboolean("export_cluster_config", "skip_jobs")
    logger.debug("skip_jobs value: %s", skip_jobs)

    logger.info("Preparing boolean value to determine if access management should be exported.")
    export_access_mgmnt = configparser.getboolean(
        "export_cluster_config", "export_access_management"
    )
    logger.debug("skip_jobs value: %s", export_access_mgmnt)
except (NoSectionError, NoOptionError) as err:
    logger.info("Error while fetching '%s' content, error msg: %s" % (config_file, err))

logger.info("Calling library function to pull cluster configuration info.")
cluster_config_info = library.get_cluster_config(cohesity_client)

logger.info("Calling library function to pull views info.")
views_info = library.get_views(cohesity_client)

logger.info("Calling library function to pull storage domains info.")
storage_domains_info = library.get_storage_domains(cohesity_client)

logger.info("Calling library function to pull policies info.")
policies_info = library.get_protection_policies(cohesity_client)

logger.info("Calling library function to pull protection jobs info.")
protection_jobs_info = library.get_protection_jobs(cohesity_client, skip_jobs)

logger.info("Calling library function to pull protection sources info.")
protection_sources_info = library.list_protection_sources(cohesity_client)

logger.info("Calling library function to pull external targets info.")
external_targets_info = library.get_external_targets(cohesity_client)

logger.info("Calling library function to pull sources info.")
sources_info = library.get_protection_sources(cohesity_client)

logger.info("Calling library function to pull remote clusters info.")
remote_clusters_info = library.get_remote_clusters(cohesity_client)

logger.info("Calling library function to pull SQL entity mappings info.")
sql_entity_mapping_info = library.get_sql_entity_mapping(
        cohesity_client, env_enum.KSQL
    )

logger.info("Calling library function to pull AD entity mappings info.")
ad_entity_mapping_info = library.get_ad_entity_mapping(cohesity_client, env_enum.KAD)

logger.info("Calling library function to pull Oracle entity mappings info.")
oracle_entity_mapping_info = library.get_ad_entity_mapping(
        cohesity_client, env_enum.KORACLE
    )

logger.info("Calling library function to pull whitelist info.")
whitelist_settings_info = library.get_whitelist_settings(cohesity_client, rest_obj)

logger.info("Calling library function to pull VLANs settings info.")
vlans_info = library.get_vlans(cohesity_client)

logger.info("Calling library function to pull Interface Group info.")
iface_groups_info = library.get_interface_groups(cohesity_client)

logger.info("Calling library function to pull routes info.")
routes_info = library.get_routes(cohesity_client)

logger.info("Calling library function to pull host mappings info.")
host_mappings_info = library.get_host_mapping(cohesity_client)

# Export Active directory entries and AD users and groups along with roles.
if export_access_mgmnt:
    logger.info("Access management boolean is set to TRUE, exporting corresponding settings.")
    logger.debug("Calling library function to pull AD info.")
    logger.debug("Iterating every AD configuration to get a list of domains.")
    ad_info = library.get_ad_entries(cohesity_client)
    domains = [ad.domain_name for ad in ad_info]
    logger.debug("Domains found: %s.", domains)
    logger.info("Calling library function to pull AD Objects info.")
    ad_objects_info = library.get_ad_objects(
        cohesity_client, domains)
    logger.info("Calling library function to pull roles info.")
    roles_info = cohesity_client.roles.get_roles()

logger.info("Adding all information collected into a cluster dictionary object.")
cluster_dict = {
    "cluster_config": cluster_config_info,
    "views": views_info,
    "storage_domains": storage_domains_info,
    "policies": policies_info,
    "protection_jobs": protection_jobs_info,
    "protection_sources": protection_sources_info,
    "external_targets": external_targets_info,
    "sources": sources_info,
    "remote_clusters": remote_clusters_info,
    "sql_entity_mapping": sql_entity_mapping_info,
    "ad_entity_mapping": ad_entity_mapping_info,
    "oracle_entity_mapping": oracle_entity_mapping_info,
    "whitelist_settings": whitelist_settings_info,
    "vlans": vlans_info,
    "iface_groups": iface_groups_info,
    "routes": routes_info,
    "host_mappings": host_mappings_info,
}

# Export Active directory entries and AD users and groups along with roles.
if export_access_mgmnt:
    cluster_dict["ad"] = ad_info
    cluster_dict["ad_objects"] = ad_objects_info
    cluster_dict["roles"] = roles_info

logger.info("Getting a dictionary of exported resources mapped to types.")
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

logger.info("Starting to process protection sources for the cluster. Total sources to process: {}.".format(len(cluster_dict["sources"])))
for source in cluster_dict["sources"]:
    logger.info("  - Processing source with ID: {} and environment: {}.".format(source.protection_source.id, source.protection_source.environment))

    _id = source.protection_source.id
    env = source.protection_source.environment
    logger.info("  - Checking if the source type is supported for export.")
    if env not in env_list:
        logger.debug("    |- Skipping, not in the list of supported source types (environments).")
        continue

    logger.info("  - Checking if the source type is Cassandra (API must be handled differently).")
    if env == "kCassandra":
        logger.debug("    |- Source type is Cassandra, generating API manually.")
        API = "public/protectionSources?id={}&environment={}".format(_id, env)
        _, resp = rest_obj.get(api=API)
        resp = json.loads(resp)
        source_dct[_id] = resp
    else:
        logger.debug("    |- Source type is not Cassandra, getting protection source info using the default process.")
        res = library.get_protection_source_by_id(cohesity_client, _id, env)
        source_dct[_id] = res.nodes

    logger.info("  - Checking source type to export protection source details appropriately.")
    if env in [
        env_enum.KVIEW,
        env_enum.K_VMWARE,
        env_enum.KISILON,
        "kCassandra",
        env_enum.K_HYPERV,
        env_enum.KNETAPP,
    ]:
        logger.debug("    |- Source type is: View, VMware, Isilon, Cassandra, Hyper-V or NetApp. Name retrieval is simple, using dot notation.")
        name = source.protection_source.name
        exported_res["Protection Sources"].append(name)
    else:
        logger.debug("    |- Source type is different from the standard list. Need to iterate the sources list (nodes) and pull the source name.")
        if res.nodes:
            for nodes in res.nodes:
                name = nodes["protectionSource"]["name"]
                if name not in exported_res["Protection Sources"]:
                    exported_res["Protection Sources"].append(name)

logger.info("Adding all sources dictionary into the cluster export config dictionary.")
cluster_dict["source_dct"] = source_dct

# Fetch all the gflags from the cluster.
logger.info("Fetching all gflags.")
code, resp = library.gflag(cluster_vip, username, password, domain)

if code == 200:
    logger.info("Gflags pulled succesfylly. Adding to cluster config object.")
    cluster_dict["gflag"] = resp.decode("utf-8")
else:
    # Incase of cluster versions less than 6.3, API for fetching gflags is not
    # available.
    logger.info("Gflags API not available or supported. Empty gflag value added.")
    cluster_dict["gflag"] = []

# File path is created using location and filename provided. If location and
# filename is not provided by user, default location and filename is used.
logger.info("Creating export file.")
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
logger.info("Serializing (dumping) all configuration information into the file.")
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
