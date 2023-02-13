# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LogicalStats(object):

    """Implementation of the 'LogicalStats' model.

    Provides the combined data residing on protected objects. The size of data
    before reduction by deduplication and compression.

    Attributes:
        total_logical_usage_bytes (long|int): Provides the logical usage as
            computed by the Cohesity Cluster. The size of the data without
            reduction by change-block tracking, compression and
            deduplication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_logical_usage_bytes":'totalLogicalUsageBytes'
    }

    def __init__(self,
                 total_logical_usage_bytes=None):
        """Constructor for the LogicalStats class"""

        # Initialize members of the class
        self.total_logical_usage_bytes = total_logical_usage_bytes


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
        total_logical_usage_bytes = dictionary.get('totalLogicalUsageBytes')

        # Return an object of this model
        return cls(total_logical_usage_bytes)


