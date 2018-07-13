# Copyright (c) 2016 by Cohesity, Inc.
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
        self.argparser.add_argument('--list', help='list protection sources',default = True)

    def parse_args(self):
        BaseTask.parse_args(self)

    def get_protection_sources(self):
        api_instance = cohesity.ProtectionSourcesApi()
        is_active = True 
        # bool | Filter by Inactive or Active Jobs. i
        is_deleted = True # bool | If true, return only Protection Jobs 
        include_last_run_and_stats = True 
        # bool | If true, return the last Protection Run of the Job and the summary stats. (optional)
        #ids = [56] i
        # list[int] | Filter by a list of Protection Job ids. (optional)
        #names = ['names_example'] i
        # list[str] | Filter by a list of Protection Job names. (optional)
        #policy_ids = ['policy_ids_example'] # list[str] | Filter by Policy ids that are associated with Protection Jobs. Only Jobs associated with the specified Policy ids, are returned. (optional)
        #environments = ['environments_example'] # list[str] | Filter by environment types such as 'kVMware', 'kView', 'kSQL' 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', 'kAzure'. Only Jobs protecting the specified environment types are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)

        try: 
        # List Protections Jobs filtered by the specified parameters.
            #api_response = api_instance.get_protection_jobs(is_active=is_active, is_deleted=is_deleted)
            api_response = api_instance.list_protection_sources()
        # include_last_run_and_stats=include_last_run_and_stats, ids=ids, names=names, policy_ids=policy_ids, environments=environments)
            pprint(api_response)
        except ApiException as e:
            print "Exception when calling ProtectionJobsApi->get_protection_jobs: %s\n" % e

    def run(self):
        """
        Simple command-line program for managing cohesity protection jobs.
        """
        self.get_protection_sources()


if __name__ == '__main__':
    task = CohesityProtectionSources()
    task.main()
    
