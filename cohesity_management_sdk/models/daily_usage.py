# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DailyUsage(object):

    """Implementation of the 'DailyUsage' model.

    TODO: Type model description here.

    Attributes:
        daily_usage (list of long|int): TODO: Type description here.
        feature_name (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "daily_usage": 'dailyUsage',
        "feature_name": 'featureName'
    }

    def __init__(self,
                 daily_usage=None,
                 feature_name=None):
        """Constructor for the DailyUsage class"""

        # Initialize members of the class
        self.daily_usage = daily_usage
        self.feature_name = feature_name


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
        daily_usage = dictionary.get('dailyUsage', None)
        feature_name = dictionary.get('featureName', None)

        # Return an object of this model
        return cls(daily_usage,
                   feature_name)


