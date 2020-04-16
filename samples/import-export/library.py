import logging
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

def get_cluster_config(cohesity_client):
    config = cohesity_client.cluster.get_cluster()
    return config


def get_protection_policies(cohesity_client):
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    logger.info("Loading protection policies")
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    return policy_list


def get_storage_domains(cohesity_client):
    logger.info("Loading storage domains")
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    return storage_domain_list


def get_views(cohesity_client):
    logger.info("Loading protection views")
    views = cohesity_client.views.get_views().views
    views_list = views if views else []
    return views_list


def get_protection_jobs(cohesity_client):
    logger.info("Loading protection jobs")
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    return protection_job_list


def get_protection_source_by_id(cohesity_client, id, env):
    protection_source_list = cohesity_client.protection_sources.list_protection_sources(id=id,environment=env)
    return protection_source_list[0]


def get_protection_source_object_by_id(cohesity_client, id):#, env, id):
    #protection_sources = cohesity_client.protection_sources.get_protection_sources_object_by_id(id=id)
    protection_sources = cohesity_client.protection_sources.get_protection_sources_objects(object_ids=[id])
    #print(protection_sources)
    #print(dir(protection_sources))
    #protection_sources = cohesity_client.protection_sources.list_protected_objects(environment=env,id=id)
    #print((protection_sources))
    return protection_sources

def get_protection_sources(cohesity_client):
    #sources = cohesity_client.protection_sources.list_protection_sources_registration_info().root_nodes
    sources = cohesity_client.protection_sources.list_protection_sources_root_nodes()
    sources = sources if sources else []
    return sources
    
def get_external_targets(cohesity_client):
    external_target_list = cohesity_client.vaults.get_vaults()
    return external_target_list