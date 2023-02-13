# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.stats_group
import cohesity_management_sdk.models.usage_schema_info
import cohesity_management_sdk.models.data_usage_stats

class TenantStats(object):

    """Implementation of the 'TenantStats' model.

    TODO: type model description here.

    Attributes:
        group_list (list of StatsGroup): Specifies a list of groups associated
            to this tenant (organization).
        id (string): Specifies the id of the tenant (organization).
        name (string): Specifies the name of the tenant (organization).
        schema_info_list (list of UsageSchemaInfo): Specifies a list of
            schemaInfos of the tenant (organization).
        stats (DataUsageStats): Specifies the data usage metric of the data
            stored on the Cohesity Cluster or Storage Domains (View Boxes).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_list":'groupList',
        "id":'id',
        "name":'name',
        "schema_info_list":'schemaInfoList',
        "stats":'stats'
    }

    def __init__(self,
                 group_list=None,
                 id=None,
                 name=None,
                 schema_info_list=None,
                 stats=None):
        """Constructor for the TenantStats class"""

        # Initialize members of the class
        self.group_list = group_list
        self.id = id
        self.name = name
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
        group_list = None
        if dictionary.get('groupList') != None:
            group_list = list()
            for structure in dictionary.get('groupList'):
                group_list.append(cohesity_management_sdk.models.stats_group.StatsGroup.from_dictionary(structure))
        id = dictionary.get('id')
        name = dictionary.get('name')
        schema_info_list = None
        if dictionary.get('schemaInfoList') != None:
            schema_info_list = list()
            for structure in dictionary.get('schemaInfoList'):
                schema_info_list.append(cohesity_management_sdk.models.usage_schema_info.UsageSchemaInfo.from_dictionary(structure))
        stats = cohesity_management_sdk.models.data_usage_stats.DataUsageStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None

        # Return an object of this model
        return cls(group_list,
                   id,
                   name,
                   schema_info_list,
                   stats)


