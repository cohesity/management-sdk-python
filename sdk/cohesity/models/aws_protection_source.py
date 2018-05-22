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


class AwsProtectionSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, host_type=None, ip_addresses=None, name=None, owner_id=None, region_id=None, resource_id=None, type=None, user_account_id=None, user_resource_name=None):
        """
        AwsProtectionSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'host_type': 'str',
            'ip_addresses': 'str',
            'name': 'str',
            'owner_id': 'str',
            'region_id': 'str',
            'resource_id': 'str',
            'type': 'str',
            'user_account_id': 'str',
            'user_resource_name': 'str'
        }

        self.attribute_map = {
            'host_type': 'hostType',
            'ip_addresses': 'ipAddresses',
            'name': 'name',
            'owner_id': 'ownerId',
            'region_id': 'regionId',
            'resource_id': 'resourceId',
            'type': 'type',
            'user_account_id': 'userAccountId',
            'user_resource_name': 'userResourceName'
        }

        self._host_type = host_type
        self._ip_addresses = ip_addresses
        self._name = name
        self._owner_id = owner_id
        self._region_id = region_id
        self._resource_id = resource_id
        self._type = type
        self._user_account_id = user_account_id
        self._user_resource_name = user_resource_name

    @property
    def host_type(self):
        """
        Gets the host_type of this AwsProtectionSource.
        Specifies the OS type of the Protection Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'. overrideDescription: true 'kLinux' indicates the Linux operating system. 'kWindows' indicates the Microsoft Windows operating system.

        :return: The host_type of this AwsProtectionSource.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """
        Sets the host_type of this AwsProtectionSource.
        Specifies the OS type of the Protection Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'. overrideDescription: true 'kLinux' indicates the Linux operating system. 'kWindows' indicates the Microsoft Windows operating system.

        :param host_type: The host_type of this AwsProtectionSource.
        :type: str
        """
        allowed_values = ["kLinux", "kWindows"]
        if host_type not in allowed_values:
            raise ValueError(
                "Invalid value for `host_type` ({0}), must be one of {1}"
                .format(host_type, allowed_values)
            )

        self._host_type = host_type

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this AwsProtectionSource.
        Specifies the IP address of the entity of type 'kVirtualMachine'.

        :return: The ip_addresses of this AwsProtectionSource.
        :rtype: str
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this AwsProtectionSource.
        Specifies the IP address of the entity of type 'kVirtualMachine'.

        :param ip_addresses: The ip_addresses of this AwsProtectionSource.
        :type: str
        """

        self._ip_addresses = ip_addresses

    @property
    def name(self):
        """
        Gets the name of this AwsProtectionSource.
        Specifies the name of the AWS Object set by the Cloud Provider.

        :return: The name of this AwsProtectionSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwsProtectionSource.
        Specifies the name of the AWS Object set by the Cloud Provider.

        :param name: The name of this AwsProtectionSource.
        :type: str
        """

        self._name = name

    @property
    def owner_id(self):
        """
        Gets the owner_id of this AwsProtectionSource.
        Specifies the owner id of the resource in AWS environment. With type, name and ownerId gives a globally unique identity to the AWS entity.

        :return: The owner_id of this AwsProtectionSource.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this AwsProtectionSource.
        Specifies the owner id of the resource in AWS environment. With type, name and ownerId gives a globally unique identity to the AWS entity.

        :param owner_id: The owner_id of this AwsProtectionSource.
        :type: str
        """

        self._owner_id = owner_id

    @property
    def region_id(self):
        """
        Gets the region_id of this AwsProtectionSource.
        Specifies the region Id of the entity if the entity is an EC2 instance.

        :return: The region_id of this AwsProtectionSource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this AwsProtectionSource.
        Specifies the region Id of the entity if the entity is an EC2 instance.

        :param region_id: The region_id of this AwsProtectionSource.
        :type: str
        """

        self._region_id = region_id

    @property
    def resource_id(self):
        """
        Gets the resource_id of this AwsProtectionSource.
        Specifies the unique Id of the resource given by the cloud provider.

        :return: The resource_id of this AwsProtectionSource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this AwsProtectionSource.
        Specifies the unique Id of the resource given by the cloud provider.

        :param resource_id: The resource_id of this AwsProtectionSource.
        :type: str
        """

        self._resource_id = resource_id

    @property
    def type(self):
        """
        Gets the type of this AwsProtectionSource.
        Specifies the type of an AWS Protection Source Object such as 'kStorageContainer', 'kVirtualMachine', 'kVirtualNetwork', etc. Specifies the type of an AWS source entity. 'kIAMUser' indicates a unique user within an AWS account. 'kRegion' indicates a geographical region in the global infrastructure. 'kAvailabilityZone' indicates an availability zone within a region. 'kEC2Instance' indicates a Virtual Machine running in AWS environment. 'kVPC' indicates a virtual private cloud (VPC) network within AWS. 'kSubnet' indicates a subnet inside the VPC. 'kNetworkSecurityGroup' represents a network security group. 'kInstanceType' represents various machine types. 'kKeyPair' represents a pair of public and private key used to login into a Virtual Machine.

        :return: The type of this AwsProtectionSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AwsProtectionSource.
        Specifies the type of an AWS Protection Source Object such as 'kStorageContainer', 'kVirtualMachine', 'kVirtualNetwork', etc. Specifies the type of an AWS source entity. 'kIAMUser' indicates a unique user within an AWS account. 'kRegion' indicates a geographical region in the global infrastructure. 'kAvailabilityZone' indicates an availability zone within a region. 'kEC2Instance' indicates a Virtual Machine running in AWS environment. 'kVPC' indicates a virtual private cloud (VPC) network within AWS. 'kSubnet' indicates a subnet inside the VPC. 'kNetworkSecurityGroup' represents a network security group. 'kInstanceType' represents various machine types. 'kKeyPair' represents a pair of public and private key used to login into a Virtual Machine.

        :param type: The type of this AwsProtectionSource.
        :type: str
        """
        allowed_values = ["kIAMUser", "kRegion", "kAvailabilityZone", "kEC2Instance", "kVPC", "kSubnet", "kNetworkSecurityGroup", "kInstanceType", "kKeyPair"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_account_id(self):
        """
        Gets the user_account_id of this AwsProtectionSource.
        Specifies the account id derived from the ARN of the user.

        :return: The user_account_id of this AwsProtectionSource.
        :rtype: str
        """
        return self._user_account_id

    @user_account_id.setter
    def user_account_id(self, user_account_id):
        """
        Sets the user_account_id of this AwsProtectionSource.
        Specifies the account id derived from the ARN of the user.

        :param user_account_id: The user_account_id of this AwsProtectionSource.
        :type: str
        """

        self._user_account_id = user_account_id

    @property
    def user_resource_name(self):
        """
        Gets the user_resource_name of this AwsProtectionSource.
        Specifies the Amazon Resource Name (ARN) of the user.

        :return: The user_resource_name of this AwsProtectionSource.
        :rtype: str
        """
        return self._user_resource_name

    @user_resource_name.setter
    def user_resource_name(self, user_resource_name):
        """
        Sets the user_resource_name of this AwsProtectionSource.
        Specifies the Amazon Resource Name (ARN) of the user.

        :param user_resource_name: The user_resource_name of this AwsProtectionSource.
        :type: str
        """

        self._user_resource_name = user_resource_name

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
