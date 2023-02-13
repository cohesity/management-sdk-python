# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.elastifile_cluster
import cohesity_management_sdk.models.elastifile_container

class ElastifileProtectionSource(object):

    """Implementation of the 'ElastifileProtectionSource' model.

    Specifies a Protection Source in Elastifile environment.

    Attributes:
        cluster (ElastifileCluster): Specifies information about a Elastifile
            Cluster.
        container (ElastifileContainer): Specifies information about container
            in an Elastifile Cluster.
        name (string): Specifies a unique name of the Protection Source.
        mtype (TypeElastifileProtectionSourceEnum): Specifies the type of the
            entity in an Elastifile file system like 'kCluster', 'kContainer'.
            'kCluster' indicates an Elastifile Cluster. 'kContainer' indicates
            a container on Elastifile cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster":'cluster',
        "container":'container',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 cluster=None,
                 container=None,
                 name=None,
                 mtype=None):
        """Constructor for the ElastifileProtectionSource class"""

        # Initialize members of the class
        self.cluster = cluster
        self.container = container
        self.name = name
        self.mtype = mtype


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
        cluster = cohesity_management_sdk.models.elastifile_cluster.ElastifileCluster.from_dictionary(dictionary.get('cluster')) if dictionary.get('cluster') else None
        container = cohesity_management_sdk.models.elastifile_container.ElastifileContainer.from_dictionary(dictionary.get('container')) if dictionary.get('container') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cluster,
                   container,
                   name,
                   mtype)


