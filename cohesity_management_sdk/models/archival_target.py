# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_setting

class ArchivalTarget(object):

    """Implementation of the 'ArchivalTarget' model.

    Message that specifies the details about an archival target (such as
    cloud
    or tape) where backup snapshots may be archived to.

    Attributes:
        cloud_tier_setting (ClusterConfigProto_Vault_CloudTierSetting):
        Tier settings in case of cloud target.
          Contains default tier type and information for moving snapshot data across
          cloud tiers.
        name (string): The name of the archival target.
        mtype (int): The type of the archival target.
        vault_id (long|int): The id of the archival vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_tier_setting":'cloud_tier_setting',
        "name":'name',
        "mtype":'type',
        "vault_id":'vaultId'
    }

    def __init__(self,
                 cloud_tier_setting=None,
                 name=None,
                 mtype=None,
                 vault_id=None):
        """Constructor for the ArchivalTarget class"""

        # Initialize members of the class
        self.cloud_tier_setting = cloud_tier_setting
        self.name = name
        self.mtype = mtype
        self.vault_id = vault_id


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
        cloud_tier_setting = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_setting.ClusterConfigProto_Vault_CloudTierSetting.from_dictionary(dictionary.get('cloudTierSetting')) if dictionary.get('cloudTierSetting') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        vault_id = dictionary.get('vaultId')

        # Return an object of this model
        return cls(cloud_tier_setting,
                   name,
                   mtype,
                   vault_id)


