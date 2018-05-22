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


class ProtectionPolicyFullSchedulingPolicyMonthlySchedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, day=None, day_count=None):
        """
        ProtectionPolicyFullSchedulingPolicyMonthlySchedule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'day': 'str',
            'day_count': 'str'
        }

        self.attribute_map = {
            'day': 'day',
            'day_count': 'dayCount'
        }

        self._day = day
        self._day_count = day_count

    @property
    def day(self):
        """
        Gets the day of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        Specifies the day of the week (such as 'kMonday') to start the Job Run. Used with day count to define the day in the month to start the Job Run. Specifies a day in a week such as 'kSunday', 'kMonday', etc.

        :return: The day of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """
        Sets the day of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        Specifies the day of the week (such as 'kMonday') to start the Job Run. Used with day count to define the day in the month to start the Job Run. Specifies a day in a week such as 'kSunday', 'kMonday', etc.

        :param day: The day of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        :type: str
        """
        allowed_values = ["kSunday", "kMonday", "kTuesday", "kWednesday", "kThursday", "kFriday", "kSaturday"]
        if day not in allowed_values:
            raise ValueError(
                "Invalid value for `day` ({0}), must be one of {1}"
                .format(day, allowed_values)
            )

        self._day = day

    @property
    def day_count(self):
        """
        Gets the day_count of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        Specifies the day count in the month (such as 'kThird') to start the Job Run. Used in combination with day to define the day in the month to start the Job Run. Specifies the day count in the month to start the backup. For example if day count is set to 'kThird' and day is set to 'kMonday', a backup is performed on the third Monday of every month.

        :return: The day_count of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        :rtype: str
        """
        return self._day_count

    @day_count.setter
    def day_count(self, day_count):
        """
        Sets the day_count of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        Specifies the day count in the month (such as 'kThird') to start the Job Run. Used in combination with day to define the day in the month to start the Job Run. Specifies the day count in the month to start the backup. For example if day count is set to 'kThird' and day is set to 'kMonday', a backup is performed on the third Monday of every month.

        :param day_count: The day_count of this ProtectionPolicyFullSchedulingPolicyMonthlySchedule.
        :type: str
        """
        allowed_values = ["kFirst", "kSecond", "kThird", "kFourth", "kLast"]
        if day_count not in allowed_values:
            raise ValueError(
                "Invalid value for `day_count` ({0}), must be one of {1}"
                .format(day_count, allowed_values)
            )

        self._day_count = day_count

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
