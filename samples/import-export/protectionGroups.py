import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.controllers.protection_jobs_controller import ProtectionJobsController


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('cohesity', 'host_ip'),
                                 username=configparser.get('cohesity', 'username'),
                                 password=configparser.get('cohesity', 'password'),
                                 domain= configparser.get('cohesity', 'domain'))

def get_protection_jobs():
    class_obj = ProtectionJobsController()
    protection_jobs = class_obj.get_protection_jobs()
    protection_jobs_list = []
    if not protection_jobs:
        print("No protection jobs available.")
        return protection_jobs_list

    for protection_job in protection_jobs:
        pj_obj = {}
        indexing_policy = {}
        start_time = {}
        uid = {}
        if protection_job.uid:
            uid["id"] = protection_job.uid.id
            uid["cluster_id"] = protection_job.uid.cluster_id
            uid["cluster_incarnation_id"] = protection_job.uid.cluster_incarnation_id
        if protection_job.start_time:
            start_time["hours"] = protection_job.start_time.hour
            start_time["minute"] = protection_job.start_time.minute
        policy = protection_job.indexing_policy
        if policy:
            indexing_policy["disable_indexing"] = policy.disable_indexing
            indexing_policy["allow_prefixes"] = policy.allow_prefixes
            indexing_policy["deny_prefixes"] = policy.deny_prefixes
        pj_obj["id"] = protection_job.id
        pj_obj["name"] = protection_job.name
        pj_obj["environment"] = protection_job.environment
        pj_obj["policy_id"] = protection_job.policy_id
        pj_obj["view_box_id"] = protection_job.view_box_id
        pj_obj["timezone"] = protection_job.timezone
        pj_obj["priority"] = protection_job.priority
        pj_obj["source_ids"] = protection_job.source_ids
        pj_obj["indexing_policy"] = indexing_policy
        pj_obj["start_time"] = start_time
        pj_obj["parent_source_id"] = protection_job.parent_source_id
        pj_obj["incremental_protection_sla_time_mins"] = protection_job.incremental_protection_sla_time_mins
        pj_obj["full_protection_sla_time_mins"] = protection_job.full_protection_sla_time_mins
        pj_obj["perform_source_side_dedup"] = protection_job.perform_source_side_dedup
        pj_obj["qos_type"] = protection_job.qos_type
        pj_obj["uid"] = uid
        pj_obj["policy_applied_time_msecs"] = protection_job.policy_applied_time_msecs
        pj_obj["modification_time_usecs"] = protection_job.modification_time_usecs
        pj_obj["modified_by_user"] = protection_job.modified_by_user
        pj_obj["creation_time_usecs"] = protection_job.creation_time_usecs
        pj_obj["is_deleted"] = protection_job.is_deleted
        protection_jobs_list.append(pj_obj)
    print(protection_jobs_list)
get_protection_jobs()