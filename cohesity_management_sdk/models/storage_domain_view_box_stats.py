# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.usage_and_performance_statistics
import cohesity_management_sdk.models.logical_statistics

class StorageDomainViewBoxStats(object):

    """Implementation of the 'Storage Domain (View Box) Stats.' model.

    Provides statistics about the Storage Domain (View Box).

    Attributes:
        cloud_usage_perf_stats (UsageAndPerformanceStatistics): Provides usage
            and performance statistics for entities such as a disks, Nodes or
            Clusters.
        id (long|int): Specifies the id of the Storage Domain (View Box).
        local_usage_perf_stats (UsageAndPerformanceStatistics): Provides usage
            and performance statistics for entities such as a disks, Nodes or
            Clusters.
        logical_stats (LogicalStatistics): Provides logical statistics for
            logical entities such as Clusters and Domains (View Boxes). The
            logical size is the size of the data when it is fully hydrated or
            expanded. The actual physical data stored on the Cohesity Cluster
            is reduced by change-block tracking, compression and
            deduplication.
        usage_perf_stats (UsageAndPerformanceStatistics): Provides usage and
            performance statistics for entities such as a disks, Nodes or
            Clusters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_usage_perf_stats":'cloudUsagePerfStats',
        "id":'id',
        "local_usage_perf_stats":'localUsagePerfStats',
        "logical_stats":'logicalStats',
        "usage_perf_stats":'usagePerfStats'
    }

    def __init__(self,
                 cloud_usage_perf_stats=None,
                 id=None,
                 local_usage_perf_stats=None,
                 logical_stats=None,
                 usage_perf_stats=None):
        """Constructor for the StorageDomainViewBoxStats class"""

        # Initialize members of the class
        self.cloud_usage_perf_stats = cloud_usage_perf_stats
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
        id = dictionary.get('id')
        local_usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_statistics.UsageAndPerformanceStatistics.from_dictionary(dictionary.get('localUsagePerfStats')) if dictionary.get('localUsagePerfStats') else None
        logical_stats = cohesity_management_sdk.models.logical_statistics.LogicalStatistics.from_dictionary(dictionary.get('logicalStats')) if dictionary.get('logicalStats') else None
        usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_statistics.UsageAndPerformanceStatistics.from_dictionary(dictionary.get('usagePerfStats')) if dictionary.get('usagePerfStats') else None

        # Return an object of this model
        return cls(cloud_usage_perf_stats,
                   id,
                   local_usage_perf_stats,
                   logical_stats,
                   usage_perf_stats)


