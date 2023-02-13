# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class KubernetesCredentials(object):

    """Implementation of the 'KubernetesCredentials' model.

    Specifies the credentials to authenticate with a Kubernetes Cluster.

    Attributes:
        client_private_key (string): Specifies Client private associated with
            the service account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_private_key":'clientPrivateKey'
    }

    def __init__(self,
                 client_private_key=None):
        """Constructor for the KubernetesCredentials class"""

        # Initialize members of the class
        self.client_private_key = client_private_key


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
        client_private_key = dictionary.get('clientPrivateKey')

        # Return an object of this model
        return cls(client_private_key)


