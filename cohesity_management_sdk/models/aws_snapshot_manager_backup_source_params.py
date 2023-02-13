# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ebs_volume_exclusion_params

class AWSSnapshotManagerBackupSourceParams(object):

    """Implementation of the 'AWSSnapshotManagerBackupSourceParams' model.

    Attributes:
        volume_exclusion_params (EBSVolumeExclusionParams): Specifies the different
        criteria to exclude volumes from backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "volume_exclusion_params":'volumeExclusionParams'
    }

    def __init__(self,
                 volume_exclusion_params=None):
        """Constructor for the AWSSnapshotManagerBackupSourceParams class"""

        # Initialize members of the class
        self.volume_exclusion_params = volume_exclusion_params


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
        volume_exclusion_params = cohesity_management_sdk.models.ebs_volume_exclusion_params.EBSVolumeExclusionParams.from_dictionary(dictionary.get('volumeExclusionParams')) if dictionary.get('volumeExclusionParams') else None

        # Return an object of this model
        return cls(volume_exclusion_params)


