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
from cohesity.apis.preferences_api import PreferencesApi


class TestPreferencesApi(unittest.TestCase):
    """ PreferencesApi unit test stubs """

    def setUp(self):
        self.api = cohesity.apis.preferences_api.PreferencesApi()

    def tearDown(self):
        pass

    def test_get_user_preferences(self):
        """
        Test case for get_user_preferences

        List the preferences of the session user.
        """
        pass

    def test_update_user_preferences(self):
        """
        Test case for update_user_preferences

        Update the preferences of the session user
        """
        pass


if __name__ == '__main__':
    unittest.main()
