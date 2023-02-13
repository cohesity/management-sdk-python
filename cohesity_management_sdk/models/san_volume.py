# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SanVolume(object):

    """Implementation of the 'SanVolume' model.

    Specifies a SAN Volume in a SAN Storage Array.

    Attributes:
        created_time (string): Specifies the created time (e.g.,
            "2015-07-21T17:59:41Z") of the volume.
        parent_volume (string): Specifies the name of the source volume, if
            this volume was copied or cloned from it.
        serial_number (string): Specifies the serial number of the volume.
        size_bytes (long|int): Specifies the provisioned size in bytes of the
            volume.
        used_bytes (long|int): Specifies the total space actually used by the
            volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time":'createdTime',
        "parent_volume":'parentVolume',
        "serial_number":'serialNumber',
        "size_bytes":'sizeBytes',
        "used_bytes":'usedBytes'
    }

    def __init__(self,
                 created_time=None,
                 parent_volume=None,
                 serial_number=None,
                 size_bytes=None,
                 used_bytes=None):
        """Constructor for the SanVolume class"""

        # Initialize members of the class
        self.created_time = created_time
        self.parent_volume = parent_volume
        self.serial_number = serial_number
        self.size_bytes = size_bytes
        self.used_bytes = used_bytes


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
        created_time = dictionary.get('createdTime')
        parent_volume = dictionary.get('parentVolume')
        serial_number = dictionary.get('serialNumber')
        size_bytes = dictionary.get('sizeBytes')
        used_bytes = dictionary.get('usedBytes')

        # Return an object of this model
        return cls(created_time,
                   parent_volume,
                   serial_number,
                   size_bytes,
                   used_bytes)


