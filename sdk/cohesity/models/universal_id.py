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


class UniversalId(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cluster_id=None, cluster_incarnation_id=None, id=None):
        """
        UniversalId - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cluster_id': 'int',
            'cluster_incarnation_id': 'int',
            'id': 'int'
        }

        self.attribute_map = {
            'cluster_id': 'clusterId',
            'cluster_incarnation_id': 'clusterIncarnationId',
            'id': 'id'
        }

        self._cluster_id = cluster_id
        self._cluster_incarnation_id = cluster_incarnation_id
        self._id = id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this UniversalId.
        Specifies the Cohesity Cluster id where the object was created.

        :return: The cluster_id of this UniversalId.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this UniversalId.
        Specifies the Cohesity Cluster id where the object was created.

        :param cluster_id: The cluster_id of this UniversalId.
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def cluster_incarnation_id(self):
        """
        Gets the cluster_incarnation_id of this UniversalId.
        Specifies an id for the Cohesity Cluster that is generated when a Cohesity Cluster is initially created.

        :return: The cluster_incarnation_id of this UniversalId.
        :rtype: int
        """
        return self._cluster_incarnation_id

    @cluster_incarnation_id.setter
    def cluster_incarnation_id(self, cluster_incarnation_id):
        """
        Sets the cluster_incarnation_id of this UniversalId.
        Specifies an id for the Cohesity Cluster that is generated when a Cohesity Cluster is initially created.

        :param cluster_incarnation_id: The cluster_incarnation_id of this UniversalId.
        :type: int
        """

        self._cluster_incarnation_id = cluster_incarnation_id

    @property
    def id(self):
        """
        Gets the id of this UniversalId.
        Specifies a unique id assigned to an object (such as a Job) by the Cohesity Cluster.

        :return: The id of this UniversalId.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UniversalId.
        Specifies a unique id assigned to an object (such as a Job) by the Cohesity Cluster.

        :param id: The id of this UniversalId.
        :type: int
        """

        self._id = id

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
