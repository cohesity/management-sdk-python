## Usage: 
```
python on_demand_job_run.py --job_name <name_of_protection_job>
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Example
``` 
req_body = ProtectionRunParameters()
req_body.run_type = RunType2Enum.KREGULAR
self.jobs_controller.create_run_protection_job(id=job_id, body=req_body)

# Get the status of this Job run.
jresp = cohesity_client.protection_runs.get_protection_runs(job_id=job_id, num_runs=1)[0]
```

## Example Output
```
01-01-2019 15:06:44	    VM Backup
01-01-2019 16:31:52	    Oracle 
01-01-2019 18:54:08	    NAS Backup
```

