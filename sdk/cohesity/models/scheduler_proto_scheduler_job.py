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


class SchedulerProtoSchedulerJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, enable_recurring_email=None, id=None, name=None, schedule_job_parameters=None, schedules=None, type=None):
        """
        SchedulerProtoSchedulerJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enable_recurring_email': 'bool',
            'id': 'int',
            'name': 'str',
            'schedule_job_parameters': 'SchedulerProtoSchedulerJobScheduleJobParameters',
            'schedules': 'list[SchedulerProtoSchedulerJobSchedule]',
            'type': 'str'
        }

        self.attribute_map = {
            'enable_recurring_email': 'enableRecurringEmail',
            'id': 'id',
            'name': 'name',
            'schedule_job_parameters': 'scheduleJobParameters',
            'schedules': 'schedules',
            'type': 'type'
        }

        self._enable_recurring_email = enable_recurring_email
        self._id = id
        self._name = name
        self._schedule_job_parameters = schedule_job_parameters
        self._schedules = schedules
        self._type = type

    @property
    def enable_recurring_email(self):
        """
        Gets the enable_recurring_email of this SchedulerProtoSchedulerJob.
        The boolean which specifies if this job is to be scheduled or not.

        :return: The enable_recurring_email of this SchedulerProtoSchedulerJob.
        :rtype: bool
        """
        return self._enable_recurring_email

    @enable_recurring_email.setter
    def enable_recurring_email(self, enable_recurring_email):
        """
        Sets the enable_recurring_email of this SchedulerProtoSchedulerJob.
        The boolean which specifies if this job is to be scheduled or not.

        :param enable_recurring_email: The enable_recurring_email of this SchedulerProtoSchedulerJob.
        :type: bool
        """

        self._enable_recurring_email = enable_recurring_email

    @property
    def id(self):
        """
        Gets the id of this SchedulerProtoSchedulerJob.
        The unique id for the scheduled job assigned by the cluster.

        :return: The id of this SchedulerProtoSchedulerJob.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchedulerProtoSchedulerJob.
        The unique id for the scheduled job assigned by the cluster.

        :param id: The id of this SchedulerProtoSchedulerJob.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SchedulerProtoSchedulerJob.
        The name of the scheduled job given by the user.

        :return: The name of this SchedulerProtoSchedulerJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SchedulerProtoSchedulerJob.
        The name of the scheduled job given by the user.

        :param name: The name of this SchedulerProtoSchedulerJob.
        :type: str
        """

        self._name = name

    @property
    def schedule_job_parameters(self):
        """
        Gets the schedule_job_parameters of this SchedulerProtoSchedulerJob.


        :return: The schedule_job_parameters of this SchedulerProtoSchedulerJob.
        :rtype: SchedulerProtoSchedulerJobScheduleJobParameters
        """
        return self._schedule_job_parameters

    @schedule_job_parameters.setter
    def schedule_job_parameters(self, schedule_job_parameters):
        """
        Sets the schedule_job_parameters of this SchedulerProtoSchedulerJob.


        :param schedule_job_parameters: The schedule_job_parameters of this SchedulerProtoSchedulerJob.
        :type: SchedulerProtoSchedulerJobScheduleJobParameters
        """

        self._schedule_job_parameters = schedule_job_parameters

    @property
    def schedules(self):
        """
        Gets the schedules of this SchedulerProtoSchedulerJob.


        :return: The schedules of this SchedulerProtoSchedulerJob.
        :rtype: list[SchedulerProtoSchedulerJobSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this SchedulerProtoSchedulerJob.


        :param schedules: The schedules of this SchedulerProtoSchedulerJob.
        :type: list[SchedulerProtoSchedulerJobSchedule]
        """

        self._schedules = schedules

    @property
    def type(self):
        """
        Gets the type of this SchedulerProtoSchedulerJob.
        Specifies the type of the job. The enum which defines the Job type of the job.

        :return: The type of this SchedulerProtoSchedulerJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SchedulerProtoSchedulerJob.
        Specifies the type of the job. The enum which defines the Job type of the job.

        :param type: The type of this SchedulerProtoSchedulerJob.
        :type: str
        """
        allowed_values = ["kSCHEDULER_JOB_REPORT"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
