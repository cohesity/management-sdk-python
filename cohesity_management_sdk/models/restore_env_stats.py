# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreEnvStats(object):

    """Implementation of the 'RestoreEnvStats' model.

    Specifies the aggregated statistics for restores of a specific environment
    type.

    Attributes:
        environment (EnvironmentRestoreEnvStatsEnum): Specifies the
            environment.
        object_count (long|int): TODO: type description here.
        total_bytes (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "object_count":'objectCount',
        "total_bytes":'totalBytes'
    }

    def __init__(self,
                 environment=None,
                 object_count=None,
                 total_bytes=None):
        """Constructor for the RestoreEnvStats class"""

        # Initialize members of the class
        self.environment = environment
        self.object_count = object_count
        self.total_bytes = total_bytes


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
        object_count = dictionary.get('objectCount')
        total_bytes = dictionary.get('totalBytes')

        # Return an object of this model
        return cls(environment,
                   object_count,
                   total_bytes)


