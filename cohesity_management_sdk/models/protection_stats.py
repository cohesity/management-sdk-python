# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionStats(object):

    """Implementation of the 'ProtectionStats' model.

    Protection Statistics.

    Attributes:
        num_failed (int): Number of Failed Objects.
        num_objects (int): Number of Objects.
        size_bytes (long|int): Size in Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_failed":'numFailed',
        "num_objects":'numObjects',
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 num_failed=None,
                 num_objects=None,
                 size_bytes=None):
        """Constructor for the ProtectionStats class"""

        # Initialize members of the class
        self.num_failed = num_failed
        self.num_objects = num_objects
        self.size_bytes = size_bytes


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
        num_failed = dictionary.get('numFailed')
        num_objects = dictionary.get('numObjects')
        size_bytes = dictionary.get('sizeBytes')

        # Return an object of this model
        return cls(num_failed,
                   num_objects,
                   size_bytes)


