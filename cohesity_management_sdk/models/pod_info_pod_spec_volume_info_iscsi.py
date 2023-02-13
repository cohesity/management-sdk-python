# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_ISCSI(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_ISCSI' lunl.

    Attributes:
        iqn (string):  TODO: Type description here.
        lun (int): TODO: Type description here.
        target_portal (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "iqn":'iqn',
        "lun":'lun',
        "target_portal":'targetPortal'
    }

    def __init__(self,
                 iqn=None,
                 lun=None,
                 target_portal=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_ISCSI class"""

        # Initialize members of the class
        self.iqn = iqn
        self.lun = lun
        self.target_portal = target_portal


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
        iqn = dictionary.get('iqn')
        lun = dictionary.get('lun')
        target_portal = dictionary.get('targetPortal')

        # Return an object of this model
        return cls(iqn,
                   lun,
                   target_portal)


