# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionSourceUid(object):

    """Implementation of the 'ProtectionSourceUid' model.

    Specifies universal id of the Protection source specific to a cluster.

    Attributes:
        cluster_id (long|int): Specifies the id of the cluster on which object
            is present.
        cluster_incarnation_id (long|int): Specifies the incarnation id of the
            cluster on which object is present.
        parent_source_id (long|int): Specifies parent source id of an object.
        source_id (long|int): Specifies source id of an object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "parent_source_id":'parentSourceId',
        "source_id":'sourceId'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 parent_source_id=None,
                 source_id=None):
        """Constructor for the ProtectionSourceUid class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.parent_source_id = parent_source_id
        self.source_id = source_id


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
        parent_source_id = dictionary.get('parentSourceId')
        source_id = dictionary.get('sourceId')

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   parent_source_id,
                   source_id)


