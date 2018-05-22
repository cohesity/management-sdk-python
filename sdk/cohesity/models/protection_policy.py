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


class ProtectionPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, blackout_periods=None, cloud_deploy_policies=None, days_to_keep=None, days_to_keep_log=None, days_to_keep_system=None, description=None, extended_retention_policies=None, full_scheduling_policy=None, id=None, incremental_scheduling_policy=None, last_modified_time_msecs=None, log_scheduling_policy=None, name=None, retries=None, retry_interval_mins=None, skip_interval_mins=None, snapshot_archival_copy_policies=None, snapshot_replication_copy_policies=None, system_scheduling_policy=None):
        """
        ProtectionPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'blackout_periods': 'list[BlackoutPeriod]',
            'cloud_deploy_policies': 'list[SnapshotCloudCopyPolicy]',
            'days_to_keep': 'int',
            'days_to_keep_log': 'int',
            'days_to_keep_system': 'int',
            'description': 'str',
            'extended_retention_policies': 'list[ExtendedRetentionPolicy]',
            'full_scheduling_policy': 'ProtectionPolicyFullSchedulingPolicy',
            'id': 'str',
            'incremental_scheduling_policy': 'ProtectionPolicyIncrementalSchedulingPolicy',
            'last_modified_time_msecs': 'int',
            'log_scheduling_policy': 'SchedulingPolicy',
            'name': 'str',
            'retries': 'int',
            'retry_interval_mins': 'int',
            'skip_interval_mins': 'int',
            'snapshot_archival_copy_policies': 'list[SnapshotArchivalCopyPolicy]',
            'snapshot_replication_copy_policies': 'list[SnapshotReplicationCopyPolicy]',
            'system_scheduling_policy': 'SchedulingPolicy'
        }

        self.attribute_map = {
            'blackout_periods': 'blackoutPeriods',
            'cloud_deploy_policies': 'cloudDeployPolicies',
            'days_to_keep': 'daysToKeep',
            'days_to_keep_log': 'daysToKeepLog',
            'days_to_keep_system': 'daysToKeepSystem',
            'description': 'description',
            'extended_retention_policies': 'extendedRetentionPolicies',
            'full_scheduling_policy': 'fullSchedulingPolicy',
            'id': 'id',
            'incremental_scheduling_policy': 'incrementalSchedulingPolicy',
            'last_modified_time_msecs': 'lastModifiedTimeMsecs',
            'log_scheduling_policy': 'logSchedulingPolicy',
            'name': 'name',
            'retries': 'retries',
            'retry_interval_mins': 'retryIntervalMins',
            'skip_interval_mins': 'skipIntervalMins',
            'snapshot_archival_copy_policies': 'snapshotArchivalCopyPolicies',
            'snapshot_replication_copy_policies': 'snapshotReplicationCopyPolicies',
            'system_scheduling_policy': 'systemSchedulingPolicy'
        }

        self._blackout_periods = blackout_periods
        self._cloud_deploy_policies = cloud_deploy_policies
        self._days_to_keep = days_to_keep
        self._days_to_keep_log = days_to_keep_log
        self._days_to_keep_system = days_to_keep_system
        self._description = description
        self._extended_retention_policies = extended_retention_policies
        self._full_scheduling_policy = full_scheduling_policy
        self._id = id
        self._incremental_scheduling_policy = incremental_scheduling_policy
        self._last_modified_time_msecs = last_modified_time_msecs
        self._log_scheduling_policy = log_scheduling_policy
        self._name = name
        self._retries = retries
        self._retry_interval_mins = retry_interval_mins
        self._skip_interval_mins = skip_interval_mins
        self._snapshot_archival_copy_policies = snapshot_archival_copy_policies
        self._snapshot_replication_copy_policies = snapshot_replication_copy_policies
        self._system_scheduling_policy = system_scheduling_policy

    @property
    def blackout_periods(self):
        """
        Gets the blackout_periods of this ProtectionPolicy.
        If specified, this field defines black periods when new Job Runs are not started. If a Job Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod.

        :return: The blackout_periods of this ProtectionPolicy.
        :rtype: list[BlackoutPeriod]
        """
        return self._blackout_periods

    @blackout_periods.setter
    def blackout_periods(self, blackout_periods):
        """
        Sets the blackout_periods of this ProtectionPolicy.
        If specified, this field defines black periods when new Job Runs are not started. If a Job Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod.

        :param blackout_periods: The blackout_periods of this ProtectionPolicy.
        :type: list[BlackoutPeriod]
        """

        self._blackout_periods = blackout_periods

    @property
    def cloud_deploy_policies(self):
        """
        Gets the cloud_deploy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to Cloud. CloudDeploy target where backup snapshots may be converted and stored. It also defines the retention of copied Snapshots on the Cloud.

        :return: The cloud_deploy_policies of this ProtectionPolicy.
        :rtype: list[SnapshotCloudCopyPolicy]
        """
        return self._cloud_deploy_policies

    @cloud_deploy_policies.setter
    def cloud_deploy_policies(self, cloud_deploy_policies):
        """
        Sets the cloud_deploy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to Cloud. CloudDeploy target where backup snapshots may be converted and stored. It also defines the retention of copied Snapshots on the Cloud.

        :param cloud_deploy_policies: The cloud_deploy_policies of this ProtectionPolicy.
        :type: list[SnapshotCloudCopyPolicy]
        """

        self._cloud_deploy_policies = cloud_deploy_policies

    @property
    def days_to_keep(self):
        """
        Gets the days_to_keep of this ProtectionPolicy.
        Specifies how many days to retain Snapshots on the Cohesity Cluster.

        :return: The days_to_keep of this ProtectionPolicy.
        :rtype: int
        """
        return self._days_to_keep

    @days_to_keep.setter
    def days_to_keep(self, days_to_keep):
        """
        Sets the days_to_keep of this ProtectionPolicy.
        Specifies how many days to retain Snapshots on the Cohesity Cluster.

        :param days_to_keep: The days_to_keep of this ProtectionPolicy.
        :type: int
        """

        self._days_to_keep = days_to_keep

    @property
    def days_to_keep_log(self):
        """
        Gets the days_to_keep_log of this ProtectionPolicy.
        Specifies the number of days to retain log run if Log Schedule exists.

        :return: The days_to_keep_log of this ProtectionPolicy.
        :rtype: int
        """
        return self._days_to_keep_log

    @days_to_keep_log.setter
    def days_to_keep_log(self, days_to_keep_log):
        """
        Sets the days_to_keep_log of this ProtectionPolicy.
        Specifies the number of days to retain log run if Log Schedule exists.

        :param days_to_keep_log: The days_to_keep_log of this ProtectionPolicy.
        :type: int
        """

        self._days_to_keep_log = days_to_keep_log

    @property
    def days_to_keep_system(self):
        """
        Gets the days_to_keep_system of this ProtectionPolicy.
        Specifies the number of days to retain system backups made for bare metal recovery. This field is applicable if systemSchedulingPolicy is specified.

        :return: The days_to_keep_system of this ProtectionPolicy.
        :rtype: int
        """
        return self._days_to_keep_system

    @days_to_keep_system.setter
    def days_to_keep_system(self, days_to_keep_system):
        """
        Sets the days_to_keep_system of this ProtectionPolicy.
        Specifies the number of days to retain system backups made for bare metal recovery. This field is applicable if systemSchedulingPolicy is specified.

        :param days_to_keep_system: The days_to_keep_system of this ProtectionPolicy.
        :type: int
        """

        self._days_to_keep_system = days_to_keep_system

    @property
    def description(self):
        """
        Gets the description of this ProtectionPolicy.
        Description of the Protection Policy.

        :return: The description of this ProtectionPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProtectionPolicy.
        Description of the Protection Policy.

        :param description: The description of this ProtectionPolicy.
        :type: str
        """

        self._description = description

    @property
    def extended_retention_policies(self):
        """
        Gets the extended_retention_policies of this ProtectionPolicy.
        Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it.

        :return: The extended_retention_policies of this ProtectionPolicy.
        :rtype: list[ExtendedRetentionPolicy]
        """
        return self._extended_retention_policies

    @extended_retention_policies.setter
    def extended_retention_policies(self, extended_retention_policies):
        """
        Sets the extended_retention_policies of this ProtectionPolicy.
        Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it.

        :param extended_retention_policies: The extended_retention_policies of this ProtectionPolicy.
        :type: list[ExtendedRetentionPolicy]
        """

        self._extended_retention_policies = extended_retention_policies

    @property
    def full_scheduling_policy(self):
        """
        Gets the full_scheduling_policy of this ProtectionPolicy.


        :return: The full_scheduling_policy of this ProtectionPolicy.
        :rtype: ProtectionPolicyFullSchedulingPolicy
        """
        return self._full_scheduling_policy

    @full_scheduling_policy.setter
    def full_scheduling_policy(self, full_scheduling_policy):
        """
        Sets the full_scheduling_policy of this ProtectionPolicy.


        :param full_scheduling_policy: The full_scheduling_policy of this ProtectionPolicy.
        :type: ProtectionPolicyFullSchedulingPolicy
        """

        self._full_scheduling_policy = full_scheduling_policy

    @property
    def id(self):
        """
        Gets the id of this ProtectionPolicy.
        Specifies a unique Policy id assigned by the Cohesity Cluster.

        :return: The id of this ProtectionPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProtectionPolicy.
        Specifies a unique Policy id assigned by the Cohesity Cluster.

        :param id: The id of this ProtectionPolicy.
        :type: str
        """

        self._id = id

    @property
    def incremental_scheduling_policy(self):
        """
        Gets the incremental_scheduling_policy of this ProtectionPolicy.


        :return: The incremental_scheduling_policy of this ProtectionPolicy.
        :rtype: ProtectionPolicyIncrementalSchedulingPolicy
        """
        return self._incremental_scheduling_policy

    @incremental_scheduling_policy.setter
    def incremental_scheduling_policy(self, incremental_scheduling_policy):
        """
        Sets the incremental_scheduling_policy of this ProtectionPolicy.


        :param incremental_scheduling_policy: The incremental_scheduling_policy of this ProtectionPolicy.
        :type: ProtectionPolicyIncrementalSchedulingPolicy
        """

        self._incremental_scheduling_policy = incremental_scheduling_policy

    @property
    def last_modified_time_msecs(self):
        """
        Gets the last_modified_time_msecs of this ProtectionPolicy.
        Specifies the epoch time (in milliseconds) when the Protection Policy was last modified.

        :return: The last_modified_time_msecs of this ProtectionPolicy.
        :rtype: int
        """
        return self._last_modified_time_msecs

    @last_modified_time_msecs.setter
    def last_modified_time_msecs(self, last_modified_time_msecs):
        """
        Sets the last_modified_time_msecs of this ProtectionPolicy.
        Specifies the epoch time (in milliseconds) when the Protection Policy was last modified.

        :param last_modified_time_msecs: The last_modified_time_msecs of this ProtectionPolicy.
        :type: int
        """

        self._last_modified_time_msecs = last_modified_time_msecs

    @property
    def log_scheduling_policy(self):
        """
        Gets the log_scheduling_policy of this ProtectionPolicy.
        Specifies the Log backup schedule of a Protection Job and how long log files captured by this schedule are retained on the Cohesity Cluster.

        :return: The log_scheduling_policy of this ProtectionPolicy.
        :rtype: SchedulingPolicy
        """
        return self._log_scheduling_policy

    @log_scheduling_policy.setter
    def log_scheduling_policy(self, log_scheduling_policy):
        """
        Sets the log_scheduling_policy of this ProtectionPolicy.
        Specifies the Log backup schedule of a Protection Job and how long log files captured by this schedule are retained on the Cohesity Cluster.

        :param log_scheduling_policy: The log_scheduling_policy of this ProtectionPolicy.
        :type: SchedulingPolicy
        """

        self._log_scheduling_policy = log_scheduling_policy

    @property
    def name(self):
        """
        Gets the name of this ProtectionPolicy.
        Specifies the name of the Protection Policy.

        :return: The name of this ProtectionPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProtectionPolicy.
        Specifies the name of the Protection Policy.

        :param name: The name of this ProtectionPolicy.
        :type: str
        """

        self._name = name

    @property
    def retries(self):
        """
        Gets the retries of this ProtectionPolicy.
        Specifies the number of times to retry capturing Snapshots before the Job Run fails.

        :return: The retries of this ProtectionPolicy.
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """
        Sets the retries of this ProtectionPolicy.
        Specifies the number of times to retry capturing Snapshots before the Job Run fails.

        :param retries: The retries of this ProtectionPolicy.
        :type: int
        """

        self._retries = retries

    @property
    def retry_interval_mins(self):
        """
        Gets the retry_interval_mins of this ProtectionPolicy.
        Specifies the number of minutes before retrying a failed Protection Job.

        :return: The retry_interval_mins of this ProtectionPolicy.
        :rtype: int
        """
        return self._retry_interval_mins

    @retry_interval_mins.setter
    def retry_interval_mins(self, retry_interval_mins):
        """
        Sets the retry_interval_mins of this ProtectionPolicy.
        Specifies the number of minutes before retrying a failed Protection Job.

        :param retry_interval_mins: The retry_interval_mins of this ProtectionPolicy.
        :type: int
        """

        self._retry_interval_mins = retry_interval_mins

    @property
    def skip_interval_mins(self):
        """
        Gets the skip_interval_mins of this ProtectionPolicy.
        Specifies the period of time before skipping the execution of new Job Runs if an existing queued Job Run of the same Protection Job has not started. For example if this field is set to 30 minutes and a Job Run is scheduled to start at 5:00 AM every day but does not start due to conflicts (such as too many Jobs are running). If the new Job Run does not start by 5:30AM, the Cohesity Cluster will skip the new Job Run. If the original Job Run completes before 5:30AM the next day, a new Job Run is created and starts executing. This field is optional.

        :return: The skip_interval_mins of this ProtectionPolicy.
        :rtype: int
        """
        return self._skip_interval_mins

    @skip_interval_mins.setter
    def skip_interval_mins(self, skip_interval_mins):
        """
        Sets the skip_interval_mins of this ProtectionPolicy.
        Specifies the period of time before skipping the execution of new Job Runs if an existing queued Job Run of the same Protection Job has not started. For example if this field is set to 30 minutes and a Job Run is scheduled to start at 5:00 AM every day but does not start due to conflicts (such as too many Jobs are running). If the new Job Run does not start by 5:30AM, the Cohesity Cluster will skip the new Job Run. If the original Job Run completes before 5:30AM the next day, a new Job Run is created and starts executing. This field is optional.

        :param skip_interval_mins: The skip_interval_mins of this ProtectionPolicy.
        :type: int
        """

        self._skip_interval_mins = skip_interval_mins

    @property
    def snapshot_archival_copy_policies(self):
        """
        Gets the snapshot_archival_copy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to  Archival External Targets (such as AWS or Tape). It also defines the retention of copied Snapshots on an External Targets such as AWS and Tape.

        :return: The snapshot_archival_copy_policies of this ProtectionPolicy.
        :rtype: list[SnapshotArchivalCopyPolicy]
        """
        return self._snapshot_archival_copy_policies

    @snapshot_archival_copy_policies.setter
    def snapshot_archival_copy_policies(self, snapshot_archival_copy_policies):
        """
        Sets the snapshot_archival_copy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to  Archival External Targets (such as AWS or Tape). It also defines the retention of copied Snapshots on an External Targets such as AWS and Tape.

        :param snapshot_archival_copy_policies: The snapshot_archival_copy_policies of this ProtectionPolicy.
        :type: list[SnapshotArchivalCopyPolicy]
        """

        self._snapshot_archival_copy_policies = snapshot_archival_copy_policies

    @property
    def snapshot_replication_copy_policies(self):
        """
        Gets the snapshot_replication_copy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to Remote Clusters. It also defines the retention of copied Snapshots on a Remote Cluster.

        :return: The snapshot_replication_copy_policies of this ProtectionPolicy.
        :rtype: list[SnapshotReplicationCopyPolicy]
        """
        return self._snapshot_replication_copy_policies

    @snapshot_replication_copy_policies.setter
    def snapshot_replication_copy_policies(self, snapshot_replication_copy_policies):
        """
        Sets the snapshot_replication_copy_policies of this ProtectionPolicy.
        Specifies settings for copying Snapshots to Remote Clusters. It also defines the retention of copied Snapshots on a Remote Cluster.

        :param snapshot_replication_copy_policies: The snapshot_replication_copy_policies of this ProtectionPolicy.
        :type: list[SnapshotReplicationCopyPolicy]
        """

        self._snapshot_replication_copy_policies = snapshot_replication_copy_policies

    @property
    def system_scheduling_policy(self):
        """
        Gets the system_scheduling_policy of this ProtectionPolicy.
        Specifies the system backup schedule for agents running on servers to run low frequency backup jobs. Images created as part of the backup can be used to perform a \"bare metal\" recovery.

        :return: The system_scheduling_policy of this ProtectionPolicy.
        :rtype: SchedulingPolicy
        """
        return self._system_scheduling_policy

    @system_scheduling_policy.setter
    def system_scheduling_policy(self, system_scheduling_policy):
        """
        Sets the system_scheduling_policy of this ProtectionPolicy.
        Specifies the system backup schedule for agents running on servers to run low frequency backup jobs. Images created as part of the backup can be used to perform a \"bare metal\" recovery.

        :param system_scheduling_policy: The system_scheduling_policy of this ProtectionPolicy.
        :type: SchedulingPolicy
        """

        self._system_scheduling_policy = system_scheduling_policy

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
