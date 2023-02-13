# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info

class PodMetadata_VolumeInfo(object):

    """Implementation of the 'PodMetadata_VolumeInfo' model.

    All the Notification events generated for a given user. This is used for
    transferring PodMetadata_VolumeInfo over wire.

    Attributes:
        pv_name (string): The underlying PV name if this volume is a PVC.
            This will be used to identify name of the directory containing PVC data
            at the path /var/lib/kubelet/pods.
        volume (PodInfo_PodSpec_VolumeInfo): Metadata about volume.
        volume_path (string): Path in S3 view where the volume data will be stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pv_name":'pvName',
        "volume":'volume',
        "volume_path":'volumePath'
    }

    def __init__(self,
                 pv_name=None,
                 volume=None,
                 volume_path=None):
        """Constructor for the PodMetadata_VolumeInfo class"""

        # Initialize members of the class
        self.pv_name = pv_name
        self.volume = volume
        self.volume_path = volume_path


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
        pv_name = dictionary.get('pvName')
        volume = cohesity_management_sdk.models.pod_info_pod_spec_volume_info.PodInfo_PodSpec_VolumeInfo.from_dictionary(dictionary.get('volume')) if dictionary.get('volume') else None
        volume_path = dictionary.get('volumePath')

        # Return an object of this model
        return cls(pv_name,
                   volume,
                   volume_path)


