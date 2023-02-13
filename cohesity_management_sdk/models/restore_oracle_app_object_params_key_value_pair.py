# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreOracleAppObjectParams_KeyValuePair(object):

    """Implementation of the 'RestoreOracleAppObjectParams_KeyValuePair' model.

    This defines the restore Shell environment.

    Attributes:
        x_key (string): Name of the key.
        x_value (string): Value of the key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "x_key": 'xKey',
        "x_value": 'xValue'
    }

    def __init__(self,
                 x_key=None,
                 x_value=None):
        """Constructor for the RestoreOracleAppObjectParams_KeyValuePair class"""

        # Initialize members of the class
        self.x_key = x_key
        self.x_value = x_value


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
        x_key = dictionary.get('xKey', None)
        x_value = dictionary.get('xValue', None)

        # Return an object of this model
        return cls(x_key,
                   x_value)


