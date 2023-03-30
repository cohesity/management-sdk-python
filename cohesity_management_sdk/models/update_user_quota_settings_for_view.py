# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy


class UpdateUserQuotaSettingsForView(object):

    """Implementation of the 'UpdateUserQuotaSettingsForView' model.

    Specifies the parameters to update user quota metadata in a view.


    Attributes:

        default_user_quota_policy (QuotaPolicy): The default user quota policy
            for this view.
        enable_user_quota (bool): If set, it enables/disables the user quota
            overrides for a view. Otherwise, it leaves it at it's previous
            state.
        inherit_default_policy_from_viewbox (bool): If set to true, the
            default_policy in view metadata will be cleared and the default
            policy from viewbox will take effect for all users in the view.
        view_name (string): View name of input view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "default_user_quota_policy":'defaultUserQuotaPolicy',
        "enable_user_quota":'enableUserQuota',
        "inherit_default_policy_from_viewbox":'inheritDefaultPolicyFromViewbox',
        "view_name":'viewName',
    }
    def __init__(self,
                 default_user_quota_policy=None,
                 enable_user_quota=None,
                 inherit_default_policy_from_viewbox=None,
                 view_name=None,
            ):

        """Constructor for the UpdateUserQuotaSettingsForView class"""

        # Initialize members of the class
        self.default_user_quota_policy = default_user_quota_policy
        self.enable_user_quota = enable_user_quota
        self.inherit_default_policy_from_viewbox = inherit_default_policy_from_viewbox
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
        default_user_quota_policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('defaultUserQuotaPolicy')) if dictionary.get('defaultUserQuotaPolicy') else None
        enable_user_quota = dictionary.get('enableUserQuota')
        inherit_default_policy_from_viewbox = dictionary.get('inheritDefaultPolicyFromViewbox')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(
            default_user_quota_policy,
            enable_user_quota,
            inherit_default_policy_from_viewbox,
            view_name
)