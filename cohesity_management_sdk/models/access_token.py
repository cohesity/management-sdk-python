# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AccessToken(object):

    """Implementation of the 'AccessToken' model.

    Specifies an Access Token that provides permissions for a client to
    access
    the Cohesity REST API available from a Cohesity Cluster.

    Attributes:
        access_token (string): Generated access token.
        privileges (list of string): Privileges for the user.
        token_type (string): Access token type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_token":'accessToken',
        "privileges":'privileges',
        "token_type":'tokenType'
    }

    def __init__(self,
                 access_token=None,
                 privileges=None,
                 token_type=None):
        """Constructor for the AccessToken class"""

        # Initialize members of the class
        self.access_token = access_token
        self.privileges = privileges
        self.token_type = token_type


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
        access_token = dictionary.get('accessToken')
        privileges = dictionary.get('privileges')
        token_type = dictionary.get('tokenType')

        # Return an object of this model
        return cls(access_token,
                   privileges,
                   token_type)


