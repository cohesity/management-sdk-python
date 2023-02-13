# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MonthlyEntitlement(object):

    """Implementation of the 'MonthlyEntitlement' model.

    TODO: Type model description here.

    Attributes:
        feature_name (string): TODO: Type description here.
        monthly_avg_entitlement (list of long|int): TODO: Type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_name": 'featureName',
        "monthly_avg_entitlement": 'monthlyAvgEntitlement'
    }

    def __init__(self,
                 feature_name=None,
                 monthly_avg_entitlement=None):
        """Constructor for the MonthlyEntitlement class"""

        # Initialize members of the class
        self.feature_name = feature_name
        self.monthly_avg_entitlement = monthly_avg_entitlement


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
        feature_name = dictionary.get('featureName', None)
        monthly_avg_entitlement = dictionary.get('monthlyAvgEntitlement', None)

        # Return an object of this model
        return cls(feature_name,
                   monthly_avg_entitlement)


