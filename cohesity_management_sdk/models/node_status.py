# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodeStatus(object):

    """Implementation of the 'NodeStatus' model.

    Specifies the status of each node in the cluster being created.

    Attributes:
        error_message (string): Specifies an optional message relating to the
            node status.
        ipmi_ip (string): Specifies the IPMI IP of the node (if physical
            cluster).
        node_id (long|int): Specifies the ID of the node.
        node_ip (string): For physical nodes this will specify the IP address
            of the node.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_message":'errorMessage',
        "ipmi_ip":'ipmiIp',
        "node_id":'nodeId',
        "node_ip":'nodeIp'
    }

    def __init__(self,
                 error_message=None,
                 ipmi_ip=None,
                 node_id=None,
                 node_ip=None):
        """Constructor for the NodeStatus class"""

        # Initialize members of the class
        self.error_message = error_message
        self.ipmi_ip = ipmi_ip
        self.node_id = node_id
        self.node_ip = node_ip


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
        error_message = dictionary.get('errorMessage')
        ipmi_ip = dictionary.get('ipmiIp')
        node_id = dictionary.get('nodeId')
        node_ip = dictionary.get('nodeIp')

        # Return an object of this model
        return cls(error_message,
                   ipmi_ip,
                   node_id,
                   node_ip)


