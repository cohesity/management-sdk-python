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


class VmwareCloneParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, datastore_folder_id=None, disable_network=None, network_id=None, powered_on=None, prefix=None, resource_pool_id=None, suffix=None, vm_folder_id=None):
        """
        VmwareCloneParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'datastore_folder_id': 'int',
            'disable_network': 'bool',
            'network_id': 'int',
            'powered_on': 'bool',
            'prefix': 'str',
            'resource_pool_id': 'int',
            'suffix': 'str',
            'vm_folder_id': 'int'
        }

        self.attribute_map = {
            'datastore_folder_id': 'datastoreFolderId',
            'disable_network': 'disableNetwork',
            'network_id': 'networkId',
            'powered_on': 'poweredOn',
            'prefix': 'prefix',
            'resource_pool_id': 'resourcePoolId',
            'suffix': 'suffix',
            'vm_folder_id': 'vmFolderId'
        }

        self._datastore_folder_id = datastore_folder_id
        self._disable_network = disable_network
        self._network_id = network_id
        self._powered_on = powered_on
        self._prefix = prefix
        self._resource_pool_id = resource_pool_id
        self._suffix = suffix
        self._vm_folder_id = vm_folder_id

    @property
    def datastore_folder_id(self):
        """
        Gets the datastore_folder_id of this VmwareCloneParameters.
        Specifies the folder where the restore datastore should be created. This is applicable only when the VMs are being cloned.

        :return: The datastore_folder_id of this VmwareCloneParameters.
        :rtype: int
        """
        return self._datastore_folder_id

    @datastore_folder_id.setter
    def datastore_folder_id(self, datastore_folder_id):
        """
        Sets the datastore_folder_id of this VmwareCloneParameters.
        Specifies the folder where the restore datastore should be created. This is applicable only when the VMs are being cloned.

        :param datastore_folder_id: The datastore_folder_id of this VmwareCloneParameters.
        :type: int
        """

        self._datastore_folder_id = datastore_folder_id

    @property
    def disable_network(self):
        """
        Gets the disable_network of this VmwareCloneParameters.
        Specifies whether the network should be left in disabled state. Attached network is enabled by default. Set this flag to true to disable it.

        :return: The disable_network of this VmwareCloneParameters.
        :rtype: bool
        """
        return self._disable_network

    @disable_network.setter
    def disable_network(self, disable_network):
        """
        Sets the disable_network of this VmwareCloneParameters.
        Specifies whether the network should be left in disabled state. Attached network is enabled by default. Set this flag to true to disable it.

        :param disable_network: The disable_network of this VmwareCloneParameters.
        :type: bool
        """

        self._disable_network = disable_network

    @property
    def network_id(self):
        """
        Gets the network_id of this VmwareCloneParameters.
        Specifies a network configuration to be attached to the cloned or recovered object. For kCloneVMs and kRecoverVMs tasks, original network configuration is detached if the cloned or recovered object is kept under a different parent Protection Source or a different Resource Pool. By default, for kRecoverVMs task, original network configuration is preserved if the recovered object is kept under the same parent Protection Source and the same Resource Pool. Specify this field to override the preserved network configuration or to attach a new network configuration to the cloned or recovered objects. You can get the networkId of the kNetwork object by setting includeNetworks to 'true' in the GET /public/protectionSources operation. In the response, get the id of the desired kNetwork object, the resource pool, and the registered parent Protection Source.

        :return: The network_id of this VmwareCloneParameters.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """
        Sets the network_id of this VmwareCloneParameters.
        Specifies a network configuration to be attached to the cloned or recovered object. For kCloneVMs and kRecoverVMs tasks, original network configuration is detached if the cloned or recovered object is kept under a different parent Protection Source or a different Resource Pool. By default, for kRecoverVMs task, original network configuration is preserved if the recovered object is kept under the same parent Protection Source and the same Resource Pool. Specify this field to override the preserved network configuration or to attach a new network configuration to the cloned or recovered objects. You can get the networkId of the kNetwork object by setting includeNetworks to 'true' in the GET /public/protectionSources operation. In the response, get the id of the desired kNetwork object, the resource pool, and the registered parent Protection Source.

        :param network_id: The network_id of this VmwareCloneParameters.
        :type: int
        """

        self._network_id = network_id

    @property
    def powered_on(self):
        """
        Gets the powered_on of this VmwareCloneParameters.
        Specifies the power state of the cloned or recovered objects. By default, the cloned or recovered objects are powered off.

        :return: The powered_on of this VmwareCloneParameters.
        :rtype: bool
        """
        return self._powered_on

    @powered_on.setter
    def powered_on(self, powered_on):
        """
        Sets the powered_on of this VmwareCloneParameters.
        Specifies the power state of the cloned or recovered objects. By default, the cloned or recovered objects are powered off.

        :param powered_on: The powered_on of this VmwareCloneParameters.
        :type: bool
        """

        self._powered_on = powered_on

    @property
    def prefix(self):
        """
        Gets the prefix of this VmwareCloneParameters.
        Specifies a prefix to prepended to the source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :return: The prefix of this VmwareCloneParameters.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this VmwareCloneParameters.
        Specifies a prefix to prepended to the source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :param prefix: The prefix of this VmwareCloneParameters.
        :type: str
        """

        self._prefix = prefix

    @property
    def resource_pool_id(self):
        """
        Gets the resource_pool_id of this VmwareCloneParameters.
        Specifies the resource pool where the cloned or recovered objects are attached. This field is mandatory for kCloneVMs Restore Tasks always. For kRecoverVMs Restore Tasks, this field is mandatory only if newParentId field is specified. If this field is not specified, recovered objects are attached to the original resource pool under the original parent.

        :return: The resource_pool_id of this VmwareCloneParameters.
        :rtype: int
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """
        Sets the resource_pool_id of this VmwareCloneParameters.
        Specifies the resource pool where the cloned or recovered objects are attached. This field is mandatory for kCloneVMs Restore Tasks always. For kRecoverVMs Restore Tasks, this field is mandatory only if newParentId field is specified. If this field is not specified, recovered objects are attached to the original resource pool under the original parent.

        :param resource_pool_id: The resource_pool_id of this VmwareCloneParameters.
        :type: int
        """

        self._resource_pool_id = resource_pool_id

    @property
    def suffix(self):
        """
        Gets the suffix of this VmwareCloneParameters.
        Specifies a suffix to appended to the original source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :return: The suffix of this VmwareCloneParameters.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this VmwareCloneParameters.
        Specifies a suffix to appended to the original source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :param suffix: The suffix of this VmwareCloneParameters.
        :type: str
        """

        self._suffix = suffix

    @property
    def vm_folder_id(self):
        """
        Gets the vm_folder_id of this VmwareCloneParameters.
        Specifies a folder where the VMs should be restored. This is applicable only when the VMs are being restored to an alternate location or if clone is being performed.

        :return: The vm_folder_id of this VmwareCloneParameters.
        :rtype: int
        """
        return self._vm_folder_id

    @vm_folder_id.setter
    def vm_folder_id(self, vm_folder_id):
        """
        Sets the vm_folder_id of this VmwareCloneParameters.
        Specifies a folder where the VMs should be restored. This is applicable only when the VMs are being restored to an alternate location or if clone is being performed.

        :param vm_folder_id: The vm_folder_id of this VmwareCloneParameters.
        :type: int
        """

        self._vm_folder_id = vm_folder_id

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
