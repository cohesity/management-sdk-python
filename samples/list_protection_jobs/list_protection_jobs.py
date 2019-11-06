# Copyright 2019 Cohesity Inc.
#
# Python example to get a list Protection jobs.
#
# Usage: python list_protection_jobs.py

import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'

class ProtectionJobsList(object):

    def display_protection_jobs(self, cohesity_client):
        """
        Method to display the list of Active
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        protection_jobs = cohesity_client.protection_jobs
        jobs_list = protection_jobs.get_protection_jobs()
        for job in jobs_list:
            print ('{0:<10}\t\t{1:>8}'.format(
                self.epoch_to_date(job.creation_time_usecs), job.name))

    @staticmethod
    def epoch_to_date(epoch):
        """
        Method to convert epoch time in usec to date format
        :param epoch(int): Epoch time of the job run.
        :return: date(str): Date format of the job runj.
        """
        date = datetime.datetime.fromtimestamp(epoch/10**6).\
            strftime('%m-%d-%Y %H:%M:%S')
        return date

def main():

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    protect_object = ProtectionJobsList()
    protect_object.display_protection_jobs(cohesity_client)

if __name__ == '__main__':
    main()
