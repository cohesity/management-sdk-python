# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectedObjectsByEnv(object):

    """Implementation of the 'ProtectedObjectsByEnv' model.

    Number of Protected Objects by Type.

    Attributes:
        env_type (string): Environment Type.
        protected_count (int): Number of Protected Objects.
        protected_size_bytes (long|int): Size of Protected Objects.
        unprotected_count (int): Number of Unprotected Objects.
        unprotected_size_bytes (long|int): Size of Unprotected Objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "env_type":'envType',
        "protected_count":'protectedCount',
        "protected_size_bytes":'protectedSizeBytes',
        "unprotected_count":'unprotectedCount',
        "unprotected_size_bytes":'unprotectedSizeBytes'
    }

    def __init__(self,
                 env_type=None,
                 protected_count=None,
                 protected_size_bytes=None,
                 unprotected_count=None,
                 unprotected_size_bytes=None):
        """Constructor for the ProtectedObjectsByEnv class"""

        # Initialize members of the class
        self.env_type = env_type
        self.protected_count = protected_count
        self.protected_size_bytes = protected_size_bytes
        self.unprotected_count = unprotected_count
        self.unprotected_size_bytes = unprotected_size_bytes


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
        env_type = dictionary.get('envType')
        protected_count = dictionary.get('protectedCount')
        protected_size_bytes = dictionary.get('protectedSizeBytes')
        unprotected_count = dictionary.get('unprotectedCount')
        unprotected_size_bytes = dictionary.get('unprotectedSizeBytes')

        # Return an object of this model
        return cls(env_type,
                   protected_count,
                   protected_size_bytes,
                   unprotected_count,
                   unprotected_size_bytes)


