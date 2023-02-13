# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protected_objects_summary_by_env

class ProtectedObjectsSummary(object):

    """Implementation of the 'ProtectedObjectsSummary' model.

    Specifies the statistics of the protected objects on the cluster.

    Attributes:
        num_objects_protected (long|int): Specifies the total number of
            protected objects.
        num_objects_unprotected (long|int): Specifies the total number of
            unprotected objects.
        protected_size_bytes (long|int): Specifies the total size of protected
            objects in bytes.
        stats_by_env (list of ProtectedObjectsSummaryByEnv): Specifies the
            stats of Protected objects by environment.
        unprotected_size_bytes (long|int): Specifies the total size of
            unprotected objects in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_objects_protected":'numObjectsProtected',
        "num_objects_unprotected":'numObjectsUnprotected',
        "protected_size_bytes":'protectedSizeBytes',
        "stats_by_env":'statsByEnv',
        "unprotected_size_bytes":'unprotectedSizeBytes'
    }

    def __init__(self,
                 num_objects_protected=None,
                 num_objects_unprotected=None,
                 protected_size_bytes=None,
                 stats_by_env=None,
                 unprotected_size_bytes=None):
        """Constructor for the ProtectedObjectsSummary class"""

        # Initialize members of the class
        self.num_objects_protected = num_objects_protected
        self.num_objects_unprotected = num_objects_unprotected
        self.protected_size_bytes = protected_size_bytes
        self.stats_by_env = stats_by_env
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
        num_objects_protected = dictionary.get('numObjectsProtected')
        num_objects_unprotected = dictionary.get('numObjectsUnprotected')
        protected_size_bytes = dictionary.get('protectedSizeBytes')
        stats_by_env = None
        if dictionary.get('statsByEnv') != None:
            stats_by_env = list()
            for structure in dictionary.get('statsByEnv'):
                stats_by_env.append(cohesity_management_sdk.models.protected_objects_summary_by_env.ProtectedObjectsSummaryByEnv.from_dictionary(structure))
        unprotected_size_bytes = dictionary.get('unprotectedSizeBytes')

        # Return an object of this model
        return cls(num_objects_protected,
                   num_objects_unprotected,
                   protected_size_bytes,
                   stats_by_env,
                   unprotected_size_bytes)


