# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LinuxSupportUserSudoAccessResult(object):

    """Implementation of the 'LinuxSupportUserSudoAccessResult' model.

    Specifies the result returned after a successful request to enable/disable
    the linux 'support' user sudo access.

    Attributes:
        result (string): Date format is in MM/DD/YYYY HH:MM:SS
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "result":'result'
    }

    def __init__(self,
                 result=None):
        """Constructor for the LinuxSupportUserSudoAccessResult class"""

        # Initialize members of the class
        self.result = result


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
        result = dictionary.get('result')

        # Return an object of this model
        return cls(result)


