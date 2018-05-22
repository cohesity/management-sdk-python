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


class AddedActiveDirectoryPrincipal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_time_msecs=None, description=None, domain=None, last_updated_time_msecs=None, object_class=None, principal_name=None, restricted=None, roles=None, sid=None):
        """
        AddedActiveDirectoryPrincipal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_time_msecs': 'int',
            'description': 'str',
            'domain': 'str',
            'last_updated_time_msecs': 'int',
            'object_class': 'str',
            'principal_name': 'str',
            'restricted': 'bool',
            'roles': 'list[str]',
            'sid': 'str'
        }

        self.attribute_map = {
            'created_time_msecs': 'createdTimeMsecs',
            'description': 'description',
            'domain': 'domain',
            'last_updated_time_msecs': 'lastUpdatedTimeMsecs',
            'object_class': 'objectClass',
            'principal_name': 'principalName',
            'restricted': 'restricted',
            'roles': 'roles',
            'sid': 'sid'
        }

        self._created_time_msecs = created_time_msecs
        self._description = description
        self._domain = domain
        self._last_updated_time_msecs = last_updated_time_msecs
        self._object_class = object_class
        self._principal_name = principal_name
        self._restricted = restricted
        self._roles = roles
        self._sid = sid

    @property
    def created_time_msecs(self):
        """
        Gets the created_time_msecs of this AddedActiveDirectoryPrincipal.
        Specifies the epoch time in milliseconds when the group or user was added to the Cohesity Cluster.

        :return: The created_time_msecs of this AddedActiveDirectoryPrincipal.
        :rtype: int
        """
        return self._created_time_msecs

    @created_time_msecs.setter
    def created_time_msecs(self, created_time_msecs):
        """
        Sets the created_time_msecs of this AddedActiveDirectoryPrincipal.
        Specifies the epoch time in milliseconds when the group or user was added to the Cohesity Cluster.

        :param created_time_msecs: The created_time_msecs of this AddedActiveDirectoryPrincipal.
        :type: int
        """

        self._created_time_msecs = created_time_msecs

    @property
    def description(self):
        """
        Gets the description of this AddedActiveDirectoryPrincipal.
        Specifies a description about the user or group.

        :return: The description of this AddedActiveDirectoryPrincipal.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddedActiveDirectoryPrincipal.
        Specifies a description about the user or group.

        :param description: The description of this AddedActiveDirectoryPrincipal.
        :type: str
        """

        self._description = description

    @property
    def domain(self):
        """
        Gets the domain of this AddedActiveDirectoryPrincipal.
        Specifies the domain of the Active Directory where the referenced principal is stored.

        :return: The domain of this AddedActiveDirectoryPrincipal.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this AddedActiveDirectoryPrincipal.
        Specifies the domain of the Active Directory where the referenced principal is stored.

        :param domain: The domain of this AddedActiveDirectoryPrincipal.
        :type: str
        """

        self._domain = domain

    @property
    def last_updated_time_msecs(self):
        """
        Gets the last_updated_time_msecs of this AddedActiveDirectoryPrincipal.
        Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster.

        :return: The last_updated_time_msecs of this AddedActiveDirectoryPrincipal.
        :rtype: int
        """
        return self._last_updated_time_msecs

    @last_updated_time_msecs.setter
    def last_updated_time_msecs(self, last_updated_time_msecs):
        """
        Sets the last_updated_time_msecs of this AddedActiveDirectoryPrincipal.
        Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster.

        :param last_updated_time_msecs: The last_updated_time_msecs of this AddedActiveDirectoryPrincipal.
        :type: int
        """

        self._last_updated_time_msecs = last_updated_time_msecs

    @property
    def object_class(self):
        """
        Gets the object_class of this AddedActiveDirectoryPrincipal.
        Specifies the type of the referenced Active Directory principal. If 'kGroup', the referenced Active Directory principal is a group. If 'kUser', the referenced Active Directory principal is a user. 'kUser' specifies a user object class. 'kGroup' specifies a group object class.

        :return: The object_class of this AddedActiveDirectoryPrincipal.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """
        Sets the object_class of this AddedActiveDirectoryPrincipal.
        Specifies the type of the referenced Active Directory principal. If 'kGroup', the referenced Active Directory principal is a group. If 'kUser', the referenced Active Directory principal is a user. 'kUser' specifies a user object class. 'kGroup' specifies a group object class.

        :param object_class: The object_class of this AddedActiveDirectoryPrincipal.
        :type: str
        """
        allowed_values = ["kUser", "kGroup"]
        if object_class not in allowed_values:
            raise ValueError(
                "Invalid value for `object_class` ({0}), must be one of {1}"
                .format(object_class, allowed_values)
            )

        self._object_class = object_class

    @property
    def principal_name(self):
        """
        Gets the principal_name of this AddedActiveDirectoryPrincipal.
        Specifies the name of the Active Directory principal, that will be referenced by the group or user. The name of the Active Directory principal is used for naming the new group or user on the Cohesity Cluster.

        :return: The principal_name of this AddedActiveDirectoryPrincipal.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """
        Sets the principal_name of this AddedActiveDirectoryPrincipal.
        Specifies the name of the Active Directory principal, that will be referenced by the group or user. The name of the Active Directory principal is used for naming the new group or user on the Cohesity Cluster.

        :param principal_name: The principal_name of this AddedActiveDirectoryPrincipal.
        :type: str
        """

        self._principal_name = principal_name

    @property
    def restricted(self):
        """
        Gets the restricted of this AddedActiveDirectoryPrincipal.
        Whether the principal is a restricted principal. A restricted principal can only view the objects he has permissions to.

        :return: The restricted of this AddedActiveDirectoryPrincipal.
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this AddedActiveDirectoryPrincipal.
        Whether the principal is a restricted principal. A restricted principal can only view the objects he has permissions to.

        :param restricted: The restricted of this AddedActiveDirectoryPrincipal.
        :type: bool
        """

        self._restricted = restricted

    @property
    def roles(self):
        """
        Gets the roles of this AddedActiveDirectoryPrincipal.
        Specifies the Cohesity roles to associate with this user or group such as 'Admin', 'Ops' or 'View'. The Cohesity roles determine privileges on the Cohesity Cluster for this group or user. For example if the 'joe' user is added for the Active Directory 'joe' user principal and is associated with the Cohesity 'View' role, 'joe' can log in to the Cohesity Dashboard and has a read-only view of the data on the Cohesity Cluster.

        :return: The roles of this AddedActiveDirectoryPrincipal.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this AddedActiveDirectoryPrincipal.
        Specifies the Cohesity roles to associate with this user or group such as 'Admin', 'Ops' or 'View'. The Cohesity roles determine privileges on the Cohesity Cluster for this group or user. For example if the 'joe' user is added for the Active Directory 'joe' user principal and is associated with the Cohesity 'View' role, 'joe' can log in to the Cohesity Dashboard and has a read-only view of the data on the Cohesity Cluster.

        :param roles: The roles of this AddedActiveDirectoryPrincipal.
        :type: list[str]
        """

        self._roles = roles

    @property
    def sid(self):
        """
        Gets the sid of this AddedActiveDirectoryPrincipal.
        Specifies the unique Security ID (SID) of the Active Directory principal associated with this group or user.

        :return: The sid of this AddedActiveDirectoryPrincipal.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this AddedActiveDirectoryPrincipal.
        Specifies the unique Security ID (SID) of the Active Directory principal associated with this group or user.

        :param sid: The sid of this AddedActiveDirectoryPrincipal.
        :type: str
        """

        self._sid = sid

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
