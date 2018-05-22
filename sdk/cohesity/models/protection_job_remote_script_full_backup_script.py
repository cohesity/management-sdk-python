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


class ProtectionJobRemoteScriptFullBackupScript(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, script_params=None, script_path=None):
        """
        ProtectionJobRemoteScriptFullBackupScript - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'script_params': 'str',
            'script_path': 'str'
        }

        self.attribute_map = {
            'script_params': 'scriptParams',
            'script_path': 'scriptPath'
        }

        self._script_params = script_params
        self._script_path = script_path

    @property
    def script_params(self):
        """
        Gets the script_params of this ProtectionJobRemoteScriptFullBackupScript.
        Specifies the parameters and values to pass into the remote script. For example if the script expects values for the 'database' and 'user' parameters, specify the parameters and values using the following string: \"database=myDatabase user=me\".

        :return: The script_params of this ProtectionJobRemoteScriptFullBackupScript.
        :rtype: str
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        """
        Sets the script_params of this ProtectionJobRemoteScriptFullBackupScript.
        Specifies the parameters and values to pass into the remote script. For example if the script expects values for the 'database' and 'user' parameters, specify the parameters and values using the following string: \"database=myDatabase user=me\".

        :param script_params: The script_params of this ProtectionJobRemoteScriptFullBackupScript.
        :type: str
        """

        self._script_params = script_params

    @property
    def script_path(self):
        """
        Gets the script_path of this ProtectionJobRemoteScriptFullBackupScript.
        Specifies the path to the script on the remote host.

        :return: The script_path of this ProtectionJobRemoteScriptFullBackupScript.
        :rtype: str
        """
        return self._script_path

    @script_path.setter
    def script_path(self, script_path):
        """
        Sets the script_path of this ProtectionJobRemoteScriptFullBackupScript.
        Specifies the path to the script on the remote host.

        :param script_path: The script_path of this ProtectionJobRemoteScriptFullBackupScript.
        :type: str
        """

        self._script_path = script_path

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
