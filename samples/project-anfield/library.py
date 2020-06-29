# Copyright 2020 Cohesity Inc.
#
# Python libraries with functions to import/export the cluster config.

from collections import defaultdict
from rest_client import RestClient

import json
import logging
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

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


def get_protection_jobs(cohesity_client):
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    active_job_list = []
    for job in protection_job_list:
        if job.is_deleted or job.is_active == False:
            continue
        active_job_list.append(job)
        exported_res_dict["Protection Jobs"].append(job.name)
    return active_job_list


def get_protection_source_by_id(cohesity_client, id, env):
    protection_source_list = cohesity_client.protection_sources.list_protection_sources(
        id=id, environment=env)
    return_list = protection_source_list[0] if protection_source_list else None
    return return_list


def get_protection_sources(cohesity_client):
    sources = cohesity_client.protection_sources.list_protection_sources_root_nodes()
    sources = sources if sources else []
    return sources


def get_external_targets(cohesity_client):
    external_target_list = cohesity_client.vaults.get_vaults()
    for target in external_target_list:
        exported_res_dict["External Targets"].append(target.name)
    return external_target_list


def get_remote_clusters(coheity_client):
    remote_cluster_list = coheity_client.remote_cluster.get_remote_clusters()
    return remote_cluster_list


def debug():
    return exported_res_dict
