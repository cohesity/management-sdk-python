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



class CohesityCluster(BaseTask):
    """Cohesity class to do protection job operations."""
    
    def __init__(self):
        BaseTask.__init__(self, "cluster")
    def parse_args(self):
        BaseTask.parse_args(self)

    def get_cluster(self):
        api_instance = cohesity.ClusterApi()
        try:
          api_response = api_instance.get_cluster()
          pprint(api_response)
        except ApiException as e:
            print "Exception when calling get_clustern" % e

    def run(self):
        """
        Simple command-line program for managing cohesity protection jobs.
        """
        self.get_cluster()


if __name__ == '__main__':
    task = CohesityCluster()
    task.main()
