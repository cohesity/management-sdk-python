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
This tool can be used to filter & resolve alerts in some time range (or) last n days.
While resolving, an existing resolution can be used or a new resolution can be created

Sample Commands:
# python resolve_alerts_task.py --user=admin --password=admin --host=10.2.37.99 --start=1518787396549595 --end=1518787396549595 --resolution_id=332635
# python resolve_alerts_task.py --user=admin --password=admin --host=10.2.37.99  --last_n_days=5 --summary='DummySummary1'
'''

import argparse
import time
import sys
from pprint import pprint

import cohesity
from cohesity.api_client import ApiClient
from cohesity.rest import ApiException
from cohesity.configuration import Configuration

from base_task import BaseTask

class ResolveAlertsTask(BaseTask):

    def __init__(self):
        BaseTask.__init__(self, "Update Retention Period of snapshots in a protection job run")

        self.argparser.add_argument('--summary', action='store', dest='summary',
                            help='Summary for new resolution')

        # args for resolving using existing resolution

        self.argparser.add_argument('--resolution_id',
                            help='resolution_id to be used for resolving the alerts')

        # args for filtering alerts

        self.argparser.add_argument('--severity_list',
                            default='kInfo',
                            help='Comma seperated list of severity to filter the alerts to be resolved')

        self.argparser.add_argument('--last_n_days',
                            type=int,
                            help='Last n days to look for while fetching alerts')

        self.argparser.add_argument('--start',
                            default=int(time.time()*1000000),
                            type=int,
                            help='Num days in (today-start_date)')

        self.argparser.add_argument('--end',
                            default=int(time.time()*1000000),
                            type=int,
                            help='Num days in (today-end_date)')

        self.argparser.add_argument('--max_alerts',
                            default=100,
                            type=int,
                            help='max no. of alerts to be fetched')

    def parse_args(self):
        BaseTask.parse_args(self)

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

    def get_resolutions(self):
        api_instance = cohesity.AlertsApi()
        max_resolutions = 100 # int | Limit the number of returned Alert Resolutions. The newest Resolutions are returned.

        try:
            # List the Alert Resolutions on the Cohesity Cluster.
            api_response = api_instance.get_resolutions(max_resolutions)
            return api_response
        except ApiException as e:
            print "Exception when calling AlertsApi->get_resolutions: %s\n" % e
            return None

    def show_resolutions(self, api_response=None):
        if api_response is None:
            api_response = self.get_resolutions()
        table_header = ['resolution_id', 'resolution_summary', 'timestamp_usecs', 'alert_id_count']
        table_data = []
        for resolution in api_response:
            details = resolution.resolution_details
            table_data.append([details.resolution_id,
                details.resolution_summary,
                details.timestamp_usecs,
                len(resolution.alert_id_list)])
        self.print_table(table_header, table_data)

    def get_alerts(self):
        # Create an instance of the API class
        api_instance = cohesity.AlertsApi()
        max_alerts = 100 # int | Limit the number of returned Alerts. The newest Alerts are returned.
        try:
            api_response = api_instance.get_alerts(max_alerts)
            return api_response
        except ApiException as e:
            print "Exception when calling AlertsApi->get_alerts: %s\n" % e
            return None

    def get_filtered_alerts(self,
        alert_state_list, alert_severity_list, start_date_usecs,
        end_date_usecs, alert_id_list=[], resolution_id_list=[],
        alert_type_list=[], max_alerts=100, alert_category_list=[]):
        # create an instance of the API class
        api_instance = cohesity.AlertsApi()
        try:
            # List the Alerts on the Cohesity Cluster.
            api_response = api_instance.get_alerts(
                max_alerts,
                # alert_category_list=alert_category_list,
                # alert_id_list=alert_id_list,
                # alert_type_list=alert_type_list,
                alert_state_list=alert_state_list,
                alert_severity_list=alert_severity_list,
                # resolution_id_list=resolution_id_list,
                # start_date_usecs=start_date_usecs,
                # end_date_usecs=end_date_usecs
            )
            return api_response
        except ApiException as e:
            print "Exception when calling AlertsApi->get_alerts: %s\n" % e
            return None

    def show_alerts(self, api_response=None):
        if api_response is None:
            api_response = self.get_alerts()
        table_header = [ 'alert_name', 'alert_category', 'alert_state',
                         'severity', 'latest_timestamp_usecs', 'id']
        table_data = []
        for alert in api_response:
            table_data.append([
                alert.alert_document.alert_name,
                alert.alert_category,
                alert.alert_state,
                alert.severity,
                alert.latest_timestamp_usecs,
                alert.id])
        self.print_table(table_header, table_data)

    def create_resolution(self, summary, username, api_response):
        alert_id_list = []
        for alert in api_response:
            alert_id_list.append(alert.id)

        # create an instance of the API class
        api_instance = cohesity.AlertsApi()
        body = cohesity.AlertResolutionRequest() # AlertResolutionRequest | Request to create an Alert Resolution and apply it to the specified Alerts.
        body.resolution_details = cohesity.AlertResolutionDetails(
            resolution_summary=summary, user_name=username)
        body.alert_id_list = alert_id_list

        try:
            # Create an Alert Resolution.
            api_response = api_instance.create_resolution(body)
            self.show_resolutions([api_response])
            return api_response
        except ApiException as e:
            print "Exception when calling AlertsApi->create_resolution: %s\n" % e
            return None

    def resolve_alerts(self, api_response, resolution_id):
        alert_id_list = []
        for alert in api_response:
            alert_id_list.append(alert.id)

        # create an instance of the API class
        api_instance = cohesity.AlertsApi()
        body = cohesity.UpdateResolutionParams(alert_id_list=alert_id_list)

        try:
            # Apply an existing Alert Resolution to additional Alerts.
            api_response = api_instance.update_resolution(resolution_id, body)
            self.show_resolutions(api_response)
            return api_response
        except ApiException as e:
            print "Exception when calling AlertsApi->update_resolution: %s\n" % e
            return None

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

        # Show all alerts
        print('All alerts:')
        self.show_alerts()
        print('')

        if self.args.last_n_days is not None:
            start_date_usecs = int(time.time()*1000000) - (86400*1000000*self.args.last_n_days)
            end_date_usecs = int(time.time()*1000000)
        else:
            start_date_usecs = self.args.start
            end_date_usecs = self.args.end

        api_response = self.get_filtered_alerts(
            max_alerts = self.args.max_alerts,
            alert_state_list = ['kOpen'],
            alert_severity_list = self.args.severity_list.split(','),
            start_date_usecs = start_date_usecs,
            end_date_usecs = end_date_usecs)

        # Show filtered alerts which are selected to be resolved
        print('Open alerts:')
        self.show_alerts(api_response)
        print('')

        print('Alert Resolutions:')
        self.show_resolutions()
        print('')

        # Resolve the selected alerts using an existing resolution or by creating a new resolution
        if self.args.summary is not None:
            print
            if api_response is not None:
                self.create_resolution(summary=self.args.summary, username=self.args.user,
                    api_response=api_response)
            else:
                print('Please check if alerts exist with this filter')
        else:
            self.resolve_alerts(api_response, resolution_id=self.args.resolution_id)

if __name__ == '__main__':
    task = ResolveAlertsTask()
    task.main()
