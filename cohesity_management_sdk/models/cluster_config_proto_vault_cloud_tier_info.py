# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_type


class ClusterConfigProto_Vault_CloudTierInfo(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudTierInfo' model.

    TODO: type description here.


    Attributes:

        honor_tier_info (bool): Flag that determines whether this tiering info
            is to be honored or not. By default this tiering setting will be
            ignored. This must be explicitly set to true in order to honor this
            setting.
        num_secs_to_move_after (long|int): Represents the number of seconds
            since the snapshot first got archived (to default tier) after which
            it needs to be moved to the target tier. For example, if user
            selects target as an AWS vault (default: S3 tier) with 3 months
            retention, move to glacier after 1 month, and move to deep glacier
            after 2 months, then the below field should be set to appropriate
            number of seconds corresponding to 1 or 2 months by iris. The
            snapshot will reside in S3 (default tier) for 1 month, then 1 month
            in glacier tier, and then another 1 month in deep glacier before
            being deleted.
        target_tier_type (ClusterConfigProto_Vault_CloudTierType): Represents
            the target tier to which a archive snapshot needs to be
            moved/migrated. Currently we only allow down-tiering (i.e. moving
            snapshots to a colder tier compared to current tier).
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "honor_tier_info":'honorTierInfo',
        "num_secs_to_move_after":'numSecsToMoveAfter',
        "target_tier_type":'targetTierType',
    }
    def __init__(self,
                 honor_tier_info=None,
                 num_secs_to_move_after=None,
                 target_tier_type=None,
            ):

        """Constructor for the ClusterConfigProto_Vault_CloudTierInfo class"""

        # Initialize members of the class
        self.honor_tier_info = honor_tier_info
        self.num_secs_to_move_after = num_secs_to_move_after
        self.target_tier_type = target_tier_type

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
        honor_tier_info = dictionary.get('honorTierInfo')
        num_secs_to_move_after = dictionary.get('numSecsToMoveAfter')
        target_tier_type = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_tier_type.ClusterConfigProto_Vault_CloudTierType.from_dictionary(dictionary.get('targetTierType')) if dictionary.get('targetTierType') else None

        # Return an object of this model
        return cls(
            honor_tier_info,
            num_secs_to_move_after,
            target_tier_type
)