# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.usage_and_performance_stats

class NodeStats(object):

    """Implementation of the 'NodeStats' model.

    NodeStats provides various statistics for the node.

    Attributes:
        id (long|int): Id is the Id of the Node.
        usage_perf_stats (UsageAndPerformanceStats): Provides usage and
            performance statistics for entities such as a disks, Nodes or
            Clusters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "usage_perf_stats":'usagePerfStats'
    }

    def __init__(self,
                 id=None,
                 usage_perf_stats=None):
        """Constructor for the NodeStats class"""

        # Initialize members of the class
        self.id = id
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
        id = dictionary.get('id')
        usage_perf_stats = cohesity_management_sdk.models.usage_and_performance_stats.UsageAndPerformanceStats.from_dictionary(dictionary.get('usagePerfStats')) if dictionary.get('usagePerfStats') else None

        # Return an object of this model
        return cls(id,
                   usage_perf_stats)


