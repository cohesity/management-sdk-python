This script upgrades the agents across all tenants, workflow:

1. Get all tenant IDs across cluster.
2. Get all Agent IDs per tenants.
3. Get all Agents unassigned to tenants.
4. Upgrade the agents if they are upgradeable to current release.

## Usage: 
```
python upgrade_agents.py
```

## Connect to the Cohesity Cluster
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)
```

## Get Tenants

```python
resp_tenants = cohesity_client.tenant.get_tenants()
```

## Get Agents
```python
resp_agents = cohesity_client.protection_sources.list_protection_sources(
                              tenant_ids=tenant,
                              environments=EnvironmentEnum.KPHYSICAL)
```

## Upgrade Agent list
```python
body = UpgradePhysicalServerAgents()
body.agent_ids = [agent_id1, agent_id2, agent_id3]
result = cohesity_client.protection_sources.create_upgrade_physical_agents(body)
```

## Example Output
```
Adding Tenant: coke
Adding Tenant: pepsi
Adding Tenant: coco
Adding Tenant: alo
Tenant list: [u'coke/', u'pepsi/', u'coco/', u'alo/'] 

Adding agent: windows_agent to upgrade list
Excluding Agent from upgrade list: aix_agent because upgradability state is : kCurrent 
Adding agent: linux_agent to upgrade list
Adding agent: solaris_agent to upgrade list
Upgrading agents: [u'windows_agent', u'linux_agent', u'solaris_agent']
Agents upgraded [u'windows_agent', u'linux_agent', u'solaris_agent']
Adding agent: ms_sql_agent to upgrade list
Upgrading agents: [u'ms_sql_agent']
Agents upgraded [u'ms_sql_agent'] upgraded
```

