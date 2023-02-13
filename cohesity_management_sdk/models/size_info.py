# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SizeInfo(object):

    """Implementation of the 'SizeInfo' model.

    Message to capture the size information of an object or its snapshot. The
    calculation method can vary depending on the adapter and based on the
    evolving needs. E.g. This information can be used for billing calculations
    in DMaaS.

    Attributes:
        computation_method (int): The computation method used for "size_bytes".
        size_bytes (long|int): Size in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "computation_method": 'computationMethod',
        "size_bytes": 'sizeBytes'
    }

    def __init__(self,
                 computation_method=None,
                 size_bytes=None):
        """Constructor for the SizeInfo class"""

        # Initialize members of the class
        self.computation_method = computation_method
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
        computation_method = dictionary.get('computationMethod', None)
        size_bytes = dictionary.get('sizeBytes', None)

        # Return an object of this model
        return cls(computation_method,
                   size_bytes)


