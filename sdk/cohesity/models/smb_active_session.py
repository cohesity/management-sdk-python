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


class SmbActiveSession(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active_opens=None, client_ip=None, domain=None, server_ip=None, session_id=None, username=None):
        """
        SmbActiveSession - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_opens': 'list[SmbActiveOpen]',
            'client_ip': 'str',
            'domain': 'str',
            'server_ip': 'str',
            'session_id': 'int',
            'username': 'str'
        }

        self.attribute_map = {
            'active_opens': 'activeOpens',
            'client_ip': 'clientIp',
            'domain': 'domain',
            'server_ip': 'serverIp',
            'session_id': 'sessionId',
            'username': 'username'
        }

        self._active_opens = active_opens
        self._client_ip = client_ip
        self._domain = domain
        self._server_ip = server_ip
        self._session_id = session_id
        self._username = username

    @property
    def active_opens(self):
        """
        Gets the active_opens of this SmbActiveSession.


        :return: The active_opens of this SmbActiveSession.
        :rtype: list[SmbActiveOpen]
        """
        return self._active_opens

    @active_opens.setter
    def active_opens(self, active_opens):
        """
        Sets the active_opens of this SmbActiveSession.


        :param active_opens: The active_opens of this SmbActiveSession.
        :type: list[SmbActiveOpen]
        """

        self._active_opens = active_opens

    @property
    def client_ip(self):
        """
        Gets the client_ip of this SmbActiveSession.
        Specifies the IP address from which the file is still open.

        :return: The client_ip of this SmbActiveSession.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """
        Sets the client_ip of this SmbActiveSession.
        Specifies the IP address from which the file is still open.

        :param client_ip: The client_ip of this SmbActiveSession.
        :type: str
        """

        self._client_ip = client_ip

    @property
    def domain(self):
        """
        Gets the domain of this SmbActiveSession.
        Specifies the domain of the user.

        :return: The domain of this SmbActiveSession.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this SmbActiveSession.
        Specifies the domain of the user.

        :param domain: The domain of this SmbActiveSession.
        :type: str
        """

        self._domain = domain

    @property
    def server_ip(self):
        """
        Gets the server_ip of this SmbActiveSession.
        Specifies the IP address of the server where the file exists.

        :return: The server_ip of this SmbActiveSession.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        """
        Sets the server_ip of this SmbActiveSession.
        Specifies the IP address of the server where the file exists.

        :param server_ip: The server_ip of this SmbActiveSession.
        :type: str
        """

        self._server_ip = server_ip

    @property
    def session_id(self):
        """
        Gets the session_id of this SmbActiveSession.
        Specifies the id of the session.

        :return: The session_id of this SmbActiveSession.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this SmbActiveSession.
        Specifies the id of the session.

        :param session_id: The session_id of this SmbActiveSession.
        :type: int
        """

        self._session_id = session_id

    @property
    def username(self):
        """
        Gets the username of this SmbActiveSession.
        Specifies the username who keeps the file open.

        :return: The username of this SmbActiveSession.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SmbActiveSession.
        Specifies the username who keeps the file open.

        :param username: The username of this SmbActiveSession.
        :type: str
        """

        self._username = username

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
