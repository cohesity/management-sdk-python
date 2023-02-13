# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.consumer_stats

class GetConsumerStatsResult(object):

    """Implementation of the 'GetConsumerStatsResult' model.

    GetConsumerStatsResult is the result of get consumerStats api.

    Attributes:
        cookie (string): Specifies an opaque string to pass to get the next
            set of active opens. If null is returned, this response is the
            last set of active opens.
        stats_list (list of ConsumerStats): Specifies a list of consumer
            stats.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cookie":'cookie',
        "stats_list":'statsList'
    }

    def __init__(self,
                 cookie=None,
                 stats_list=None):
        """Constructor for the GetConsumerStatsResult class"""

        # Initialize members of the class
        self.cookie = cookie
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
        cookie = dictionary.get('cookie')
        stats_list = None
        if dictionary.get('statsList') != None:
            stats_list = list()
            for structure in dictionary.get('statsList'):
                stats_list.append(cohesity_management_sdk.models.consumer_stats.ConsumerStats.from_dictionary(structure))

        # Return an object of this model
        return cls(cookie,
                   stats_list)


