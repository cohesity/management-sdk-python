# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.storage_domain_stats

class GetViewBoxStatsResult(object):

    """Implementation of the 'GetViewBoxStatsResult' model.

    GetViewBoxStatsResult is the result of get viewBoxStats api.

    Attributes:
        stats_list (list of StorageDomainStats): Specifies a list of view box
            stats.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "stats_list":'statsList'
    }

    def __init__(self,
                 stats_list=None):
        """Constructor for the GetViewBoxStatsResult class"""

        # Initialize members of the class
        self.stats_list = stats_list


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
        stats_list = None
        if dictionary.get('statsList') != None:
            stats_list = list()
            for structure in dictionary.get('statsList'):
                stats_list.append(cohesity_management_sdk.models.storage_domain_stats.StorageDomainStats.from_dictionary(structure))

        # Return an object of this model
        return cls(stats_list)


