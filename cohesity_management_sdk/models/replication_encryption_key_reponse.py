# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ReplicationEncryptionKeyReponse(object):

    """Implementation of the 'ReplicationEncryptionKeyReponse' model.

    Specifies the encryption key that is used for encrypting replication data
    from this Cluster to a remote Cluster.

    Attributes:
        encryption_key (string): Specifies a replication encryption key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "encryption_key":'encryptionKey'
    }

    def __init__(self,
                 encryption_key=None):
        """Constructor for the ReplicationEncryptionKeyReponse class"""

        # Initialize members of the class
        self.encryption_key = encryption_key


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
        encryption_key = dictionary.get('encryptionKey')

        # Return an object of this model
        return cls(encryption_key)


