# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_audit_log

class ClusterAuditLogsSearchResult(object):

    """Implementation of the 'ClusterAuditLogsSearchResult' model.

    Returns the Cluster audit logs that match the specified filter criteria
    up to the limit specified in pageCount.

    Attributes:
        cluster_audit_logs (list of ClusterAuditLog): Array of Cluster Audit
            Logs.  Specifies a list of Cluster audit logs that match the
            specified filter criteria up to the limit specified in pageCount.
        total_count (long|int): Specifies the total number of logs that match
            the specified filter criteria. (This number might be larger than
            the size of the Cluster Audit Logs array.) This count is provided
            to indicate if additional requests must be made to get the full
            result.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_audit_logs":'clusterAuditLogs',
        "total_count":'totalCount'
    }

    def __init__(self,
                 cluster_audit_logs=None,
                 total_count=None):
        """Constructor for the ClusterAuditLogsSearchResult class"""

        # Initialize members of the class
        self.cluster_audit_logs = cluster_audit_logs
        self.total_count = total_count


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
        cluster_audit_logs = None
        if dictionary.get('clusterAuditLogs') != None:
            cluster_audit_logs = list()
            for structure in dictionary.get('clusterAuditLogs'):
                cluster_audit_logs.append(cohesity_management_sdk.models.cluster_audit_log.ClusterAuditLog.from_dictionary(structure))
        total_count = dictionary.get('totalCount')

        # Return an object of this model
        return cls(cluster_audit_logs,
                   total_count)


