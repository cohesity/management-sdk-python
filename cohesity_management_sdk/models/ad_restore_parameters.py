# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.credentials

class AdRestoreParameters(object):

    """Implementation of the 'AdRestoreParameters' model.

    Specifies the parameters specific to Application domain controller.

    Attributes:
        credentials (Credentials): Specifies credentials to access a target
            source.
        port (int): Specifies the port on which the AD domain controller's
            NTDS database will be mounted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credentials":'credentials',
        "port":'port'
    }

    def __init__(self,
                 credentials=None,
                 port=None):
        """Constructor for the AdRestoreParameters class"""

        # Initialize members of the class
        self.credentials = credentials
        self.port = port


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
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        port = dictionary.get('port')

        # Return an object of this model
        return cls(credentials,
                   port)


