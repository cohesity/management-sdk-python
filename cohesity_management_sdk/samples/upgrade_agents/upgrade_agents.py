# Copyright 2019 Cohesity Inc.
#
# This script upgrades the agents across all tenants.
# Workflow:
# 1. Get all tenant IDs across cluster.
# 2. Get all Agent IDs per tenants.
# 2. Get all Agents unassigned to tenants.
# 3. Upgrade the agents per tenant.
# Usage: python upgrade_agents.py
# Fill in the cluster credentials below:

CLUSTER_VIP = 'cluster-vip'
CLUSTER_USERNAME = 'username'
CLUSTER_PASSWORD = 'password'
CLUSTER_DOMAIN = 'domain'
AGENT_PARALLEL_UPGRADES = 10

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.environments_2_enum import Environments2Enum
from cohesity_management_sdk.models.upgrade_physical_server_agents_request import UpgradePhysicalServerAgentsRequest

try:
    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
                                     domain=CLUSTER_DOMAIN)
except APIException as ex:
    print("Unable to initialze the client due to : %s " % ex.context)
    SystemExit

def get_tenants():
    """
    Function to get tenant ID list.
    :return tenant_list[list{str}]: List of tenant_id string.
    """
    tenant_list = []
    try:
        resp_tenants = cohesity_client.tenant.get_tenants()
    except APIException as ex:
        print("Unable to get tenant list: %s" % ex.context.response.raw_body)
        raise SystemExit
    for tenant in resp_tenants:
        tenant_list.append(tenant.tenant_id)
        print("Adding Tenant: %s" % tenant.name)
    return tenant_list

def _get_agents(tenant=None, agent_dict=None):
    try:
        resp_agents = cohesity_client.protection_sources.list_protection_sources(
                              tenant_ids=tenant,
                              environments=Environments2Enum.KPHYSICAL)
    except APIException as ex:
        raise SystemExit("Unable to get agent list: %s" %
                         ex.context.response.raw_body)
    if len(resp_agents) == 0:
        return
    node_list = resp_agents[0].nodes
    for agent in node_list:
        agent_src = agent['protectionSource']['physicalProtectionSource']['agents'][0]
        agent_dict[agent_src[ 'id']] = {
            'upgradability':agent_src['upgradability'],
            'name': agent['protectionSource']['physicalProtectionSource']['name'],
            'status':agent_src['status']}

def get_agents(tenant_list):
    """
    Function to construct agents dictionary per tenant.
    :param tenant_list[{str}]: List of tenant IDs.
    :return agent_dict: Dictionary of agents with format:
    agent_dict : {'name': 'agent_name',
                  'upgradability': 'kUpgradeable | kCurrent'
                  'status': 'kHealthy' | 'kUnreachable'}
    """
    agent_dict = {}
    for tenant in tenant_list:
        _get_agents(tenant, agent_dict)
    # For agents which do not have any tenants.
    _get_agents(agent_dict=agent_dict)
    return agent_dict

def _upgrade_agents(temp_upgrade_list):
    body = UpgradePhysicalServerAgentsRequest()
    body.agent_ids = temp_upgrade_list
    try:
        result = cohesity_client.protection_sources \
            .create_upgrade_physical_agents(body)
        if result.message == "Upgrading physical agents started.":
            return True
    except APIException as ex:
        print("Unable to get agent list: %s" %
              ex.context.response.raw_body)
        print("Continuing the operation")
    return False

def upgrade_agents(agent_dict):
    """
    Function to upgrade the Physical Agents in the cluster.
    :param agent_dict:
    :return: None
    """
    temp_upgrade_list = []
    temp_agent_names = []
    pagination = 0

    for agent_id, agent in agent_dict.iteritems():
        if agent['upgradability'] == 'kUpgradable':
            temp_upgrade_list.append(agent_id)
            temp_agent_names.append(agent['name'])
            pagination += 1
            print("Adding agent: %s to upgrade list"% agent['name'] )
        else:
            print("Excluding Agent from upgrade list: %s because upgradability "
                  "state is : %s " % (agent['name'], agent['upgradability']))
        if pagination >= AGENT_PARALLEL_UPGRADES:
            print("Upgrading agents: %s" % temp_agent_names)
            result = _upgrade_agents(temp_upgrade_list)
            if result:
                print("Agents %s upgraded\n" % temp_agent_names)
            temp_agent_names = []
            temp_upgrade_list = []
            pagination = 0
    if temp_upgrade_list:
        print("Upgrading agents: %s" % temp_agent_names)
        result = _upgrade_agents(temp_upgrade_list)
        if result:
            print("Agents upgraded %s" % temp_agent_names)

def main():

    tenant_list = get_tenants()
    print("Tenant list: %s\n" % tenant_list)
    agent_dict = get_agents(tenant_list)
    upgrade_agents(agent_dict)

if __name__ == '__main__':
    main()