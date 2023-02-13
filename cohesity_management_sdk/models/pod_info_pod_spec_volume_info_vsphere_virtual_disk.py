# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_VsphereVirtualDisk(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_VsphereVirtualDisk' model.

    Attributes:
        fs_type (string): TODO: Type description here.
        storage_policy_id (string): TODO: Type description here.
        storage_policy_name (string): TODO: Type description here.
        volume_path (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "storage_policy_id":'storagePolicyID',
        "storage_policy_name":'storagePolicyName',
        "volume_path":'volumePath'
    }

    def __init__(self,
                 fs_type=None,
                 storage_policy_id=None,
                 storage_policy_name=None,
                 volume_path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_VsphereVirtualDisk class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.storage_policy_id = storage_policy_id
        self.storage_policy_name = storage_policy_name
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
        fs_type = dictionary.get('fsType')
        storage_policy_id = dictionary.get('storagePolicyID')
        storage_policy_name = dictionary.get('storagePolicyName')
        volume_path = dictionary.get('volumePath')

        # Return an object of this model
        return cls(fs_type,
                   storage_policy_id,
                   storage_policy_name,
                   volume_path)


