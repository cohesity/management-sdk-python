# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pvc_info

class PodInfo_PodSpec_VolumeInfo_EphemeralVolumeSource(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_EphemeralVolumeSource' model.

    Represents an ephemeral volume that is handled by a normal storage
    driver.

    Attributes:
        read_only (bool): TODO: Type description here.
        volume_claim_template (PVCInfo): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "read_only": 'readOnly',
        "volume_claim_template": 'volumeClaimTemplate'
    }

    def __init__(self,
                 read_only=None,
                 volume_claim_template=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_EphemeralVolumeSource class"""

        # Initialize members of the class
        self.read_only = read_only
        self.volume_claim_template = volume_claim_template


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
        read_only = dictionary.get('readOnly', None)
        volume_claim_template = cohesity_management_sdk.models.pvc_info.PVCInfo.from_dictionary(dictionary.get('volumeClaimTemplate')) if dictionary.get('volumeClaimTemplate') else None

        # Return an object of this model
        return cls(read_only,
                   volume_claim_template)


