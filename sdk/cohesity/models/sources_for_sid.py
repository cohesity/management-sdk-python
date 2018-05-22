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


class SourcesForSid(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, protection_sources=None, sid=None, views=None):
        """
        SourcesForSid - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'protection_sources': 'list[ProtectionSource]',
            'sid': 'str',
            'views': 'list[View]'
        }

        self.attribute_map = {
            'protection_sources': 'protectionSources',
            'sid': 'sid',
            'views': 'views'
        }

        self._protection_sources = protection_sources
        self._sid = sid
        self._views = views

    @property
    def protection_sources(self):
        """
        Gets the protection_sources of this SourcesForSid.
        Specifies the Protection Source objects that the specified principal has permissions to access.

        :return: The protection_sources of this SourcesForSid.
        :rtype: list[ProtectionSource]
        """
        return self._protection_sources

    @protection_sources.setter
    def protection_sources(self, protection_sources):
        """
        Sets the protection_sources of this SourcesForSid.
        Specifies the Protection Source objects that the specified principal has permissions to access.

        :param protection_sources: The protection_sources of this SourcesForSid.
        :type: list[ProtectionSource]
        """

        self._protection_sources = protection_sources

    @property
    def sid(self):
        """
        Gets the sid of this SourcesForSid.
        Specifies the security identifier (SID) of the principal.

        :return: The sid of this SourcesForSid.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this SourcesForSid.
        Specifies the security identifier (SID) of the principal.

        :param sid: The sid of this SourcesForSid.
        :type: str
        """

        self._sid = sid

    @property
    def views(self):
        """
        Gets the views of this SourcesForSid.
        Specifies the names of the Views that the specified principal has permissions to access.

        :return: The views of this SourcesForSid.
        :rtype: list[View]
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this SourcesForSid.
        Specifies the names of the Views that the specified principal has permissions to access.

        :param views: The views of this SourcesForSid.
        :type: list[View]
        """

        self._views = views

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
