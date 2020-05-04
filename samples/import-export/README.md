# Cohesity Cluster Export/Import

## Overview

Import export tasks provide option to export and import the cluster resources namely
  * Protection Sources
  * Cohesity Views
  * Storage Domains, 
  * External targets(NAS, s3) 
  * Cluster Configs
    * DNS
    * NTP Servers
    * Domain Names
  * Protection Jobs
  * Protection Sources(NAS, Views, VMware)
  * Protection Policies
  
## Installation
```
pip install cohesity_management_sdk configparser 
```
This will work for Python 2 >=2.7.9 and Python 3 >=3.4.

## Prerequisite
```
1. The API connectivity from the box which is running these scripts to the exported/imported cluster(s).
        2. In config.ini : 
            a. Exported Cluster credentials.
            b. Imported Cluster credentials.
            c. Replicated cluster credentials 
            d. Protection sources such as vCenter credentials
            3. S3 Secret Access key. 
```
## Note
```
1. This is not a restore point feature. It doesn't add/delete incremental updates for existing entities.
```

## Export 

Run the following command to export resources.
```
python export_cluster_config.py
```
The above command will generate a <export-config-timestamp> file (eg: export-config-2020-04-17-12:15) which needs be provided while importing resources.

### Ouput 
```
INFO:export_app:Exporting resources from cluster 'xyzzy'
INFO:export_app:
 *** Exported resources summary ***

INFO:export_app:	*** Protection Views ***:
Check, NaveenaView, Test, DemoUI, Target

INFO:export_app:	*** Storage Domains ***:
DefaultStorageDomain, StorageRe;l, Physical

INFO:export_app:	*** Protection Policies ***:
Default Policy, Bronze, Gold, viewpolicy, Nas policy, Replication policy, Silver, Physical

INFO:export_app:	*** Protection Jobs ***:
newmanJob-1584050541627-412, VMWare-job, Replication Job , DB_tier

INFO:export_app:	*** External Targets ***:
Newman-vault-1586863576896, Newman-vault-1586870313194, TestTarget, check, CheckTarget

INFO:export_app:	*** Protection Sources ***:
 10.2.x.y:/target, x.y.z.y, 10.2.145.23, 10.2..x.y, vcenter.eng.cohesity.com
```

 ## Import
```
python import_cluster_config.py <export-config-Cluster-Name-timestamp>
```

### Output
```
INFO:import_app:
 *** Imported resources summary ***

INFO:import_app:Successfully registered/created the following Protection Views:
Check, NaveenaView, Test, DemoUI, Target

INFO:import_app:Successfully registered/created the following External Targets:
TestTarget, check, CheckTarget

INFO:import_app:Successfully registered/created the following Protection Sources:
10.2.x.y:/target, 10.2.x.y, 10.2.x.y

INFO:import_app:Successfully registered/created the following Protection Policies:
Default Policy, Bronze, Gold, viewpolicy, Nas policy, Replication policy, Silver, Physical

INFO:import_app:Successfully registered/created the following Protection Jobs:
SingleVm

*** Corrective actions/errors  ***
ERROR:import_app: Please specify the password for vCenter vcenter.eng.cohesity.com source in config.ini
ERROR:import_app:Response status code: 500, Response message: Specified parent source vcenter.eng.cohesity.com does not match the real parent source 10.2.x.y of entity App-tier-vms-0
```
