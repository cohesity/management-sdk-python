import configparser
from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.controllers.protection_policies_controller import ProtectionPoliciesController


# Fetch the Cluster credentials from config file.
configparser = configparser.ConfigParser()
configparser.read('config.ini')

cohesity_client = CohesityClient(cluster_vip=configparser.get('cohesity', 'host_ip'),
                                 username=configparser.get('cohesity', 'username'),
                                 password=configparser.get('cohesity', 'password'),
                                 domain= configparser.get('cohesity', 'domain'))

def get_protection_policies(id=None):
    policy_list = []
    class_obj = ProtectionPoliciesController()
    protection_policies = class_obj.get_protection_policies(ids=id)
    if not protection_policies:
        print("No protection policies available")
        return policy_list
    for each_policy in protection_policies:
        policy_obj = {}
        retention_policy = []
        if each_policy.extended_retention_policies:
            for ret_pol in each_policy.extended_retention_policies:
                obj = {}
                obj["days_to_keep"] = ret_pol.days_to_keep
                obj["multiplier"] = ret_pol.days_to_keep
                obj['periodicity'] = ret_pol.periodicity
                retention_policy.append(obj)

        try:
            policy_obj["type"] = each_policy.mtype
        except Exception as err:
            pass
        policy_obj["extended_retention_policies"] = retention_policy
        policy_obj["id"] = each_policy.id
        policy_obj["is_usable"] = each_policy.is_usable
        policy_obj["days_to_keep"] = each_policy.days_to_keep
        policy_obj["name"] = each_policy.name
        policy_obj["retries"] = each_policy.retries
        policy_obj["retry_interval_mins"] = each_policy.retry_interval_mins
        policy_list.append(policy_obj)
    print(policy_list)
get_protection_policies()
