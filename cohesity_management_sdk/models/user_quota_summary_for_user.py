# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UserQuotaSummaryForUser(object):

    """Implementation of the 'UserQuotaSummaryForUser' model.

    Speifies the summary of quota information for a particular user.

    Attributes:
        num_views_above_alert_threshold (int): Number of views in which user
            has exceeded alert threshold limit.
        num_views_above_hard_limit (int): Number of views in which the user
            has exceeded hard limit.
        total_num_views (int): Total number of views in which the user has a
            quota policy specified or has non-zero usage.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_views_above_alert_threshold":'numViewsAboveAlertThreshold',
        "num_views_above_hard_limit":'numViewsAboveHardLimit',
        "total_num_views":'totalNumViews'
    }

    def __init__(self,
                 num_views_above_alert_threshold=None,
                 num_views_above_hard_limit=None,
                 total_num_views=None):
        """Constructor for the UserQuotaSummaryForUser class"""

        # Initialize members of the class
        self.num_views_above_alert_threshold = num_views_above_alert_threshold
        self.num_views_above_hard_limit = num_views_above_hard_limit
        self.total_num_views = total_num_views


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
        num_views_above_alert_threshold = dictionary.get('numViewsAboveAlertThreshold')
        num_views_above_hard_limit = dictionary.get('numViewsAboveHardLimit')
        total_num_views = dictionary.get('totalNumViews')

        # Return an object of this model
        return cls(num_views_above_alert_threshold,
                   num_views_above_hard_limit,
                   total_num_views)


