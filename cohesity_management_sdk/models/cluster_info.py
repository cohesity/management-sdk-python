# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterInfo(object):

    """Implementation of the 'ClusterInfo' model.

    IP Range for range of vip address addition.

    Attributes:
        cluster_id (long|int): Specifies the id of the cluster.
        incarnation_id (int|long): Specifies the incarnation id of the cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id": 'clusterId',
        "incarnation_id": 'incarnationId'
    }

    def __init__(self,
                 cluster_id=None,
                 incarnation_id=None):
        """Constructor for the ClusterInfo class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.incarnation_id = incarnation_id


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
        cluster_id = dictionary.get('clusterId', None)
        incarnation_id = dictionary.get('incarnationId', None)

        # Return an object of this model
        return cls(cluster_id,
                   incarnation_id)


