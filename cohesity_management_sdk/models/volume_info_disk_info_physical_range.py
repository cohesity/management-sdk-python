# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VolumeInfoDiskInfoPhysicalRange(object):

    """Implementation of the 'VolumeInfo_DiskInfo_PhysicalRange' model.

    This message represents a physical contiguous range in disk file.

    Attributes:
        length (long|int): Length of this range in bytes.
        offset (long|int): Offset of this range in disk file from beginning of
            file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "length":'length',
        "offset":'offset'
    }

    def __init__(self,
                 length=None,
                 offset=None):
        """Constructor for the VolumeInfoDiskInfoPhysicalRange class"""

        # Initialize members of the class
        self.length = length
        self.offset = offset


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
        length = dictionary.get('length')
        offset = dictionary.get('offset')

        # Return an object of this model
        return cls(length,
                   offset)


