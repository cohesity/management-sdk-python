# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.user_quota

class ViewUserQuotaParameters(object):

    """Implementation of the 'ViewUserQuotaParameters' model.

    Specifies the params to create and edit a user quota policy in a view.

    Attributes:
        user_quota_policy (UserQuota): The user quota policies that need to be
            updated.
        view_name (string): View name of input view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_quota_policy":'userQuotaPolicy',
        "view_name":'viewName'
    }

    def __init__(self,
                 user_quota_policy=None,
                 view_name=None):
        """Constructor for the ViewUserQuotaParameters class"""

        # Initialize members of the class
        self.user_quota_policy = user_quota_policy
        self.view_name = view_name


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
        user_quota_policy = cohesity_management_sdk.models.user_quota.UserQuota.from_dictionary(dictionary.get('userQuotaPolicy')) if dictionary.get('userQuotaPolicy') else None
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(user_quota_policy,
                   view_name)


