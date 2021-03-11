# Copyright 2021 Cohesity Inc.

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.exceptions.api_exception import APIException

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'

def get_jobs(args):

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    # Clone a cluster with name.
    try:
        jobs = cohesity_client.protection_jobs.get_protection_jobs(is_deleted=False)
        print("Please find the list of available jobs:")
        for job in jobs:
            print("Job %s, environment type %s." % (job.name, job.environment))
    except APIException as e:
        print ("Error : %s" % e.context.response.raw_body)
