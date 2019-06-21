# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class HypervBackupEnvParams(object):

    """Implementation of the 'HyperVBackupEnvParams' model.

    Message to capture any additional backup params for a HyperV environment.

    Attributes:
        allow_crash_consistent_snapshot (bool): Whether to fallback to take a
            crash-consistent snapshot incase taking an app-consistent snapshot
            fails.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_crash_consistent_snapshot":'allowCrashConsistentSnapshot'
    }

    def __init__(self,
                 allow_crash_consistent_snapshot=None):
        """Constructor for the HypervBackupEnvParams class"""

        # Initialize members of the class
        self.allow_crash_consistent_snapshot = allow_crash_consistent_snapshot


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
        allow_crash_consistent_snapshot = dictionary.get('allowCrashConsistentSnapshot')

        # Return an object of this model
        return cls(allow_crash_consistent_snapshot)


