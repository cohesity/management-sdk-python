# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.usage_and_performance_statistics
import cohesity_management_sdk.models.logical_statistics

class CohesityClusterStatistics(object):

    """Implementation of the 'Cohesity Cluster Statistics.' model.

    Specifies statistics about this Cohesity Cluster.

    Attributes:
        cloud_usage_perf_stats (UsageAndPerformanceStatistics): Provides usage
            and performance statistics for the remote data stored on a Cloud
            Tier by the Cohesity Cluster.
        data_reduction_ratio (float): Specifies the ratio of logical bytes
            (not reduced by change-block tracking, compression and
            deduplication) to physical bytes (reduced by change-block
            tracking, compression and deduplication).
        id (long|int): Specifies the id of the Cohesity Cluster.
        local_usage_perf_stats (UsageAndPerformanceStatistics): Provides usage
            and performance statistics for local data stored directly on the
            Cohesity Cluster.
        logical_stats (LogicalStatistics): Specifies the total logical data
            size of all the local and Cloud Tier data stored by the Cohesity
            Cluster before the data is reduced by change-block tracking,
            compression and deduplication. The size of the data if the data is
            fully hydrated or expanded.
        usage_perf_stats (UsageAndPerformanceStatistics): Provides usage and
            performance statistics about the local data stored directly on the
            Cohesity Cluster and the remote data stored on a Cloud Tier for
            the Cohesity Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_usage_perf_stats":'cloudUsagePerfStats',
        "data_reduction_ratio":'dataReductionRatio',
        "id":'id',
        "local_usage_perf_stats":'localUsagePerfStats',
        "logical_stats":'logicalStats',
        "usage_perf_stats":'usagePerfStats'
    }

    def __init__(self,
                 cloud_usage_perf_stats=None,
                 data_reduction_ratio=None,
                 id=None,
                 local_usage_perf_stats=None,
                 logical_stats=None,
                 usage_perf_stats=None):
        """Constructor for the CohesityClusterStatistics class"""

        # Initialize members of the class
        self.cloud_usage_perf_stats = cloud_usage_perf_stats
        self.data_reduction_ratio = data_reduction_ratio
        self.id = id
        self.local_usage_perf_stats = local_usage_perf_stats
        self.logical_stats = logical_stats
        self.usage_perf_stats = usage_perf_stats


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
        cloud_usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_statistics.UsageAndPerformanceStatistics.from_dictionary(dictionary.get('cloudUsagePerfStats')) if dictionary.get('cloudUsagePerfStats') else None
        data_reduction_ratio = dictionary.get('dataReductionRatio')
        id = dictionary.get('id')
        local_usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_statistics.UsageAndPerformanceStatistics.from_dictionary(dictionary.get('localUsagePerfStats')) if dictionary.get('localUsagePerfStats') else None
        logical_stats = cohesity_management_sdk.models.logical_statistics.LogicalStatistics.from_dictionary(dictionary.get('logicalStats')) if dictionary.get('logicalStats') else None
        usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_statistics.UsageAndPerformanceStatistics.from_dictionary(dictionary.get('usagePerfStats')) if dictionary.get('usagePerfStats') else None

        # Return an object of this model
        return cls(cloud_usage_perf_stats,
                   data_reduction_ratio,
                   id,
                   local_usage_perf_stats,
                   logical_stats,
                   usage_perf_stats)


