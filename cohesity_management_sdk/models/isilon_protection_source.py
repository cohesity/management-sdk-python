# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.isilon_access_zone
import cohesity_management_sdk.models.isilon_cluster
import cohesity_management_sdk.models.isilon_mount_point

class IsilonProtectionSource(object):

    """Implementation of the 'IsilonProtectionSource' model.

    Specifies a Protection Source in Isilon OneFs environment.

    Attributes:
        access_zone (IsilonAccessZone): Specifies information about access
            zone in an Isilon Cluster.
        cluster (IsilonCluster): Specifies information about an Isilon
            Cluster.
        mount_point (IsilonMountPoint): Specifies information about a mount
            point in an Isilon OneFs Cluster.
        name (string): Specifies a unique name of the Protection Source.
        mtype (TypeIsilonProtectionSourceEnum): Specifies the type of the
            entity in an Isilon OneFs file system like 'kCluster', 'kZone',
            or, 'kMountPoint'. 'kCluster' indicates an Isilon OneFs Cluster.
            'kZone' indicates an access zone in an Isilon OneFs Cluster.
            'kMountPoint' indicates a mount point exposed by an Isilon OneFs
            Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_zone":'accessZone',
        "cluster":'cluster',
        "mount_point":'mountPoint',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 access_zone=None,
                 cluster=None,
                 mount_point=None,
                 name=None,
                 mtype=None):
        """Constructor for the IsilonProtectionSource class"""

        # Initialize members of the class
        self.access_zone = access_zone
        self.cluster = cluster
        self.mount_point = mount_point
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
        access_zone = cohesity_management_sdk.models.isilon_access_zone.IsilonAccessZone.from_dictionary(dictionary.get('accessZone')) if dictionary.get('accessZone') else None
        cluster = cohesity_management_sdk.models.isilon_cluster.IsilonCluster.from_dictionary(dictionary.get('cluster')) if dictionary.get('cluster') else None
        mount_point = cohesity_management_sdk.models.isilon_mount_point.IsilonMountPoint.from_dictionary(dictionary.get('mountPoint')) if dictionary.get('mountPoint') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(access_zone,
                   cluster,
                   mount_point,
                   name,
                   mtype)


