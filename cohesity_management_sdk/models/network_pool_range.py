# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NetworkPoolRange(object):

    """Implementation of the 'NetworkPoolRange' model.

    Specifies the IP address range for the network pool.

    Attributes:
        high (string): Specifies the high range of the IP address.
        low (string):Specifies the low range of the IP address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "high": 'high',
        "low": 'low'
    }

    def __init__(self,
                 high=None,
                 low=None):
        """Constructor for the NetworkPoolRange class"""

        # Initialize members of the class
        self.high = high
        self.low = low


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The highs
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        high = dictionary.get('high')
        low = dictionary.get('low')

        # Return an object of this model
        return cls(high,
                   low)


