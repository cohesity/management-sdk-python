Introduction
============

The *Cohesity Management SDK*  provides an easy-to-use language binding to
harness the power of *Cohesity REST APIs* in your python applications.

-------

.. sidebar:: About Cohesity

    * **Website**: `www.cohesity.com/ <www.cohesity.com/>`_
    * **Source code**: `https://github.com/cohesity/management-sdk-python <https://github.com/cohesity/management-sdk-python>`_
    * **Twitter**: `@cohesity <https://twitter.com/cohesity>`_

Installation
++++++++++++

Cohesity Management Sdk can be either installed from source or through pip.


**Install via pip**

|   ``pip install cohesity-management-sdk``


**Install from source**

The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using `pip <https://pip.pypa.io/en/stable/>`_.
This SDK uses the Requests library and will work for Python **2 >=2.7.9** and Python **3 >=3.4**.


::

    * git clone https://github.com/cohesity/management-sdk-python.git
    * cd management-sdk-python
    * pip install -r requirements.txt
    * python setup.py install

------

Upgrade
+++++++

To upgrade the package:

|   ``pip install cohesity-management-sdk --upgrade``


To upgade the package to specific release:

|   ``pip install cohesity-management-sdk==1.5.1``


.. note::

  Refer `Python docs <https://developer.cohesity.com/versions.html>`_ for your cluster version.

-------

How to Use
++++++++++

This SDK exposes all the functionality provided by *Cohesity REST API*.


To initialize the API client, the following parameters need to be passed.

+--------------+---------+-----------------------------------------------------------+
| Parameter    |    Type |                       Description                         |
+==============+=========+===========================================================+
| username     | string  | Specifies the login name of the Cohesity user.            |
+--------------+---------+-----------------------------------------------------------+
| password     | string  | Specifies the password of the Cohesity user account.      |
+--------------+---------+----------------+------------------------------------------+
| domain       | string  | Specifies the  | * For a Local user model, the domain is  |
|              |         | domain the user|   always LOCAL.                          |
|              |         | is logging in. | * For LDAP / AD user models, the domain  |
|              |         |                |   will map to an LDAP connection string. |
|              |         |                | * A user is uniquely identified by a     |
|              |         |                |   combination of username and domain.    |
+--------------+---------+----------------+------------------------------------------+
| cluster_vip  |  string | VIP or DNS name of cohesity cluster.                      |
|              |         | Default: '{CLUSTER_VIP}'                                  |
+--------------+---------+-----------------------------------------------------------+

.. important :: If **domain** is not set '**LOCAL**' is assigned.

**Initializing the Client**


.. code-block:: python
    :linenos:
    :emphasize-lines: 3, 9, 11

    """ Sample code to create a cohesity client. """

    from cohesity_management_sdk.cohesity_client import CohesityClient

    username = 'Username'
    password = 'Password'
    domain = 'Domain' #optional
    cluster_vip = 'cluster_vip'
    client = CohesityClient(cluster_vip, username, password, domain)
    cluster_controller = client.cluster
    result = cluster_controller.get_basic_cluster_info()
    print(result_dict.cluster_software_version)


**Output**

``6.4.1_release-20191219_aafe3274``

-------

Questions or Feedback
+++++++++++++++++++++

We would love to hear from you. Please send your questions and feedback to: cohesity-api-sdks@cohesity.com


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started

   Introduction <intro.rst>
   Examples <examples.rst>
   License <license.rst>


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: API Endpoints

   Controllers <controllers.rst>


.. toctree::
   :maxdepth: 4
   :hidden:
   :caption: Models

   Structures <models.rst>
   Exceptions <exceptions.rst>
   Enumerations <enum.rst>
