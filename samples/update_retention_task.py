#!/usr/bin/env python

# Copyright (c) 2018 by Cohesity, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

'''
This tool can be used to extend the expiry time of a snapshots in a protection job run.

Sample Commands:
# python update_retention_task.py --user=admin --password=admin --host=10.2.37.99 --job_id=3636 --run_start_time_usecs=1519478134032549 --extend_n_days=1
'''

import argparse
import sys
from pprint import pprint

import cohesity
from cohesity.api_client import ApiClient
from cohesity.rest import ApiException
from cohesity.configuration import Configuration

from base_task import BaseTask

class UpdateRetentionTask(BaseTask):

    def __init__(self):
        BaseTask.__init__(self, "Update Retention Period of snapshots in a protection job run")

        self.argparser.add_argument('--job_id', help='Protection Job id')

        self.argparser.add_argument('--extend_n_days', type=int,
                                    help='Extend retention period by n days')

        self.argparser.add_argument('--run_start_time_usecs', type=int,
                                    help='Job run start time for which retention needs to be changed')

    # TODO : fix the login issue happening when access_token is set from BaseTask & remove below function
    def setup_access_token(self):
        config = Configuration()
        config.host = 'https://{}/irisservices/api/v1'.format(self.host)
        config.username = self.user
        config.password = self.password
        config.verify_ssl = False
        body = cohesity.AccessTokenCredential(
            username=self.user,
            password=self.password)
            # AccessTokenCredential | Request to generate access token.
        try:
            # Generate an Access Token.
            api_instance = cohesity.AccessTokensApi()
            api_response = api_instance.generate_access_token(body)
            config.api_client = ApiClient(header_name="Authorization", header_value= \
                               api_response.token_type + ' '+ \
                               api_response.access_token)
        except ApiException as ex:
            print "Exception when calling AccessTokensApi->generate_access_token: %s\n" % ex

    def parse_args(self):
        BaseTask.parse_args(self)
        self.job_id = self.args.job_id
        self.extend_n_days = self.args.extend_n_days
        self.run_start_time_usecs =self.args.run_start_time_usecs

    def get_protection_runs(self, job_id, started_time_usecs):
        # create an instance of the API class
        api_instance = cohesity.ProtectionRunsApi()

        try: 
            # List Protection Job Runs filtered by the specified parameters.
            api_response = api_instance.get_protection_runs(
                job_id=job_id, started_time_usecs=started_time_usecs)
            return api_response
        except ApiException as e:
            print "Exception when calling ProtectionRunsApi->get_protection_runs: %s\n" % e
            return None

    def show_protection_runs(self, job_id, started_time_usecs):
        api_response = self.get_protection_runs(job_id, started_time_usecs)
        table_header = [ 'job_run_id', 'job_id', 'job_name',
                         'start_time_usecs', 'environment',
                         'snapshots_deleted', 'expiry_time_usecs']
        table_data = []
        for job_run in api_response:
            expiry_time_usecs = '-'
            for copy_run in job_run.copy_run:
                if copy_run.target.type == 'kLocal':
                    expiry_time_usecs = copy_run.expiry_time_usecs
            table_data.append([
                job_run.backup_run.job_run_id,
                job_run.job_id,
                job_run.job_name,
                job_run.backup_run.stats.start_time_usecs,
                job_run.backup_run.environment,
                job_run.backup_run.snapshots_deleted,
                expiry_time_usecs])
        self.print_table(table_header, table_data)
        return table_header, table_data

    def update_protection_runs(self, extend_n_days, job_id, run_start_time_usecs):
        api_response = self.get_protection_runs(job_id, run_start_time_usecs)

        # Update the expiration date (retention period) for the specified Protection Job Runs and their snapshots. 
        # After an expiration time is reached, the Job Run and its snapshots are deleted. 
        # If an expiration time of 0 is specified, a Job Run and its snapshots are immediately deleted.
        expiry_time_usecs = ''
        for job_run in api_response:
            if job_run.backup_run.stats.start_time_usecs == run_start_time_usecs:
                copy_run = job_run.copy_run
                job_uid = job_run.job_uid
                for run in job_run.copy_run:
                    if run.target.type == 'kLocal':
                        expiry_time_usecs = run.expiry_time_usecs
        if expiry_time_usecs == '':
            raise ValueError('Unable to find expiry_time_usecs for the job run')

        for i in xrange(len(copy_run)):
            if copy_run[i].target.type in ['kLocal']:
                copy_run_targets = [
                    cohesity.RunJobSnapshotTarget(
                            archival_target=copy_run[i].target.archival_target,
                            days_to_keep=extend_n_days,
                            replication_target=copy_run[i].target.replication_target,
                            type=copy_run[i].target.type)
                ]
        # create an instance of the API class
        api_instance = cohesity.ProtectionRunsApi()
        body = cohesity.UpdateProtectionJobRunsParam(
            [cohesity.UpdateProtectionJobRun(
                            copy_run_targets=copy_run_targets,
                            # Updating expiry_time_usecs below is not affecting the expiry. Check days_to_keep param above
                            expiry_time_usecs=expiry_time_usecs+(extend_n_days*86400*1000000), 
                            job_uid=job_uid,
                            run_start_time_usecs=run_start_time_usecs)])
        try: 
            # Update how long Protection Job Runs and their snapshots are retained on the Cohesity Cluster.
            api_instance.update_protection_runs(body)
        except ApiException as e:
            print "Exception when calling ProtectionRunsApi->update_protection_runs: %s\n" % e

    def run(self):
        self.setup_access_token()

        print('Protection Job Run Info : Before Update')
        self.show_protection_runs(self.job_id, self.run_start_time_usecs)

        self.update_protection_runs(self.extend_n_days, self.job_id, self.run_start_time_usecs)

        print('--------------------------------------')
        print('Protection Job Run Info : After Update')
        self.show_protection_runs(self.job_id, self.run_start_time_usecs)

if __name__ == '__main__':
    task = UpdateRetentionTask()
    task.main()
