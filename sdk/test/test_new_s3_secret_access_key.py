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
from cohesity.models.new_s3_secret_access_key import NewS3SecretAccessKey


class TestNewS3SecretAccessKey(unittest.TestCase):
    """ NewS3SecretAccessKey unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNewS3SecretAccessKey(self):
        """
        Test NewS3SecretAccessKey
        """
        model = cohesity.models.new_s3_secret_access_key.NewS3SecretAccessKey()


if __name__ == '__main__':
    unittest.main()
