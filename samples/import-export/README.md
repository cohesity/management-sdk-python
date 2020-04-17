# IMPORT EXPORT TASKS

## Overview

Import export tasks provide option to export cluster resources like sources, views, storage domains, external targets from one cluster to another.

## Installation

The generated code uses Python packages named jsonpickle and dateutil. You can resolve these dependencies using pip. This will work for Python 2 >=2.7.9 and Python 3 >=3.4.

## Prerequisite

In config.ini file, update the cluster credentials of cluster which needs to be imported/exported.

## How to do

Run the following command to export resources.
```
python3 export_cluster_config.py
```
The above command will generate a export-config file which needs be provided while importing resources.

Run the following command to import resources
```
python3 import_cluster_config.py <export-config file>
```

## Output

* INFO:import_cluster_config.py:Please find the imported resources summary.
* INFO:import_cluster_config.py:Successfully registered/created the following Protection Jobs:
newmanJob-1584050541627-412, MultipleVms, Replication Job Test, SingleVm
* INFO:import_cluster_config.py:Successfully registered/created the following Protection Views:
Check, Test, DemoUI, Target
* INFO:import_cluster_config.py:Successfully registered/created the following Protection Sources:
10.2.102.11:/target, 10.2.102.11:/Test, 10.2.167.151, 10.2.145.23, vc-67.eco.eng.cohesity.com, sv4-qa-vcenter65-01.eng.cohesity.com
* INFO:import_cluster_config.py:Successfully registered/created the following Protection Policies:
Default Policy, Bronze, Gold, viewpolicy, Nas policy, Replication policy, Silver, Physical
* INFO:import_cluster_config.py:Successfully registered/created the following External Targets:
TestTarget, check, CheckTarget
