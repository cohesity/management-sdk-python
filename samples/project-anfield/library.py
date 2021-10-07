# Copyright 2020 Cohesity Inc.
#
# Python libraries with functions to import/export the cluster config.

from collections import defaultdict
from rest_client import RestClient

import json
import logging

from cohesity_management_sdk.models.exclude_type_enum import ExcludeTypeEnum as enum
from cohesity_management_sdk.models.environment_enum import EnvironmentEnum as env_enum

from configparser import ConfigParser

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

ad_list = list()
config_dict = defaultdict()
exported_res_dict = defaultdict(list)


def gflag(endpoint, user, password, domain, body={}, action="get"):
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
    config = cohesity_client.cluster.get_cluster()
    return config


def get_protection_policies(cohesity_client):
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    policy_list = policy_list if policy_list else []
    for policy in policy_list:
        exported_res_dict["Protection Policies"].append(policy.name)
    return policy_list


def get_storage_domains(cohesity_client):
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    for domain in storage_domain_list:
        exported_res_dict["Storage Domains"].append(domain.name)
    return storage_domain_list


def get_views(cohesity_client):
    views = cohesity_client.views.get_views().views
    views_list = views if views else []
    for view in views_list:
        exported_res_dict["Protection Views"].append(view.name)
    return views_list


def get_protection_jobs(cohesity_client, skip_jobs=False):
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    active_job_list = []
    for job in protection_job_list:
        # Jobs which are deleted are ignored.
        if job.is_deleted:
            continue
        # Skip jobs which are paused or in-active(failover ready).
        if skip_jobs and (job.is_paused or job.is_active == False):
            continue
        active_job_list.append(job)
        exported_res_dict["Protection Jobs"].append(job.name)
    return active_job_list


def get_protection_source_by_id(cohesity_client, id, env):
    global config_dict
    protection_source_list = cohesity_client.protection_sources.list_protection_sources(
        id=id, environment=env, exclude_types=[enum.KCOMPUTERESOURCE,
         enum.KDATASTORE, enum.KDISTRIBUTEDVIRTUALPORTGROUP,
         enum.KNETWORK, enum.KRESOURCEPOOL, enum.KSTORAGEPOD,
        enum.KVIRTUALAPP])
    return_list = protection_source_list[0] if protection_source_list else None
    if env == env_enum.KGENERICNAS and return_list and return_list.nodes:
        for item in return_list.nodes:
            if item["protectionSource"]["nasProtectionSource"]["protocol"] == "kNfs3":
                continue
            name = str(item["protectionSource"]["name"])
            config_dict[name]=None
    return return_list


def get_protection_sources(cohesity_client):
    global config_dict
    sources = cohesity_client.protection_sources.list_protection_sources_root_nodes()
    sources = sources if sources else []
    for source in sources:
        keys = None
        environment = source.protection_source.environment
        if source.protection_source.environment == env_enum.K_VMWARE:
            name = source.protection_source.name
        elif environment == env_enum.KISILON:
            name = source.protection_source.isilon_protection_source.name
        elif environment == "kCassandra":
            name = source.protection_source.name
            keys = ["username", "password", "db_username", "db_password"]
        else:
            continue
        config_dict[name]= keys
    return sources


def list_protection_sources(cohesity_client, env="kView"):
    sources = cohesity_client.protection_sources.list_protection_sources(
            environments=env)
    sources = sources if sources else []

    return sources


def get_external_targets(cohesity_client):
    global config_dict
    external_target_list = cohesity_client.vaults.get_vaults()
    for target in external_target_list:
        #config[target.name] = dict()
        if target.config.amazon:
            config_dict[target.name] = ["secret_access_key"]
        else:
            config_dict[target.name] = None
        exported_res_dict["External Targets"].append(target.name)
    return external_target_list


def get_remote_clusters(cohesity_client):
    global config_dict
    remote_cluster_list = cohesity_client.remote_cluster.get_remote_clusters()
    for cluster in remote_cluster_list:
        config_dict[cluster.name] = None
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
                    "protectionSource"]["name"]
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
            mapping[_id][node["protectionSource"]["id"]] = \
                node["protectionSource"]["name"]
    return mapping


def get_ad_entries(cohesity_client):
    resp = cohesity_client.active_directory.get_active_directory_entry()
    if resp:
        ad_list = [ad.domain_name for ad in resp]
        exported_res_dict["Active directories"] = ad_list
    return resp


def get_ad_objects(cohesity_client, ad_list=ad_list):
    ad_objects = defaultdict(dict)
    for domain in ad_list:
        # Fetch list of groups and users added to the cluster.
        users = cohesity_client.principals.get_users(domain=domain)
        groups = cohesity_client.groups.get_groups(domain=domain)
        ad_objects[domain]["users"] = users
        ad_objects[domain]["groups"] = groups
    return ad_objects


def get_interface_groups(cohesity_client):
    iface_groups = cohesity_client.interface_group.get_interface_groups()
    iface_groups = [] if not iface_groups else iface_groups
    return iface_groups


def get_whitelist_settings(cohesity_client, rest_obj):
    """"
    Function to fetch available subnet whitelists and NIS netgroups.
    """
    try:
        settings = dict()
        subnets = cohesity_client.clusters.get_external_client_subnets(\
            ).client_subnets
        settings["subnets"] = subnets if subnets else []
        exported_res_dict["Subnet whitelists"] = [
            subnet.ip for subnet in settings["subnets"]]

        NIS_PROVIDER_API = "nis-providers"
        _, resp = rest_obj.get(NIS_PROVIDER_API, version="v2")
        settings["nis_providers"] = json.loads(resp)["nisProviders"]

        NIS_NETGROUPS_API = "nis-netgroups"
        _, resp = rest_obj.get(NIS_NETGROUPS_API, version="v2")
        netgroups = json.loads(resp)["nisNetgroups"]
        settings["netgroups"] = netgroups if netgroups else []
        exported_res_dict["NIS Netgroups"] = [
            group["name"] for group in settings["netgroups"]]
        return settings
    except Exception as err:
        print(
            "Error while impoting global whitelist settings, err msg %s" % err)


def get_vlans(cohesity_client):
    vlans = cohesity_client.vlan.get_vlans()
    vlans = vlans if vlans else []
    for vlan in vlans:
        exported_res_dict["Vlans"].append(vlan.iface_group_name)
    return vlans


def debug():
    return exported_res_dict


def auto_populate_config():
    """
    Function to auto-fill config.ini file based on exported cluster details.
    """
    global config_dict
    config = ConfigParser()

    # Fetch existing config details.
    config_parser = ConfigParser()
    config_parser.read("config.ini")

    # Update import and export config details from existing config.ini file.
    config["export_cluster_config"] = config_parser["export_cluster_config"]
    config["import_cluster_config"] = config_parser["import_cluster_config"]
    for section, keys in config_dict.items():
        config[section] = dict()
        if not keys:
            config[section]["password"] = ""
            continue
        for key in keys:
            config[section][key] = ""

    # Update config.ini file.
    with open("config.ini", "w") as f:
        config.write(f)
