# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HostInfo(object):

    """Implementation of the 'HostInfo' model.

    Specifies the list of all hosts on which the certificate is deployed.

    Attributes:
        password (string): Specifies the password of the host to establish
            SSH connection. The certificate is copied to the host after
            generating the certificate on the cluster.
        server_name (string): Specifies the servername of the host where
            certificate is to be deployed.
        target (string): Specifies the target location on the host where the
            certificate is deployed.
        user_name (string): Specifies the username of the host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "password":'password',
        "server_name":'serverName',
        "target":'target',
        "user_name":'userName'
    }

    def __init__(self,
                 password=None,
                 server_name=None,
                 target=None,
                 user_name=None):
        """Constructor for the HostInfo class"""

        # Initialize members of the class
        self.password = password
        self.server_name = server_name
        self.target = target
        self.user_name = user_name


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
        server_name = dictionary.get('serverName')
        target = dictionary.get('target')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(password,
                   server_name,
                   target,
                   user_name)


