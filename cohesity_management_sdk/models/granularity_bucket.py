# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GranularityBucket(object):

    """Implementation of the 'GranularityBucket' model.

    Message that specifies the frequency granularity at which to copy the
    snapshots from a backup job's runs.

    Attributes:
        granularity (int): The base time period granularity that determines
            the frequency at which backup run snapshots will be copied.  NOTE:
            The granularity (in combination with the 'multiplier' field below)
            that is specified should be such that the frequency of copying
            snapshots is lower than the frequency of actually creating the
            snapshots (i.e., lower than the frequency of the backup job
            runs).
        multiplier (int): A factor to multiply the granularity by. For
            example, if this is 2 and the granularity is kHour, then snapshots
            from the first eligible run from every 2 hour period will be
            copied.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "granularity":'granularity',
        "multiplier":'multiplier'
    }

    def __init__(self,
                 granularity=None,
                 multiplier=None):
        """Constructor for the GranularityBucket class"""

        # Initialize members of the class
        self.granularity = granularity
        self.multiplier = multiplier


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
        granularity = dictionary.get('granularity')
        multiplier = dictionary.get('multiplier')

        # Return an object of this model
        return cls(granularity,
                   multiplier)


