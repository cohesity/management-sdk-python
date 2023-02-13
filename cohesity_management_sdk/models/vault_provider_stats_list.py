# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_provider_stats_info

class VaultProviderStatsList(object):

    """Implementation of the 'VaultProviderStatsList' model.

    Specifies the stats by provider for each vault.

    Attributes:
    vault_provider_stats_info (list of VaultProviderStatsInfo)
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault_provider_stats_info":'VaultProviderStatsInfo'
    }

    def __init__(self,
                 vault_provider_stats_info=None):
        """Constructor for the VaultProviderStatsList class"""

        # Initialize members of the class
        self.vault_provider_stats_info = vault_provider_stats_info


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
        vault_provider_stats_info = cohesity_management_sdk.models.vault_provider_stats_info.VaultProviderStatsInfo.from_dictionary(dictionary.get('VaultProviderStatsInfo')) if dictionary.get('VaultProviderStatsInfo') else None

        # Return an object of this model
        return cls(vault_provider_stats_info)


