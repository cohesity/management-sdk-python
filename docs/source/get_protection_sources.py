# Copyright 2021 Cohesity Inc.

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'cluster_vip'
DOMAIN = 'LOCAL'

def get_protection_sources(args):

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    # Clone a cluster with name.
    try:
        sources = cohesity_client.protection_sources.list_protection_sources()
        print("Please find the list of available sources:")
        for source in sources:
            print("Source %s, environment type %s." % (
                source.protection_source.name, source.protection_source.environment))
    except APIException as e:
        print ("Error : %s" % e.context.response.raw_body)
