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


class VMwareObjectId(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mor_item=None, mor_type=None, uuid=None):
        """
        VMwareObjectId - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mor_item': 'str',
            'mor_type': 'str',
            'uuid': 'str'
        }

        self.attribute_map = {
            'mor_item': 'morItem',
            'mor_type': 'morType',
            'uuid': 'uuid'
        }

        self._mor_item = mor_item
        self._mor_type = mor_type
        self._uuid = uuid

    @property
    def mor_item(self):
        """
        Gets the mor_item of this VMwareObjectId.
        Specifies the Managed Object Reference Item.

        :return: The mor_item of this VMwareObjectId.
        :rtype: str
        """
        return self._mor_item

    @mor_item.setter
    def mor_item(self, mor_item):
        """
        Sets the mor_item of this VMwareObjectId.
        Specifies the Managed Object Reference Item.

        :param mor_item: The mor_item of this VMwareObjectId.
        :type: str
        """

        self._mor_item = mor_item

    @property
    def mor_type(self):
        """
        Gets the mor_type of this VMwareObjectId.
        Specifies the Managed Object Reference Type.

        :return: The mor_type of this VMwareObjectId.
        :rtype: str
        """
        return self._mor_type

    @mor_type.setter
    def mor_type(self, mor_type):
        """
        Sets the mor_type of this VMwareObjectId.
        Specifies the Managed Object Reference Type.

        :param mor_type: The mor_type of this VMwareObjectId.
        :type: str
        """

        self._mor_type = mor_type

    @property
    def uuid(self):
        """
        Gets the uuid of this VMwareObjectId.
        Specifies a Universally Unique Identifier (UUID) of a VMware Object.

        :return: The uuid of this VMwareObjectId.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this VMwareObjectId.
        Specifies a Universally Unique Identifier (UUID) of a VMware Object.

        :param uuid: The uuid of this VMwareObjectId.
        :type: str
        """

        self._uuid = uuid

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
