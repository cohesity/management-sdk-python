# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.node_status

class CreateClusterResult(object):

    """Implementation of the 'CreateClusterResult' model.

    Specifies the immediate result of a Cluster creation request. Contains
    validation results for each node. If the request is valid, it also
    indicates that the individual node bringup operation is started in
    the background.

    Attributes:
        cluster_id (long|int): Specifies the ID of the new Cluster.
        cluster_name (string): Specifies the name of the new Cluster.
        cluster_sw_version (string): Specifies the software version of the new
            Cluster.
        healthy_nodes (list of NodeStatus): Specifies the status of the Nodes
            in the Cluster. All Nodes that are accepted to the Cluster are
            appended to this list.
        incarnation_id (long|int): Specifies the Incarnation ID of the new
            Cluster.
        message (string): Specifies an optional message field.
        unhealthy_nodes (list of NodeStatus): Specifies the status of the
            Nodes in the Cluster. All Nodes that are not accepted to the
            Cluster are appended to this list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_name":'clusterName',
        "cluster_sw_version":'clusterSwVersion',
        "healthy_nodes":'healthyNodes',
        "incarnation_id":'incarnationId',
        "message":'message',
        "unhealthy_nodes":'unhealthyNodes'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_name=None,
                 cluster_sw_version=None,
                 healthy_nodes=None,
                 incarnation_id=None,
                 message=None,
                 unhealthy_nodes=None):
        """Constructor for the CreateClusterResult class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_sw_version = cluster_sw_version
        self.healthy_nodes = healthy_nodes
        self.incarnation_id = incarnation_id
        self.message = message
        self.unhealthy_nodes = unhealthy_nodes


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
        cluster_name = dictionary.get('clusterName')
        cluster_sw_version = dictionary.get('clusterSwVersion')
        healthy_nodes = None
        if dictionary.get('healthyNodes') != None:
            healthy_nodes = list()
            for structure in dictionary.get('healthyNodes'):
                healthy_nodes.append(cohesity_management_sdk.models.node_status.NodeStatus.from_dictionary(structure))
        incarnation_id = dictionary.get('incarnationId')
        message = dictionary.get('message')
        unhealthy_nodes = None
        if dictionary.get('unhealthyNodes') != None:
            unhealthy_nodes = list()
            for structure in dictionary.get('unhealthyNodes'):
                unhealthy_nodes.append(cohesity_management_sdk.models.node_status.NodeStatus.from_dictionary(structure))

        # Return an object of this model
        return cls(cluster_id,
                   cluster_name,
                   cluster_sw_version,
                   healthy_nodes,
                   incarnation_id,
                   message,
                   unhealthy_nodes)


