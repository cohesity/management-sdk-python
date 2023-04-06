# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SpogContext(object):

    """Implementation of the 'SpogContext' model.

    SpogContext specifies all of the information about the user and cluster
    which is performing action on this cluster.


    Attributes:

        primary_cluster_id (long|int): Specifies the ID of the remote cluster
            which is accessing this cluster via SPOG.
        primary_cluster_user_sid (string): Specifies the SID of the user who is
            accessing this cluster via SPOG.
        primary_cluster_username (string): Specifies the username of the user
            who is accessing this cluster via SPOG.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "primary_cluster_id":'PrimaryClusterId',
        "primary_cluster_user_sid":'PrimaryClusterUserSid',
        "primary_cluster_username":'PrimaryClusterUsername',
    }
    def __init__(self,
                 primary_cluster_id=None,
                 primary_cluster_user_sid=None,
                 primary_cluster_username=None,
            ):

        """Constructor for the SpogContext class"""

        # Initialize members of the class
        self.primary_cluster_id = primary_cluster_id
        self.primary_cluster_user_sid = primary_cluster_user_sid
        self.primary_cluster_username = primary_cluster_username

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
        primary_cluster_id = dictionary.get('PrimaryClusterId')
        primary_cluster_user_sid = dictionary.get('PrimaryClusterUserSid')
        primary_cluster_username = dictionary.get('PrimaryClusterUsername')

        # Return an object of this model
        return cls(
            primary_cluster_id,
            primary_cluster_user_sid,
            primary_cluster_username
)