# Copyright 2020 Cohesity Inc.
#
# Python libraries with functions to import/export the cluster config.

# Standard import statements
from collections import defaultdict

import json
import logging
import requests
import sys

# Check for python version
if float(sys.version[:3]) >= 3:
    import configparser
else:
    import ConfigParser as configparser

# Standard import statements
from cohesity_management_sdk.models.exclude_type_enum import ExcludeTypeEnum as enum
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum as env_enum

from rest_client import RestClient

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

ad_list = list()
config_dict = defaultdict()
exported_res_dict = defaultdict(list)


def gflag(endpoint, user, password, domain, body=None, action="get"):
    """
    To fetch gflag details, V1 Private API is called.
    : Return return code and response.
    """
    # Function to get and update the gflags from the clusters.
    # Returns response code and response.
    api = "clusters/gflag"
    rest_obj = RestClient(endpoint, user, password, domain)
    if action == "get":
        code, resp = rest_obj.get(api)
    else:
        code, resp = rest_obj.put(api, data=body)
    # If the response code is failed, returns empty list. Gflags APIs are
    # supported in cluster version >= 6.3.
    if code == 404:
        resp = json.dumps([]).encode("utf-8")
    return code, resp


def get_cluster_config(cohesity_client):
    """
    Fetch the cluster configuration details.
    : return config.
    """
    config = cohesity_client.cluster.get_cluster()
    return config


def get_protection_policies(cohesity_client):
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    : return list of protection policies.
    """
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    policy_list = policy_list if policy_list else []
    for policy in policy_list:
        exported_res_dict["Protection Policies"].append(policy.name)
    return policy_list


def get_storage_domains(cohesity_client):
    """
    Function to fetch list of available views boxes.
    : return list of viewboxes.
    """
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    for domain in storage_domain_list:
        exported_res_dict["Storage Domains"].append(domain.name)
    return storage_domain_list


def get_views(cohesity_client):
    """
    Function to fetch list of available views.
    : return list of views.
    """
    views = cohesity_client.views.get_views().views
    views_list = views if views else []
    for view in views_list:
        exported_res_dict["Protection Views"].append(view.name)
    return views_list


def get_protection_jobs(cohesity_client, skip_jobs=False):
    """
    Function to fetch list of available active protection jobs
    available in the cluster.
    If skip_jobs flag is set, in-active and deleted jobs are ignored.
    : return list of jobs.
    """
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    active_job_list = []
    for job in protection_job_list:
        # Jobs which are deleted are ignored.
        if job.is_deleted:
            continue
        # Skip jobs which are paused or in-active(failover ready).
        if skip_jobs and (job.is_paused or job.is_active != None):
            continue
        active_job_list.append(job)
        exported_res_dict["Protection Jobs"].append(job.name)
    return active_job_list


def get_protection_source_by_id(cohesity_client, _id, env):
    """
    Function to fetch list of source by id and environment.
    : return.
    """
    protection_source_list = cohesity_client.protection_sources.list_protection_sources(
        id=_id,
        environment=env,
        exclude_types=[
            enum.KCOMPUTERESOURCE,
            enum.KDATASTORE,
            enum.KDISTRIBUTEDVIRTUALPORTGROUP,
            enum.KNETWORK,
            enum.KRESOURCEPOOL,
            enum.KSTORAGEPOD,
            enum.KVIRTUALAPP,
        ],
    )
    return_list = protection_source_list[0] if protection_source_list else None
    if env == env_enum.KGENERICNAS and return_list and return_list.nodes:
        for item in return_list.nodes:
            if item["protectionSource"]["nasProtectionSource"]["protocol"] == "kNfs3":
                continue
            name = str(item["protectionSource"]["name"])
            config_dict[name] = None
    return return_list


def get_protection_sources(cohesity_client):
    """
    Function to fetch list of available root nodes present in the cluster.
    : return list of root nodes.
    """
    sources = cohesity_client.protection_sources.list_protection_sources_root_nodes()
    sources = sources if sources else []
    for source in sources:
        keys = None
        environment = source.protection_source.environment
        if source.protection_source.environment == env_enum.K_VMWARE:
            name = source.protection_source.name
        elif environment in [env_enum.KISILON, env_enum.KNETAPP]:
            name = source.protection_source.isilon_protection_source.name \
                if source.protection_source.isilon_protection_source else \
                    source.protection_source.netapp_protection_source.name
            keys = ["password", "smb_password"]
        elif environment == "kCassandra":
            name = source.protection_source.name
            keys = ["username", "password", "db_username", "db_password"]
        else:
            continue
        config_dict[name] = keys
    return sources


def list_protection_sources(cohesity_client, env="kView"):
    """
    Function to fetch sources filtered by environment.
    : return source list
    """
    sources = cohesity_client.protection_sources.list_protection_sources(
        environments=env
    )
    sources = sources if sources else []
    return sources


def get_external_targets(cohesity_client):
    """
    Function to fetch external targets added to the cluster.
    : return list of targets.
    """
    external_target_list = cohesity_client.vaults.get_vaults()
    for target in external_target_list:
        # config[target.name] = dict()
        if target.config.amazon:
            config_dict[target.name] = ["secret_access_key"]
        elif target.config.azure:
            config_dict[target.name] = ["storage_access_key"]
        else:
            config_dict[target.name] = None
        exported_res_dict["External Targets"].append(target.name)
    return external_target_list


def get_remote_clusters(cohesity_client):
    """
    Function to fetch remote clusters available in the cluster.
    : return list of remote clusters.
    """
    remote_cluster_list = cohesity_client.remote_cluster.get_remote_clusters()
    for cluster in remote_cluster_list:
        config_dict[cluster.name] = None
        exported_res_dict["Remote Clusters"].append(cluster.name)
    return remote_cluster_list


def get_sql_entity_mapping(cohesity_client, env):
    """
    Function to fetch SQL sources available in the cluster along with instance
    name and ids.
    """
    sql_mapping = {}
    sources = list_protection_sources(cohesity_client, env)
    if not sources:
        return sql_mapping
    # Iterate each node(sql server) and fetch database available in the
    # server.
    for source in sources[0].nodes:
        _id = source["protectionSource"]["id"]
        sql_mapping[_id] = {}
        if source.get("applicationNodes"):
            nodes = source["applicationNodes"]
            for sql_node in nodes:
                for node in sql_node.get("nodes", []):
                    sql_mapping[_id][node["protectionSource"]["id"]] = node[
                        "protectionSource"
                    ]["name"]
    return sql_mapping


def get_ad_entity_mapping(cohesity_client, env):
    """
    Function to fetch SQL/AD sources available in the cluster along with instance
    name and ids.
    """
    mapping = {}
    sources = list_protection_sources(cohesity_client, env)
    if not sources:
        return mapping

    for source in sources[0].nodes:
        _id = source["protectionSource"]["id"]
        mapping[_id] = {}
        for node in source.get("applicationNodes", []):
            mapping[_id][node["protectionSource"]["id"]] = node["protectionSource"][
                "name"
            ]
    return mapping


def get_ad_entries(cohesity_client):
    """
    Function to get list of AD added to cluster
    : return AD list
    """
    resp = cohesity_client.active_directory.get_active_directory_entry()
    if resp:
        ad_list = list()
        for each_ad in resp:
            ad_list.append(each_ad.domain_name)
            config_dict[each_ad.domain_name] = [
                    "username", "password", "machine_accounts"]
        exported_res_dict["Active directories"] = ad_list
    return resp


def get_ad_objects(cohesity_client, domains=None):
    """
    Function to get list of AD objects available in cluster.
    : return AD objects list
    """
    ad_objects = defaultdict(dict)
    if not domains:
        domains = ad_list
    for domain in domains:
        # Fetch list of groups and users added to the cluster.
        users = cohesity_client.principals.get_users(domain=domain)
        groups = cohesity_client.groups.get_groups(domain=domain)
        ad_objects[domain]["users"] = users
        ad_objects[domain]["groups"] = groups
    return ad_objects


def get_interface_groups(cohesity_client):
    """
    Function to get list of interface groups available in the cluster.
    : return interface group list
    """
    iface_groups = cohesity_client.interface_group.get_interface_groups()
    iface_groups = [] if not iface_groups else iface_groups
    return iface_groups


def get_whitelist_settings(cohesity_client, rest_obj):
    """ "
    Function to fetch available subnet whitelists and NIS netgroups.
    """
    try:
        settings = dict()
        subnets = cohesity_client.clusters.get_external_client_subnets().client_subnets
        settings["subnets"] = subnets if subnets else []
        exported_res_dict["Subnet whitelists"] = [
            subnet.ip for subnet in settings["subnets"]
        ]
        NIS_PROVIDER_API = "nis-providers"
        _, resp = rest_obj.get(NIS_PROVIDER_API, version="v2")
        settings["nis_providers"] = json.loads(resp)["nisProviders"]

        NIS_NETGROUPS_API = "nis-netgroups"
        _, resp = rest_obj.get(NIS_NETGROUPS_API, version="v2")
        netgroups = json.loads(resp)["nisNetgroups"]
        settings["netgroups"] = netgroups if netgroups else []
        exported_res_dict["NIS Netgroups"] = [
            group["name"] for group in settings["netgroups"]
        ]
        return settings
    except Exception as err:
        print(
            "Error while importing global whitelist settings, err msg %s" % err)
        return None


def get_vlans(cohesity_client):
    """
    Function to fetch Vlans available in the cluster.
    returns: list of Vlans.
    """
    vlans = cohesity_client.vlan.get_vlans()
    vlans = vlans if vlans else []
    for vlan in vlans:
        exported_res_dict["Vlans"].append(vlan.iface_group_name)
    return vlans


def get_routes(cohesity_client):
    """
    Function to fetch the network routes mapping.
    """
    routes = cohesity_client.routes.get_routes() or []
    for route in routes:
        exported_res_dict["Routes"].append(route.iface_group_name)
    return routes


def get_host_mapping(cohesity_client):
    """
    Function to fetch the network routes mapping.
    """
    hosts = cohesity_client.network.list_hosts() or []
    for host in hosts:
        exported_res_dict["Hosts Mapping"].append(host.ip)
    return hosts


def debug():
    """
    Function to return exported resources with types as dict.
    """
    return exported_res_dict


def auto_populate_config(file_name="config.ini"):
    """
    Function to auto-fill ini file based on exported cluster details. From
    existing ini file, import_cluster_config and export_cluster_config sections
    are retained.
    By default config.ini file available in the current directory is updated oe
    else custom provided ini file is updated.
    """
    config = configparser.ConfigParser()

    # Fetch existing config details.
    config_parser = configparser.ConfigParser()
    config_parser.read(file_name)

    # Update import and export config details from existing ini file.
    config["export_cluster_config"] = config_parser["export_cluster_config"]
    config["import_cluster_config"] = config_parser["import_cluster_config"]

    for section, keys in config_dict.items():
        config[section] = dict()
        if not keys:
            config[section]["password"] = ""
            continue
        for key in keys:
            config[section][key] = ""
    try:
        # Update ini file.
        with open(file_name, "w") as file_obj:
            config.write(file_obj)
        return True
    except Exception as err:
        return False
