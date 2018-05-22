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


class DataTransferToVaultPerProtectionJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, num_logical_bytes_transferred=None, num_physical_bytes_transferred=None, protection_job_name=None):
        """
        DataTransferToVaultPerProtectionJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'num_logical_bytes_transferred': 'int',
            'num_physical_bytes_transferred': 'int',
            'protection_job_name': 'str'
        }

        self.attribute_map = {
            'num_logical_bytes_transferred': 'numLogicalBytesTransferred',
            'num_physical_bytes_transferred': 'numPhysicalBytesTransferred',
            'protection_job_name': 'protectionJobName'
        }

        self._num_logical_bytes_transferred = num_logical_bytes_transferred
        self._num_physical_bytes_transferred = num_physical_bytes_transferred
        self._protection_job_name = protection_job_name

    @property
    def num_logical_bytes_transferred(self):
        """
        Gets the num_logical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        Specifies the total number of logical bytes that are transferred from this Cohesity Cluster to this Vault for this Protection Job. The logical size is when the data is fully hydrated or expanded.

        :return: The num_logical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        :rtype: int
        """
        return self._num_logical_bytes_transferred

    @num_logical_bytes_transferred.setter
    def num_logical_bytes_transferred(self, num_logical_bytes_transferred):
        """
        Sets the num_logical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        Specifies the total number of logical bytes that are transferred from this Cohesity Cluster to this Vault for this Protection Job. The logical size is when the data is fully hydrated or expanded.

        :param num_logical_bytes_transferred: The num_logical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        :type: int
        """

        self._num_logical_bytes_transferred = num_logical_bytes_transferred

    @property
    def num_physical_bytes_transferred(self):
        """
        Gets the num_physical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        Specifies the total number of physical bytes that are transferred from this Cohesity Cluster to this Vault for this Protection Job.

        :return: The num_physical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        :rtype: int
        """
        return self._num_physical_bytes_transferred

    @num_physical_bytes_transferred.setter
    def num_physical_bytes_transferred(self, num_physical_bytes_transferred):
        """
        Sets the num_physical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        Specifies the total number of physical bytes that are transferred from this Cohesity Cluster to this Vault for this Protection Job.

        :param num_physical_bytes_transferred: The num_physical_bytes_transferred of this DataTransferToVaultPerProtectionJob.
        :type: int
        """

        self._num_physical_bytes_transferred = num_physical_bytes_transferred

    @property
    def protection_job_name(self):
        """
        Gets the protection_job_name of this DataTransferToVaultPerProtectionJob.
        Specifies the name of the Protection Job.

        :return: The protection_job_name of this DataTransferToVaultPerProtectionJob.
        :rtype: str
        """
        return self._protection_job_name

    @protection_job_name.setter
    def protection_job_name(self, protection_job_name):
        """
        Sets the protection_job_name of this DataTransferToVaultPerProtectionJob.
        Specifies the name of the Protection Job.

        :param protection_job_name: The protection_job_name of this DataTransferToVaultPerProtectionJob.
        :type: str
        """

        self._protection_job_name = protection_job_name

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
