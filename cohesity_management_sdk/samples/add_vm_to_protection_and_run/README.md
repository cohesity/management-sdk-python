## Usage: 
```
python add_vm_to_protection_and_run.py --job_name <name_of_protection_job> --vm_list list_of_vms
```

## Connect to the Cohesity Cluster
First make sure that you are connected to a Cohesity Cluster.
```python
cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                 username=CLUSTER_USERNAME, 
                                 password=CLUSTER_PASSWORD)
```
Note: Alternatively, you can set the above parameters in cohesity_management_sdk/configuration.py

## Example list VMs from Source
```
resp_vm_list = cohesity_client.protection_sources.list_virtual_machines(str_vm_list)
vm_id_list = [vm.id for vm in resp_vm_list]
```

## Example Add VMs source_id to a Protection Job.
```
resp.source_ids = vm_id_list + resp.source_ids
update_resp = self.cohesity_client.protection_jobs.update_protection_job(body=resp, id=resp.id)
```

