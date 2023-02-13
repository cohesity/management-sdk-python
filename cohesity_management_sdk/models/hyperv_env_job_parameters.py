# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HypervEnvJobParameters(object):

    """Implementation of the 'HypervEnvJobParameters' model.

    Specifies job parameters applicable for all 'kHyperV' Environment type
    Protection Sources in a Protection Job.

    Attributes:
        fallback_to_crash_consistent (bool): If true, takes a crash-consistent
            snapshot when app-consistent snapshot fails. Otherwise, the
            snapshot attempt is marked failed. By default, this field is set
            to false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fallback_to_crash_consistent":'fallbackToCrashConsistent'
    }

    def __init__(self,
                 fallback_to_crash_consistent=None):
        """Constructor for the HypervEnvJobParameters class"""

        # Initialize members of the class
        self.fallback_to_crash_consistent = fallback_to_crash_consistent


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
        fallback_to_crash_consistent = dictionary.get('fallbackToCrashConsistent')

        # Return an object of this model
        return cls(fallback_to_crash_consistent)


