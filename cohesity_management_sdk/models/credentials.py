# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Credentials(object):

    """Implementation of the 'Credentials' model.

    Specifies credentials to access a target source.

    Attributes:
        password (string): Specifies password of the username to access the
            target source.
        username (string): Specifies username to access the target source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "password":'password',
        "username":'username'
    }

    def __init__(self,
                 password=None,
                 username=None):
        """Constructor for the Credentials class"""

        # Initialize members of the class
        self.password = password
        self.username = username


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
        password = dictionary.get('password')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(password,
                   username)


