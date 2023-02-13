# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SendSnmpTestTrapResult(object):

    """Implementation of the 'SendSnmpTestTrapResult' model.

    Specifies the result returned after a successful request to send
    SNMP Test Trap.

    Attributes:
        message (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message":'message'
    }

    def __init__(self,
                 message=None):
        """Constructor for the SendSnmpTestTrapResult class"""

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


