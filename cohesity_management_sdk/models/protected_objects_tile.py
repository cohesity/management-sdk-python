# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protected_objects_by_env

class ProtectedObjectsTile(object):

    """Implementation of the 'ProtectedObjectsTile' model.

    Protected Objects information.

    Attributes:
        objects_protected (list of ProtectedObjectsByEnv): Protected Objects
            breakdown by object type.
        protected_count (int): Number of Protected Objects.
        protected_size_bytes (long|int): Size of Protected Objects.
        unprotected_count (int): Number of Unprotected Objects.
        unprotected_size_bytes (long|int): Size of Unprotected Objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "objects_protected":'objectsProtected',
        "protected_count":'protectedCount',
        "protected_size_bytes":'protectedSizeBytes',
        "unprotected_count":'unprotectedCount',
        "unprotected_size_bytes":'unprotectedSizeBytes'
    }

    def __init__(self,
                 objects_protected=None,
                 protected_count=None,
                 protected_size_bytes=None,
                 unprotected_count=None,
                 unprotected_size_bytes=None):
        """Constructor for the ProtectedObjectsTile class"""

        # Initialize members of the class
        self.objects_protected = objects_protected
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
        objects_protected = None
        if dictionary.get('objectsProtected') != None:
            objects_protected = list()
            for structure in dictionary.get('objectsProtected'):
                objects_protected.append(cohesity_management_sdk.models.protected_objects_by_env.ProtectedObjectsByEnv.from_dictionary(structure))
        protected_count = dictionary.get('protectedCount')
        protected_size_bytes = dictionary.get('protectedSizeBytes')
        unprotected_count = dictionary.get('unprotectedCount')
        unprotected_size_bytes = dictionary.get('unprotectedSizeBytes')

        # Return an object of this model
        return cls(objects_protected,
                   protected_count,
                   protected_size_bytes,
                   unprotected_count,
                   unprotected_size_bytes)


