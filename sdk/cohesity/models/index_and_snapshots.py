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


class IndexAndSnapshots(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, archive_task_uid=None, end_time_usecs=None, remote_protection_job_uid=None, start_time_usecs=None, view_box_id=None):
        """
        IndexAndSnapshots - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'archive_task_uid': 'IndexAndSnapshotsArchiveTaskUid',
            'end_time_usecs': 'int',
            'remote_protection_job_uid': 'IndexAndSnapshotsRemoteProtectionJobUid',
            'start_time_usecs': 'int',
            'view_box_id': 'int'
        }

        self.attribute_map = {
            'archive_task_uid': 'archiveTaskUid',
            'end_time_usecs': 'endTimeUsecs',
            'remote_protection_job_uid': 'remoteProtectionJobUid',
            'start_time_usecs': 'startTimeUsecs',
            'view_box_id': 'viewBoxId'
        }

        self._archive_task_uid = archive_task_uid
        self._end_time_usecs = end_time_usecs
        self._remote_protection_job_uid = remote_protection_job_uid
        self._start_time_usecs = start_time_usecs
        self._view_box_id = view_box_id

    @property
    def archive_task_uid(self):
        """
        Gets the archive_task_uid of this IndexAndSnapshots.


        :return: The archive_task_uid of this IndexAndSnapshots.
        :rtype: IndexAndSnapshotsArchiveTaskUid
        """
        return self._archive_task_uid

    @archive_task_uid.setter
    def archive_task_uid(self, archive_task_uid):
        """
        Sets the archive_task_uid of this IndexAndSnapshots.


        :param archive_task_uid: The archive_task_uid of this IndexAndSnapshots.
        :type: IndexAndSnapshotsArchiveTaskUid
        """

        self._archive_task_uid = archive_task_uid

    @property
    def end_time_usecs(self):
        """
        Gets the end_time_usecs of this IndexAndSnapshots.
        Specifies the end time as a Unix epoch Timestamp (in microseconds). If set, only index and Snapshots for Protection Job Runs that started before the specified end time are restored.

        :return: The end_time_usecs of this IndexAndSnapshots.
        :rtype: int
        """
        return self._end_time_usecs

    @end_time_usecs.setter
    def end_time_usecs(self, end_time_usecs):
        """
        Sets the end_time_usecs of this IndexAndSnapshots.
        Specifies the end time as a Unix epoch Timestamp (in microseconds). If set, only index and Snapshots for Protection Job Runs that started before the specified end time are restored.

        :param end_time_usecs: The end_time_usecs of this IndexAndSnapshots.
        :type: int
        """

        self._end_time_usecs = end_time_usecs

    @property
    def remote_protection_job_uid(self):
        """
        Gets the remote_protection_job_uid of this IndexAndSnapshots.


        :return: The remote_protection_job_uid of this IndexAndSnapshots.
        :rtype: IndexAndSnapshotsRemoteProtectionJobUid
        """
        return self._remote_protection_job_uid

    @remote_protection_job_uid.setter
    def remote_protection_job_uid(self, remote_protection_job_uid):
        """
        Sets the remote_protection_job_uid of this IndexAndSnapshots.


        :param remote_protection_job_uid: The remote_protection_job_uid of this IndexAndSnapshots.
        :type: IndexAndSnapshotsRemoteProtectionJobUid
        """

        self._remote_protection_job_uid = remote_protection_job_uid

    @property
    def start_time_usecs(self):
        """
        Gets the start_time_usecs of this IndexAndSnapshots.
        Specifies the start time as a Unix epoch Timestamp (in microseconds). If set, only the index and Snapshots for Protection Job Runs that started after the specified start time are restored.

        :return: The start_time_usecs of this IndexAndSnapshots.
        :rtype: int
        """
        return self._start_time_usecs

    @start_time_usecs.setter
    def start_time_usecs(self, start_time_usecs):
        """
        Sets the start_time_usecs of this IndexAndSnapshots.
        Specifies the start time as a Unix epoch Timestamp (in microseconds). If set, only the index and Snapshots for Protection Job Runs that started after the specified start time are restored.

        :param start_time_usecs: The start_time_usecs of this IndexAndSnapshots.
        :type: int
        """

        self._start_time_usecs = start_time_usecs

    @property
    def view_box_id(self):
        """
        Gets the view_box_id of this IndexAndSnapshots.
        Specifies the id of the local Storage Domain (View Box) where the index and the Snapshot will be restored to.

        :return: The view_box_id of this IndexAndSnapshots.
        :rtype: int
        """
        return self._view_box_id

    @view_box_id.setter
    def view_box_id(self, view_box_id):
        """
        Sets the view_box_id of this IndexAndSnapshots.
        Specifies the id of the local Storage Domain (View Box) where the index and the Snapshot will be restored to.

        :param view_box_id: The view_box_id of this IndexAndSnapshots.
        :type: int
        """

        self._view_box_id = view_box_id

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
