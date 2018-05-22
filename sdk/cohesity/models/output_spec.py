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


class OutputSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, num_reduce_shards=None, output_dir=None, partition_id=None, reduce_output_prefix=None, view_box_id=None, view_name=None):
        """
        OutputSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'num_reduce_shards': 'int',
            'output_dir': 'str',
            'partition_id': 'int',
            'reduce_output_prefix': 'str',
            'view_box_id': 'int',
            'view_name': 'str'
        }

        self.attribute_map = {
            'num_reduce_shards': 'numReduceShards',
            'output_dir': 'outputDir',
            'partition_id': 'partitionId',
            'reduce_output_prefix': 'reduceOutputPrefix',
            'view_box_id': 'viewBoxId',
            'view_name': 'viewName'
        }

        self._num_reduce_shards = num_reduce_shards
        self._output_dir = output_dir
        self._partition_id = partition_id
        self._reduce_output_prefix = reduce_output_prefix
        self._view_box_id = view_box_id
        self._view_name = view_name

    @property
    def num_reduce_shards(self):
        """
        Gets the num_reduce_shards of this OutputSpec.
        Number of reduce shards.

        :return: The num_reduce_shards of this OutputSpec.
        :rtype: int
        """
        return self._num_reduce_shards

    @num_reduce_shards.setter
    def num_reduce_shards(self, num_reduce_shards):
        """
        Sets the num_reduce_shards of this OutputSpec.
        Number of reduce shards.

        :param num_reduce_shards: The num_reduce_shards of this OutputSpec.
        :type: int
        """

        self._num_reduce_shards = num_reduce_shards

    @property
    def output_dir(self):
        """
        Gets the output_dir of this OutputSpec.
        Name of output directory.

        :return: The output_dir of this OutputSpec.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """
        Sets the output_dir of this OutputSpec.
        Name of output directory.

        :param output_dir: The output_dir of this OutputSpec.
        :type: str
        """

        self._output_dir = output_dir

    @property
    def partition_id(self):
        """
        Gets the partition_id of this OutputSpec.
        Partition id where output will go.

        :return: The partition_id of this OutputSpec.
        :rtype: int
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """
        Sets the partition_id of this OutputSpec.
        Partition id where output will go.

        :param partition_id: The partition_id of this OutputSpec.
        :type: int
        """

        self._partition_id = partition_id

    @property
    def reduce_output_prefix(self):
        """
        Gets the reduce_output_prefix of this OutputSpec.
        Prefix of the reduce output files. File names will be: ${reduce_output_prefix}-00000-of-00100 if num_reduce_shards=100 This name can contain some path components. e.g. \"awb_results/run1\" is a valid value. output_dir is deprecated.

        :return: The reduce_output_prefix of this OutputSpec.
        :rtype: str
        """
        return self._reduce_output_prefix

    @reduce_output_prefix.setter
    def reduce_output_prefix(self, reduce_output_prefix):
        """
        Sets the reduce_output_prefix of this OutputSpec.
        Prefix of the reduce output files. File names will be: ${reduce_output_prefix}-00000-of-00100 if num_reduce_shards=100 This name can contain some path components. e.g. \"awb_results/run1\" is a valid value. output_dir is deprecated.

        :param reduce_output_prefix: The reduce_output_prefix of this OutputSpec.
        :type: str
        """

        self._reduce_output_prefix = reduce_output_prefix

    @property
    def view_box_id(self):
        """
        Gets the view_box_id of this OutputSpec.
        Viewbox id where the output will go.

        :return: The view_box_id of this OutputSpec.
        :rtype: int
        """
        return self._view_box_id

    @view_box_id.setter
    def view_box_id(self, view_box_id):
        """
        Sets the view_box_id of this OutputSpec.
        Viewbox id where the output will go.

        :param view_box_id: The view_box_id of this OutputSpec.
        :type: int
        """

        self._view_box_id = view_box_id

    @property
    def view_name(self):
        """
        Gets the view_name of this OutputSpec.
        Name of the view where output will go. This will be filled up by yoda.

        :return: The view_name of this OutputSpec.
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """
        Sets the view_name of this OutputSpec.
        Name of the view where output will go. This will be filled up by yoda.

        :param view_name: The view_name of this OutputSpec.
        :type: str
        """

        self._view_name = view_name

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
