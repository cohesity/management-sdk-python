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


class FilesystemVolumeLogicalVolume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_root_node=None, group_name=None, group_uuid=None, name=None, uuid=None):
        """
        FilesystemVolumeLogicalVolume - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_root_node': 'DeviceTree',
            'group_name': 'str',
            'group_uuid': 'str',
            'name': 'str',
            'uuid': 'str'
        }

        self.attribute_map = {
            'device_root_node': 'deviceRootNode',
            'group_name': 'groupName',
            'group_uuid': 'groupUuid',
            'name': 'name',
            'uuid': 'uuid'
        }

        self._device_root_node = device_root_node
        self._group_name = group_name
        self._group_uuid = group_uuid
        self._name = name
        self._uuid = uuid

    @property
    def device_root_node(self):
        """
        Gets the device_root_node of this FilesystemVolumeLogicalVolume.
        Specifies the device tree defining how to combine partitions to create this logical volume.

        :return: The device_root_node of this FilesystemVolumeLogicalVolume.
        :rtype: DeviceTree
        """
        return self._device_root_node

    @device_root_node.setter
    def device_root_node(self, device_root_node):
        """
        Sets the device_root_node of this FilesystemVolumeLogicalVolume.
        Specifies the device tree defining how to combine partitions to create this logical volume.

        :param device_root_node: The device_root_node of this FilesystemVolumeLogicalVolume.
        :type: DeviceTree
        """

        self._device_root_node = device_root_node

    @property
    def group_name(self):
        """
        Gets the group_name of this FilesystemVolumeLogicalVolume.
        Specifies the group name of the logical volume.

        :return: The group_name of this FilesystemVolumeLogicalVolume.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this FilesystemVolumeLogicalVolume.
        Specifies the group name of the logical volume.

        :param group_name: The group_name of this FilesystemVolumeLogicalVolume.
        :type: str
        """

        self._group_name = group_name

    @property
    def group_uuid(self):
        """
        Gets the group_uuid of this FilesystemVolumeLogicalVolume.
        Specifies the group uuid of the logical volume.

        :return: The group_uuid of this FilesystemVolumeLogicalVolume.
        :rtype: str
        """
        return self._group_uuid

    @group_uuid.setter
    def group_uuid(self, group_uuid):
        """
        Sets the group_uuid of this FilesystemVolumeLogicalVolume.
        Specifies the group uuid of the logical volume.

        :param group_uuid: The group_uuid of this FilesystemVolumeLogicalVolume.
        :type: str
        """

        self._group_uuid = group_uuid

    @property
    def name(self):
        """
        Gets the name of this FilesystemVolumeLogicalVolume.
        Specifies the name of the logical volume.

        :return: The name of this FilesystemVolumeLogicalVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FilesystemVolumeLogicalVolume.
        Specifies the name of the logical volume.

        :param name: The name of this FilesystemVolumeLogicalVolume.
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """
        Gets the uuid of this FilesystemVolumeLogicalVolume.
        Specifies the uuid of the logical volume.

        :return: The uuid of this FilesystemVolumeLogicalVolume.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this FilesystemVolumeLogicalVolume.
        Specifies the uuid of the logical volume.

        :param uuid: The uuid of this FilesystemVolumeLogicalVolume.
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
