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


class CloneTaskRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, clone_view_parameters=None, continue_on_error=None, hyperv_parameters=None, name=None, new_parent_id=None, objects=None, target_view_name=None, type=None, vlan_parameters=None, vmware_parameters=None):
        """
        CloneTaskRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'clone_view_parameters': 'CloneTaskRequestCloneViewParameters',
            'continue_on_error': 'bool',
            'hyperv_parameters': 'HypervCloneParameters',
            'name': 'str',
            'new_parent_id': 'int',
            'objects': 'list[RestoreObject]',
            'target_view_name': 'str',
            'type': 'str',
            'vlan_parameters': 'VlanParameters',
            'vmware_parameters': 'VmwareCloneParameters'
        }

        self.attribute_map = {
            'clone_view_parameters': 'cloneViewParameters',
            'continue_on_error': 'continueOnError',
            'hyperv_parameters': 'hypervParameters',
            'name': 'name',
            'new_parent_id': 'newParentId',
            'objects': 'objects',
            'target_view_name': 'targetViewName',
            'type': 'type',
            'vlan_parameters': 'vlanParameters',
            'vmware_parameters': 'vmwareParameters'
        }

        self._clone_view_parameters = clone_view_parameters
        self._continue_on_error = continue_on_error
        self._hyperv_parameters = hyperv_parameters
        self._name = name
        self._new_parent_id = new_parent_id
        self._objects = objects
        self._target_view_name = target_view_name
        self._type = type
        self._vlan_parameters = vlan_parameters
        self._vmware_parameters = vmware_parameters

    @property
    def clone_view_parameters(self):
        """
        Gets the clone_view_parameters of this CloneTaskRequest.


        :return: The clone_view_parameters of this CloneTaskRequest.
        :rtype: CloneTaskRequestCloneViewParameters
        """
        return self._clone_view_parameters

    @clone_view_parameters.setter
    def clone_view_parameters(self, clone_view_parameters):
        """
        Sets the clone_view_parameters of this CloneTaskRequest.


        :param clone_view_parameters: The clone_view_parameters of this CloneTaskRequest.
        :type: CloneTaskRequestCloneViewParameters
        """

        self._clone_view_parameters = clone_view_parameters

    @property
    def continue_on_error(self):
        """
        Gets the continue_on_error of this CloneTaskRequest.
        Specifies if the Restore Task should continue when some operations on some objects fail. If true, the Cohesity Cluster ignores intermittent errors and restores as many objects as possible.

        :return: The continue_on_error of this CloneTaskRequest.
        :rtype: bool
        """
        return self._continue_on_error

    @continue_on_error.setter
    def continue_on_error(self, continue_on_error):
        """
        Sets the continue_on_error of this CloneTaskRequest.
        Specifies if the Restore Task should continue when some operations on some objects fail. If true, the Cohesity Cluster ignores intermittent errors and restores as many objects as possible.

        :param continue_on_error: The continue_on_error of this CloneTaskRequest.
        :type: bool
        """

        self._continue_on_error = continue_on_error

    @property
    def hyperv_parameters(self):
        """
        Gets the hyperv_parameters of this CloneTaskRequest.
        Specifies additional parameters for 'kHyperV' restore objects.

        :return: The hyperv_parameters of this CloneTaskRequest.
        :rtype: HypervCloneParameters
        """
        return self._hyperv_parameters

    @hyperv_parameters.setter
    def hyperv_parameters(self, hyperv_parameters):
        """
        Sets the hyperv_parameters of this CloneTaskRequest.
        Specifies additional parameters for 'kHyperV' restore objects.

        :param hyperv_parameters: The hyperv_parameters of this CloneTaskRequest.
        :type: HypervCloneParameters
        """

        self._hyperv_parameters = hyperv_parameters

    @property
    def name(self):
        """
        Gets the name of this CloneTaskRequest.
        Specifies the name of the Restore Task. This field must be set and must be a unique name.

        :return: The name of this CloneTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloneTaskRequest.
        Specifies the name of the Restore Task. This field must be set and must be a unique name.

        :param name: The name of this CloneTaskRequest.
        :type: str
        """

        self._name = name

    @property
    def new_parent_id(self):
        """
        Gets the new_parent_id of this CloneTaskRequest.
        Specify a new registered parent Protection Source. If specified the selected objects are cloned or recovered to this new Protection Source. If not specified, objects are cloned or recovered to the original Protection Source that was managing them.

        :return: The new_parent_id of this CloneTaskRequest.
        :rtype: int
        """
        return self._new_parent_id

    @new_parent_id.setter
    def new_parent_id(self, new_parent_id):
        """
        Sets the new_parent_id of this CloneTaskRequest.
        Specify a new registered parent Protection Source. If specified the selected objects are cloned or recovered to this new Protection Source. If not specified, objects are cloned or recovered to the original Protection Source that was managing them.

        :param new_parent_id: The new_parent_id of this CloneTaskRequest.
        :type: int
        """

        self._new_parent_id = new_parent_id

    @property
    def objects(self):
        """
        Gets the objects of this CloneTaskRequest.
        Specifies a list of Protection Source objects or Protection Job objects (with specified Protection Source objects).

        :return: The objects of this CloneTaskRequest.
        :rtype: list[RestoreObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this CloneTaskRequest.
        Specifies a list of Protection Source objects or Protection Job objects (with specified Protection Source objects).

        :param objects: The objects of this CloneTaskRequest.
        :type: list[RestoreObject]
        """

        self._objects = objects

    @property
    def target_view_name(self):
        """
        Gets the target_view_name of this CloneTaskRequest.
        Specifies the name of the View where the cloned VMs are stored. This field is required for a 'kCloneVMs' Restore Task.

        :return: The target_view_name of this CloneTaskRequest.
        :rtype: str
        """
        return self._target_view_name

    @target_view_name.setter
    def target_view_name(self, target_view_name):
        """
        Sets the target_view_name of this CloneTaskRequest.
        Specifies the name of the View where the cloned VMs are stored. This field is required for a 'kCloneVMs' Restore Task.

        :param target_view_name: The target_view_name of this CloneTaskRequest.
        :type: str
        """

        self._target_view_name = target_view_name

    @property
    def type(self):
        """
        Gets the type of this CloneTaskRequest.
        Specifies the type of Restore Task such as 'kCloneVMs' or 'kCloneView'. 'kCloneVMs' specifies a Restore Task that clones VMs. 'kCloneView' specifies a Restore Task that clones a View.

        :return: The type of this CloneTaskRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloneTaskRequest.
        Specifies the type of Restore Task such as 'kCloneVMs' or 'kCloneView'. 'kCloneVMs' specifies a Restore Task that clones VMs. 'kCloneView' specifies a Restore Task that clones a View.

        :param type: The type of this CloneTaskRequest.
        :type: str
        """
        allowed_values = ["kCloneVMs", "kCloneView"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vlan_parameters(self):
        """
        Gets the vlan_parameters of this CloneTaskRequest.
        Specifies VLAN parameters for the restore operation.

        :return: The vlan_parameters of this CloneTaskRequest.
        :rtype: VlanParameters
        """
        return self._vlan_parameters

    @vlan_parameters.setter
    def vlan_parameters(self, vlan_parameters):
        """
        Sets the vlan_parameters of this CloneTaskRequest.
        Specifies VLAN parameters for the restore operation.

        :param vlan_parameters: The vlan_parameters of this CloneTaskRequest.
        :type: VlanParameters
        """

        self._vlan_parameters = vlan_parameters

    @property
    def vmware_parameters(self):
        """
        Gets the vmware_parameters of this CloneTaskRequest.
        Specifies additional parameters for 'kVmware' restore objects.

        :return: The vmware_parameters of this CloneTaskRequest.
        :rtype: VmwareCloneParameters
        """
        return self._vmware_parameters

    @vmware_parameters.setter
    def vmware_parameters(self, vmware_parameters):
        """
        Sets the vmware_parameters of this CloneTaskRequest.
        Specifies additional parameters for 'kVmware' restore objects.

        :param vmware_parameters: The vmware_parameters of this CloneTaskRequest.
        :type: VmwareCloneParameters
        """

        self._vmware_parameters = vmware_parameters

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
