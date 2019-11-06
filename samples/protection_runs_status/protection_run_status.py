# Copyright 2019 Cohesity Inc.
#
# Python example to get a status of a protection run
#
# Usage: python protection_run_status.py

import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient

CLUSTER_VIP = 'CLUSTER_VIP'
CLUSTER_USERNAME = 'CLUSTER_USERNAME'
CLUSTER_PASSWORD = 'CLUSTER_PASSWORD'
DOMAIN = 'DOMAIN'

class ProtectionRunsList(object):

    def display_protection_runs(self, cohesity_client):
        """
        Method to display the list of protection runs
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        protection_runs = cohesity_client.protection_runs
        run_list = protection_runs.get_protection_runs()
        for run in run_list:
            print(self.epoch_to_date(run.backup_run.stats.start_time_usecs), run.job_name, run.backup_run.job_run_id, run.backup_run.status)

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
    protection_runs = ProtectionRunsList()
    protection_runs.display_protection_runs(cohesity_client)

if __name__ == '__main__':
    main()
