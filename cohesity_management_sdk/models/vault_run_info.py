# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VaultRunInfo(object):

    """Implementation of the 'VaultRunInfo' model.

    Specifies the information about a specific vault run.

    Attributes:
        count (long|int): Specifies the count of runs that ended in the
            specified state between the start time passed in and the current
            timestamp.
        timestamp (long|int): Specifies the Unix timestamp at which the run
            entered the specified state.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "timestamp":'timestamp'
    }

    def __init__(self,
                 count=None,
                 timestamp=None):
        """Constructor for the VaultRunInfo class"""

        # Initialize members of the class
        self.count = count
        self.timestamp = timestamp


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
        count = dictionary.get('count')
        timestamp = dictionary.get('timestamp')

        # Return an object of this model
        return cls(count,
                   timestamp)


