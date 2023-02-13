# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.view_stat_info

class ViewStatsSnapshot(object):

    """Implementation of the 'ViewStatsSnapshot' model.

    Specifies the list statistics for each View for a given timestamp.

    Attributes:
        timestamp (long|int): Specifies the unix time in milliseconds when
            these values were generated
        view_stats_list (list of ViewStatInfo): Specifies the list of Views
            and their statistics at the given timestamp.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp":'timestamp',
        "view_stats_list":'viewStatsList'
    }

    def __init__(self,
                 timestamp=None,
                 view_stats_list=None):
        """Constructor for the ViewStatsSnapshot class"""

        # Initialize members of the class
        self.timestamp = timestamp
        self.view_stats_list = view_stats_list


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
        timestamp = dictionary.get('timestamp')
        view_stats_list = None
        if dictionary.get('viewStatsList') != None:
            view_stats_list = list()
            for structure in dictionary.get('viewStatsList'):
                view_stats_list.append(cohesity_management_sdk.models.view_stat_info.ViewStatInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(timestamp,
                   view_stats_list)


