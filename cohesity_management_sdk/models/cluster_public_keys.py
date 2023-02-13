# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterPublicKeys(object):

    """Implementation of the 'ClusterPublicKeys' model.

    Specifies public keys stored on the Cluster.

    Attributes:
        ssh_public_key (string): Specifies the SSH public key used to login to
            Cluster nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ssh_public_key":'sshPublicKey'
    }

    def __init__(self,
                 ssh_public_key=None):
        """Constructor for the ClusterPublicKeys class"""

        # Initialize members of the class
        self.ssh_public_key = ssh_public_key


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
        ssh_public_key = dictionary.get('sshPublicKey')

        # Return an object of this model
        return cls(ssh_public_key)


