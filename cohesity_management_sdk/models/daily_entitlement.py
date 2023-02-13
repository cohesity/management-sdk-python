# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DailyEntitlement(object):

    """Implementation of the 'DailyEntitlement' model.

    TODO: Type model description here.

    Attributes:
        daily_entitlement (list of long|int): TODO: Type description here.
        feature_name (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "daily_entitlement": 'dailyEntitlement',
        "feature_name": 'featureName'
    }

    def __init__(self,
                 daily_entitlement=None,
                 feature_name=None):
        """Constructor for the DailyEntitlement class"""

        # Initialize members of the class
        self.daily_entitlement = daily_entitlement
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
        daily_entitlement = dictionary.get('dailyEntitlement', None)
        feature_name = dictionary.get('featureName', None)

        # Return an object of this model
        return cls(daily_entitlement,
                   feature_name)


