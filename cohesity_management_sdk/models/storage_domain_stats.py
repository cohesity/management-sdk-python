# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.stats_group
import cohesity_management_sdk.models.usage_schema_info
import cohesity_management_sdk.models.data_usage_stats

class StorageDomainStats(object):

    """Implementation of the 'StorageDomainStats' model.

    TODO: type model description here.

    Attributes:
        cloud_spill_vault_id (long|int): Specifies the cloud spill vault id of
            the view box (storage domain).
        group_list (list of StatsGroup): Specifies a list of groups associated
            to this view box (storage domain).
        id (long|int): Specifies the id of the view box (storage domain).
        name (string): Specifies the name of the view box (storage domain).
        quota_hard_limit_bytes (long|int): Specifies the hard limit of
            physical quota of the view box (storage domain).
        schema_info_list (list of UsageSchemaInfo): Specifies a list of
            schemaInfos of the view box (storage domain).
        stats (DataUsageStats): Specifies details of statistics of the view
            box (storage domain).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_spill_vault_id":'cloudSpillVaultId',
        "group_list":'groupList',
        "id":'id',
        "name":'name',
        "quota_hard_limit_bytes":'quotaHardLimitBytes',
        "schema_info_list":'schemaInfoList',
        "stats":'stats'
    }

    def __init__(self,
                 cloud_spill_vault_id=None,
                 group_list=None,
                 id=None,
                 name=None,
                 quota_hard_limit_bytes=None,
                 schema_info_list=None,
                 stats=None):
        """Constructor for the StorageDomainStats class"""

        # Initialize members of the class
        self.cloud_spill_vault_id = cloud_spill_vault_id
        self.group_list = group_list
        self.id = id
        self.name = name
        self.quota_hard_limit_bytes = quota_hard_limit_bytes
        self.schema_info_list = schema_info_list
        self.stats = stats


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
        cloud_spill_vault_id = dictionary.get('cloudSpillVaultId')
        group_list = None
        if dictionary.get('groupList') != None:
            group_list = list()
            for structure in dictionary.get('groupList'):
                group_list.append(cohesity_management_sdk.models.stats_group.StatsGroup.from_dictionary(structure))
        id = dictionary.get('id')
        name = dictionary.get('name')
        quota_hard_limit_bytes = dictionary.get('quotaHardLimitBytes')
        schema_info_list = None
        if dictionary.get('schemaInfoList') != None:
            schema_info_list = list()
            for structure in dictionary.get('schemaInfoList'):
                schema_info_list.append(cohesity_management_sdk.models.usage_schema_info.UsageSchemaInfo.from_dictionary(structure))
        stats = cohesity_management_sdk.models.data_usage_stats.DataUsageStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None

        # Return an object of this model
        return cls(cloud_spill_vault_id,
                   group_list,
                   id,
                   name,
                   quota_hard_limit_bytes,
                   schema_info_list,
                   stats)


