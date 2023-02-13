# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VolumeInfo_SubVolumeInfo(object):

    """Implementation of the 'VolumeInfo_SubVolumeInfo' model.

    The proto is used only for storing BTRFS subvolume fields. This is
    required for handling of mountable subvolume.


    Attributes:
        subvolume_name (string): Name of subvolume. Used to provide relevant mount
            options.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subvolume_name":'subvolumeName'
    }

    def __init__(self,
                 subvolume_name=None):
        """Constructor for the VolumeInfo_SubVolumeInfo class"""

        # Initialize members of the class
        self.subvolume_name = subvolume_name


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
        subvolume_name = dictionary.get('subvolumeName')

        # Return an object of this model
        return cls(subvolume_name)


