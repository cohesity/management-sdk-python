# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.feature_usage
import cohesity_management_sdk.models.licensed_usage
import cohesity_management_sdk.models.overusage

class LicenseAccountUsageRsp(object):

    """Implementation of the 'LicenseAccountUsageRsp' model.

    Structure to hold account usage response

    Attributes:
        feature_over_usage (list of Overusage): Holds information about
            consumption usage of overused features.
        free_setup_mode (bool): Free setup mode.
        is_trail (bool): Check if trial license.
        last_update_time (int): Last time, this report was updated.
        licensed_usage (list of LicensedUsage): LicenseFeatureUsages holds information
            about each feature from license orders.
        trial_expiration (int): Trial expiration period.
        usage (dict<object, list of FeatureUsage>): Creating a map of cluster
            id and feature usage to make it consistent display usage UI for
            the helios server license page UI.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_over_usage":'featureOverUsage',
        "free_setup_mode":'freeSetupNode',
        "is_trail":'isTrail',
        "last_update_time":'lastUpdateTime',
        "licensed_usage":'licensedUsage',
        "trial_expiration":'trialExpiration',
        "usage":'usage'
    }

    def __init__(self,
                 feature_over_usage=None,
                 free_setup_mode=None,
                 is_trail=None,
                 last_update_time=None,
                 licensed_usage=None,
                 trial_expiration=None,
                 usage=None):
        """Constructor for the LicenseAccountUsageRsp class"""

        # Initialize members of the class
        self.feature_over_usage = feature_over_usage
        self.free_setup_mode = free_setup_mode
        self.is_trail = is_trail
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
        feature_over_usage = None
        if dictionary.get('featureOverUsage') != None:
            feature_over_usage = list()
            for structure in dictionary.get('featureOverUsage'):
                feature_over_usage.append(cohesity_management_sdk.models.overusage.Overusage.from_dictionary(structure))
        free_setup_mode = dictionary.get('freeSetupNode')
        is_trail = dictionary.get('isTrail')
        last_update_time = dictionary.get('lastUpdateTime')
        licensed_usage = None
        if dictionary.get('licensedUsage') != None:
            licensed_usage = list()
            for structure in dictionary.get('licensedUsage'):
                licensed_usage.append(cohesity_management_sdk.models.licensed_usage.LicensedUsage.from_dictionary(structure))
        trial_expiration = dictionary.get('trialExpiration')
        usage = dictionary.get('usage')

        # Return an object of this model
        return cls(feature_over_usage,
                   free_setup_mode,
                   is_trail,
                   last_update_time,
                   licensed_usage,
                   trial_expiration,
                   usage)

