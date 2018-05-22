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


class Alert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alert_category=None, alert_code=None, alert_document=None, alert_state=None, alert_type=None, dedup_count=None, dedup_timestamps=None, first_timestamp_usecs=None, id=None, latest_timestamp_usecs=None, property_list=None, resolution_details=None, severity=None, suppression_id=None):
        """
        Alert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alert_category': 'str',
            'alert_code': 'str',
            'alert_document': 'AlertDocument',
            'alert_state': 'str',
            'alert_type': 'int',
            'dedup_count': 'int',
            'dedup_timestamps': 'list[int]',
            'first_timestamp_usecs': 'int',
            'id': 'str',
            'latest_timestamp_usecs': 'int',
            'property_list': 'list[AlertProperty]',
            'resolution_details': 'AlertResolutionDetails',
            'severity': 'str',
            'suppression_id': 'int'
        }

        self.attribute_map = {
            'alert_category': 'alertCategory',
            'alert_code': 'alertCode',
            'alert_document': 'alertDocument',
            'alert_state': 'alertState',
            'alert_type': 'alertType',
            'dedup_count': 'dedupCount',
            'dedup_timestamps': 'dedupTimestamps',
            'first_timestamp_usecs': 'firstTimestampUsecs',
            'id': 'id',
            'latest_timestamp_usecs': 'latestTimestampUsecs',
            'property_list': 'propertyList',
            'resolution_details': 'resolutionDetails',
            'severity': 'severity',
            'suppression_id': 'suppressionId'
        }

        self._alert_category = alert_category
        self._alert_code = alert_code
        self._alert_document = alert_document
        self._alert_state = alert_state
        self._alert_type = alert_type
        self._dedup_count = dedup_count
        self._dedup_timestamps = dedup_timestamps
        self._first_timestamp_usecs = first_timestamp_usecs
        self._id = id
        self._latest_timestamp_usecs = latest_timestamp_usecs
        self._property_list = property_list
        self._resolution_details = resolution_details
        self._severity = severity
        self._suppression_id = suppression_id

    @property
    def alert_category(self):
        """
        Gets the alert_category of this Alert.
        Specifies the category for the Alert such as 'kDisk', 'kNode', 'kCluster\", etc.

        :return: The alert_category of this Alert.
        :rtype: str
        """
        return self._alert_category

    @alert_category.setter
    def alert_category(self, alert_category):
        """
        Sets the alert_category of this Alert.
        Specifies the category for the Alert such as 'kDisk', 'kNode', 'kCluster\", etc.

        :param alert_category: The alert_category of this Alert.
        :type: str
        """
        allowed_values = ["kDisk", "kNode", "kCluster", "kNodeHealth", "kClusterHealth", "kBackupRestore", "kEncryption", "kArchivalRestore"]
        if alert_category not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_category` ({0}), must be one of {1}"
                .format(alert_category, allowed_values)
            )

        self._alert_category = alert_category

    @property
    def alert_code(self):
        """
        Gets the alert_code of this Alert.
        Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the next 3 digits is the id of the Alert Category (e.g. 002 for 'kNode') and the last 5 digits is the id of the Alert Type (e.g. 00014 for 'kNodeHighCpuUsage').

        :return: The alert_code of this Alert.
        :rtype: str
        """
        return self._alert_code

    @alert_code.setter
    def alert_code(self, alert_code):
        """
        Sets the alert_code of this Alert.
        Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the next 3 digits is the id of the Alert Category (e.g. 002 for 'kNode') and the last 5 digits is the id of the Alert Type (e.g. 00014 for 'kNodeHighCpuUsage').

        :param alert_code: The alert_code of this Alert.
        :type: str
        """

        self._alert_code = alert_code

    @property
    def alert_document(self):
        """
        Gets the alert_document of this Alert.
        Specifies documentation about the Alert such as name, description, cause and how to resolve the Alert.

        :return: The alert_document of this Alert.
        :rtype: AlertDocument
        """
        return self._alert_document

    @alert_document.setter
    def alert_document(self, alert_document):
        """
        Sets the alert_document of this Alert.
        Specifies documentation about the Alert such as name, description, cause and how to resolve the Alert.

        :param alert_document: The alert_document of this Alert.
        :type: AlertDocument
        """

        self._alert_document = alert_document

    @property
    def alert_state(self):
        """
        Gets the alert_state of this Alert.
        Specifies the current state of the Alert: 'kOpen' or 'kResolved'.

        :return: The alert_state of this Alert.
        :rtype: str
        """
        return self._alert_state

    @alert_state.setter
    def alert_state(self, alert_state):
        """
        Sets the alert_state of this Alert.
        Specifies the current state of the Alert: 'kOpen' or 'kResolved'.

        :param alert_state: The alert_state of this Alert.
        :type: str
        """
        allowed_values = ["kOpen", "kResolved"]
        if alert_state not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_state` ({0}), must be one of {1}"
                .format(alert_state, allowed_values)
            )

        self._alert_state = alert_state

    @property
    def alert_type(self):
        """
        Gets the alert_type of this Alert.
        Specifies a 5 digit unique digital id for the Alert Type, such as 00014 for 'kNodeHighCpuUsage'. This id is used in alertCode.

        :return: The alert_type of this Alert.
        :rtype: int
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this Alert.
        Specifies a 5 digit unique digital id for the Alert Type, such as 00014 for 'kNodeHighCpuUsage'. This id is used in alertCode.

        :param alert_type: The alert_type of this Alert.
        :type: int
        """

        self._alert_type = alert_type

    @property
    def dedup_count(self):
        """
        Gets the dedup_count of this Alert.
        Provides the total count of duplicated Alerts even if there are more than 25 occurrences.

        :return: The dedup_count of this Alert.
        :rtype: int
        """
        return self._dedup_count

    @dedup_count.setter
    def dedup_count(self, dedup_count):
        """
        Sets the dedup_count of this Alert.
        Provides the total count of duplicated Alerts even if there are more than 25 occurrences.

        :param dedup_count: The dedup_count of this Alert.
        :type: int
        """

        self._dedup_count = dedup_count

    @property
    def dedup_timestamps(self):
        """
        Gets the dedup_timestamps of this Alert.
        Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. 'dedupCount' always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100.

        :return: The dedup_timestamps of this Alert.
        :rtype: list[int]
        """
        return self._dedup_timestamps

    @dedup_timestamps.setter
    def dedup_timestamps(self, dedup_timestamps):
        """
        Sets the dedup_timestamps of this Alert.
        Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. 'dedupCount' always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100.

        :param dedup_timestamps: The dedup_timestamps of this Alert.
        :type: list[int]
        """

        self._dedup_timestamps = dedup_timestamps

    @property
    def first_timestamp_usecs(self):
        """
        Gets the first_timestamp_usecs of this Alert.
        Creation Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert.

        :return: The first_timestamp_usecs of this Alert.
        :rtype: int
        """
        return self._first_timestamp_usecs

    @first_timestamp_usecs.setter
    def first_timestamp_usecs(self, first_timestamp_usecs):
        """
        Sets the first_timestamp_usecs of this Alert.
        Creation Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert.

        :param first_timestamp_usecs: The first_timestamp_usecs of this Alert.
        :type: int
        """

        self._first_timestamp_usecs = first_timestamp_usecs

    @property
    def id(self):
        """
        Gets the id of this Alert.
        Unique id of this Alert.

        :return: The id of this Alert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Alert.
        Unique id of this Alert.

        :param id: The id of this Alert.
        :type: str
        """

        self._id = id

    @property
    def latest_timestamp_usecs(self):
        """
        Gets the latest_timestamp_usecs of this Alert.
        Creation Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert.

        :return: The latest_timestamp_usecs of this Alert.
        :rtype: int
        """
        return self._latest_timestamp_usecs

    @latest_timestamp_usecs.setter
    def latest_timestamp_usecs(self, latest_timestamp_usecs):
        """
        Sets the latest_timestamp_usecs of this Alert.
        Creation Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert.

        :param latest_timestamp_usecs: The latest_timestamp_usecs of this Alert.
        :type: int
        """

        self._latest_timestamp_usecs = latest_timestamp_usecs

    @property
    def property_list(self):
        """
        Gets the property_list of this Alert.
        Array of key-value pairs associated with the Alert. The Cohesity Cluster may autogenerate properties depending on the Alert type. This list includes both autogenerated and specified properties.

        :return: The property_list of this Alert.
        :rtype: list[AlertProperty]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        """
        Sets the property_list of this Alert.
        Array of key-value pairs associated with the Alert. The Cohesity Cluster may autogenerate properties depending on the Alert type. This list includes both autogenerated and specified properties.

        :param property_list: The property_list of this Alert.
        :type: list[AlertProperty]
        """

        self._property_list = property_list

    @property
    def resolution_details(self):
        """
        Gets the resolution_details of this Alert.
        Specifies information about the Alert Resolution such as a summary, id assigned by the Cohesity Cluster, user who resolved the Alerts, etc.

        :return: The resolution_details of this Alert.
        :rtype: AlertResolutionDetails
        """
        return self._resolution_details

    @resolution_details.setter
    def resolution_details(self, resolution_details):
        """
        Sets the resolution_details of this Alert.
        Specifies information about the Alert Resolution such as a summary, id assigned by the Cohesity Cluster, user who resolved the Alerts, etc.

        :param resolution_details: The resolution_details of this Alert.
        :type: AlertResolutionDetails
        """

        self._resolution_details = resolution_details

    @property
    def severity(self):
        """
        Gets the severity of this Alert.
        Specifies the severity level of an Alert. 'kCritical' means immediate action is required because the system detects a serious problem. 'kWarning' means action is required but the affected functionality is still working. 'kInfo' means no action is required and the Alert provides an informational message.

        :return: The severity of this Alert.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Alert.
        Specifies the severity level of an Alert. 'kCritical' means immediate action is required because the system detects a serious problem. 'kWarning' means action is required but the affected functionality is still working. 'kInfo' means no action is required and the Alert provides an informational message.

        :param severity: The severity of this Alert.
        :type: str
        """
        allowed_values = ["kCritical", "kWarning", "kInfo"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def suppression_id(self):
        """
        Gets the suppression_id of this Alert.
        Unique id generated when the Alert is suppressed by the admin.

        :return: The suppression_id of this Alert.
        :rtype: int
        """
        return self._suppression_id

    @suppression_id.setter
    def suppression_id(self, suppression_id):
        """
        Sets the suppression_id of this Alert.
        Unique id generated when the Alert is suppressed by the admin.

        :param suppression_id: The suppression_id of this Alert.
        :type: int
        """

        self._suppression_id = suppression_id

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
