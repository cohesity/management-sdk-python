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


class UpdateProtectionJobRun(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, copy_run_targets=None, expiry_time_usecs=None, job_uid=None, run_start_time_usecs=None, source_ids=None):
        """
        UpdateProtectionJobRun - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'copy_run_targets': 'list[RunJobSnapshotTarget]',
            'expiry_time_usecs': 'int',
            'job_uid': 'UpdateProtectionJobRunJobUid',
            'run_start_time_usecs': 'int',
            'source_ids': 'list[int]'
        }

        self.attribute_map = {
            'copy_run_targets': 'copyRunTargets',
            'expiry_time_usecs': 'expiryTimeUsecs',
            'job_uid': 'jobUid',
            'run_start_time_usecs': 'runStartTimeUsecs',
            'source_ids': 'sourceIds'
        }

        self._copy_run_targets = copy_run_targets
        self._expiry_time_usecs = expiry_time_usecs
        self._job_uid = job_uid
        self._run_start_time_usecs = run_start_time_usecs
        self._source_ids = source_ids

    @property
    def copy_run_targets(self):
        """
        Gets the copy_run_targets of this UpdateProtectionJobRun.
        Specifies the retention for archival, replication or extended local retention.

        :return: The copy_run_targets of this UpdateProtectionJobRun.
        :rtype: list[RunJobSnapshotTarget]
        """
        return self._copy_run_targets

    @copy_run_targets.setter
    def copy_run_targets(self, copy_run_targets):
        """
        Sets the copy_run_targets of this UpdateProtectionJobRun.
        Specifies the retention for archival, replication or extended local retention.

        :param copy_run_targets: The copy_run_targets of this UpdateProtectionJobRun.
        :type: list[RunJobSnapshotTarget]
        """

        self._copy_run_targets = copy_run_targets

    @property
    def expiry_time_usecs(self):
        """
        Gets the expiry_time_usecs of this UpdateProtectionJobRun.
        Specifies a new expiration time as a Unix epoch Timestamp (in microseconds). This expiration time defines the retention period for the snapshot. After an expiration time for a Job Run is reached, the Job Run and the snapshot captured by this Job Run are deleted. If 0 is specified, the Job Run and the snapshot are immediately deleted.

        :return: The expiry_time_usecs of this UpdateProtectionJobRun.
        :rtype: int
        """
        return self._expiry_time_usecs

    @expiry_time_usecs.setter
    def expiry_time_usecs(self, expiry_time_usecs):
        """
        Sets the expiry_time_usecs of this UpdateProtectionJobRun.
        Specifies a new expiration time as a Unix epoch Timestamp (in microseconds). This expiration time defines the retention period for the snapshot. After an expiration time for a Job Run is reached, the Job Run and the snapshot captured by this Job Run are deleted. If 0 is specified, the Job Run and the snapshot are immediately deleted.

        :param expiry_time_usecs: The expiry_time_usecs of this UpdateProtectionJobRun.
        :type: int
        """

        self._expiry_time_usecs = expiry_time_usecs

    @property
    def job_uid(self):
        """
        Gets the job_uid of this UpdateProtectionJobRun.


        :return: The job_uid of this UpdateProtectionJobRun.
        :rtype: UpdateProtectionJobRunJobUid
        """
        return self._job_uid

    @job_uid.setter
    def job_uid(self, job_uid):
        """
        Sets the job_uid of this UpdateProtectionJobRun.


        :param job_uid: The job_uid of this UpdateProtectionJobRun.
        :type: UpdateProtectionJobRunJobUid
        """

        self._job_uid = job_uid

    @property
    def run_start_time_usecs(self):
        """
        Gets the run_start_time_usecs of this UpdateProtectionJobRun.
        Specifies the start time of the Job Run to update. The start time is specified as a Unix epoch Timestamp (in microseconds). This uniquely identifies a snapshot. This parameter is required.

        :return: The run_start_time_usecs of this UpdateProtectionJobRun.
        :rtype: int
        """
        return self._run_start_time_usecs

    @run_start_time_usecs.setter
    def run_start_time_usecs(self, run_start_time_usecs):
        """
        Sets the run_start_time_usecs of this UpdateProtectionJobRun.
        Specifies the start time of the Job Run to update. The start time is specified as a Unix epoch Timestamp (in microseconds). This uniquely identifies a snapshot. This parameter is required.

        :param run_start_time_usecs: The run_start_time_usecs of this UpdateProtectionJobRun.
        :type: int
        """

        self._run_start_time_usecs = run_start_time_usecs

    @property
    def source_ids(self):
        """
        Gets the source_ids of this UpdateProtectionJobRun.
        Ids of the Protection Sources. If this is specified, retention time will only be updated for the sources specified.

        :return: The source_ids of this UpdateProtectionJobRun.
        :rtype: list[int]
        """
        return self._source_ids

    @source_ids.setter
    def source_ids(self, source_ids):
        """
        Sets the source_ids of this UpdateProtectionJobRun.
        Ids of the Protection Sources. If this is specified, retention time will only be updated for the sources specified.

        :param source_ids: The source_ids of this UpdateProtectionJobRun.
        :type: list[int]
        """

        self._source_ids = source_ids

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
