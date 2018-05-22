Cohesity Management SDK
=================

![logo](cohesity_python.png)

## Overview

The *Cohesity Management SDK*  provides an easy-to-use language binding to 
harness the power of *Cohesity REST APIs* in your python applications.


## Getting Started
The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using pip ( https://pip.pypa.io/en/stable/ ).
This SDK uses the Requests library and will work for Python ```2 >=2.7.9``` and Python ```3 >=3.4```.

  1. Invoke ```git clone https://github.com/cohesity/management-sdk-python.git```
  2. ```cd management-sdk-python```
  2. Invoke ```pip install -r requirements.txt```
  3. Install cohesity_management_package: ```python setup.py install```. 
  This will install the package in PYTHONPATH.

## How to Use:
This SDK exposes all the functionality provided by `Cohesity REST API`.

Initializing the Client:
```python
username = 'Username'
password = 'Password'
domain = 'Domain' #optional
cluster_vip = 'prod-cluster.eng.cohesity.com'
client = CohesityClient(cluster_vip, username, password, domain)

```

You can perform a wide range of operations such as,
* Retrieve `Cohesity Cluster` details
* List protection sources
* List the protection jobs
* Resolve alerts
* And much more...
Check out the scripts included under `samples` for reference.

## Configure:

The generated code will pick up the default configurations from 
cohesity_management_sdk/configuration.py, hence alternatively, you 
can use configuration.py to set the attributes such as username, password, 
cluster VIP before compilation.
 
 Note : These parameters can be easily overwritten in scripts. Please refer 
 to scripts under sample folder.
 
## Questions or Feedback :

We would love to hear from you. Please send your questions and feedback to: *cohesity-api-sdks@cohesity.com*
