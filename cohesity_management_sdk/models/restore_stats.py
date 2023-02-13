# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_env_stats

class RestoreStats(object):

    """Implementation of the 'RestoreStats' model.

    Specifies the restore statistics details.

    Attributes:
        num_cloned_objects (long|int): Specifies the count of cloned objects
            in the given time frame.
        num_recovered_objects (long|int): Specifies the count of recovered
            objects in the given time frame.
        stats_by_environment (list of RestoreEnvStats): Specifies the stats of
            recovery jobs aggregated by the environment type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_cloned_objects":'numClonedObjects',
        "num_recovered_objects":'numRecoveredObjects',
        "stats_by_environment":'statsByEnvironment'
    }

    def __init__(self,
                 num_cloned_objects=None,
                 num_recovered_objects=None,
                 stats_by_environment=None):
        """Constructor for the RestoreStats class"""

        # Initialize members of the class
        self.num_cloned_objects = num_cloned_objects
        self.num_recovered_objects = num_recovered_objects
        self.stats_by_environment = stats_by_environment


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
        num_cloned_objects = dictionary.get('numClonedObjects')
        num_recovered_objects = dictionary.get('numRecoveredObjects')
        stats_by_environment = None
        if dictionary.get('statsByEnvironment') != None:
            stats_by_environment = list()
            for structure in dictionary.get('statsByEnvironment'):
                stats_by_environment.append(cohesity_management_sdk.models.restore_env_stats.RestoreEnvStats.from_dictionary(structure))

        # Return an object of this model
        return cls(num_cloned_objects,
                   num_recovered_objects,
                   stats_by_environment)


