# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UniversalId(object):

    """Implementation of the 'UniversalId' model.

    Specifies an id for an object that is unique across Cohesity Clusters.
    The id is composite of all the ids listed below.

    Attributes:
        cluster_id (long|int): Specifies the Cohesity Cluster id where the
            object was created.
        cluster_incarnation_id (long|int): Specifies an id for the Cohesity
            Cluster that is generated when a Cohesity Cluster is initially
            created.
        id (long|int): Specifies a unique id assigned to an object (such as a
            Job) by the Cohesity Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "id":'id'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 id=None):
        """Constructor for the UniversalId class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.id = id


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
        id = dictionary.get('id')

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   id)


