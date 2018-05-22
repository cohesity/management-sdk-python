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


class EulaConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, license_key=None, signed_version=None):
        """
        EulaConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'license_key': 'str',
            'signed_by_user': 'str',
            'signed_time': 'int',
            'signed_version': 'int'
        }

        self.attribute_map = {
            'license_key': 'licenseKey',
            'signed_by_user': 'signedByUser',
            'signed_time': 'signedTime',
            'signed_version': 'signedVersion'
        }

        self._signed_by_user = None
        self._signed_time = None
        self._license_key = license_key
        self._signed_version = signed_version

    @property
    def license_key(self):
        """
        Gets the license_key of this EulaConfig.
        Specifies the license key.

        :return: The license_key of this EulaConfig.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """
        Sets the license_key of this EulaConfig.
        Specifies the license key.

        :param license_key: The license_key of this EulaConfig.
        :type: str
        """

        self._license_key = license_key

    @property
    def signed_by_user(self):
        """
        Gets the signed_by_user of this EulaConfig.
        Specifies the login account name for the Cohesity user who accepted the End User License Agreement.

        :return: The signed_by_user of this EulaConfig.
        :rtype: str
        """
        return self._signed_by_user

    @property
    def signed_time(self):
        """
        Gets the signed_time of this EulaConfig.
        Specifies the time that the End User License Agreement was accepted.

        :return: The signed_time of this EulaConfig.
        :rtype: int
        """
        return self._signed_time

    @property
    def signed_version(self):
        """
        Gets the signed_version of this EulaConfig.
        Specifies the version of the End User License Agreement that was accepted.

        :return: The signed_version of this EulaConfig.
        :rtype: int
        """
        return self._signed_version

    @signed_version.setter
    def signed_version(self, signed_version):
        """
        Sets the signed_version of this EulaConfig.
        Specifies the version of the End User License Agreement that was accepted.

        :param signed_version: The signed_version of this EulaConfig.
        :type: int
        """

        self._signed_version = signed_version

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
