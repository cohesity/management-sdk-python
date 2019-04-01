Cohesity Management SDK
=================

## Overview

The *Cohesity Management SDK*  provides an easy-to-use language binding to
harness the power of *Cohesity REST APIs* in your python applications.


## Install

Install via pip:
```
pip install cohesity-management-sdk
```

Install from source:

The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using [pip](https://pip.pypa.io/en/stable/).
This SDK uses the Requests library and will work for Python *2 >=2.7.9*
and Python *3 >=3.4*.
```
git clone https://github.com/cohesity/management-sdk-python.git
cd management-sdk-python
pip install -r requirements.txt
python setup.py install
```

## How to Use:
This SDK exposes all the functionality provided by *Cohesity REST API*.

Initializing the Client:
```
username = 'Username'
password = 'Password'
domain = 'Domain' #optional
cluster_vip = 'prod-cluster.eng.cohesity.com'
client = CohesityClient(cluster_vip, username, password, domain)
```

You can perform a wide range of operations such as:

* Retrieve *Cohesity Cluster* details
* List protection sources
* List the protection jobs
* Resolve alerts
* vCenter workflows
* AWS boto3 object store workflows

And much more, check out the scripts included under
`cohesity_management_sdk/samples` for reference.

## Upgrade

To upgrade the package:

```
 pip install cohesity-management-sdk --upgrade
```

To upgade the package to specific release:

```
pip install cohesity-management-sdk==1.0.2
```
## Questions or Feedback :

We would love to hear from you. Please send your questions and feedback to: *cohesity-api-sdks@cohesity.com*
