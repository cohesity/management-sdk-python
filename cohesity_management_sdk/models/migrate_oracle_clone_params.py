# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MigrateOracleCloneParams(object):

    """Implementation of the 'MigrateOracleCloneParams' model.

    OracleUpdateRestoreTaskOptions encapsulates information needed for
    executing migration of a successful Oracle Clone task.

    Attributes:
        delay_secs (long|int): The delay in secs, after which the migration of
            the Clone should be triggered.
            "0" - Means the Migration should start as soon as the Clone
            successfully finished. That is the default behaviour.

            0 < - Means the migration will start when user triggers migration
            from UI.

            > 0 - Means the delay in seconds after which the migration of the
            clone would be triggered. [ For now this is not supported ]

        target_path_vec (list of string): Vector of paths where the contents
            (i.e. datafile/redo-logs) of the clone DB will be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delay_secs": 'delaySecs',
        "target_path_vec": 'targetPathVec'
    }

    def __init__(self,
                 delay_secs=None,
                 target_path_vec=None):
        """Constructor for the MigrateOracleCloneParams class"""

        # Initialize members of the class
        self.delay_secs = delay_secs
        self.target_path_vec = target_path_vec


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
        delay_secs = dictionary.get('delaySecs', None)
        target_path_vec = dictionary.get('targetPathVec', None)

        # Return an object of this model
        return cls(delay_secs,
                   target_path_vec)


