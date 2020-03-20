# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.granularity_bucket
import cohesity_management_sdk.models.retention_policy_proto
import cohesity_management_sdk.models.snapshot_target

class SnapshotTargetPolicyProto(object):

    """Implementation of the 'SnapshotTargetPolicyProto' model.

    Message that specifies the policy for copying backup snapshots to a
    target.
    This message also specifies the retention policy that should be applied
    to
    the snapshots after they have been copied to the specified target.

    Attributes:
        copy_partially_successful_run (bool): If this is false, then only
            snapshots from the first completely successful run in the given
            time granularity will be considered for being copied. If this is
            true, then snapshots from the first partially successful run will
            also be eligible to be copied.
        granularity_bucket (GranularityBucket): Message that specifies the
            frequency granularity at which to copy the snapshots from a backup
            job's runs.
        num_days_to_keep (long|int): Specifies how to determine the expiration
            time for snapshots copied due to this policy. The snapshots will
            be marked as expiring (i.e., eligible to be garbage collected) in
            'num_days_to_keep' days from when the snapshots were created.
        retention_policy (RetentionPolicyProto): Message that specifies the
            retention policy for backup snapshots.
        snapshot_target (SnapshotTarget): Message that specifies details about
            a target (such as a replication or archival target) where a backup
            snapshot may be copied to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_partially_successful_run":'copyPartiallySuccessfulRun',
        "granularity_bucket":'granularityBucket',
        "num_days_to_keep":'numDaysToKeep',
        "retention_policy":'retentionPolicy',
        "snapshot_target":'snapshotTarget'
    }

    def __init__(self,
                 copy_partially_successful_run=None,
                 granularity_bucket=None,
                 num_days_to_keep=None,
                 retention_policy=None,
                 snapshot_target=None):
        """Constructor for the SnapshotTargetPolicyProto class"""

        # Initialize members of the class
        self.copy_partially_successful_run = copy_partially_successful_run
        self.granularity_bucket = granularity_bucket
        self.num_days_to_keep = num_days_to_keep
        self.retention_policy = retention_policy
        self.snapshot_target = snapshot_target


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
        copy_partially_successful_run = dictionary.get('copyPartiallySuccessfulRun')
        granularity_bucket = cohesity_management_sdk.models.granularity_bucket.GranularityBucket.from_dictionary(dictionary.get('granularityBucket')) if dictionary.get('granularityBucket') else None
        num_days_to_keep = dictionary.get('numDaysToKeep')
        retention_policy = cohesity_management_sdk.models.retention_policy_proto.RetentionPolicyProto.from_dictionary(dictionary.get('retentionPolicy')) if dictionary.get('retentionPolicy') else None
        snapshot_target = cohesity_management_sdk.models.snapshot_target.SnapshotTarget.from_dictionary(dictionary.get('snapshotTarget')) if dictionary.get('snapshotTarget') else None

        # Return an object of this model
        return cls(copy_partially_successful_run,
                   granularity_bucket,
                   num_days_to_keep,
                   retention_policy,
                   snapshot_target)


