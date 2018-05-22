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


class PrivilegeInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category=None, description=None, is_custom_role_default=None, is_special=None, is_view_only=None, label=None, name=None):
        """
        PrivilegeInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'description': 'str',
            'is_custom_role_default': 'bool',
            'is_special': 'bool',
            'is_view_only': 'bool',
            'label': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'description': 'description',
            'is_custom_role_default': 'isCustomRoleDefault',
            'is_special': 'isSpecial',
            'is_view_only': 'isViewOnly',
            'label': 'label',
            'name': 'name'
        }

        self._category = category
        self._description = description
        self._is_custom_role_default = is_custom_role_default
        self._is_special = is_special
        self._is_view_only = is_view_only
        self._label = label
        self._name = name

    @property
    def category(self):
        """
        Gets the category of this PrivilegeInfo.
        Specifies a category for the privilege such as 'Access Management'.

        :return: The category of this PrivilegeInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this PrivilegeInfo.
        Specifies a category for the privilege such as 'Access Management'.

        :param category: The category of this PrivilegeInfo.
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """
        Gets the description of this PrivilegeInfo.
        Specifies a description defining what the privilege provides.

        :return: The description of this PrivilegeInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrivilegeInfo.
        Specifies a description defining what the privilege provides.

        :param description: The description of this PrivilegeInfo.
        :type: str
        """

        self._description = description

    @property
    def is_custom_role_default(self):
        """
        Gets the is_custom_role_default of this PrivilegeInfo.
        Specifies if this privilege is automatically assigned to custom roles.

        :return: The is_custom_role_default of this PrivilegeInfo.
        :rtype: bool
        """
        return self._is_custom_role_default

    @is_custom_role_default.setter
    def is_custom_role_default(self, is_custom_role_default):
        """
        Sets the is_custom_role_default of this PrivilegeInfo.
        Specifies if this privilege is automatically assigned to custom roles.

        :param is_custom_role_default: The is_custom_role_default of this PrivilegeInfo.
        :type: bool
        """

        self._is_custom_role_default = is_custom_role_default

    @property
    def is_special(self):
        """
        Gets the is_special of this PrivilegeInfo.
        Specifies if this privilege is automatically assigned to the default System Admin user called 'admin'. If true, the privilege is NOT assigned to the default System Admin user called 'admin'. By default, privileges are automatically assigned to the default System Admin user called 'admin'.

        :return: The is_special of this PrivilegeInfo.
        :rtype: bool
        """
        return self._is_special

    @is_special.setter
    def is_special(self, is_special):
        """
        Sets the is_special of this PrivilegeInfo.
        Specifies if this privilege is automatically assigned to the default System Admin user called 'admin'. If true, the privilege is NOT assigned to the default System Admin user called 'admin'. By default, privileges are automatically assigned to the default System Admin user called 'admin'.

        :param is_special: The is_special of this PrivilegeInfo.
        :type: bool
        """

        self._is_special = is_special

    @property
    def is_view_only(self):
        """
        Gets the is_view_only of this PrivilegeInfo.
        Specifies if privilege is view-only privilege that cannot make changes.

        :return: The is_view_only of this PrivilegeInfo.
        :rtype: bool
        """
        return self._is_view_only

    @is_view_only.setter
    def is_view_only(self, is_view_only):
        """
        Sets the is_view_only of this PrivilegeInfo.
        Specifies if privilege is view-only privilege that cannot make changes.

        :param is_view_only: The is_view_only of this PrivilegeInfo.
        :type: bool
        """

        self._is_view_only = is_view_only

    @property
    def label(self):
        """
        Gets the label of this PrivilegeInfo.
        Specifies the label for the privilege as displayed on the Cohesity Dashboard such as 'Access Management View'.

        :return: The label of this PrivilegeInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this PrivilegeInfo.
        Specifies the label for the privilege as displayed on the Cohesity Dashboard such as 'Access Management View'.

        :param label: The label of this PrivilegeInfo.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this PrivilegeInfo.
        Specifies the Cluster name for the privilege such as PRINCIPAL_VIEW.

        :return: The name of this PrivilegeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PrivilegeInfo.
        Specifies the Cluster name for the privilege such as PRINCIPAL_VIEW.

        :param name: The name of this PrivilegeInfo.
        :type: str
        """

        self._name = name

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
