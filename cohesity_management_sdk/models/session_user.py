# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SessionUser(object):

    """Implementation of the 'SessionUser' model.

    Attributes:
        group_sids (list of string):  SIDs of the groups the user is a member
            of.
        is_node_in_cluster (bool): Whether node is in cluster.
        privileges (list of string): Privileges is the array of privileges the
            current user has.
        user (string): User is the current session user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_sids":'groupSids',
        "is_node_in_cluster":'isNodeInCluster',
        "privileges":'privileges',
        "user":'user'
    }

    def __init__(self,
                 group_sids=None,
                 is_node_in_cluster=None,
                 privileges=None,
                 user=None):
        """Constructor for the SessionUser class"""

        # Initialize members of the class
        self.group_sids = group_sids
        self.is_node_in_cluster = is_node_in_cluster
        self.privileges = privileges
        self.user = user


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
        group_sids = dictionary.get('groupSids')
        is_node_in_cluster = dictionary.get('isNodeInCluster')
        privileges = dictionary.get('privileges')
        user = dictionary.get('user')

        # Return an object of this model
        return cls(group_sids,
                   is_node_in_cluster,
                   privileges,
                   user)


