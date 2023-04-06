# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.blackout_period
import cohesity_management_sdk.models.data_lock_config
import cohesity_management_sdk.models.extended_retention_policy
import cohesity_management_sdk.models.rpo_policy_settings
import cohesity_management_sdk.models.scheduling_policy
import cohesity_management_sdk.models.snapshot_archival_copy_policy
import cohesity_management_sdk.models.snapshot_cloud_copy_policy
import cohesity_management_sdk.models.snapshot_replication_copy_policy


class ProtectionPolicy(object):

    """Implementation of the 'ProtectionPolicy' model.

    TODO: type description here.


    Attributes:

        blackout_periods (list of BlackoutPeriod): Array of QuietTime Periods. 
            If specified, this field defines black periods when new Job Runs
            are not started. If a Job Run has been scheduled but not yet
            executed and the QuietTime period starts, the behavior depends on
            the policy field AbortInBlackoutPeriod.
        cdp_scheduling_policy (SchedulingPolicy): Specifies the CDP backup
            schedule of a Protection Job and how long log files captured by
            this schedule are retained on the Cohesity Cluster.
        cloud_deploy_policies (list of SnapshotCloudCopyPolicy): Array of Cloud
            Deploy Policies.  Specifies settings for copying Snapshots to
            Cloud. CloudDeploy target where backup snapshots may be converted
            and stored. It also defines the retention of copied Snapshots on
            the Cloud.
        datalock_config (DataLockConfig): Specifies WORM retention type for the
            incremental/full snapshots. When a WORM retention type is
            specified, the snapshots of the Protection Groups using this policy
            will be kept for the last N days as specified in the duration of
            the datalock. During that time, the snapshots cannot be deleted.
        datalock_config_log (DataLockConfig): Specifies WORM retention type for
            the log snapshots. When a WORM retention type is specified, the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        datalock_config_system (DataLockConfig): Specifies WORM retention type
            for the BMR snapshots. When a WORM retention type is specified, the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        days_to_keep (long|int): Specifies how many days to retain Snapshots on
            the Cohesity Cluster.
        days_to_keep_log (long|int): Specifies the number of days to retain log
            run if Log Schedule exists.
        days_to_keep_system (long|int): Specifies the number of days to retain
            system backups made for bare metal recovery. This field is
            applicable if systemSchedulingPolicy is specified.
        description (string): Description of the Protection Policy.
        extended_retention_policies (list of ExtendedRetentionPolicy):
            Specifies additional retention policies that should be applied to
            the backup snapshots. A backup snapshot will be retained up to a
            time that is the maximum of all retention policies that are
            applicable to it.
        full_scheduling_policy (SchedulingPolicy): Specifies the Full (no CBT)
            backup schedule of a Protection Job and how long Snapshots captured
            by this schedule are retained on the Cohesity Cluster.
        id (string): Specifies a unique Policy id assigned by the Cohesity
            Cluster.
        incremental_scheduling_policy (SchedulingPolicy): Specifies the
            CBT-based backup schedule of a Protection Job and how long
            Snapshots captured by this schedule are retained on the Cohesity
            Cluster.
        is_cascaded_replication_policy (bool): Specifies if the policy is
            associated with cascaded replication.
        is_replicated (bool): Specifies the policy is replicated policy.
        is_usable (bool): Specifies if the policy can be used to create a job.
        last_modified_time_msecs (long|int): Specifies the epoch time (in
            milliseconds) when the Protection Policy was last modified.
        log_scheduling_policy (SchedulingPolicy): Specifies the Log backup
            schedule of a Protection Job and how long log files captured by
            this schedule are retained on the Cohesity Cluster.
        name (string): Specifies the name of the Protection Policy.
        num_linked_policies (long|int): Species the number of policies linked
            to a global policy.
        num_secs_to_keep (int): Specifies the number of mins/hours/days in
            seconds to retain CDP backups if CDP schedule exists.
        parent_policy_id (string): Specifies the parent global policy Id. This
            must be specified when creating a policy from global policy
            template.
        retries (int): Specifies the number of times to retry capturing
            Snapshots before the Job Run fails.
        retry_interval_mins (int): Specifies the number of minutes before
            retrying a failed Protection Job.
        rpo_policy_settings (RpoPolicySettings): Specifies the RPO Policy
            related settings.
        skip_interval_mins (int): Specifies the period of time before skipping
            the execution of new Job Runs if an existing queued Job Run of the
            same Protection Job has not started. For example if this field is
            set to 30 minutes and a Job Run is scheduled to start at 5:00 AM
            every day but does not start due to conflicts (such as too many
            Jobs are running). If the new Job Run does not start by 5:30AM, the
            Cohesity Cluster will skip the new Job Run. If the original Job Run
            completes before 5:30AM the next day, a new Job Run is created and
            starts executing. This field is optional.
        snapshot_archival_copy_policies (list of SnapshotArchivalCopyPolicy):
            Array of External Targets.  Specifies settings for copying
            Snapshots to  Archival External Targets (such as AWS or Tape). It
            also defines the retention of copied Snapshots on an External
            Targets such as AWS and Tape.
        snapshot_replication_copy_policies (list of
            SnapshotReplicationCopyPolicy): Array of Remote Clusters. 
            Specifies settings for copying Snapshots to Remote Clusters. It
            also defines the retention of copied Snapshots on a Remote Cluster.
        storage_array_snapshot_scheduling_policy (SchedulingPolicy): Specifies
            the storage array snapshot backup schedule of a Protection Job and
            how long snapshot captured by this schedule are retained on the
            Storage Array.
        system_scheduling_policy (SchedulingPolicy): Specifies the system
            backup schedule for agents running on servers to run low frequency
            backup jobs. Images created as part of the backup can be used to
            perform a "bare metal" recovery.
        tenant_ids (list of string): Specifies which organizations have been
            assigned this policy. This value is only populated for the cluster
            admin for now.
        mtype (TypeProtectionPolicyEnum): Specifies the type of the protection
            policy. 'kRegular' means a regular Protection Policy. 'kRPO' means
            an RPO Protection Policy.
        worm_retention_type (WormRetentionTypeEnum): Specifies WORM retention
            type for the snapshots. When a WORM retention type is specified,
            the snapshots of the Protection Jobs using this policy will be kept
            until the maximum of the snapshot retention time. During that time,
            the snapshots cannot be deleted. This field is deprecated. Use
            DataLockConfig for incremental runs, DataLockConfigLog for log
            runs, DataLockConfigSystem for BMR runs, and DataLockConfig in
            extended retention and for copy targets config. deprecated: true
            'kNone' implies there is no WORM retention set. 'kCompliance'
            implies WORM retention is set for compliance reason.
            'kAdministrative' implies WORM retention is set for administrative
            purposes.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "blackout_periods":'blackoutPeriods',
        "cdp_scheduling_policy":'cdpSchedulingPolicy',
        "cloud_deploy_policies":'cloudDeployPolicies',
        "datalock_config":'datalockConfig',
        "datalock_config_log":'datalockConfigLog',
        "datalock_config_system":'datalockConfigSystem',
        "days_to_keep":'daysToKeep',
        "days_to_keep_log":'daysToKeepLog',
        "days_to_keep_system":'daysToKeepSystem',
        "description":'description',
        "extended_retention_policies":'extendedRetentionPolicies',
        "full_scheduling_policy":'fullSchedulingPolicy',
        "id":'id',
        "incremental_scheduling_policy":'incrementalSchedulingPolicy',
        "is_cascaded_replication_policy":'isCascadedReplicationPolicy',
        "is_replicated":'isReplicated',
        "is_usable":'isUsable',
        "last_modified_time_msecs":'lastModifiedTimeMsecs',
        "log_scheduling_policy":'logSchedulingPolicy',
        "name":'name',
        "num_linked_policies":'numLinkedPolicies',
        "num_secs_to_keep":'numSecsToKeep',
        "parent_policy_id":'parentPolicyId',
        "retries":'retries',
        "retry_interval_mins":'retryIntervalMins',
        "rpo_policy_settings":'rpoPolicySettings',
        "skip_interval_mins":'skipIntervalMins',
        "snapshot_archival_copy_policies":'snapshotArchivalCopyPolicies',
        "snapshot_replication_copy_policies":'snapshotReplicationCopyPolicies',
        "storage_array_snapshot_scheduling_policy":'storageArraySnapshotSchedulingPolicy',
        "system_scheduling_policy":'systemSchedulingPolicy',
        "tenant_ids":'tenantIds',
        "mtype":'type',
        "worm_retention_type":'wormRetentionType',
    }
    def __init__(self,
                 blackout_periods=None,
                 cdp_scheduling_policy=None,
                 cloud_deploy_policies=None,
                 datalock_config=None,
                 datalock_config_log=None,
                 datalock_config_system=None,
                 days_to_keep=None,
                 days_to_keep_log=None,
                 days_to_keep_system=None,
                 description=None,
                 extended_retention_policies=None,
                 full_scheduling_policy=None,
                 id=None,
                 incremental_scheduling_policy=None,
                 is_cascaded_replication_policy=None,
                 is_replicated=None,
                 is_usable=None,
                 last_modified_time_msecs=None,
                 log_scheduling_policy=None,
                 name=None,
                 num_linked_policies=None,
                 num_secs_to_keep=None,
                 parent_policy_id=None,
                 retries=None,
                 retry_interval_mins=None,
                 rpo_policy_settings=None,
                 skip_interval_mins=None,
                 snapshot_archival_copy_policies=None,
                 snapshot_replication_copy_policies=None,
                 storage_array_snapshot_scheduling_policy=None,
                 system_scheduling_policy=None,
                 tenant_ids=None,
                 mtype=None,
                 worm_retention_type=None,
            ):

        """Constructor for the ProtectionPolicy class"""

        # Initialize members of the class
        self.blackout_periods = blackout_periods
        self.cdp_scheduling_policy = cdp_scheduling_policy
        self.cloud_deploy_policies = cloud_deploy_policies
        self.datalock_config = datalock_config
        self.datalock_config_log = datalock_config_log
        self.datalock_config_system = datalock_config_system
        self.days_to_keep = days_to_keep
        self.days_to_keep_log = days_to_keep_log
        self.days_to_keep_system = days_to_keep_system
        self.description = description
        self.extended_retention_policies = extended_retention_policies
        self.full_scheduling_policy = full_scheduling_policy
        self.id = id
        self.incremental_scheduling_policy = incremental_scheduling_policy
        self.is_cascaded_replication_policy = is_cascaded_replication_policy
        self.is_replicated = is_replicated
        self.is_usable = is_usable
        self.last_modified_time_msecs = last_modified_time_msecs
        self.log_scheduling_policy = log_scheduling_policy
        self.name = name
        self.num_linked_policies = num_linked_policies
        self.num_secs_to_keep = num_secs_to_keep
        self.parent_policy_id = parent_policy_id
        self.retries = retries
        self.retry_interval_mins = retry_interval_mins
        self.rpo_policy_settings = rpo_policy_settings
        self.skip_interval_mins = skip_interval_mins
        self.snapshot_archival_copy_policies = snapshot_archival_copy_policies
        self.snapshot_replication_copy_policies = snapshot_replication_copy_policies
        self.storage_array_snapshot_scheduling_policy = storage_array_snapshot_scheduling_policy
        self.system_scheduling_policy = system_scheduling_policy
        self.tenant_ids = tenant_ids
        self.mtype = mtype
        self.worm_retention_type = worm_retention_type

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        blackout_periods = None
        if dictionary.get('blackoutPeriods') != None:
            blackout_periods = list()
            for structure in dictionary.get('blackoutPeriods'):
                blackout_periods.append(cohesity_management_sdk.models.blackout_period.BlackoutPeriod.from_dictionary(structure))
        cdp_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('cdpSchedulingPolicy')) if dictionary.get('cdpSchedulingPolicy') else None
        cloud_deploy_policies = None
        if dictionary.get('cloudDeployPolicies') != None:
            cloud_deploy_policies = list()
            for structure in dictionary.get('cloudDeployPolicies'):
                cloud_deploy_policies.append(cohesity_management_sdk.models.snapshot_cloud_copy_policy.SnapshotCloudCopyPolicy.from_dictionary(structure))
        datalock_config = cohesity_management_sdk.models.data_lock_config.DataLockConfig.from_dictionary(dictionary.get('datalockConfig')) if dictionary.get('datalockConfig') else None
        datalock_config_log = cohesity_management_sdk.models.data_lock_config.DataLockConfig.from_dictionary(dictionary.get('datalockConfigLog')) if dictionary.get('datalockConfigLog') else None
        datalock_config_system = cohesity_management_sdk.models.data_lock_config.DataLockConfig.from_dictionary(dictionary.get('datalockConfigSystem')) if dictionary.get('datalockConfigSystem') else None
        days_to_keep = dictionary.get('daysToKeep')
        days_to_keep_log = dictionary.get('daysToKeepLog')
        days_to_keep_system = dictionary.get('daysToKeepSystem')
        description = dictionary.get('description')
        extended_retention_policies = None
        if dictionary.get('extendedRetentionPolicies') != None:
            extended_retention_policies = list()
            for structure in dictionary.get('extendedRetentionPolicies'):
                extended_retention_policies.append(cohesity_management_sdk.models.extended_retention_policy.ExtendedRetentionPolicy.from_dictionary(structure))
        full_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('fullSchedulingPolicy')) if dictionary.get('fullSchedulingPolicy') else None
        id = dictionary.get('id')
        incremental_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('incrementalSchedulingPolicy')) if dictionary.get('incrementalSchedulingPolicy') else None
        is_cascaded_replication_policy = dictionary.get('isCascadedReplicationPolicy')
        is_replicated = dictionary.get('isReplicated')
        is_usable = dictionary.get('isUsable')
        last_modified_time_msecs = dictionary.get('lastModifiedTimeMsecs')
        log_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('logSchedulingPolicy')) if dictionary.get('logSchedulingPolicy') else None
        name = dictionary.get('name')
        num_linked_policies = dictionary.get('numLinkedPolicies')
        num_secs_to_keep = dictionary.get('numSecsToKeep')
        parent_policy_id = dictionary.get('parentPolicyId')
        retries = dictionary.get('retries')
        retry_interval_mins = dictionary.get('retryIntervalMins')
        rpo_policy_settings = cohesity_management_sdk.models.rpo_policy_settings.RpoPolicySettings.from_dictionary(dictionary.get('rpoPolicySettings')) if dictionary.get('rpoPolicySettings') else None
        skip_interval_mins = dictionary.get('skipIntervalMins')
        snapshot_archival_copy_policies = None
        if dictionary.get('snapshotArchivalCopyPolicies') != None:
            snapshot_archival_copy_policies = list()
            for structure in dictionary.get('snapshotArchivalCopyPolicies'):
                snapshot_archival_copy_policies.append(cohesity_management_sdk.models.snapshot_archival_copy_policy.SnapshotArchivalCopyPolicy.from_dictionary(structure))
        snapshot_replication_copy_policies = None
        if dictionary.get('snapshotReplicationCopyPolicies') != None:
            snapshot_replication_copy_policies = list()
            for structure in dictionary.get('snapshotReplicationCopyPolicies'):
                snapshot_replication_copy_policies.append(cohesity_management_sdk.models.snapshot_replication_copy_policy.SnapshotReplicationCopyPolicy.from_dictionary(structure))
        storage_array_snapshot_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('storageArraySnapshotSchedulingPolicy')) if dictionary.get('storageArraySnapshotSchedulingPolicy') else None
        system_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('systemSchedulingPolicy')) if dictionary.get('systemSchedulingPolicy') else None
        tenant_ids = dictionary.get("tenantIds")
        mtype = dictionary.get('type')
        worm_retention_type = dictionary.get('wormRetentionType')

        # Return an object of this model
        return cls(
            blackout_periods,
            cdp_scheduling_policy,
            cloud_deploy_policies,
            datalock_config,
            datalock_config_log,
            datalock_config_system,
            days_to_keep,
            days_to_keep_log,
            days_to_keep_system,
            description,
            extended_retention_policies,
            full_scheduling_policy,
            id,
            incremental_scheduling_policy,
            is_cascaded_replication_policy,
            is_replicated,
            is_usable,
            last_modified_time_msecs,
            log_scheduling_policy,
            name,
            num_linked_policies,
            num_secs_to_keep,
            parent_policy_id,
            retries,
            retry_interval_mins,
            rpo_policy_settings,
            skip_interval_mins,
            snapshot_archival_copy_policies,
            snapshot_replication_copy_policies,
            storage_array_snapshot_scheduling_policy,
            system_scheduling_policy,
            tenant_ids,
            mtype,
            worm_retention_type
)