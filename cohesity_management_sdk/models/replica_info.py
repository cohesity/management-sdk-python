# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.snapshot_target_settings
import cohesity_management_sdk.models.universal_id

class ReplicaInfo(object):

    """Implementation of the 'ReplicaInfo' model.

    Specifies the Replication information about a snapshot.

    Attributes:
        expiry_time_usecs (long|int): Specifies the expiration time of the
            snapshot within the target location.
        snapshot_target_settings (SnapshotTargetSettings): Specifies the
            snapshot target settings for the given snapshot.
        uid (UniversalId): Specifies a global Protection Job id that is unique
            across Cohesity Clusters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expiry_time_usecs":'expiryTimeUsecs',
        "snapshot_target_settings":'snapshotTargetSettings',
        "uid":'uid'
    }

    def __init__(self,
                 expiry_time_usecs=None,
                 snapshot_target_settings=None,
                 uid=None):
        """Constructor for the ReplicaInfo class"""

        # Initialize members of the class
        self.expiry_time_usecs = expiry_time_usecs
        self.snapshot_target_settings = snapshot_target_settings
        self.uid = uid


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
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        snapshot_target_settings = cohesity_management_sdk.models.snapshot_target_settings.SnapshotTargetSettings.from_dictionary(dictionary.get('snapshotTargetSettings')) if dictionary.get('snapshotTargetSettings') else None
        uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('uid')) if dictionary.get('uid') else None

        # Return an object of this model
        return cls(expiry_time_usecs,
                   snapshot_target_settings,
                   uid)


