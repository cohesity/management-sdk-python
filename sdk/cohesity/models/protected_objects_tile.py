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


class ProtectedObjectsTile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, objects_protected=None, protected_count=None, protected_size_bytes=None, unprotected_count=None, unprotected_size_bytes=None):
        """
        ProtectedObjectsTile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'objects_protected': 'list[ProtectedObjectsByEnv]',
            'protected_count': 'int',
            'protected_size_bytes': 'int',
            'unprotected_count': 'int',
            'unprotected_size_bytes': 'int'
        }

        self.attribute_map = {
            'objects_protected': 'objectsProtected',
            'protected_count': 'protectedCount',
            'protected_size_bytes': 'protectedSizeBytes',
            'unprotected_count': 'unprotectedCount',
            'unprotected_size_bytes': 'unprotectedSizeBytes'
        }

        self._objects_protected = objects_protected
        self._protected_count = protected_count
        self._protected_size_bytes = protected_size_bytes
        self._unprotected_count = unprotected_count
        self._unprotected_size_bytes = unprotected_size_bytes

    @property
    def objects_protected(self):
        """
        Gets the objects_protected of this ProtectedObjectsTile.


        :return: The objects_protected of this ProtectedObjectsTile.
        :rtype: list[ProtectedObjectsByEnv]
        """
        return self._objects_protected

    @objects_protected.setter
    def objects_protected(self, objects_protected):
        """
        Sets the objects_protected of this ProtectedObjectsTile.


        :param objects_protected: The objects_protected of this ProtectedObjectsTile.
        :type: list[ProtectedObjectsByEnv]
        """

        self._objects_protected = objects_protected

    @property
    def protected_count(self):
        """
        Gets the protected_count of this ProtectedObjectsTile.
        Number of Protected Objects.

        :return: The protected_count of this ProtectedObjectsTile.
        :rtype: int
        """
        return self._protected_count

    @protected_count.setter
    def protected_count(self, protected_count):
        """
        Sets the protected_count of this ProtectedObjectsTile.
        Number of Protected Objects.

        :param protected_count: The protected_count of this ProtectedObjectsTile.
        :type: int
        """

        self._protected_count = protected_count

    @property
    def protected_size_bytes(self):
        """
        Gets the protected_size_bytes of this ProtectedObjectsTile.
        Size of Protected Objects.

        :return: The protected_size_bytes of this ProtectedObjectsTile.
        :rtype: int
        """
        return self._protected_size_bytes

    @protected_size_bytes.setter
    def protected_size_bytes(self, protected_size_bytes):
        """
        Sets the protected_size_bytes of this ProtectedObjectsTile.
        Size of Protected Objects.

        :param protected_size_bytes: The protected_size_bytes of this ProtectedObjectsTile.
        :type: int
        """

        self._protected_size_bytes = protected_size_bytes

    @property
    def unprotected_count(self):
        """
        Gets the unprotected_count of this ProtectedObjectsTile.
        Number of Unprotected Objects.

        :return: The unprotected_count of this ProtectedObjectsTile.
        :rtype: int
        """
        return self._unprotected_count

    @unprotected_count.setter
    def unprotected_count(self, unprotected_count):
        """
        Sets the unprotected_count of this ProtectedObjectsTile.
        Number of Unprotected Objects.

        :param unprotected_count: The unprotected_count of this ProtectedObjectsTile.
        :type: int
        """

        self._unprotected_count = unprotected_count

    @property
    def unprotected_size_bytes(self):
        """
        Gets the unprotected_size_bytes of this ProtectedObjectsTile.
        Size of Unprotected Objects.

        :return: The unprotected_size_bytes of this ProtectedObjectsTile.
        :rtype: int
        """
        return self._unprotected_size_bytes

    @unprotected_size_bytes.setter
    def unprotected_size_bytes(self, unprotected_size_bytes):
        """
        Sets the unprotected_size_bytes of this ProtectedObjectsTile.
        Size of Unprotected Objects.

        :param unprotected_size_bytes: The unprotected_size_bytes of this ProtectedObjectsTile.
        :type: int
        """

        self._unprotected_size_bytes = unprotected_size_bytes

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
