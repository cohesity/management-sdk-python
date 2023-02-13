# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.isilon_nfs_mount_point
import cohesity_management_sdk.models.isilon_smb_mount_point

class IsilonMountPoint(object):

    """Implementation of the 'IsilonMountPoint' model.

    Specifies information about a mount point in an Isilon OneFs Cluster.

    Attributes:
        access_zone_name (string): Specifies the name of access zone.
        nfs_mount_point (IsilonNfsMountPoint): Specifies NFS Mount Point
            exposed by Isilon Protection Source.
        path (string): Specifies the path of the access zone in ifs. This
            should include the leading "/ifs/".
        protocols (list of ProtocolEnum): List of Protocols on Isilon.
            Specifies the list of protocols enabled on Isilon OneFs file
            system. 'kNfs' indicates NFS exports in an Isilon Cluster. 'kSmb'
            indicates CIFS/SMB Shares in an Isilon Cluster.
        smb_mount_points (list of IsilonSmbMountPoint): Specifies information
            about an SMB share. This field is set if the file system supports
            protocol type 'kSmb'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_zone_name":'accessZoneName',
        "nfs_mount_point":'nfsMountPoint',
        "path":'path',
        "protocols":'protocols',
        "smb_mount_points":'smbMountPoints'
    }

    def __init__(self,
                 access_zone_name=None,
                 nfs_mount_point=None,
                 path=None,
                 protocols=None,
                 smb_mount_points=None):
        """Constructor for the IsilonMountPoint class"""

        # Initialize members of the class
        self.access_zone_name = access_zone_name
        self.nfs_mount_point = nfs_mount_point
        self.path = path
        self.protocols = protocols
        self.smb_mount_points = smb_mount_points


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
        access_zone_name = dictionary.get('accessZoneName')
        nfs_mount_point = cohesity_management_sdk.models.isilon_nfs_mount_point.IsilonNfsMountPoint.from_dictionary(dictionary.get('nfsMountPoint')) if dictionary.get('nfsMountPoint') else None
        path = dictionary.get('path')
        protocols = dictionary.get('protocols')
        smb_mount_points = None
        if dictionary.get('smbMountPoints') != None:
            smb_mount_points = list()
            for structure in dictionary.get('smbMountPoints'):
                smb_mount_points.append(cohesity_management_sdk.models.isilon_smb_mount_point.IsilonSmbMountPoint.from_dictionary(structure))

        # Return an object of this model
        return cls(access_zone_name,
                   nfs_mount_point,
                   path,
                   protocols,
                   smb_mount_points)


