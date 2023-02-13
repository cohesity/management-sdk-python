# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UserSshKey(object):

    """Implementation of the 'UserSshKey' model.

    UserSshKey specifies username and ssh key.

    Attributes:
        ssh_key (string): Specifies SSH key needed to be added to the username
            passed.
        username (string): Specifies name of the user to add.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ssh_key":'sshKey',
        "username":'username'
    }

    def __init__(self,
                 ssh_key=None,
                 username=None):
        """Constructor for the UserSshKey class"""

        # Initialize members of the class
        self.ssh_key = ssh_key
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
        ssh_key = dictionary.get('sshKey')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(ssh_key,
                   username)


