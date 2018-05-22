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

from pprint import pformat
from six import iteritems
import re


class RegisteredApplicationServer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, application_server=None, registered_protection_source=None):
        """
        RegisteredApplicationServer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'application_server': 'RegisteredApplicationServerApplicationServer',
            'registered_protection_source': 'RegisteredApplicationServerRegisteredProtectionSource'
        }

        self.attribute_map = {
            'application_server': 'applicationServer',
            'registered_protection_source': 'registeredProtectionSource'
        }

        self._application_server = application_server
        self._registered_protection_source = registered_protection_source

    @property
    def application_server(self):
        """
        Gets the application_server of this RegisteredApplicationServer.


        :return: The application_server of this RegisteredApplicationServer.
        :rtype: RegisteredApplicationServerApplicationServer
        """
        return self._application_server

    @application_server.setter
    def application_server(self, application_server):
        """
        Sets the application_server of this RegisteredApplicationServer.


        :param application_server: The application_server of this RegisteredApplicationServer.
        :type: RegisteredApplicationServerApplicationServer
        """

        self._application_server = application_server

    @property
    def registered_protection_source(self):
        """
        Gets the registered_protection_source of this RegisteredApplicationServer.


        :return: The registered_protection_source of this RegisteredApplicationServer.
        :rtype: RegisteredApplicationServerRegisteredProtectionSource
        """
        return self._registered_protection_source

    @registered_protection_source.setter
    def registered_protection_source(self, registered_protection_source):
        """
        Sets the registered_protection_source of this RegisteredApplicationServer.


        :param registered_protection_source: The registered_protection_source of this RegisteredApplicationServer.
        :type: RegisteredApplicationServerRegisteredProtectionSource
        """

        self._registered_protection_source = registered_protection_source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
