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


class ProtectionSourceNodeRegistrationInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_info=None, authentication_error_message=None, authentication_status=None, environments=None, minimum_free_space_gb=None, nas_mount_credentials=None, password=None, refresh_error_message=None, refresh_time_usecs=None, registration_time_usecs=None, throttling_policy=None, throttling_policy_overrides=None, username=None, warning_messages=None):
        """
        ProtectionSourceNodeRegistrationInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_info': 'ConnectorParams',
            'authentication_error_message': 'str',
            'authentication_status': 'str',
            'environments': 'list[str]',
            'minimum_free_space_gb': 'int',
            'nas_mount_credentials': 'ProtectionSourceNodeRegistrationInfoNasMountCredentials',
            'password': 'str',
            'refresh_error_message': 'str',
            'refresh_time_usecs': 'int',
            'registration_time_usecs': 'int',
            'throttling_policy': 'ThrottlingPolicy',
            'throttling_policy_overrides': 'list[ThrottlingPolicyOverride]',
            'username': 'str',
            'warning_messages': 'list[str]'
        }

        self.attribute_map = {
            'access_info': 'accessInfo',
            'authentication_error_message': 'authenticationErrorMessage',
            'authentication_status': 'authenticationStatus',
            'environments': 'environments',
            'minimum_free_space_gb': 'minimumFreeSpaceGB',
            'nas_mount_credentials': 'nasMountCredentials',
            'password': 'password',
            'refresh_error_message': 'refreshErrorMessage',
            'refresh_time_usecs': 'refreshTimeUsecs',
            'registration_time_usecs': 'registrationTimeUsecs',
            'throttling_policy': 'throttlingPolicy',
            'throttling_policy_overrides': 'throttlingPolicyOverrides',
            'username': 'username',
            'warning_messages': 'warningMessages'
        }

        self._access_info = access_info
        self._authentication_error_message = authentication_error_message
        self._authentication_status = authentication_status
        self._environments = environments
        self._minimum_free_space_gb = minimum_free_space_gb
        self._nas_mount_credentials = nas_mount_credentials
        self._password = password
        self._refresh_error_message = refresh_error_message
        self._refresh_time_usecs = refresh_time_usecs
        self._registration_time_usecs = registration_time_usecs
        self._throttling_policy = throttling_policy
        self._throttling_policy_overrides = throttling_policy_overrides
        self._username = username
        self._warning_messages = warning_messages

    @property
    def access_info(self):
        """
        Gets the access_info of this ProtectionSourceNodeRegistrationInfo.
        Specifies the parameters required to establish a connection with a particular environment.

        :return: The access_info of this ProtectionSourceNodeRegistrationInfo.
        :rtype: ConnectorParams
        """
        return self._access_info

    @access_info.setter
    def access_info(self, access_info):
        """
        Sets the access_info of this ProtectionSourceNodeRegistrationInfo.
        Specifies the parameters required to establish a connection with a particular environment.

        :param access_info: The access_info of this ProtectionSourceNodeRegistrationInfo.
        :type: ConnectorParams
        """

        self._access_info = access_info

    @property
    def authentication_error_message(self):
        """
        Gets the authentication_error_message of this ProtectionSourceNodeRegistrationInfo.
        Specifies an authentication error message. This indicates the given credentials are rejected and the registration of the source is not successful.

        :return: The authentication_error_message of this ProtectionSourceNodeRegistrationInfo.
        :rtype: str
        """
        return self._authentication_error_message

    @authentication_error_message.setter
    def authentication_error_message(self, authentication_error_message):
        """
        Sets the authentication_error_message of this ProtectionSourceNodeRegistrationInfo.
        Specifies an authentication error message. This indicates the given credentials are rejected and the registration of the source is not successful.

        :param authentication_error_message: The authentication_error_message of this ProtectionSourceNodeRegistrationInfo.
        :type: str
        """

        self._authentication_error_message = authentication_error_message

    @property
    def authentication_status(self):
        """
        Gets the authentication_status of this ProtectionSourceNodeRegistrationInfo.
        Specifies the status of the authenticating to the Protection Source when registering it with Cohesity Cluster. If the status is 'kFinished' and there is no error, registration is successful. Specifies the status of the authentication during the registration of a Protection Source. 'kPending' indicates the authentication is in progress. 'kScheduled' indicates the authentication is scheduled. 'kFinished' indicates the authentication is completed.

        :return: The authentication_status of this ProtectionSourceNodeRegistrationInfo.
        :rtype: str
        """
        return self._authentication_status

    @authentication_status.setter
    def authentication_status(self, authentication_status):
        """
        Sets the authentication_status of this ProtectionSourceNodeRegistrationInfo.
        Specifies the status of the authenticating to the Protection Source when registering it with Cohesity Cluster. If the status is 'kFinished' and there is no error, registration is successful. Specifies the status of the authentication during the registration of a Protection Source. 'kPending' indicates the authentication is in progress. 'kScheduled' indicates the authentication is scheduled. 'kFinished' indicates the authentication is completed.

        :param authentication_status: The authentication_status of this ProtectionSourceNodeRegistrationInfo.
        :type: str
        """
        allowed_values = ["kPending", "kScheduled", "kFinished"]
        if authentication_status not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_status` ({0}), must be one of {1}"
                .format(authentication_status, allowed_values)
            )

        self._authentication_status = authentication_status

    @property
    def environments(self):
        """
        Gets the environments of this ProtectionSourceNodeRegistrationInfo.
        Specifies a list of applications environment that are registered with this Protection Source such as 'kSQL'. Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :return: The environments of this ProtectionSourceNodeRegistrationInfo.
        :rtype: list[str]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """
        Sets the environments of this ProtectionSourceNodeRegistrationInfo.
        Specifies a list of applications environment that are registered with this Protection Source such as 'kSQL'. Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.

        :param environments: The environments of this ProtectionSourceNodeRegistrationInfo.
        :type: list[str]
        """
        allowed_values = ["kVMware", "kSQL", "kView", "kPuppeteer", "kPhysical", "kPure", "kNetapp", "kGenericNas", "kHyperV", "kAcropolis", "kAzure"]
        if environments not in allowed_values:
            raise ValueError(
                "Invalid value for `environments` ({0}), must be one of {1}"
                .format(environments, allowed_values)
            )

        self._environments = environments

    @property
    def minimum_free_space_gb(self):
        """
        Gets the minimum_free_space_gb of this ProtectionSourceNodeRegistrationInfo.
        Specifies the minimum free space in GiB of the space expected to be available on the datastore where the virtual disks of the VM being backed up. If the amount of free space(in GiB) is lower than the value given by this field, backup will be aborted. Note that this field is applicable only to 'kVMware' type of environments.

        :return: The minimum_free_space_gb of this ProtectionSourceNodeRegistrationInfo.
        :rtype: int
        """
        return self._minimum_free_space_gb

    @minimum_free_space_gb.setter
    def minimum_free_space_gb(self, minimum_free_space_gb):
        """
        Sets the minimum_free_space_gb of this ProtectionSourceNodeRegistrationInfo.
        Specifies the minimum free space in GiB of the space expected to be available on the datastore where the virtual disks of the VM being backed up. If the amount of free space(in GiB) is lower than the value given by this field, backup will be aborted. Note that this field is applicable only to 'kVMware' type of environments.

        :param minimum_free_space_gb: The minimum_free_space_gb of this ProtectionSourceNodeRegistrationInfo.
        :type: int
        """

        self._minimum_free_space_gb = minimum_free_space_gb

    @property
    def nas_mount_credentials(self):
        """
        Gets the nas_mount_credentials of this ProtectionSourceNodeRegistrationInfo.


        :return: The nas_mount_credentials of this ProtectionSourceNodeRegistrationInfo.
        :rtype: ProtectionSourceNodeRegistrationInfoNasMountCredentials
        """
        return self._nas_mount_credentials

    @nas_mount_credentials.setter
    def nas_mount_credentials(self, nas_mount_credentials):
        """
        Sets the nas_mount_credentials of this ProtectionSourceNodeRegistrationInfo.


        :param nas_mount_credentials: The nas_mount_credentials of this ProtectionSourceNodeRegistrationInfo.
        :type: ProtectionSourceNodeRegistrationInfoNasMountCredentials
        """

        self._nas_mount_credentials = nas_mount_credentials

    @property
    def password(self):
        """
        Gets the password of this ProtectionSourceNodeRegistrationInfo.
        Specifies password of the username to access the target source.

        :return: The password of this ProtectionSourceNodeRegistrationInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ProtectionSourceNodeRegistrationInfo.
        Specifies password of the username to access the target source.

        :param password: The password of this ProtectionSourceNodeRegistrationInfo.
        :type: str
        """

        self._password = password

    @property
    def refresh_error_message(self):
        """
        Gets the refresh_error_message of this ProtectionSourceNodeRegistrationInfo.
        Specifies a message if there was any error encountered during the last rebuild of the Protection Source tree. If there was no error during the last rebuild, this field is reset.

        :return: The refresh_error_message of this ProtectionSourceNodeRegistrationInfo.
        :rtype: str
        """
        return self._refresh_error_message

    @refresh_error_message.setter
    def refresh_error_message(self, refresh_error_message):
        """
        Sets the refresh_error_message of this ProtectionSourceNodeRegistrationInfo.
        Specifies a message if there was any error encountered during the last rebuild of the Protection Source tree. If there was no error during the last rebuild, this field is reset.

        :param refresh_error_message: The refresh_error_message of this ProtectionSourceNodeRegistrationInfo.
        :type: str
        """

        self._refresh_error_message = refresh_error_message

    @property
    def refresh_time_usecs(self):
        """
        Gets the refresh_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        Specifies the Unix epoch time (in microseconds) when the Protection Source tree was most recently fetched and built.

        :return: The refresh_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        :rtype: int
        """
        return self._refresh_time_usecs

    @refresh_time_usecs.setter
    def refresh_time_usecs(self, refresh_time_usecs):
        """
        Sets the refresh_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        Specifies the Unix epoch time (in microseconds) when the Protection Source tree was most recently fetched and built.

        :param refresh_time_usecs: The refresh_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        :type: int
        """

        self._refresh_time_usecs = refresh_time_usecs

    @property
    def registration_time_usecs(self):
        """
        Gets the registration_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        Specifies the Unix epoch time (in microseconds) when the Protection Source was registered.

        :return: The registration_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        :rtype: int
        """
        return self._registration_time_usecs

    @registration_time_usecs.setter
    def registration_time_usecs(self, registration_time_usecs):
        """
        Sets the registration_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        Specifies the Unix epoch time (in microseconds) when the Protection Source was registered.

        :param registration_time_usecs: The registration_time_usecs of this ProtectionSourceNodeRegistrationInfo.
        :type: int
        """

        self._registration_time_usecs = registration_time_usecs

    @property
    def throttling_policy(self):
        """
        Gets the throttling_policy of this ProtectionSourceNodeRegistrationInfo.
        Specifies the throttling policy that should be applied to all datastores under this registered Protection Source.

        :return: The throttling_policy of this ProtectionSourceNodeRegistrationInfo.
        :rtype: ThrottlingPolicy
        """
        return self._throttling_policy

    @throttling_policy.setter
    def throttling_policy(self, throttling_policy):
        """
        Sets the throttling_policy of this ProtectionSourceNodeRegistrationInfo.
        Specifies the throttling policy that should be applied to all datastores under this registered Protection Source.

        :param throttling_policy: The throttling_policy of this ProtectionSourceNodeRegistrationInfo.
        :type: ThrottlingPolicy
        """

        self._throttling_policy = throttling_policy

    @property
    def throttling_policy_overrides(self):
        """
        Gets the throttling_policy_overrides of this ProtectionSourceNodeRegistrationInfo.
        Specifies a list of Throttling Policy for datastores that override the common throttling policy specified for the registered Protection Source. For datastores not in this list, common policy will still apply.

        :return: The throttling_policy_overrides of this ProtectionSourceNodeRegistrationInfo.
        :rtype: list[ThrottlingPolicyOverride]
        """
        return self._throttling_policy_overrides

    @throttling_policy_overrides.setter
    def throttling_policy_overrides(self, throttling_policy_overrides):
        """
        Sets the throttling_policy_overrides of this ProtectionSourceNodeRegistrationInfo.
        Specifies a list of Throttling Policy for datastores that override the common throttling policy specified for the registered Protection Source. For datastores not in this list, common policy will still apply.

        :param throttling_policy_overrides: The throttling_policy_overrides of this ProtectionSourceNodeRegistrationInfo.
        :type: list[ThrottlingPolicyOverride]
        """

        self._throttling_policy_overrides = throttling_policy_overrides

    @property
    def username(self):
        """
        Gets the username of this ProtectionSourceNodeRegistrationInfo.
        Specifies username to access the target source.

        :return: The username of this ProtectionSourceNodeRegistrationInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ProtectionSourceNodeRegistrationInfo.
        Specifies username to access the target source.

        :param username: The username of this ProtectionSourceNodeRegistrationInfo.
        :type: str
        """

        self._username = username

    @property
    def warning_messages(self):
        """
        Gets the warning_messages of this ProtectionSourceNodeRegistrationInfo.
        Though the registration may succeed, warning messages imply the host environment requires some cleanup or fixing.

        :return: The warning_messages of this ProtectionSourceNodeRegistrationInfo.
        :rtype: list[str]
        """
        return self._warning_messages

    @warning_messages.setter
    def warning_messages(self, warning_messages):
        """
        Sets the warning_messages of this ProtectionSourceNodeRegistrationInfo.
        Though the registration may succeed, warning messages imply the host environment requires some cleanup or fixing.

        :param warning_messages: The warning_messages of this ProtectionSourceNodeRegistrationInfo.
        :type: list[str]
        """

        self._warning_messages = warning_messages

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
