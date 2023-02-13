# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_policy_proto
import cohesity_management_sdk.models.snapshot_target_policy_proto

class JobPolicyProto(object):

    """Implementation of the 'JobPolicyProto' model.

    A message that specifies the policies to use for a job.

    Attributes:
        backup_policy (BackupPolicyProto): If a backup does not get a chance
            to when it's due (either due to the system being busy or a
            conflict with another instance of the same job), the backup will
            still be run when the conflicts go away. But, if there are
            multiple instances of the same job that are due to be run, only
            the latest instance would be run.
        snapshot_target_policy_vec (list of SnapshotTargetPolicyProto):
            Specifies additional policies that can be used to copy snapshots
            created by a backup run to different targets (such as a remote
            replica, tape etc). Each policy also specifies the retention
            policy that should be applied to the copied snapshots at the
            respective target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_policy":'backupPolicy',
        "snapshot_target_policy_vec":'snapshotTargetPolicyVec'
    }

    def __init__(self,
                 backup_policy=None,
                 snapshot_target_policy_vec=None):
        """Constructor for the JobPolicyProto class"""

        # Initialize members of the class
        self.backup_policy = backup_policy
        self.snapshot_target_policy_vec = snapshot_target_policy_vec


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
        backup_policy = cohesity_management_sdk.models.backup_policy_proto.BackupPolicyProto.from_dictionary(dictionary.get('backupPolicy')) if dictionary.get('backupPolicy') else None
        snapshot_target_policy_vec = None
        if dictionary.get('snapshotTargetPolicyVec') != None:
            snapshot_target_policy_vec = list()
            for structure in dictionary.get('snapshotTargetPolicyVec'):
                snapshot_target_policy_vec.append(cohesity_management_sdk.models.snapshot_target_policy_proto.SnapshotTargetPolicyProto.from_dictionary(structure))

        # Return an object of this model
        return cls(backup_policy,
                   snapshot_target_policy_vec)


