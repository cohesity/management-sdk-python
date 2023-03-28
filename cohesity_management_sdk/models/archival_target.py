# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_setting


class ArchivalTarget(object):

    """Implementation of the 'ArchivalTarget' model.

    Message that specifies the details about an archival target (such as cloud
    or tape) where backup snapshots may be archived to.


    Attributes:

        cloud_tier_setting (ClusterConfigProto_Vault_CloudTierSetting): Tier
            settings in case of cloud target. Contains default tier type and
            information for moving snapshot data across cloud tiers.
        name (string): The name of the archival target.
        ownership_context (int): OwnershipContext of an archival target.
        mtype (int): The type of the archival target.
        usage_type (int): Usage of the archival target. Regular archival and
            RPaas archival are potential UsageType. By default it is regular
            archival. A vault can only be used for one UsageType and UsageType
            should not be changed once set.  Note: This field will be
            deprecated in future. Use OwnershipContext instead.
        vault_id (long|int): The id of the archival vault.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_tier_setting":'cloudTierSetting',
        "name":'name',
        "ownership_context":'ownershipContext',
        "mtype":'type',
        "usage_type":'usageType',
        "vault_id":'vaultId',
    }
    def __init__(self,
                 cloud_tier_setting=None,
                 name=None,
                 ownership_context=None,
                 mtype=None,
                 usage_type=None,
                 vault_id=None,
            ):

        """Constructor for the ArchivalTarget class"""

        # Initialize members of the class
        self.cloud_tier_setting = cloud_tier_setting
        self.name = name
        self.ownership_context = ownership_context
        self.mtype = mtype
        self.usage_type = usage_type
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
        ownership_context = dictionary.get('ownershipContext')
        mtype = dictionary.get('type')
        usage_type = dictionary.get('usageType')
        vault_id = dictionary.get('vaultId')

        # Return an object of this model
        return cls(
            cloud_tier_setting,
            name,
            ownership_context,
            mtype,
            usage_type,
            vault_id
)