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


class RegisterApplicationServersParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, applications=None, has_persistent_agent=None, password=None, protection_source_id=None, username=None):
        """
        RegisterApplicationServersParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'applications': 'list[str]',
            'has_persistent_agent': 'bool',
            'password': 'str',
            'protection_source_id': 'int',
            'username': 'str'
        }

        self.attribute_map = {
            'applications': 'applications',
            'has_persistent_agent': 'hasPersistentAgent',
            'password': 'password',
            'protection_source_id': 'protectionSourceId',
            'username': 'username'
        }

        self._applications = applications
        self._has_persistent_agent = has_persistent_agent
        self._password = password
        self._protection_source_id = protection_source_id
        self._username = username

    @property
    def applications(self):
        """
        Gets the applications of this RegisterApplicationServersParameters.
        Specifies the types of applications such as 'kSQL', 'kExchange' running on the Protection Source. overrideDescription: true Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :return: The applications of this RegisterApplicationServersParameters.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """
        Sets the applications of this RegisterApplicationServersParameters.
        Specifies the types of applications such as 'kSQL', 'kExchange' running on the Protection Source. overrideDescription: true Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :param applications: The applications of this RegisterApplicationServersParameters.
        :type: list[str]
        """
        allowed_values = ["kVMware", "kSQL", "kView", "kPuppeteer", "kPhysical", "kPure", "kNetapp", "kGenericNas", "kHyperV", "kAcropolis", "kAzure"]
        if applications not in allowed_values:
            raise ValueError(
                "Invalid value for `applications` ({0}), must be one of {1}"
                .format(applications, allowed_values)
            )

        self._applications = applications

    @property
    def has_persistent_agent(self):
        """
        Gets the has_persistent_agent of this RegisterApplicationServersParameters.
        Set this to true if a persistent agent is running on the host. If this is specified, then credentials would not be used to log into the host environment. This mechanism may be used in environments such as VMware to get around UAC permission issues by running the agent as a service with the right credentials. If this field is not specified, credentials must be specified.

        :return: The has_persistent_agent of this RegisterApplicationServersParameters.
        :rtype: bool
        """
        return self._has_persistent_agent

    @has_persistent_agent.setter
    def has_persistent_agent(self, has_persistent_agent):
        """
        Sets the has_persistent_agent of this RegisterApplicationServersParameters.
        Set this to true if a persistent agent is running on the host. If this is specified, then credentials would not be used to log into the host environment. This mechanism may be used in environments such as VMware to get around UAC permission issues by running the agent as a service with the right credentials. If this field is not specified, credentials must be specified.

        :param has_persistent_agent: The has_persistent_agent of this RegisterApplicationServersParameters.
        :type: bool
        """

        self._has_persistent_agent = has_persistent_agent

    @property
    def password(self):
        """
        Gets the password of this RegisterApplicationServersParameters.
        Specifies password of the username to access the target source.

        :return: The password of this RegisterApplicationServersParameters.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this RegisterApplicationServersParameters.
        Specifies password of the username to access the target source.

        :param password: The password of this RegisterApplicationServersParameters.
        :type: str
        """

        self._password = password

    @property
    def protection_source_id(self):
        """
        Gets the protection_source_id of this RegisterApplicationServersParameters.
        Specifies the Id of the Protection Source that contains one or more Application Servers running on it.

        :return: The protection_source_id of this RegisterApplicationServersParameters.
        :rtype: int
        """
        return self._protection_source_id

    @protection_source_id.setter
    def protection_source_id(self, protection_source_id):
        """
        Sets the protection_source_id of this RegisterApplicationServersParameters.
        Specifies the Id of the Protection Source that contains one or more Application Servers running on it.

        :param protection_source_id: The protection_source_id of this RegisterApplicationServersParameters.
        :type: int
        """

        self._protection_source_id = protection_source_id

    @property
    def username(self):
        """
        Gets the username of this RegisterApplicationServersParameters.
        Specifies username to access the target source.

        :return: The username of this RegisterApplicationServersParameters.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this RegisterApplicationServersParameters.
        Specifies username to access the target source.

        :param username: The username of this RegisterApplicationServersParameters.
        :type: str
        """

        self._username = username

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
