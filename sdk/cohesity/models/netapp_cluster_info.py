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


class NetappClusterInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, contact_info=None, location=None, serial_number=None):
        """
        NetappClusterInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_info': 'str',
            'location': 'str',
            'serial_number': 'str'
        }

        self.attribute_map = {
            'contact_info': 'contactInfo',
            'location': 'location',
            'serial_number': 'serialNumber'
        }

        self._contact_info = contact_info
        self._location = location
        self._serial_number = serial_number

    @property
    def contact_info(self):
        """
        Gets the contact_info of this NetappClusterInfo.
        Specifies information about the contact for the NetApp cluster such as a name, phone number, and email address.

        :return: The contact_info of this NetappClusterInfo.
        :rtype: str
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """
        Sets the contact_info of this NetappClusterInfo.
        Specifies information about the contact for the NetApp cluster such as a name, phone number, and email address.

        :param contact_info: The contact_info of this NetappClusterInfo.
        :type: str
        """

        self._contact_info = contact_info

    @property
    def location(self):
        """
        Gets the location of this NetappClusterInfo.
        Specifies where this NetApp cluster is located. This location identification string is configured by the NetApp system administrator. This field does not contain the NetApp cluster hostname or IP address.

        :return: The location of this NetappClusterInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this NetappClusterInfo.
        Specifies where this NetApp cluster is located. This location identification string is configured by the NetApp system administrator. This field does not contain the NetApp cluster hostname or IP address.

        :param location: The location of this NetappClusterInfo.
        :type: str
        """

        self._location = location

    @property
    def serial_number(self):
        """
        Gets the serial_number of this NetappClusterInfo.
        Specifies the serial number of the NetApp cluster in the format: x-xx-xxxxxx.

        :return: The serial_number of this NetappClusterInfo.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this NetappClusterInfo.
        Specifies the serial number of the NetApp cluster in the format: x-xx-xxxxxx.

        :param serial_number: The serial_number of this NetappClusterInfo.
        :type: str
        """

        self._serial_number = serial_number

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
