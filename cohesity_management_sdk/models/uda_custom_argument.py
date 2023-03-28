# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UdaCustomArgument(object):

    """Implementation of the 'UdaCustomArgument' model.

    Wrapper for the custom arguments that are supplied to UDA scripts for the
    various workflows like regidtration, backup & recovery. This contains
    either a value or in case of sensitive data, an encrypted value.


    Attributes:

        encrypted_value (list of long|int): Encrypted value in case the custom
            argument contains sensitive data like passwords, tokens, etc.
        value (string): Value for the custom argument.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "encrypted_value":'encryptedValue',
        "value":'value',
    }
    def __init__(self,
                 encrypted_value=None,
                 value=None,
            ):

        """Constructor for the UdaCustomArgument class"""

        # Initialize members of the class
        self.encrypted_value = encrypted_value
        self.value = value

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
        encrypted_value = dictionary.get("encryptedValue")
        value = dictionary.get('value')

        # Return an object of this model
        return cls(
            encrypted_value,
            value
)