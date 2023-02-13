# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HBaseTable(object):

    """Implementation of the 'HBaseTable' model.

    Specifies an Object containing information about a HBase table.

    Attributes:
    approx_size_bytes (int): Specifies the approx size of the table in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "approx_size_bytes":'approxSizeBytes'
    }

    def __init__(self,
                 approx_size_bytes=None):
        """Constructor for the HBaseTable class"""

        # Initialize members of the class
        self.approx_size_bytes = approx_size_bytes


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
        approx_size_bytes = dictionary.get('approxSizeBytes')

        # Return an object of this model
        return cls(approx_size_bytes)


