# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilePartitionBlock(object):

    """Implementation of the 'FilePartitionBlock' model.

    Defines a leaf node of a device tree. This refers to a logical
    partition in a virtual disk file.

    Attributes:
        disk_file_name (string): Specifies the disk file name where the
            logical partition is.
        length_bytes (long|int): Specifies the length of the block in bytes.
        number (long|int): Specifies a unique number of the partition within
            the linear disk file.
        offset_bytes (long|int): Specifies the offset of the block (in bytes)
            from the beginning of the containing object such as a physical
            disk or a virtual disk file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_file_name":'diskFileName',
        "length_bytes":'lengthBytes',
        "number":'number',
        "offset_bytes":'offsetBytes'
    }

    def __init__(self,
                 disk_file_name=None,
                 length_bytes=None,
                 number=None,
                 offset_bytes=None):
        """Constructor for the FilePartitionBlock class"""

        # Initialize members of the class
        self.disk_file_name = disk_file_name
        self.length_bytes = length_bytes
        self.number = number
        self.offset_bytes = offset_bytes


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
        disk_file_name = dictionary.get('diskFileName')
        length_bytes = dictionary.get('lengthBytes')
        number = dictionary.get('number')
        offset_bytes = dictionary.get('offsetBytes')

        # Return an object of this model
        return cls(disk_file_name,
                   length_bytes,
                   number,
                   offset_bytes)


