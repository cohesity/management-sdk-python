# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.node_ipmi_user


class ClusterUpdateIpmiUsersParameters(object):

    """Implementation of the 'ClusterUpdateIpmiUsersParameters' model.

    Specifies the cluster level IPMI user credentials and/or Node level IPMI
    user credentials.


    Attributes:

        cluster_ipmi_user (string): Cluster level IPMI User name.
        ipmi_password (string): Cluster level IPMI Password.
        node_ipmi_users (list of NodeIpmiUser): Node level IPMI User config.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_ipmi_user":'clusterIpmiUser',
        "ipmi_password":'ipmiPassword',
        "node_ipmi_users":'nodeIpmiUsers',
    }
    def __init__(self,
                 cluster_ipmi_user=None,
                 ipmi_password=None,
                 node_ipmi_users=None,
            ):

        """Constructor for the ClusterUpdateIpmiUsersParameters class"""

        # Initialize members of the class
        self.cluster_ipmi_user = cluster_ipmi_user
        self.ipmi_password = ipmi_password
        self.node_ipmi_users = node_ipmi_users

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
        cluster_ipmi_user = dictionary.get('clusterIpmiUser')
        ipmi_password = dictionary.get('ipmiPassword')
        node_ipmi_users = None
        if dictionary.get('nodeIpmiUsers') != None:
            node_ipmi_users = list()
            for structure in dictionary.get('nodeIpmiUsers'):
                node_ipmi_users.append(cohesity_management_sdk.models.node_ipmi_user.NodeIpmiUser.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cluster_ipmi_user,
            ipmi_password,
            node_ipmi_users
)