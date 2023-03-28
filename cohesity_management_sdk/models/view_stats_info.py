# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.view_stats_in_last_hours


class ViewStatsInfo(object):

    """Implementation of the 'ViewStatsInfo' model.

    Specifies the View stats.


    Attributes:

        metric (string): Specifies the stats metric.
        value_in_last_hours (list of ViewStatsInLastHours): Specifies the stats
            value in last hours.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "metric":'metric',
        "value_in_last_hours":'valueInLastHours',
    }
    def __init__(self,
                 metric=None,
                 value_in_last_hours=None,
            ):

        """Constructor for the ViewStatsInfo class"""

        # Initialize members of the class
        self.metric = metric
        self.value_in_last_hours = value_in_last_hours

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
        metric = dictionary.get('metric')
        value_in_last_hours = None
        if dictionary.get('valueInLastHours') != None:
            value_in_last_hours = list()
            for structure in dictionary.get('valueInLastHours'):
                value_in_last_hours.append(cohesity_management_sdk.models.view_stats_in_last_hours.ViewStatsInLastHours.from_dictionary(structure))

        # Return an object of this model
        return cls(
            metric,
            value_in_last_hours
)