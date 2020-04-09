ENVIRONMENT = ""
ID = ""

def get_cluster_config(cohesity_client):
    config = cohesity_client.cluster.get_cluster()
    print(config)
    print(dir(config))
    return config


def get_protection_policies(cohesity_client):
    """
    Fetches the protection policies available in the cluster and save the response
    to a file.
    """
    policy_list = cohesity_client.protection_policies.get_protection_policies()
    return policy_list


def get_storage_domains(cohesity_client):
    storage_domain_list = cohesity_client.view_boxes.get_view_boxes()
    return storage_domain_list


def get_views(cohesity_client):
    views = cohesity_client.views.get_views().views
    views_list = views if views else []
    return views_list


def get_protection_jobs(cohesity_client):
    protection_job_list = cohesity_client.protection_jobs.get_protection_jobs()
    return protection_job_list


def get_all_protection_sources(cohesity_client, id):#, env, id):
    protection_sources = cohesity_client.protection_sources.get_protection_sources_objects(object_ids=[id])
    #protection_sources = cohesity_client.protection_sources.list_protected_objects(environment=env,id=id)
    #print((protection_sources))
    return protection_sources

def get_protection_sources(cohesity_client):
    protection_source_list = []
    #sources = cohesity_client.protection_sources.list_protection_sources_registration_info().root_nodes
    sources = cohesity_client.protection_sources.list_protection_sources_root_nodes()
    sources = sources if sources else []
    #return sources
    for source in sources:
        if source.protection_source.environment in ["kView"]:
            #continue
            pass
        protection_source_list.append(source)
    return protection_source_list


def get_external_targets(cohesity_client):
    external_target_list = cohesity_client.vaults.get_vaults()
    return external_target_list