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


class ProtectionSourcePureProtectionSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, storage_array=None, type=None, volume=None):
        """
        ProtectionSourcePureProtectionSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'storage_array': 'PureStorageArray',
            'type': 'str',
            'volume': 'PureVolume'
        }

        self.attribute_map = {
            'name': 'name',
            'storage_array': 'storageArray',
            'type': 'type',
            'volume': 'volume'
        }

        self._name = name
        self._storage_array = storage_array
        self._type = type
        self._volume = volume

    @property
    def name(self):
        """
        Gets the name of this ProtectionSourcePureProtectionSource.
        Specifies a human readable name of the Protection Source.

        :return: The name of this ProtectionSourcePureProtectionSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProtectionSourcePureProtectionSource.
        Specifies a human readable name of the Protection Source.

        :param name: The name of this ProtectionSourcePureProtectionSource.
        :type: str
        """

        self._name = name

    @property
    def storage_array(self):
        """
        Gets the storage_array of this ProtectionSourcePureProtectionSource.
        Specifies a Pure Storage Array information. This is set only when the type is kStorageArray.

        :return: The storage_array of this ProtectionSourcePureProtectionSource.
        :rtype: PureStorageArray
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this ProtectionSourcePureProtectionSource.
        Specifies a Pure Storage Array information. This is set only when the type is kStorageArray.

        :param storage_array: The storage_array of this ProtectionSourcePureProtectionSource.
        :type: PureStorageArray
        """

        self._storage_array = storage_array

    @property
    def type(self):
        """
        Gets the type of this ProtectionSourcePureProtectionSource.
        Specifies the type of managed Object in a pure Protection Source like a kStorageArray or kVolume. Examples of Pure Objects include 'kStorageArray' and 'kVolume'.

        :return: The type of this ProtectionSourcePureProtectionSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProtectionSourcePureProtectionSource.
        Specifies the type of managed Object in a pure Protection Source like a kStorageArray or kVolume. Examples of Pure Objects include 'kStorageArray' and 'kVolume'.

        :param type: The type of this ProtectionSourcePureProtectionSource.
        :type: str
        """
        allowed_values = ["kStorageArray", "kVolume"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def volume(self):
        """
        Gets the volume of this ProtectionSourcePureProtectionSource.
        Specifies a Pure Volume information within a storage array. This is set only when the type is kVolume.

        :return: The volume of this ProtectionSourcePureProtectionSource.
        :rtype: PureVolume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this ProtectionSourcePureProtectionSource.
        Specifies a Pure Volume information within a storage array. This is set only when the type is kVolume.

        :param volume: The volume of this ProtectionSourcePureProtectionSource.
        :type: PureVolume
        """

        self._volume = volume

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
