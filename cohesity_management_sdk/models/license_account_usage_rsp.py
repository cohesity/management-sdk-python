# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.licensed_usage
import cohesity_management_sdk.models.overusage


class LicenseAccountUsageRsp(object):

    """Implementation of the 'LicenseAccountUsageRsp' model.

    Structure to hold account usage response


    Attributes:

        feature_overusage (list of Overusage): Holds information about
            consumption usage of overused features
        free_setup_mode (bool): Free Setup Mode
        is_trial (bool): Check if trial license.
        last_12_months_avg_entitlement (object): Holds monthly avg usage values
            of feature
        last_12_months_avg_usage (object): Holds monthly avg usage values of
            feature
        last_30_days_entitlement (object): Holds daily entitled capacity values
            of feature
        last_30_days_usage (object): Holds daily usage values of feature
        last_update_time (long|int): Last time, this report was updated.
        licensed_usage (list of LicensedUsage): LicenseFeatureUsages holds
            information about each feature from license orders.
        trial_expiration (long|int): Trial expiration period.
        usage (object): Creating a map of cluster id and feature usage to make
            it consistent display usage UI for the helios server license page
            UI.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "feature_overusage":'featureOverusage',
        "free_setup_mode":'freeSetupMode',
        "is_trial":'isTrial',
        "last_12_months_avg_entitlement":'last12MonthsAvgEntitlement',
        "last_12_months_avg_usage":'last12MonthsAvgUsage',
        "last_30_days_entitlement":'last30DaysEntitlement',
        "last_30_days_usage":'last30DaysUsage',
        "last_update_time":'lastUpdateTime',
        "licensed_usage":'licensedUsage',
        "trial_expiration":'trialExpiration',
        "usage":'usage',
    }
    def __init__(self,
                 feature_overusage=None,
                 free_setup_mode=None,
                 is_trial=None,
                 last_12_months_avg_entitlement=None,
                 last_12_months_avg_usage=None,
                 last_30_days_entitlement=None,
                 last_30_days_usage=None,
                 last_update_time=None,
                 licensed_usage=None,
                 trial_expiration=None,
                 usage=None,
            ):

        """Constructor for the LicenseAccountUsageRsp class"""

        # Initialize members of the class
        self.feature_overusage = feature_overusage
        self.free_setup_mode = free_setup_mode
        self.is_trial = is_trial
        self.last_12_months_avg_entitlement = last_12_months_avg_entitlement
        self.last_12_months_avg_usage = last_12_months_avg_usage
        self.last_30_days_entitlement = last_30_days_entitlement
        self.last_30_days_usage = last_30_days_usage
        self.last_update_time = last_update_time
        self.licensed_usage = licensed_usage
        self.trial_expiration = trial_expiration
        self.usage = usage

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
        feature_overusage = None
        if dictionary.get('featureOverusage') != None:
            feature_overusage = list()
            for structure in dictionary.get('featureOverusage'):
                feature_overusage.append(cohesity_management_sdk.models.overusage.Overusage.from_dictionary(structure))
        free_setup_mode = dictionary.get('freeSetupMode')
        is_trial = dictionary.get('isTrial')
        last_12_months_avg_entitlement = dictionary.get('last12MonthsAvgEntitlement')
        last_12_months_avg_usage = dictionary.get('last12MonthsAvgUsage')
        last_30_days_entitlement = dictionary.get('last30DaysEntitlement')
        last_30_days_usage = dictionary.get('last30DaysUsage')
        last_update_time = dictionary.get('lastUpdateTime')
        licensed_usage = None
        if dictionary.get('licensedUsage') != None:
            licensed_usage = list()
            for structure in dictionary.get('licensedUsage'):
                licensed_usage.append(cohesity_management_sdk.models.licensed_usage.LicensedUsage.from_dictionary(structure))
        trial_expiration = dictionary.get('trialExpiration')
        usage = dictionary.get('usage')

        # Return an object of this model
        return cls(
            feature_overusage,
            free_setup_mode,
            is_trial,
            last_12_months_avg_entitlement,
            last_12_months_avg_usage,
            last_30_days_entitlement,
            last_30_days_usage,
            last_update_time,
            licensed_usage,
            trial_expiration,
            usage
)