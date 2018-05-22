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


class CapacityByTier(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, storage_tier=None, tier_max_physical_capacity_bytes=None):
        """
        CapacityByTier - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'storage_tier': 'int',
            'tier_max_physical_capacity_bytes': 'int'
        }

        self.attribute_map = {
            'storage_tier': 'storageTier',
            'tier_max_physical_capacity_bytes': 'tierMaxPhysicalCapacityBytes'
        }

        self._storage_tier = storage_tier
        self._tier_max_physical_capacity_bytes = tier_max_physical_capacity_bytes

    @property
    def storage_tier(self):
        """
        Gets the storage_tier of this CapacityByTier.
        StorageTier is the type of StorageTier.

        :return: The storage_tier of this CapacityByTier.
        :rtype: int
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """
        Sets the storage_tier of this CapacityByTier.
        StorageTier is the type of StorageTier.

        :param storage_tier: The storage_tier of this CapacityByTier.
        :type: int
        """

        self._storage_tier = storage_tier

    @property
    def tier_max_physical_capacity_bytes(self):
        """
        Gets the tier_max_physical_capacity_bytes of this CapacityByTier.
        TierMaxPhysicalCapacityBytes is the maximum physical capacity in bytes of the storage tier.

        :return: The tier_max_physical_capacity_bytes of this CapacityByTier.
        :rtype: int
        """
        return self._tier_max_physical_capacity_bytes

    @tier_max_physical_capacity_bytes.setter
    def tier_max_physical_capacity_bytes(self, tier_max_physical_capacity_bytes):
        """
        Sets the tier_max_physical_capacity_bytes of this CapacityByTier.
        TierMaxPhysicalCapacityBytes is the maximum physical capacity in bytes of the storage tier.

        :param tier_max_physical_capacity_bytes: The tier_max_physical_capacity_bytes of this CapacityByTier.
        :type: int
        """

        self._tier_max_physical_capacity_bytes = tier_max_physical_capacity_bytes

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
