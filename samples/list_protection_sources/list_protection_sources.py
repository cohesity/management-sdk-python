# Copyright 2019 Cohesity Inc.
#
# Python example to get a list Protection jobs.
#
# Usage: python list_protection_jobs.py

import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient

CLUSTER_USERNAME = 'admin'
CLUSTER_PASSWORD = 'admin'
CLUSTER_VIP = '10.14.7.145'
DOMAIN = 'LOCAL'

class ProtectionSourcesList(object):

    def list_protection_sources(self, cohesity_client):
        """
        Method to display the list of ProtectionSources
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        protection_sources = cohesity_client.protection_sources
        srcs_list = protection_sources.list_protection_sources()
        for srcs in srcs_list:
            print(srcs)



def main():

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    protection_srcs = ProtectionSourcesList()
    protection_srcs.list_protection_sources(cohesity_client)

if __name__ == '__main__':
    main()