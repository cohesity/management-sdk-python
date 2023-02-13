# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_distribution_metrics

class FileDistributionStats(object):

    """Implementation of the 'FileDistributionStats' model.

    Specifies the File distribution stats.

    Attributes:
        cluster_id (long|int): Specifies the cluster Id.
        cluster_incarnation_id (long|int): Specifies the cluster Incarnation
            Id.
        entity_id (long|int): Specifies the id of the entity for which file
            distribution stats are computed.
        entity_name (string): Specifies the name of the entity for which file
            distribution stats are computed.
        metrics_list (list of FileDistributionMetrics): Specifies the list of
            file stats for different file extensions.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "entity_id":'entityId',
        "entity_name":'entityName',
        "metrics_list":'metricsList'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 entity_id=None,
                 entity_name=None,
                 metrics_list=None):
        """Constructor for the FileDistributionStats class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.metrics_list = metrics_list


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
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        entity_id = dictionary.get('entityId')
        entity_name = dictionary.get('entityName')
        metrics_list = None
        if dictionary.get('metricsList') != None:
            metrics_list = list()
            for structure in dictionary.get('metricsList'):
                metrics_list.append(cohesity_management_sdk.models.file_distribution_metrics.FileDistributionMetrics.from_dictionary(structure))

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   entity_id,
                   entity_name,
                   metrics_list)


