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


class MapReduceInstanceWrapper(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, log_path=None, mr_instance=None, output_file_path_list=None):
        """
        MapReduceInstanceWrapper - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'log_path': 'str',
            'mr_instance': 'MapReduceInstance',
            'output_file_path_list': 'list[str]'
        }

        self.attribute_map = {
            'log_path': 'logPath',
            'mr_instance': 'mrInstance',
            'output_file_path_list': 'outputFilePathList'
        }

        self._log_path = log_path
        self._mr_instance = mr_instance
        self._output_file_path_list = output_file_path_list

    @property
    def log_path(self):
        """
        Gets the log_path of this MapReduceInstanceWrapper.
        LogPath is the path of the log files for the MR instance run.

        :return: The log_path of this MapReduceInstanceWrapper.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """
        Sets the log_path of this MapReduceInstanceWrapper.
        LogPath is the path of the log files for the MR instance run.

        :param log_path: The log_path of this MapReduceInstanceWrapper.
        :type: str
        """

        self._log_path = log_path

    @property
    def mr_instance(self):
        """
        Gets the mr_instance of this MapReduceInstanceWrapper.
        InstanceInfo is the information about the map reduce application instance.

        :return: The mr_instance of this MapReduceInstanceWrapper.
        :rtype: MapReduceInstance
        """
        return self._mr_instance

    @mr_instance.setter
    def mr_instance(self, mr_instance):
        """
        Sets the mr_instance of this MapReduceInstanceWrapper.
        InstanceInfo is the information about the map reduce application instance.

        :param mr_instance: The mr_instance of this MapReduceInstanceWrapper.
        :type: MapReduceInstance
        """

        self._mr_instance = mr_instance

    @property
    def output_file_path_list(self):
        """
        Gets the output_file_path_list of this MapReduceInstanceWrapper.
        OutputFilePathList is the list containing the output files path suffix that Yoda uses to build the full path of the MR instance run output files.

        :return: The output_file_path_list of this MapReduceInstanceWrapper.
        :rtype: list[str]
        """
        return self._output_file_path_list

    @output_file_path_list.setter
    def output_file_path_list(self, output_file_path_list):
        """
        Sets the output_file_path_list of this MapReduceInstanceWrapper.
        OutputFilePathList is the list containing the output files path suffix that Yoda uses to build the full path of the MR instance run output files.

        :param output_file_path_list: The output_file_path_list of this MapReduceInstanceWrapper.
        :type: list[str]
        """

        self._output_file_path_list = output_file_path_list

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
