# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_info
import cohesity_management_sdk.models.snapshot_target_settings

class FullSnapshotInfo(object):

    """Implementation of the 'FullSnapshotInfo' model.

    Specifies the info regarding how to restore to a particular full or
    incremental snapshot.

    Attributes:
        restore_info (RestoreInfo): Specifies the info regarding a full SQL
            snapshot.
        snapshot_target (list of SnapshotTargetSettings): Specifies the
            location holding snapshot copies that may be used for restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_info":'restoreInfo',
        "snapshot_target":'snapshotTarget'
    }

    def __init__(self,
                 restore_info=None,
                 snapshot_target=None):
        """Constructor for the FullSnapshotInfo class"""

        # Initialize members of the class
        self.restore_info = restore_info
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
        restore_info = cohesity_management_sdk.models.restore_info.RestoreInfo.from_dictionary(dictionary.get('restoreInfo')) if dictionary.get('restoreInfo') else None
        snapshot_target = None
        if dictionary.get('snapshotTarget') != None:
            snapshot_target = list()
            for structure in dictionary.get('snapshotTarget'):
                snapshot_target.append(cohesity_management_sdk.models.snapshot_target_settings.SnapshotTargetSettings.from_dictionary(structure))

        # Return an object of this model
        return cls(restore_info,
                   snapshot_target)


