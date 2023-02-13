# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_info

class ClusterConfigProto_Vault_CloudTierSetting(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudTierSetting' model.

    Proto representing snapshot tier setting for a cloud target.

    Attributes:
        tier_info_vec (list of ClusterConfigProto_Vault_CloudTierInfo): Information
            about tiering/migrating the cloud snapshots.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tier_info_vec":'tierInfoVec'
    }

    def __init__(self,
                 tier_info_vec=None):
        """Constructor for the ClusterConfigProto_Vault_CloudTierSetting class"""

        # Initialize members of the class
        self.tier_info_vec = tier_info_vec


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
        tier_info_vec = None
        if dictionary.get('tierInfoVec') != None:
            tier_info_vec = list()
            for structure in dictionary.get('tierInfoVec'):
                tier_info_vec.append(cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_info.ClusterConfigProto_Vault_CloudTierInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(tier_info_vec)


