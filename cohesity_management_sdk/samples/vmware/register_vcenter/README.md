## Usage: 
```
python add_vm_to_protection_and_run.py --job_name <name_of_protection_job> --vm_list list_of_vms
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

## Example: Adding vCenter
``` 
req_body = RegisterProtectionSourceParameters()
req_body.endpoint = VCENTER_IP
req_body.username = VCENTER_USERNAME
req_body.password = VCENTER_PASSWORD
req_body.environment = EnvironmentEnum.K_VMWARE
req_body.vmware_type = VmwareTypeEnum.KVCENTER

source = cohesity_client.protection_sources
resp = source.create_register_protection_source(req_body)
```
