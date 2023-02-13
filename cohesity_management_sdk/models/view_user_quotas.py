# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_and_usage_in_view
import cohesity_management_sdk.models.user_quota_summary_for_user
import cohesity_management_sdk.models.user_quota_summary_for_view
import cohesity_management_sdk.models.user_quota_settings
import cohesity_management_sdk.models.user_quota_and_usage

class ViewUserQuotas(object):

    """Implementation of the 'ViewUserQuotas' model.

    Specifies the Result parameters for all user quotas
    of a view.

    Attributes:
        cookie (string): This cookie can be used in the succeeding call to
            list user quotas and usages to get the next set of user quota
            overrides. If set to nil, it means that there's no more results
            that the server could provide.
        quota_and_usage_in_all_views (list of QuotaAndUsageInView): The quota
            and usage information for a user in all his views.
        summary_for_user (UserQuotaSummaryForUser): UserQuotaSummaryForUser is
            the summary for user quotas in all views for a user.
        summary_for_view (UserQuotaSummaryForView): UserQuotaSummaryForView is
            the summary for user quotas in a view.
        user_quota_settings (UserQuotaSettings): The default user quota policy
            for this view.
        users_quota_and_usage (list of UserQuotaAndUsage): The list of user
            quota policies/overrides and usages.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cookie":'cookie',
        "quota_and_usage_in_all_views":'quotaAndUsageInAllViews',
        "summary_for_user":'summaryForUser',
        "summary_for_view":'summaryForView',
        "user_quota_settings":'userQuotaSettings',
        "users_quota_and_usage":'usersQuotaAndUsage'
    }

    def __init__(self,
                 cookie=None,
                 quota_and_usage_in_all_views=None,
                 summary_for_user=None,
                 summary_for_view=None,
                 user_quota_settings=None,
                 users_quota_and_usage=None):
        """Constructor for the ViewUserQuotas class"""

        # Initialize members of the class
        self.cookie = cookie
        self.quota_and_usage_in_all_views = quota_and_usage_in_all_views
        self.summary_for_user = summary_for_user
        self.summary_for_view = summary_for_view
        self.user_quota_settings = user_quota_settings
        self.users_quota_and_usage = users_quota_and_usage


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
        quota_and_usage_in_all_views = None
        if dictionary.get('quotaAndUsageInAllViews') != None:
            quota_and_usage_in_all_views = list()
            for structure in dictionary.get('quotaAndUsageInAllViews'):
                quota_and_usage_in_all_views.append(cohesity_management_sdk.models.quota_and_usage_in_view.QuotaAndUsageInView.from_dictionary(structure))
        summary_for_user = cohesity_management_sdk.models.user_quota_summary_for_user.UserQuotaSummaryForUser.from_dictionary(dictionary.get('summaryForUser')) if dictionary.get('summaryForUser') else None
        summary_for_view = cohesity_management_sdk.models.user_quota_summary_for_view.UserQuotaSummaryForView.from_dictionary(dictionary.get('summaryForView')) if dictionary.get('summaryForView') else None
        user_quota_settings = cohesity_management_sdk.models.user_quota_settings.UserQuotaSettings.from_dictionary(dictionary.get('userQuotaSettings')) if dictionary.get('userQuotaSettings') else None
        users_quota_and_usage = None
        if dictionary.get('usersQuotaAndUsage') != None:
            users_quota_and_usage = list()
            for structure in dictionary.get('usersQuotaAndUsage'):
                users_quota_and_usage.append(cohesity_management_sdk.models.user_quota_and_usage.UserQuotaAndUsage.from_dictionary(structure))

        # Return an object of this model
        return cls(cookie,
                   quota_and_usage_in_all_views,
                   summary_for_user,
                   summary_for_view,
                   user_quota_settings,
                   users_quota_and_usage)


