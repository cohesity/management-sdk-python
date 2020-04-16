# IMPORT EXPORT TASKS

## Overview

Import export tasks provide option to export cluster resources like sources, views, storage domains, external targets from one cluster to another.


## Prerequisite

In config.ini file, update the cluster credentials of cluster which needs to be imported/exported.


## How to do

Run the following command to export resources.
```
python3 export_cluster_config.py
```

Run the following command to import resources
```
python3 import_cluster_config.py
```
