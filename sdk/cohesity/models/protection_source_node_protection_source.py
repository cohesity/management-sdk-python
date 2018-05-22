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


class ProtectionSourceNodeProtectionSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, acropolis_protection_source=None, aws_protection_source=None, azure_protection_source=None, environment=None, hyperv_protection_source=None, id=None, kvm_protection_source=None, name=None, nas_protection_source=None, netapp_protection_source=None, parent_id=None, physical_protection_source=None, pure_protection_source=None, sql_protection_source=None, view_protection_source=None, vm_ware_protection_source=None):
        """
        ProtectionSourceNodeProtectionSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'acropolis_protection_source': 'ProtectionSourceAcropolisProtectionSource',
            'aws_protection_source': 'ProtectionSourceAwsProtectionSource',
            'azure_protection_source': 'ProtectionSourceAzureProtectionSource',
            'environment': 'str',
            'hyperv_protection_source': 'ProtectionSourceHypervProtectionSource',
            'id': 'int',
            'kvm_protection_source': 'ProtectionSourceKvmProtectionSource',
            'name': 'str',
            'nas_protection_source': 'ProtectionSourceNasProtectionSource',
            'netapp_protection_source': 'ProtectionSourceNetappProtectionSource',
            'parent_id': 'int',
            'physical_protection_source': 'ProtectionSourcePhysicalProtectionSource',
            'pure_protection_source': 'ProtectionSourcePureProtectionSource',
            'sql_protection_source': 'ProtectionSourceSqlProtectionSource',
            'view_protection_source': 'ProtectionSourceViewProtectionSource',
            'vm_ware_protection_source': 'ProtectionSourceVmWareProtectionSource'
        }

        self.attribute_map = {
            'acropolis_protection_source': 'acropolisProtectionSource',
            'aws_protection_source': 'awsProtectionSource',
            'azure_protection_source': 'azureProtectionSource',
            'environment': 'environment',
            'hyperv_protection_source': 'hypervProtectionSource',
            'id': 'id',
            'kvm_protection_source': 'kvmProtectionSource',
            'name': 'name',
            'nas_protection_source': 'nasProtectionSource',
            'netapp_protection_source': 'netappProtectionSource',
            'parent_id': 'parentId',
            'physical_protection_source': 'physicalProtectionSource',
            'pure_protection_source': 'pureProtectionSource',
            'sql_protection_source': 'sqlProtectionSource',
            'view_protection_source': 'viewProtectionSource',
            'vm_ware_protection_source': 'vmWareProtectionSource'
        }

        self._acropolis_protection_source = acropolis_protection_source
        self._aws_protection_source = aws_protection_source
        self._azure_protection_source = azure_protection_source
        self._environment = environment
        self._hyperv_protection_source = hyperv_protection_source
        self._id = id
        self._kvm_protection_source = kvm_protection_source
        self._name = name
        self._nas_protection_source = nas_protection_source
        self._netapp_protection_source = netapp_protection_source
        self._parent_id = parent_id
        self._physical_protection_source = physical_protection_source
        self._pure_protection_source = pure_protection_source
        self._sql_protection_source = sql_protection_source
        self._view_protection_source = view_protection_source
        self._vm_ware_protection_source = vm_ware_protection_source

    @property
    def acropolis_protection_source(self):
        """
        Gets the acropolis_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The acropolis_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceAcropolisProtectionSource
        """
        return self._acropolis_protection_source

    @acropolis_protection_source.setter
    def acropolis_protection_source(self, acropolis_protection_source):
        """
        Sets the acropolis_protection_source of this ProtectionSourceNodeProtectionSource.


        :param acropolis_protection_source: The acropolis_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceAcropolisProtectionSource
        """

        self._acropolis_protection_source = acropolis_protection_source

    @property
    def aws_protection_source(self):
        """
        Gets the aws_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The aws_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceAwsProtectionSource
        """
        return self._aws_protection_source

    @aws_protection_source.setter
    def aws_protection_source(self, aws_protection_source):
        """
        Sets the aws_protection_source of this ProtectionSourceNodeProtectionSource.


        :param aws_protection_source: The aws_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceAwsProtectionSource
        """

        self._aws_protection_source = aws_protection_source

    @property
    def azure_protection_source(self):
        """
        Gets the azure_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The azure_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceAzureProtectionSource
        """
        return self._azure_protection_source

    @azure_protection_source.setter
    def azure_protection_source(self, azure_protection_source):
        """
        Sets the azure_protection_source of this ProtectionSourceNodeProtectionSource.


        :param azure_protection_source: The azure_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceAzureProtectionSource
        """

        self._azure_protection_source = azure_protection_source

    @property
    def environment(self):
        """
        Gets the environment of this ProtectionSourceNodeProtectionSource.
        Specifies the environment (such as 'kVMware' or 'kSQL') where the Protection Source exists. Depending on the environment, one of the following Protection Sources are initialized.  NOTE: kPuppeteer refers to Cohesity's Remote Adapter. Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :return: The environment of this ProtectionSourceNodeProtectionSource.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this ProtectionSourceNodeProtectionSource.
        Specifies the environment (such as 'kVMware' or 'kSQL') where the Protection Source exists. Depending on the environment, one of the following Protection Sources are initialized.  NOTE: kPuppeteer refers to Cohesity's Remote Adapter. Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :param environment: The environment of this ProtectionSourceNodeProtectionSource.
        :type: str
        """
        allowed_values = ["kVMware", "kSQL", "kView", "kPuppeteer", "kPhysical", "kPure", "kNetapp", "kGenericNas", "kHyperV", "kAcropolis", "kAzure"]
        if environment not in allowed_values:
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"
                .format(environment, allowed_values)
            )

        self._environment = environment

    @property
    def hyperv_protection_source(self):
        """
        Gets the hyperv_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The hyperv_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceHypervProtectionSource
        """
        return self._hyperv_protection_source

    @hyperv_protection_source.setter
    def hyperv_protection_source(self, hyperv_protection_source):
        """
        Sets the hyperv_protection_source of this ProtectionSourceNodeProtectionSource.


        :param hyperv_protection_source: The hyperv_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceHypervProtectionSource
        """

        self._hyperv_protection_source = hyperv_protection_source

    @property
    def id(self):
        """
        Gets the id of this ProtectionSourceNodeProtectionSource.
        Specifies an id of the Protection Source.

        :return: The id of this ProtectionSourceNodeProtectionSource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProtectionSourceNodeProtectionSource.
        Specifies an id of the Protection Source.

        :param id: The id of this ProtectionSourceNodeProtectionSource.
        :type: int
        """

        self._id = id

    @property
    def kvm_protection_source(self):
        """
        Gets the kvm_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The kvm_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceKvmProtectionSource
        """
        return self._kvm_protection_source

    @kvm_protection_source.setter
    def kvm_protection_source(self, kvm_protection_source):
        """
        Sets the kvm_protection_source of this ProtectionSourceNodeProtectionSource.


        :param kvm_protection_source: The kvm_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceKvmProtectionSource
        """

        self._kvm_protection_source = kvm_protection_source

    @property
    def name(self):
        """
        Gets the name of this ProtectionSourceNodeProtectionSource.
        Specifies a name of the Protection Source.

        :return: The name of this ProtectionSourceNodeProtectionSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProtectionSourceNodeProtectionSource.
        Specifies a name of the Protection Source.

        :param name: The name of this ProtectionSourceNodeProtectionSource.
        :type: str
        """

        self._name = name

    @property
    def nas_protection_source(self):
        """
        Gets the nas_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The nas_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceNasProtectionSource
        """
        return self._nas_protection_source

    @nas_protection_source.setter
    def nas_protection_source(self, nas_protection_source):
        """
        Sets the nas_protection_source of this ProtectionSourceNodeProtectionSource.


        :param nas_protection_source: The nas_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceNasProtectionSource
        """

        self._nas_protection_source = nas_protection_source

    @property
    def netapp_protection_source(self):
        """
        Gets the netapp_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The netapp_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceNetappProtectionSource
        """
        return self._netapp_protection_source

    @netapp_protection_source.setter
    def netapp_protection_source(self, netapp_protection_source):
        """
        Sets the netapp_protection_source of this ProtectionSourceNodeProtectionSource.


        :param netapp_protection_source: The netapp_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceNetappProtectionSource
        """

        self._netapp_protection_source = netapp_protection_source

    @property
    def parent_id(self):
        """
        Gets the parent_id of this ProtectionSourceNodeProtectionSource.
        Specifies an id of the parent of the Protection Source.

        :return: The parent_id of this ProtectionSourceNodeProtectionSource.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this ProtectionSourceNodeProtectionSource.
        Specifies an id of the parent of the Protection Source.

        :param parent_id: The parent_id of this ProtectionSourceNodeProtectionSource.
        :type: int
        """

        self._parent_id = parent_id

    @property
    def physical_protection_source(self):
        """
        Gets the physical_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The physical_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourcePhysicalProtectionSource
        """
        return self._physical_protection_source

    @physical_protection_source.setter
    def physical_protection_source(self, physical_protection_source):
        """
        Sets the physical_protection_source of this ProtectionSourceNodeProtectionSource.


        :param physical_protection_source: The physical_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourcePhysicalProtectionSource
        """

        self._physical_protection_source = physical_protection_source

    @property
    def pure_protection_source(self):
        """
        Gets the pure_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The pure_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourcePureProtectionSource
        """
        return self._pure_protection_source

    @pure_protection_source.setter
    def pure_protection_source(self, pure_protection_source):
        """
        Sets the pure_protection_source of this ProtectionSourceNodeProtectionSource.


        :param pure_protection_source: The pure_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourcePureProtectionSource
        """

        self._pure_protection_source = pure_protection_source

    @property
    def sql_protection_source(self):
        """
        Gets the sql_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The sql_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceSqlProtectionSource
        """
        return self._sql_protection_source

    @sql_protection_source.setter
    def sql_protection_source(self, sql_protection_source):
        """
        Sets the sql_protection_source of this ProtectionSourceNodeProtectionSource.


        :param sql_protection_source: The sql_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceSqlProtectionSource
        """

        self._sql_protection_source = sql_protection_source

    @property
    def view_protection_source(self):
        """
        Gets the view_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The view_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceViewProtectionSource
        """
        return self._view_protection_source

    @view_protection_source.setter
    def view_protection_source(self, view_protection_source):
        """
        Sets the view_protection_source of this ProtectionSourceNodeProtectionSource.


        :param view_protection_source: The view_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceViewProtectionSource
        """

        self._view_protection_source = view_protection_source

    @property
    def vm_ware_protection_source(self):
        """
        Gets the vm_ware_protection_source of this ProtectionSourceNodeProtectionSource.


        :return: The vm_ware_protection_source of this ProtectionSourceNodeProtectionSource.
        :rtype: ProtectionSourceVmWareProtectionSource
        """
        return self._vm_ware_protection_source

    @vm_ware_protection_source.setter
    def vm_ware_protection_source(self, vm_ware_protection_source):
        """
        Sets the vm_ware_protection_source of this ProtectionSourceNodeProtectionSource.


        :param vm_ware_protection_source: The vm_ware_protection_source of this ProtectionSourceNodeProtectionSource.
        :type: ProtectionSourceVmWareProtectionSource
        """

        self._vm_ware_protection_source = vm_ware_protection_source

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
