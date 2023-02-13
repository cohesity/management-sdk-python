# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.network_params

class Interface(object):

    """Implementation of the 'Interface' model.

    TODO: type model description here.

    Attributes:
        message (string): TODO: type description here.
        name (string): TODO: type description here.
        network_params (NetworkParams): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message":'message',
        "name":'name',
        "network_params":'networkParams'
    }

    def __init__(self,
                 message=None,
                 name=None,
                 network_params=None):
        """Constructor for the Interface class"""

        # Initialize members of the class
        self.message = message
        self.name = name
        self.network_params = network_params


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
        name = dictionary.get('name')
        network_params = cohesity_management_sdk.models.network_params.NetworkParams.from_dictionary(dictionary.get('networkParams')) if dictionary.get('networkParams') else None

        # Return an object of this model
        return cls(message,
                   name,
                   network_params)


