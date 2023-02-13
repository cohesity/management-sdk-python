# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ViewBoxPairInfo(object):

    """Implementation of the 'ViewBoxPairInfo' model.

    Specifies a pairing between a Storage Domain (View Box) on local Cluster
    with a Storage Domain (View Box) on a remote Cluster.
    When replication is configured between a local Cluster and a
    remote Cluster, the Snapshots are replicated from the specified
    Storage Domain (View Box) on the local Cluster to the Storage Domain
    (View Box) on the remote Cluster. See the online help for details about
    the
    supported Storage Domains (View Box) pairings between Clusters.

    Attributes:
        local_view_box_id (long|int): Specifies the id of the Storage Domain
            (View Box) on the local Cluster.
        local_view_box_name (string): Specifies the name of the Storage Domain
            (View Box) on the local Cluster.
        remote_view_box_id (long|int): Specifies the id of the Storage Domain
            (View Box) on the remote Cluster.
        remote_view_box_name (string): Specifies the name of the Storage
            Domain (View Box) on the remote Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "local_view_box_id":'localViewBoxId',
        "local_view_box_name":'localViewBoxName',
        "remote_view_box_id":'remoteViewBoxId',
        "remote_view_box_name":'remoteViewBoxName'
    }

    def __init__(self,
                 local_view_box_id=None,
                 local_view_box_name=None,
                 remote_view_box_id=None,
                 remote_view_box_name=None):
        """Constructor for the ViewBoxPairInfo class"""

        # Initialize members of the class
        self.local_view_box_id = local_view_box_id
        self.local_view_box_name = local_view_box_name
        self.remote_view_box_id = remote_view_box_id
        self.remote_view_box_name = remote_view_box_name


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
        local_view_box_id = dictionary.get('localViewBoxId')
        local_view_box_name = dictionary.get('localViewBoxName')
        remote_view_box_id = dictionary.get('remoteViewBoxId')
        remote_view_box_name = dictionary.get('remoteViewBoxName')

        # Return an object of this model
        return cls(local_view_box_id,
                   local_view_box_name,
                   remote_view_box_id,
                   remote_view_box_name)


