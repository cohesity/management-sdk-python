## Usage 
```
python protection_runs_status.py
```
Output is formatteed as

```
date time job_name job_run_id status
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
protection_runs = cohesity_client.protection_runs
run_list = protection_runs.get_protection_runs()

```
## Example Output
```
10-21-2019 11:44:45 SQL_File_CBT 166561 kSuccess
10-21-2019 22:09:00 MSMITH-Demo 167096 kSuccess
10-21-2019 17:27:01 Protect_Delete_me_andy 166885 kSuccess
10-22-2019 08:43:05 Replica 167605 kSuccess
```

