## Usage 
```
python list_protection_sources.py
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD,
                                 domain=DOMAIN)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Example
``` 
protection_sources = cohesity_client.protection_sources
sources_list = protection_sources.list_protection_sources()

```
## Example Output
```
list of Protection Sources
```