Cohesity Management SDK
=================
[![License: Apache2](https://img.shields.io/hexpm/l/plug.svg)](https://github.com/cohesity/management-sdk-python/blob/master/LICENSE)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/cohesity/management-sdk-python?include_prereleases)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cohesity_management_sdk)
![Maintenance](https://img.shields.io/maintenance/yes/2021)
## Overview

The *Cohesity Management SDK*  provides an easy-to-use language binding to
harness the power of *Cohesity REST APIs* in your python applications.

## Table of contents :scroll:

 - [Getting Started](#get-started)
 - [Documentation](#documentation)
 - [How to use](#howto)
 - [More samples](#sample)
 - [How can you contribute](#contribute)
 - [Suggestions and Feedback](#suggest)
 

## <a name="get-started"></a> Let's get started :hammer_and_pick:

### Installation

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

### Upgrade

To upgrade the package:

```
 pip install cohesity-management-sdk --upgrade
```

To upgade the package to specific release:

```
pip install cohesity-management-sdk==1.5.1
```

## <a name="documentation"></a> Documentation :books:

<a href="https://developer.cohesity.com/versions.html">Refer Python docs for your cluster version. </a>

## <a name="howto"></a> How to Use: :mag_right:

This SDK exposes all the functionality provided by *Cohesity REST API*.

Initializing the Client:
```
username = 'Username'
password = 'Password'
domain = 'Domain' #optional
cluster_vip = 'prod-cluster.eng.cohesity.com'
client = CohesityClient(cluster_vip, username, password, domain)
cluster_controller = client.cluster
result = cluster_controller.get_basic_cluster_info()
result_dict =  result.__dict__
print(result_dict['cluster_software_version']) 


#OUTPUT
6.4.1_release-20191219_aafe3274
```

## <a name="sample"></a> More sample code to get going: :bulb:

Check out the scripts included under [`samples`](./samples) for reference.

## <a name="contribute"></a> Contribute :handshake:

* [Refer our contribution guideline](./CONTRIBUTING.md).


## <a name ="suggest"></a> Questions or Feedback :raised_hand:

We would love to hear from you. Please send your questions and feedback to: *cohesity-api-sdks@cohesity.com*
