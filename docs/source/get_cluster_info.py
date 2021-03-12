# Copyright 2021 Cohesity Inc.

""" Script to fetch cluster info. """

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'cluster_vip'
DOMAIN = 'LOCAL'

def get_cluster_info(args):

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    # Clone a cluster with name.
    try:
        cluster = cohesity_client.cluster.get_basic_cluster_info()
        print("Please find the cluster details:")
        print("Cluster Name is %s" % cluster.name)
        print("Cluster type is %s" % cluster.cluster_type)
        print("Cluster Version is %s" % cluster.cluster_software_version)

    except APIException as e:
        print ("Error : %s" % e.context.response.raw_body)
