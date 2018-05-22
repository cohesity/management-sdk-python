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


class CloudDeployTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, aws_params=None, azure_params=None, id=None, name=None, type=None):
        """
        CloudDeployTarget - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aws_params': 'AwsParams',
            'azure_params': 'AzureParams',
            'id': 'int',
            'name': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'aws_params': 'awsParams',
            'azure_params': 'azureParams',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._aws_params = aws_params
        self._azure_params = azure_params
        self._id = id
        self._name = name
        self._type = type

    @property
    def aws_params(self):
        """
        Gets the aws_params of this CloudDeployTarget.
        Specifies various resources when converting and deploying a VM to AWS.

        :return: The aws_params of this CloudDeployTarget.
        :rtype: AwsParams
        """
        return self._aws_params

    @aws_params.setter
    def aws_params(self, aws_params):
        """
        Sets the aws_params of this CloudDeployTarget.
        Specifies various resources when converting and deploying a VM to AWS.

        :param aws_params: The aws_params of this CloudDeployTarget.
        :type: AwsParams
        """

        self._aws_params = aws_params

    @property
    def azure_params(self):
        """
        Gets the azure_params of this CloudDeployTarget.
        Specifies various resources when converting and deploying a VM to Azure.

        :return: The azure_params of this CloudDeployTarget.
        :rtype: AzureParams
        """
        return self._azure_params

    @azure_params.setter
    def azure_params(self, azure_params):
        """
        Sets the azure_params of this CloudDeployTarget.
        Specifies various resources when converting and deploying a VM to Azure.

        :param azure_params: The azure_params of this CloudDeployTarget.
        :type: AzureParams
        """

        self._azure_params = azure_params

    @property
    def id(self):
        """
        Gets the id of this CloudDeployTarget.
        Entity corresponding to the cloud deploy target.  Specifies the id field inside the EntityProto.

        :return: The id of this CloudDeployTarget.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudDeployTarget.
        Entity corresponding to the cloud deploy target.  Specifies the id field inside the EntityProto.

        :param id: The id of this CloudDeployTarget.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CloudDeployTarget.
        Specifies the inner object's name or a human-readable string made off the salient attributes. This is only plumbed when Entity objects are exposed to Iris BE or to Yoda.

        :return: The name of this CloudDeployTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudDeployTarget.
        Specifies the inner object's name or a human-readable string made off the salient attributes. This is only plumbed when Entity objects are exposed to Iris BE or to Yoda.

        :param name: The name of this CloudDeployTarget.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this CloudDeployTarget.
        Specifies the type of the CloudDeploy target.

        :return: The type of this CloudDeployTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudDeployTarget.
        Specifies the type of the CloudDeploy target.

        :param type: The type of this CloudDeployTarget.
        :type: str
        """
        allowed_values = ["kAzure", "kAws"]
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
