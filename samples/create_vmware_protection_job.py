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
"""
APIs for Cohesity Protection Policy Jobs
"""
import argparse
import sys
from pprint import pprint
import datetime
import os.path
import json

sys.path.append('../sdk')
import cohesity
from cohesity.api_client import ApiClient
from cohesity.rest import ApiException
from cohesity.configuration import Configuration

from base_task import BaseTask

class CohesityProtectionSources(BaseTask):
    """Cohesity class to do protection job operations."""
    
    def __init__(self):
        BaseTask.__init__(self, "Protection Sources")
        self.argparser.add_argument('--sources', help='Enter source name(s)')
        self.argparser.add_argument('--file_name', help='Enter the parameter \
                   file with proper relative or absolute \
                   path', default='default_params.json')

    def parse_args(self):
        BaseTask.parse_args(self)
        self.source_names = self.args.sources.split(',')
        self.file_name = self.args.file_name
        if (not os.path.isfile(self.file_name)):
            print("Please enter the valid file name\n")
            sys.exit(1)     

    def parse_params_file(self):
        with open(self.file_name) as f:
             self.params = json.load(f)
        for section, data in self.params.iteritems() :
            if (section == 'protection_policy'):
                self.pol_days_to_keep = int(data['days_to_keep'])
                self.pol_description = data['description']
                self.pol_retries = int(data['retries'])
                self.pol_retry_interval_mins = int(data['retry_interval_mins'])
                self.pol_inc_periodicity = data['inc_periodicity']
                self.pol_inc_backup_mins = int(data['inc_backup_mins'])
                self.pol_inc_days = None
                self.pol_inc_day = None
                self.pol_inc_day_count = None

            if (section == 'protection_job'):
                self.job_full_protection_sla_time_mins = \
        int(data['full_protection_sla_time_mins'])
                self.job_description = data['description']
                self.job_incremental_protection_sla_time_mins = \
        int(data['incremental_protection_sla_time_mins'])
        

    def create_protection_job(self, job_name, policy_id, storage_domain_id):
        start_time_hr = int(datetime.datetime.now().strftime("%H"))
        start_time_min = int(datetime.datetime.now().strftime("%M"))
        timezone = 'America/Los_Angeles'
        self.start_time = cohesity.ProtectionJobStartTime(start_time_hr, start_time_min)
        payload = cohesity.ProtectionJobRequestBody(description = 
    self.job_description, \
    full_protection_sla_time_mins = self.job_full_protection_sla_time_mins,\
         incremental_protection_sla_time_mins = \
    self.job_incremental_protection_sla_time_mins,\
    name = job_name,\
         parent_source_id = self.parent_source_id,\
    policy_id = policy_id, source_ids = self.source_ids, \
         start_time = self.start_time, timezone = timezone,\
    view_box_id = storage_domain_id)
        try:
            api_instance = cohesity.ProtectionJobsApi()
            api_response = api_instance.create_protection_job(payload)

        except ApiException as e :
            print("Exception invoking protection job Api %s \n" %e)
            sys.exit(1)
        print(api_response)
        print("protection job created %s\n" %job_name)
        print("SUCCESS")   

    def create_protection_policy(self, pol_name):
        self.inc_schedule_continuous_schedule = \
    cohesity.ProtectionPolicyFullSchedulingPolicyContinuousSchedule(self.pol_inc_backup_mins)
        self.inc_schedule_daily_schedule = \
    cohesity.ProtectionPolicyFullSchedulingPolicyDailySchedule(self.pol_inc_days)
        self.inc_schedule_monthly_schedule = \
    cohesity.ProtectionPolicyFullSchedulingPolicyMonthlySchedule(self.pol_inc_day, self.pol_inc_day_count)
        self.incremental_scheduling_policy = \
    cohesity.ProtectionPolicyFullSchedulingPolicy(self.inc_schedule_continuous_schedule, \
         self.inc_schedule_daily_schedule, self.inc_schedule_monthly_schedule, \
         self.pol_inc_periodicity)

        payload = cohesity.ProtectionPolicyRequest(\
    days_to_keep = self.pol_days_to_keep, \
    description = self.pol_description, \
    name = pol_name, \
    retries = self.pol_retries, \
         retry_interval_mins = self.pol_retry_interval_mins, \
         incremental_scheduling_policy = self.incremental_scheduling_policy)
        try:
            api_instance = cohesity.ProtectionPoliciesApi()
            api_response = api_instance.create_protection_policy(payload)
            print(api_response)
            print("protection policy created %s\n" %pol_name)
            return api_response.id 
        except ApiException as e:
            print "Exception invoking protection policy Api %s\n" % e
            sys.exit(1)

    def get_vms_info_by_name(self, source_names):
        api_instance = cohesity.ProtectionSourcesApi()
        print("source names :",source_names)
        self.source_ids = []
        try:
            api_response = api_instance.list_virtual_machines(\
        names = source_names)
            for sources_info in api_response:
                self.parent_source_id = sources_info.parent_id
                break

            for sources_info in api_response:
                if sources_info.parent_id == self.parent_source_id:
                    self.source_ids.append(sources_info.id)
            if len(self.source_ids) == 0:
                print("No valid source ids found for the source names\n")
                sys.exit(1)
            print("source ids :",self.source_ids)        
        except ApiException as e:
          print("Exception occured during invocation of list \
      virtual machine %s\n",e)
          return None    

    def get_storage_domains(self):
        api_instance = cohesity.ViewBoxesApi()
        try:
            api_response = api_instance.get_view_boxes()
            # we take the first storage domain by default because there is no 
       #way to get the deafult storage domain
            return api_response[0].id
        except ApiException as e:
            print("Exception occured during invocation of list virtual machine \
             %s\n",e)
            return None    

    def run(self):
        """
        Simple command-line program for creating vmware cohesity protection 
        jobs.

        """
        usec_str = datetime.datetime.now().strftime("%S_%f")
        pol_name = 'policy_' + usec_str
        job_name = 'job_' + usec_str
        self.parse_params_file()
        self.get_vms_info_by_name(self.source_names)
        storage_domain_id = self.get_storage_domains()
        policy_id = self.create_protection_policy(pol_name)
        self.create_protection_job(job_name, policy_id, storage_domain_id)

if __name__ == '__main__':
    task = CohesityProtectionSources()
    task.main()
