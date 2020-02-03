# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.dir_quota_config
import cohesity_management_sdk.models.dir_quota_policy

class DirQuotaInfo(object):

    """Implementation of the 'DirQuotaInfo' model.

    Specifies the configuration and policy details for directory quota in a
    view.

    Attributes:
        config (DirQuotaConfig): Specifies the configuration object of a
            directory quota.
        quotas (list of DirQuotaPolicy): Specifies the list of directory quota
            policies applied on the view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "config":'config',
        "quotas":'quotas'
    }

    def __init__(self,
                 config=None,
                 quotas=None):
        """Constructor for the DirQuotaInfo class"""

        # Initialize members of the class
        self.config = config
        self.quotas = quotas


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
        config = cohesity_management_sdk.models.dir_quota_config.DirQuotaConfig.from_dictionary(dictionary.get('config')) if dictionary.get('config') else None
        quotas = None
        if dictionary.get('quotas') != None:
            quotas = list()
            for structure in dictionary.get('quotas'):
                quotas.append(cohesity_management_sdk.models.dir_quota_policy.DirQuotaPolicy.from_dictionary(structure))

        # Return an object of this model
        return cls(config,
                   quotas)


