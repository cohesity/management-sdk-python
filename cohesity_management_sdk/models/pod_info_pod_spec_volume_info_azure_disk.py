# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_AzureDisk(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_AzureDisk' model.

    Attributes:
        disk_name (string): TODO: Type description here.
        disk_uri (string): TODO: Type description here.  

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_name": 'diskName',
        "disk_uri": 'diskUri'
    }

    def __init__(self,
                 disk_name=None,
                 disk_uri=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_AzureDisk class"""

        # Initialize members of the class
        self.disk_name = disk_name
        self.disk_uri = disk_uri


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
        disk_name = dictionary.get('diskName', None)
        disk_uri = dictionary.get('diskUri', None)

        # Return an object of this model
        return cls(disk_name,
                   disk_uri)


