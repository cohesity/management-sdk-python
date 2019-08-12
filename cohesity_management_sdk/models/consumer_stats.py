# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.stats_group
import cohesity_management_sdk.models.usage_schema_info
import cohesity_management_sdk.models.data_usage_stats

class ConsumerStats(object):

    """Implementation of the 'ConsumerStats' model.

    ConsumerStats is the stats of a single consumer. A consumer is a entity
    which consumes the storage space of a storage domain. A consumer can be a
    View, Protection Job or a Replication Job.

    Attributes:
        consumer_type (ConsumerTypeEnum): Specifies the type of the consumer.
            Type of the consumer can be one of the following three,  'kViews',
            indicates the stats info of Views used per organization (tenant)
            per view box (storage domain). 'kProtectionRuns', indicates the
            stats info of Protection Runs used per organization (tenant) per
            view box (storage domain). 'kReplicationRuns', indicates the stats
            info of Replication In used per organization (tenant) per view box
            (storage domain).
        group_list (list of StatsGroup): Specifies a list of groups associated
            to this consumer.
        id (long|int): Specifies the id of the consumer.
        name (string): Specifies the name of the consumer.
        quota_hard_limit_bytes (long|int): Specifies the hard limit of logical
            quota of the consumer. This field will be returned only if
            consumer type is view.
        schema_info_list (list of UsageSchemaInfo): Specifies a list of
            schemaInfos of the consumer.
        stats (DataUsageStats): Specifies the data usage metric of the data
            stored on the Cohesity Cluster or Storage Domains (View Boxes).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consumer_type":'consumerType',
        "group_list":'groupList',
        "id":'id',
        "name":'name',
        "quota_hard_limit_bytes":'quotaHardLimitBytes',
        "schema_info_list":'schemaInfoList',
        "stats":'stats'
    }

    def __init__(self,
                 consumer_type=None,
                 group_list=None,
                 id=None,
                 name=None,
                 quota_hard_limit_bytes=None,
                 schema_info_list=None,
                 stats=None):
        """Constructor for the ConsumerStats class"""

        # Initialize members of the class
        self.consumer_type = consumer_type
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
        consumer_type = dictionary.get('consumerType')
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
        return cls(consumer_type,
                   group_list,
                   id,
                   name,
                   quota_hard_limit_bytes,
                   schema_info_list,
                   stats)


