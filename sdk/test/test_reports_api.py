# coding: utf-8

"""
    Cohesity REST API

    This API provides operations for interfacing with the Cohesity Cluster. NOTE: To view the documentation on the responses, click 'Model' next to 'Example Value' and keep clicking to expand the hierarchy.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import cohesity
from cohesity.rest import ApiException
from cohesity.apis.reports_api import ReportsApi


class TestReportsApi(unittest.TestCase):
    """ ReportsApi unit test stubs """

    def setUp(self):
        self.api = cohesity.apis.reports_api.ReportsApi()

    def tearDown(self):
        pass

    def test_get_data_transfer_from_vaults_report_request(self):
        """
        Test case for get_data_transfer_from_vaults_report_request

        Get summary statistics about transferring data from Vaults (External Targets) to this Cohesity Cluster.
        """
        pass

    def test_get_data_transfer_to_vaults_report_request(self):
        """
        Test case for get_data_transfer_to_vaults_report_request

        Get summary statistics about transferring data from the Cohesity Cluster to Vaults (External Targets).
        """
        pass

    def test_get_protection_sources_job_runs_report_request(self):
        """
        Test case for get_protection_sources_job_runs_report_request

        Get protection details about the specified list of leaf Protection Source Objects (such as a VMs).
        """
        pass

    def test_get_protection_sources_jobs_summary_report_request(self):
        """
        Test case for get_protection_sources_jobs_summary_report_request

        Get Job Run (Snapshot) summary statistics about the leaf Protection Sources Objects that match the specified filter criteria.
        """
        pass

    def test_get_restore_summary_by_object_type_report(self):
        """
        Test case for get_restore_summary_by_object_type_report

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
