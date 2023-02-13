# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gpfs_cluster
import cohesity_management_sdk.models.gpfs_fileset
import cohesity_management_sdk.models.gpfs_filesystem

class GpfsProtectionSource(object):

    """Implementation of the 'GpfsProtectionSource' model.

    Specifies a Protection Source in GPFS environment.

    Attributes:
        cluster (GpfsCluster): Specifies information about a GPFS Cluster.
        fileset (GpfsFileset): Specifies information about a fileset in a GPFS
            file system.
        filesystem (GpfsFilesystem): Specifies information about filesystem in
            a GPFS Cluster.
        name (string): Specifies a unique name of the Protection Source.
        mtype (TypeGpfsProtectionSourceEnum): Specifies the type of the entity
            in an GPFS file system like 'kCluster', 'kFilesystem', or,
            'kFileset'. 'kCluster' indicates an GPFS Cluster. 'kFilesystem'
            indicates a top level filesystem on GPFS cluster. 'kFileset'
            indicates a fileset within a filesystem.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster":'cluster',
        "fileset":'fileset',
        "filesystem":'filesystem',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 cluster=None,
                 fileset=None,
                 filesystem=None,
                 name=None,
                 mtype=None):
        """Constructor for the GpfsProtectionSource class"""

        # Initialize members of the class
        self.cluster = cluster
        self.fileset = fileset
        self.filesystem = filesystem
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
        cluster = cohesity_management_sdk.models.gpfs_cluster.GpfsCluster.from_dictionary(dictionary.get('cluster')) if dictionary.get('cluster') else None
        fileset = cohesity_management_sdk.models.gpfs_fileset.GpfsFileset.from_dictionary(dictionary.get('fileset')) if dictionary.get('fileset') else None
        filesystem = cohesity_management_sdk.models.gpfs_filesystem.GpfsFilesystem.from_dictionary(dictionary.get('filesystem')) if dictionary.get('filesystem') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cluster,
                   fileset,
                   filesystem,
                   name,
                   mtype)


