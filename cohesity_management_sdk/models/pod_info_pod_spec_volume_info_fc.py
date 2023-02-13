# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_FC(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_FC' model.

    Fibre channel volumes

    Attributes:
        fs_type (string):  TODO: Type description here.
        lun (int): TODO: Type description here.
        target_wwn_s (list of string): Array of Fibre Channel target's
            World Wide Names

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "lun":'lun',
        "target_wwn_s":'targetWWNs'
    }

    def __init__(self,
                 fs_type=None,
                 lun=None,
                 target_wwn_s=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_FC class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.lun = lun
        self.target_wwn_s = target_wwn_s


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
        lun = dictionary.get('lun')
        target_wwn_s = dictionary.get('targetWWNs')

        # Return an object of this model
        return cls(fs_type,
                   lun,
                   target_wwn_s)


