## Usage 
```
python list_protection_jobs.py
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
protection_jobs = cohesity_client.protection_jobs
jobs_list = protection_jobs.get_protection_jobs()

```
## Example Output
```
01-01-2019 15:06:44	   VM Backup
01-01-2019 16:31:52	   Oracle 
01-01-2019 18:54:08	   NAS Backup
```

