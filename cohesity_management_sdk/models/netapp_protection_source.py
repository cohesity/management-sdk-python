# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.netapp_cluster_info
import cohesity_management_sdk.models.netapp_volume_info
import cohesity_management_sdk.models.netapp_vserver_info

class NetappProtectionSource(object):

    """Implementation of the 'NetappProtectionSource' model.

    Specifies a Protection Source in a NetApp environment.

    Attributes:
        cluster_info (NetappClusterInfo): Specifies information about a NetApp
            Cluster Protection Source.
        is_top_level (bool): Specifies if this Object is a top level Object.
            Because a top level Object can either be a NetApp cluster or a
            Vserver, this cannot be determined only by type.
        license_types (LicenseTypesEnum): Specifies the type of license
            available on Netapp Cluster
            'kSnapmirrorCloud' indicates a SnapMirror license on Netapp.
        name (string): Specifies the name of the NetApp Object.
        mtype (TypeNetappProtectionSourceEnum): Specifies the type of managed
            NetApp Object in a NetApp Protection Source such as 'kCluster',
            'kVserver' or 'kVolume'. 'kCluster' indicates a Netapp cluster as
            a protection source. 'kVserver' indicates a Netapp vserver in a
            cluster as a protection source. 'kVolume' indicates  a volume in
            Netapp vserver as a protection source.
        uuid (string): Specifies the globally unique ID of this Object
            assigned by the NetApp server.
        version (string): Specifies the version of Netapp Cluster.
        volume_info (NetappVolumeInfo): Specifies information about a volume
            in a NetApp cluster.
        vserver_info (NetappVserverInfo): Specifies information about a NetApp
            Vserver in a NetApp Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_info":'clusterInfo',
        "is_top_level":'isTopLevel',
        "license_types":'licenseTypes',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid',
        "version":'version',
        "volume_info":'volumeInfo',
        "vserver_info":'vserverInfo'
    }

    def __init__(self,
                 cluster_info=None,
                 is_top_level=None,
                 license_types=None,
                 name=None,
                 mtype=None,
                 uuid=None,
                 version=None,
                 volume_info=None,
                 vserver_info=None):
        """Constructor for the NetappProtectionSource class"""

        # Initialize members of the class
        self.cluster_info = cluster_info
        self.is_top_level = is_top_level
        self.license_types = license_types
        self.name = name
        self.mtype = mtype
        self.uuid = uuid
        self.version = version
        self.volume_info = volume_info
        self.vserver_info = vserver_info


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
        cluster_info = cohesity_management_sdk.models.netapp_cluster_info.NetappClusterInfo.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        is_top_level = dictionary.get('isTopLevel')
        license_types = dictionary.get('licenseTypes')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')
        volume_info = cohesity_management_sdk.models.netapp_volume_info.NetappVolumeInfo.from_dictionary(dictionary.get('volumeInfo')) if dictionary.get('volumeInfo') else None
        vserver_info = cohesity_management_sdk.models.netapp_vserver_info.NetappVserverInfo.from_dictionary(dictionary.get('vserverInfo')) if dictionary.get('vserverInfo') else None

        # Return an object of this model
        return cls(cluster_info,
                   is_top_level,
                   license_types,
                   name,
                   mtype,
                   uuid,
                   version,
                   volume_info,
                   vserver_info)


