# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_GcePersistentDisk(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_GcePersistentDisk' model.

    Attributes:
        fs_type (string): TODO: Type description here.
        pd_id (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type": 'fsType',
        "pd_id": 'pdName'
    }

    def __init__(self,
                 fs_type=None,
                 pd_id=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_GcePersistentDisk class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.pd_id = pd_id


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
        fs_type = dictionary.get('fsType', None)
        pd_id = dictionary.get('pdName', None)

        # Return an object of this model
        return cls(fs_type,
                   pd_id)


