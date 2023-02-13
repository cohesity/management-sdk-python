# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DiskBlock(object):

    """Implementation of the 'DiskBlock' model.

    Specifies a contiguous block by defining an offset and
    length of the block.

    Attributes:
        length_bytes (long|int): Specifies the length of the block in bytes.
        offset_bytes (long|int): Specifies the offset of the block (in bytes)
            from the beginning of the containing object such as a physical
            disk or a virtual disk file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "length_bytes":'lengthBytes',
        "offset_bytes":'offsetBytes'
    }

    def __init__(self,
                 length_bytes=None,
                 offset_bytes=None):
        """Constructor for the DiskBlock class"""

        # Initialize members of the class
        self.length_bytes = length_bytes
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
        length_bytes = dictionary.get('lengthBytes')
        offset_bytes = dictionary.get('offsetBytes')

        # Return an object of this model
        return cls(length_bytes,
                   offset_bytes)


