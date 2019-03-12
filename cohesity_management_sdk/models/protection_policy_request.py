# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.blackout_period
import cohesity_management_sdk.models.cloud_deploy_policy
import cohesity_management_sdk.models.extended_retention_policy
import cohesity_management_sdk.models.scheduling_policy
import cohesity_management_sdk.models.snapshot_copy_archival_policy
import cohesity_management_sdk.models.snapshot_copy_replication_policy

class ProtectionPolicyRequest(object):

    """Implementation of the 'Protection Policy Request.' model.

    Specifies information about a Protection Policy.

    Attributes:
        blackout_periods (list of BlackoutPeriod): Array of Blackout Periods.
            If specified, this field defines black periods when new Job Runs
            are not started. If a Job Run has been scheduled but not yet
            executed and the blackout period starts, the behavior depends on
            the policy field AbortInBlackoutPeriod.
        cloud_deploy_policies (list of CloudDeployPolicy): Array of Cloud
            Deploy Policies.  Specifies settings for copying Snapshots to
            Cloud. CloudDeploy target where backup snapshots may be converted
            and stored. It also defines the retention of copied Snapshots on
            the Cloud.
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
        retries (int): Specifies the number of times to retry capturing
            Snapshots before the Job Run fails.
        retry_interval_mins (int): Specifies the number of minutes before
            retrying a failed Protection Job.
        skip_interval_mins (int): Specifies the period of time before skipping
            the execution of new Job Runs if an existing queued Job Run of the
            same Protection Job has not started. For example if this field is
            set to 30 minutes and a Job Run is scheduled to start at 5:00 AM
            every day but does not start due to conflicts (such as too many
            Jobs are running). If the new Job Run does not start by 5:30AM,
            the Cohesity Cluster will skip the new Job Run. If the original
            Job Run completes before 5:30AM the next day, a new Job Run is
            created and starts executing. This field is optional.
        snapshot_archival_copy_policies (list of SnapshotCopyArchivalPolicy):
            Array of External Targets.  Specifies settings for copying
            Snapshots to  Archival External Targets (such as AWS or Tape). It
            also defines the retention of copied Snapshots on an External
            Targets such as AWS and Tape.
        snapshot_replication_copy_policies (list of
            SnapshotCopyReplicationPolicy): Array of Remote Clusters.
            Specifies settings for copying Snapshots to Remote Clusters. It
            also defines the retention of copied Snapshots on a Remote
            Cluster.
        system_scheduling_policy (SchedulingPolicy): Specifies settings that
            define a backup schedule for a Protection Job.
        worm_retention_type (WormRetentionType1Enum): Specifies WORM retention
            type for the snapshots. When a WORM retention type is specified,
            the snapshots of the Protection Jobs using this policy will be
            kept until the maximum of the snapshot retention time. During that
            time, the snapshots cannot be deleted. 'kNone' implies there is no
            WORM retention set. 'kCompliance' implies WORM retention is set
            for compliance reason. 'kAdministrative' implies WORM retention is
            set for administrative purposes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "blackout_periods":'blackoutPeriods',
        "cloud_deploy_policies":'cloudDeployPolicies',
        "days_to_keep":'daysToKeep',
        "days_to_keep_log":'daysToKeepLog',
        "days_to_keep_system":'daysToKeepSystem',
        "description":'description',
        "extended_retention_policies":'extendedRetentionPolicies',
        "full_scheduling_policy":'fullSchedulingPolicy',
        "incremental_scheduling_policy":'incrementalSchedulingPolicy',
        "log_scheduling_policy":'logSchedulingPolicy',
        "name":'name',
        "retries":'retries',
        "retry_interval_mins":'retryIntervalMins',
        "skip_interval_mins":'skipIntervalMins',
        "snapshot_archival_copy_policies":'snapshotArchivalCopyPolicies',
        "snapshot_replication_copy_policies":'snapshotReplicationCopyPolicies',
        "system_scheduling_policy":'systemSchedulingPolicy',
        "worm_retention_type":'wormRetentionType'
    }

    def __init__(self,
                 blackout_periods=None,
                 cloud_deploy_policies=None,
                 days_to_keep=None,
                 days_to_keep_log=None,
                 days_to_keep_system=None,
                 description=None,
                 extended_retention_policies=None,
                 full_scheduling_policy=None,
                 incremental_scheduling_policy=None,
                 log_scheduling_policy=None,
                 name=None,
                 retries=None,
                 retry_interval_mins=None,
                 skip_interval_mins=None,
                 snapshot_archival_copy_policies=None,
                 snapshot_replication_copy_policies=None,
                 system_scheduling_policy=None,
                 worm_retention_type=None):
        """Constructor for the ProtectionPolicyRequest class"""

        # Initialize members of the class
        self.blackout_periods = blackout_periods
        self.cloud_deploy_policies = cloud_deploy_policies
        self.days_to_keep = days_to_keep
        self.days_to_keep_log = days_to_keep_log
        self.days_to_keep_system = days_to_keep_system
        self.description = description
        self.extended_retention_policies = extended_retention_policies
        self.full_scheduling_policy = full_scheduling_policy
        self.incremental_scheduling_policy = incremental_scheduling_policy
        self.log_scheduling_policy = log_scheduling_policy
        self.name = name
        self.retries = retries
        self.retry_interval_mins = retry_interval_mins
        self.skip_interval_mins = skip_interval_mins
        self.snapshot_archival_copy_policies = snapshot_archival_copy_policies
        self.snapshot_replication_copy_policies = snapshot_replication_copy_policies
        self.system_scheduling_policy = system_scheduling_policy
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
        cloud_deploy_policies = None
        if dictionary.get('cloudDeployPolicies') != None:
            cloud_deploy_policies = list()
            for structure in dictionary.get('cloudDeployPolicies'):
                cloud_deploy_policies.append(cohesity_management_sdk.models.cloud_deploy_policy.CloudDeployPolicy.from_dictionary(structure))
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
        retries = dictionary.get('retries')
        retry_interval_mins = dictionary.get('retryIntervalMins')
        skip_interval_mins = dictionary.get('skipIntervalMins')
        snapshot_archival_copy_policies = None
        if dictionary.get('snapshotArchivalCopyPolicies') != None:
            snapshot_archival_copy_policies = list()
            for structure in dictionary.get('snapshotArchivalCopyPolicies'):
                snapshot_archival_copy_policies.append(cohesity_management_sdk.models.snapshot_copy_archival_policy.SnapshotCopyArchivalPolicy.from_dictionary(structure))
        snapshot_replication_copy_policies = None
        if dictionary.get('snapshotReplicationCopyPolicies') != None:
            snapshot_replication_copy_policies = list()
            for structure in dictionary.get('snapshotReplicationCopyPolicies'):
                snapshot_replication_copy_policies.append(cohesity_management_sdk.models.snapshot_copy_replication_policy.SnapshotCopyReplicationPolicy.from_dictionary(structure))
        system_scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('systemSchedulingPolicy')) if dictionary.get('systemSchedulingPolicy') else None
        worm_retention_type = dictionary.get('wormRetentionType')

        # Return an object of this model
        return cls(blackout_periods,
                   cloud_deploy_policies,
                   days_to_keep,
                   days_to_keep_log,
                   days_to_keep_system,
                   description,
                   extended_retention_policies,
                   full_scheduling_policy,
                   incremental_scheduling_policy,
                   log_scheduling_policy,
                   name,
                   retries,
                   retry_interval_mins,
                   skip_interval_mins,
                   snapshot_archival_copy_policies,
                   snapshot_replication_copy_policies,
                   system_scheduling_policy,
                   worm_retention_type)


