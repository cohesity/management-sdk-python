# Copyright 2019 Cohesity Inc.
#
# Python example to start a protection job on demand by job name.
# Usage: python on_demand_job_run.py --job_name <name_of_protection_job>

import argparse
import configparser
import time

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.protection_job_request_body import ProtectionJobRequestBody
from cohesity_management_sdk.models.run_type_enum import RunTypeEnum
from cohesity_management_sdk.models.status_source_backup_status_enum import \
    StatusSourceBackupStatusEnum

parser = configparser.ConfigParser()
parser.read('config.ini')
CLUSTER_VIP = parser.get('cohesity', 'cluster_vip')
CLUSTER_USERNAME = parser.get('cohesity', 'username')
CLUSTER_PASSWORD = parser.get('cohesity', 'password')
DOMAIN = parser.get('cohesity', 'domain')

class ProtectionJobs(object):
    """
    Class to display Alerts.
    """

    def __init__(self, cclient):
        self.cohesity_client = cclient
        self.jobs_controller = self.cohesity_client.protection_jobs
        self.run_controller = self.cohesity_client.protection_runs

    def name_to_job_id(self, job_name):
        """
        Method to convert name of the job to id. If conflicts
        :param job_name(str): Name of the Protection job.
        :return
            status(bool): If Protection job doesn't exist, this is set to False.
            job_id(int) : Protection Job ID.
        """
        result = self.jobs_controller.get_protection_jobs(names=job_name)
        if not result:
            return False, 0
        return True, result[0].id

    def run_job(self, job_name):
        """
        Method to run the Job specified on demand.
        :param job_name(str): Protection Job name.
        :return: None.
        """
        status, job_id = self.name_to_job_id(job_name)
        if not status:
            print ("Protection Job with name: %s doesn't exist" % job_name)
            exit(0)

        req_body = ProtectionJobRequestBody()
        req_body.run_type = RunTypeEnum.KREGULAR
        self.jobs_controller.create_run_protection_job(id=job_id, body=req_body)

        # Get the status of this Job run.
        jresp = self.run_controller.get_protection_runs(job_id=job_id,
                                                        num_runs=1)
        if jresp == []:
            time.sleep(20)
            jresp = self.run_controller.get_protection_runs(job_id=job_id,
                                                            num_runs=1)[0]
        else:
            jresp = jresp[0]
        if jresp.backup_run.status == StatusSourceBackupStatusEnum.KSUCCESS \
                or jresp.backup_run.status == \
                StatusSourceBackupStatusEnum.KACCEPTED:
            print ("Protection Job %s started successfully" % job_name)
        elif jresp.backup_run.status == StatusSourceBackupStatusEnum.KFAILURE:
            print ("Protection Job %s failed." % job_name)


def main(args):

    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
				                     domain=DOMAIN)
    pj = ProtectionJobs(cohesity_client)
    pj.run_job(args.job_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments needed to run this python process.")
    parser.add_argument("--job_name", help="Name of the Protection Job.",
                        required=True)
    args = parser.parse_args()
    main(args)
