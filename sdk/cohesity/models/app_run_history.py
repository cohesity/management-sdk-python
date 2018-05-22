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


class AppRunHistory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, app_info=None, mr_instances=None):
        """
        AppRunHistory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_info': 'MapReduceInfo',
            'mr_instances': 'list[MapReduceInstanceWrapper]'
        }

        self.attribute_map = {
            'app_info': 'appInfo',
            'mr_instances': 'mrInstances'
        }

        self._app_info = app_info
        self._mr_instances = mr_instances

    @property
    def app_info(self):
        """
        Gets the app_info of this AppRunHistory.
        AppInfo is the information about the map reduce application.

        :return: The app_info of this AppRunHistory.
        :rtype: MapReduceInfo
        """
        return self._app_info

    @app_info.setter
    def app_info(self, app_info):
        """
        Sets the app_info of this AppRunHistory.
        AppInfo is the information about the map reduce application.

        :param app_info: The app_info of this AppRunHistory.
        :type: MapReduceInfo
        """

        self._app_info = app_info

    @property
    def mr_instances(self):
        """
        Gets the mr_instances of this AppRunHistory.
        InstancesWrapper is the slice containing the information about the map reduce application instances.

        :return: The mr_instances of this AppRunHistory.
        :rtype: list[MapReduceInstanceWrapper]
        """
        return self._mr_instances

    @mr_instances.setter
    def mr_instances(self, mr_instances):
        """
        Sets the mr_instances of this AppRunHistory.
        InstancesWrapper is the slice containing the information about the map reduce application instances.

        :param mr_instances: The mr_instances of this AppRunHistory.
        :type: list[MapReduceInstanceWrapper]
        """

        self._mr_instances = mr_instances

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
