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


class UserIdMapping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, centrify_zone_mapping=None, custom_attributes_mapping=None, fixed_mapping=None, type=None):
        """
        UserIdMapping - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'centrify_zone_mapping': 'CentrifyZone',
            'custom_attributes_mapping': 'CustomUnixIdAttributes',
            'fixed_mapping': 'FixedUnixIdMapping',
            'type': 'str'
        }

        self.attribute_map = {
            'centrify_zone_mapping': 'centrifyZoneMapping',
            'custom_attributes_mapping': 'customAttributesMapping',
            'fixed_mapping': 'fixedMapping',
            'type': 'type'
        }

        self._centrify_zone_mapping = centrify_zone_mapping
        self._custom_attributes_mapping = custom_attributes_mapping
        self._fixed_mapping = fixed_mapping
        self._type = type

    @property
    def centrify_zone_mapping(self):
        """
        Gets the centrify_zone_mapping of this UserIdMapping.
        Specifies a centrify zone when mapping type is set to 'kCentrify'. It defines a centrify zone from which the user id mapping info would be derived.

        :return: The centrify_zone_mapping of this UserIdMapping.
        :rtype: CentrifyZone
        """
        return self._centrify_zone_mapping

    @centrify_zone_mapping.setter
    def centrify_zone_mapping(self, centrify_zone_mapping):
        """
        Sets the centrify_zone_mapping of this UserIdMapping.
        Specifies a centrify zone when mapping type is set to 'kCentrify'. It defines a centrify zone from which the user id mapping info would be derived.

        :param centrify_zone_mapping: The centrify_zone_mapping of this UserIdMapping.
        :type: CentrifyZone
        """

        self._centrify_zone_mapping = centrify_zone_mapping

    @property
    def custom_attributes_mapping(self):
        """
        Gets the custom_attributes_mapping of this UserIdMapping.
        Specifies the custom attributes when mapping type is set to 'kCustomAttributes'. It defines the attribute names to derive the mapping for a user of an Active Directory domain.

        :return: The custom_attributes_mapping of this UserIdMapping.
        :rtype: CustomUnixIdAttributes
        """
        return self._custom_attributes_mapping

    @custom_attributes_mapping.setter
    def custom_attributes_mapping(self, custom_attributes_mapping):
        """
        Sets the custom_attributes_mapping of this UserIdMapping.
        Specifies the custom attributes when mapping type is set to 'kCustomAttributes'. It defines the attribute names to derive the mapping for a user of an Active Directory domain.

        :param custom_attributes_mapping: The custom_attributes_mapping of this UserIdMapping.
        :type: CustomUnixIdAttributes
        """

        self._custom_attributes_mapping = custom_attributes_mapping

    @property
    def fixed_mapping(self):
        """
        Gets the fixed_mapping of this UserIdMapping.
        Specifies the fields when mapping type is set to 'kFixed'. It maps all Active Directory users of this domain to a fixed uid, and gid.

        :return: The fixed_mapping of this UserIdMapping.
        :rtype: FixedUnixIdMapping
        """
        return self._fixed_mapping

    @fixed_mapping.setter
    def fixed_mapping(self, fixed_mapping):
        """
        Sets the fixed_mapping of this UserIdMapping.
        Specifies the fields when mapping type is set to 'kFixed'. It maps all Active Directory users of this domain to a fixed uid, and gid.

        :param fixed_mapping: The fixed_mapping of this UserIdMapping.
        :type: FixedUnixIdMapping
        """

        self._fixed_mapping = fixed_mapping

    @property
    def type(self):
        """
        Gets the type of this UserIdMapping.
        Specifies the mapping type used. 'kRid' indicates the kRid mapping type. 'kRfc2307' indicates the kRfc2307 mapping type. 'kSfu30' indicates the kSfu30 mapping type. 'kCentrify' indicates the mapping type to refer to a centrify zone. 'kFixed' indicates the mapping from all Active Directory users to a fixed Unix uid, and gid. 'kCustomAttributes' indicates the mapping to derive from custom attributes defined in an AD domain.

        :return: The type of this UserIdMapping.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserIdMapping.
        Specifies the mapping type used. 'kRid' indicates the kRid mapping type. 'kRfc2307' indicates the kRfc2307 mapping type. 'kSfu30' indicates the kSfu30 mapping type. 'kCentrify' indicates the mapping type to refer to a centrify zone. 'kFixed' indicates the mapping from all Active Directory users to a fixed Unix uid, and gid. 'kCustomAttributes' indicates the mapping to derive from custom attributes defined in an AD domain.

        :param type: The type of this UserIdMapping.
        :type: str
        """
        allowed_values = ["kRid", "kRfc2307", "kSfu30", "kCentrify", "kFixed", "kCustomAttributes"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
