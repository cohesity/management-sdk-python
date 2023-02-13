# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_usage_stats

class ViewStats(object):

    """Implementation of the 'ViewStats' model.

    Provides statistics about the View.

    Attributes:
        data_usage_stats (DataUsageStats): Specifies the data usage
            metric of the data stored in this View.
        id (long|int): Specifies the id of the View.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_usage_stats":'dataUsageStats',
        "id":'id'
    }

    def __init__(self,
                 data_usage_stats=None,
                 id=None):
        """Constructor for the ViewStats class"""

        # Initialize members of the class
        self.data_usage_stats = data_usage_stats
        self.id = id


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
        data_usage_stats = cohesity_management_sdk.models.data_usage_stats.DataUsageStats.from_dictionary(dictionary.get('dataUsageStats')) if dictionary.get('dataUsageStats') else None
        id = dictionary.get('id')

        # Return an object of this model
        return cls(data_usage_stats,
                   id)


