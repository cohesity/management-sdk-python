# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HostResult(object):

    """Implementation of the 'HostResult' model.

    Specifies the response received after requesting a PUT, POST, or DELETE
    method on the /network/hosts endpoint.

    Attributes:
        message (string): Specifies a message describing the status of the
            Hosts request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message":'message'
    }

    def __init__(self,
                 message=None):
        """Constructor for the HostResult class"""

        # Initialize members of the class
        self.message = message


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
        message = dictionary.get('message')

        # Return an object of this model
        return cls(message)


