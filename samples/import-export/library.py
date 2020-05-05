import logging
from collections import defaultdict
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


exported_res_dict = defaultdict(list)

def get_cluster_config(cohesity_client):
    config = cohesity_client.cluster.get_cluster()
    return config


def get_cluster_partitions(cohesity_client):
    return cohesity_client.cluster_partitions.get_cluster_partitions()


def get_protection_policies(cohesity_client):
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    #logger.info("Loading protection policies")
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    policy_list = policy_list if policy_list else []
    for policy in policy_list:
        exported_res_dict["Protection Policies"].append(policy.name)
    return policy_list


def get_storage_domains(cohesity_client):
    #logger.info("Loading storage domains")
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    for domain in storage_domain_list:
        exported_res_dict["Storage Domains"].append(domain.name)

    return storage_domain_list


def get_views(cohesity_client):
    #logger.info("Loading protection views")
    views = cohesity_client.views.get_views().views
    views_list = views if views else []
    for view in views_list:
        exported_res_dict["Protection Views"].append(view.name)
    return views_list


def get_protection_jobs(cohesity_client):
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    for job in protection_job_list:
        if not job.name.startswith("_DELETED_"):
            exported_res_dict["Protection Jobs"].append(job.name)
    return protection_job_list


def get_protection_source_by_id(cohesity_client, id, env):
    protection_source_list = cohesity_client.protection_sources.list_protection_sources(id=id,environment=env)
    return protection_source_list[0]


def get_protection_source_object_by_id(cohesity_client, id):#, env, id):
    protection_sources = cohesity_client.protection_sources.get_protection_sources_objects(object_ids=[id])
    return protection_sources

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