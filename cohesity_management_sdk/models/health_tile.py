# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alert

class HealthTile(object):

    """Implementation of the 'HealthTile' model.

    Health for Dashboard.

    Attributes:
        capacity_bytes (long|int): Raw Cluster Capacity in Bytes. This is not
            usable capacity and does not take replication factor into
            account.
        cluster_cloud_usage_bytes (long|int): Usage in Bytes on the cloud.
        last_day_alerts (list of Alert): Alerts in last 24 hours.
        last_day_num_criticals (long|int): Number of Critical Alerts.
        last_day_num_warnings (long|int): Number of Warning Alerts.
        num_nodes (int): Number of nodes in the cluster.
        num_nodes_with_issues (int): Number of nodes in the cluster that are
            unhealthy.
        percent_full (float): Percent the cluster is full.
        raw_used_bytes (long|int): Raw Bytes used in the cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity_bytes":'capacityBytes',
        "cluster_cloud_usage_bytes":'clusterCloudUsageBytes',
        "last_day_alerts":'lastDayAlerts',
        "last_day_num_criticals":'lastDayNumCriticals',
        "last_day_num_warnings":'lastDayNumWarnings',
        "num_nodes":'numNodes',
        "num_nodes_with_issues":'numNodesWithIssues',
        "percent_full":'percentFull',
        "raw_used_bytes":'rawUsedBytes'
    }

    def __init__(self,
                 capacity_bytes=None,
                 cluster_cloud_usage_bytes=None,
                 last_day_alerts=None,
                 last_day_num_criticals=None,
                 last_day_num_warnings=None,
                 num_nodes=None,
                 num_nodes_with_issues=None,
                 percent_full=None,
                 raw_used_bytes=None):
        """Constructor for the HealthTile class"""

        # Initialize members of the class
        self.capacity_bytes = capacity_bytes
        self.cluster_cloud_usage_bytes = cluster_cloud_usage_bytes
        self.last_day_alerts = last_day_alerts
        self.last_day_num_criticals = last_day_num_criticals
        self.last_day_num_warnings = last_day_num_warnings
        self.num_nodes = num_nodes
        self.num_nodes_with_issues = num_nodes_with_issues
        self.percent_full = percent_full
        self.raw_used_bytes = raw_used_bytes


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
        capacity_bytes = dictionary.get('capacityBytes')
        cluster_cloud_usage_bytes = dictionary.get('clusterCloudUsageBytes')
        last_day_alerts = None
        if dictionary.get('lastDayAlerts') != None:
            last_day_alerts = list()
            for structure in dictionary.get('lastDayAlerts'):
                last_day_alerts.append(cohesity_management_sdk.models.alert.Alert.from_dictionary(structure))
        last_day_num_criticals = dictionary.get('lastDayNumCriticals')
        last_day_num_warnings = dictionary.get('lastDayNumWarnings')
        num_nodes = dictionary.get('numNodes')
        num_nodes_with_issues = dictionary.get('numNodesWithIssues')
        percent_full = dictionary.get('percentFull')
        raw_used_bytes = dictionary.get('rawUsedBytes')

        # Return an object of this model
        return cls(capacity_bytes,
                   cluster_cloud_usage_bytes,
                   last_day_alerts,
                   last_day_num_criticals,
                   last_day_num_warnings,
                   num_nodes,
                   num_nodes_with_issues,
                   percent_full,
                   raw_used_bytes)


