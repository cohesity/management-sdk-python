# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExpandCloudClusterParameters(object):

    """Implementation of the 'ExpandCloudClusterParameters' model.

    Specifies the parameters needed to expand a Cohesity Cloud Edition
    Cluster.

    Attributes:
        node_ips (list of string): Specifies the list of IPs of the new
            Nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "node_ips":'nodeIps'
    }

    def __init__(self,
                 node_ips=None):
        """Constructor for the ExpandCloudClusterParameters class"""

        # Initialize members of the class
        self.node_ips = node_ips


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
        node_ips = dictionary.get('nodeIps')

        # Return an object of this model
        return cls(node_ips)


