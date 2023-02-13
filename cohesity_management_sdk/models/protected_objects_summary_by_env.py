# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectedObjectsSummaryByEnv(object):

    """Implementation of the 'ProtectedObjectsSummaryByEnv' model.

    Specifies the protection summary of given environment type.

    Attributes:
        environment (EnvironmentProtectedObjectsSummaryByEnvEnum): Specifies
            the environment.
        num_objects_protected (long|int): Specifies the total number of
            protected objects.
        num_objects_unprotected (long|int): Specifies the total number of
            unprotected objects.
        protected_size_bytes (long|int): Specifies the total size of protected
            objects in bytes.
        unprotected_size_bytes (long|int): Specifies the total size of
            unprotected objects in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "num_objects_protected":'numObjectsProtected',
        "num_objects_unprotected":'numObjectsUnprotected',
        "protected_size_bytes":'protectedSizeBytes',
        "unprotected_size_bytes":'unprotectedSizeBytes'
    }

    def __init__(self,
                 environment=None,
                 num_objects_protected=None,
                 num_objects_unprotected=None,
                 protected_size_bytes=None,
                 unprotected_size_bytes=None):
        """Constructor for the ProtectedObjectsSummaryByEnv class"""

        # Initialize members of the class
        self.environment = environment
        self.num_objects_protected = num_objects_protected
        self.num_objects_unprotected = num_objects_unprotected
        self.protected_size_bytes = protected_size_bytes
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
        environment = dictionary.get('environment')
        num_objects_protected = dictionary.get('numObjectsProtected')
        num_objects_unprotected = dictionary.get('numObjectsUnprotected')
        protected_size_bytes = dictionary.get('protectedSizeBytes')
        unprotected_size_bytes = dictionary.get('unprotectedSizeBytes')

        # Return an object of this model
        return cls(environment,
                   num_objects_protected,
                   num_objects_unprotected,
                   protected_size_bytes,
                   unprotected_size_bytes)


