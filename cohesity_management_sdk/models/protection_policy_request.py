# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.blackout_period
import cohesity_management_sdk.models.data_lock_config
import cohesity_management_sdk.models.snapshot_cloud_copy_policy
import cohesity_management_sdk.models.extended_retention_policy
import cohesity_management_sdk.models.scheduling_policy
import cohesity_management_sdk.models.rpo_policy_settings
import cohesity_management_sdk.models.snapshot_archival_copy_policy
import cohesity_management_sdk.models.snapshot_replication_copy_policy

class ProtectionPolicyRequest(object):

    """Implementation of the 'ProtectionPolicyRequest' model.

    Specifies information about a Protection Policy.

    Attributes:
        blackout_periods (list of BlackoutPeriod): Array of Blackout Periods.
            If specified, this field defines black periods when new Job Runs
            are not started. If a Job Run has been scheduled but not yet
            executed and the blackout period starts, the behavior depends on
            the policy field AbortInBlackoutPeriod.
        cdp_scheduling_policy (SchedulingPolicy): Specifies the CDP backup
            schedule of a Protection Job and how long log files captured by
            this schedule are retained on the Cohesity Cluster.
        cloud_deploy_policies (list of SnapshotCloudCopyPolicy): Array of
            Cloud Deploy Policies.  Specifies settings for copying Snapshots
            to Cloud. CloudDeploy target where backup snapshots may be
            converted and stored. It also defines the retention of copied
            Snapshots on the Cloud.
        datalock_config (DataLockConfig): Specifies WORM retention type for
            the log snapshots. When a WORM retention type is specified, the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        datalock_config_log (DataLockConfig): Specifies WORM retention type
            for the log snapshots. When a WORM retention type is specified,the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        datalock_config_system (DataLockConfig): Specifies WORM retention type
            for the log snapshots. When a WORM retention type is specified,the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        days_to_keep (long|int): Specifies how many days to retain Snapshots
            on the Cohesity Cluster.
        days_to_keep_log (long|int): Specifies the number of days to retain
            log run if Log Schedule exists.
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
            backup schedule of a Protection Job and how long Snapshots
            captured by this schedule are retained on the Cohesity Cluster.
        incremental_scheduling_policy (SchedulingPolicy): Specifies the
            CBT-based backup schedule of a Protection Job and how long
            Snapshots captured by this schedule are retained on the Cohesity
            Cluster.
        log_scheduling_policy (SchedulingPolicy): Specifies settings that
            define a backup schedule for a Protection Job.
        name (string): Specifies the name of the Protection Policy.
        num_linked_policies (long|int): Species the number of policies linked
            to a global policy.
        parent_policy_id (string): Specifies the parent global policy Id. This
            must be specified when creating a policy from global policy
            template.
        retries (int): Specifies the number of times to retry capturing
            Snapshots before the Job Run fails.
        retry_interval_mins (int): Specifies the number of minutes before
            retrying a failed Protection Job.
        rpo_policy_settings (RpoPolicySettings): Specifies all the additional
            settings that are applicable only to an RPO policy. This can
            include storage domain, settings of different environments, etc.
        skip_interval_mins (int): Specifies the period of time before skipping
            the execution of new Job Runs if an existing queued Job Run of the
            same Protection Job has not started. For example if this field is
            set to 30 minutes and a Job Run is scheduled to start at 5:00 AM
            every day but does not start due to conflicts (such as too many
            Jobs are running). If the new Job Run does not start by 5:30AM,
            the Cohesity Cluster will skip the new Job Run. If the original
            Job Run completes before 5:30AM the next day, a new Job Run is
            created and starts executing. This field is optional.
        snapshot_archival_copy_policies (list of SnapshotArchivalCopyPolicy):
            Array of External Targets.  Specifies settings for copying
            Snapshots to  Archival External Targets (such as AWS or Tape). It
            also defines the retention of copied Snapshots on an External
            Targets such as AWS and Tape.
        snapshot_replication_copy_policies (list of
            SnapshotReplicationCopyPolicy): Array of Remote Clusters.
            Specifies settings for copying Snapshots to Remote Clusters. It
            also defines the retention of copied Snapshots on a Remote
            Cluster.
        system_scheduling_policy (SchedulingPolicy): Specifies settings that
            define a backup schedule for a Protection Job.
        mtype (TypeProtectionPolicyRequestEnum): Specifies the type of the
            protection policy. 'kRegular' means a regular Protection Policy.
            'kRPO' means an RPO Protection Policy.
        worm_retention_type (WormRetentionTypeProtectionPolicyRequestEnum):
            Specifies WORM retention type for the snapshots. When a WORM
            retention type is specified, the snapshots of the Protection Jobs
            using this policy will be kept until the maximum of the snapshot
            retention time. During that time, the snapshots cannot be deleted.
            This field is deprecated. Use DataLockConfig for incremental runs,
            DataLockConfigLog for log runs, DataLockConfigSystem for BMR runs, and
            DataLockConfig in extended retention and for copy targets config.
            deprecated: true
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
        "incremental_scheduling_policy":'incrementalSchedulingPolicy',
        "log_scheduling_policy":'logSchedulingPolicy',
        "name":'name',
        "num_linked_policies":'numLinkedPolicies',
        "parent_policy_id":'parentPolicyId',
        "retries":'retries',
        "retry_interval_mins":'retryIntervalMins',
        "rpo_policy_settings":'rpoPolicySettings',
        "skip_interval_mins":'skipIntervalMins',
        "snapshot_archival_copy_policies":'snapshotArchivalCopyPolicies',
        "snapshot_replication_copy_policies":'snapshotReplicationCopyPolicies',
        "system_scheduling_policy":'systemSchedulingPolicy',
        "mtype":'type',
        "worm_retention_type":'wormRetentionType'
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
                 incremental_scheduling_policy=None,
                 log_scheduling_policy=None,
                 name=None,
                 num_linked_policies=None,
                 parent_policy_id=None,
                 retries=None,
                 retry_interval_mins=None,
                 rpo_policy_settings=None,
                 skip_interval_mins=None,
                 snapshot_archival_copy_policies=None,
                 snapshot_replication_copy_policies=None,
                 system_scheduling_policy=None,
                 mtype=None,
                 worm_retention_type=None):
        """Constructor for the ProtectionPolicyRequest class"""

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
        self.incremental_scheduling_policy = incremental_scheduling_policy
        self.log_scheduling_policy = log_scheduling_policy
        self.name = name
        self.num_linked_policies = num_linked_policies
        self.parent_policy_id = parent_policy_id
        self.retries = retries
        self.retry_interval_mins = retry_interval_mins
        self.rpo_policy_settings = rpo_policy_settings
        self.skip_interval_mins = skip_interval_mins
        self.snapshot_archival_copy_policies = snapshot_archival_copy_policies
        self.snapshot_replication_copy_policies = snapshot_replication_copy_policies
        self.system_scheduling_policy = system_scheduling_policy
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
        incremental_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('incrementalSchedulingPolicy')) if dictionary.get('incrementalSchedulingPolicy') else None
        log_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('logSchedulingPolicy')) if dictionary.get('logSchedulingPolicy') else None
        name = dictionary.get('name')
        num_linked_policies = dictionary.get('numLinkedPolicies')
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
        system_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('systemSchedulingPolicy')) if dictionary.get('systemSchedulingPolicy') else None
        mtype = dictionary.get('type')
        worm_retention_type = dictionary.get('wormRetentionType')

        # Return an object of this model
        return cls(blackout_periods,
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
                   incremental_scheduling_policy,
                   log_scheduling_policy,
                   name,
                   num_linked_policies,
                   parent_policy_id,
                   retries,
                   retry_interval_mins,
                   rpo_policy_settings,
                   skip_interval_mins,
                   snapshot_archival_copy_policies,
                   snapshot_replication_copy_policies,
                   system_scheduling_policy,
                   mtype,
                   worm_retention_type)


