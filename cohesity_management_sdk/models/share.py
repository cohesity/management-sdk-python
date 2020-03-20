# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class Share(object):

    """Implementation of the 'Share' model.

    Specifies the share details when request is made for list of shares
    filtered by ShareName parameter.

    Attributes:
        all_smb_mount_paths (list of string): Array of SMB Paths.  Specifies
            the possible paths that can be used to mount this Share as a SMB
            share. If Active Directory has multiple account names; each
            machine account has its own path.
        nfs_mount_path (string): Specifies the path for mounting this Share as
            an NFS share.
        path (string): Specifies the path information for this share.
        s_3_access_path (string): Specifies the path to access this View as an
            S3 share.
        share_name (string): The name of the share.
        smb_mount_path (string): Specifies the main path for mounting this
            Share as an SMB share.
        tenant_id (string): Specifies the unique id of the tenant.
        view_name (string): Specifies the view name this share belongs to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_smb_mount_paths":'allSmbMountPaths',
        "nfs_mount_path":'nfsMountPath',
        "path":'path',
        "s_3_access_path":'s3AccessPath',
        "share_name":'shareName',
        "smb_mount_path":'smbMountPath',
        "tenant_id":'tenantId',
        "view_name":'viewName'
    }

    def __init__(self,
                 all_smb_mount_paths=None,
                 nfs_mount_path=None,
                 path=None,
                 s_3_access_path=None,
                 share_name=None,
                 smb_mount_path=None,
                 tenant_id=None,
                 view_name=None):
        """Constructor for the Share class"""

        # Initialize members of the class
        self.all_smb_mount_paths = all_smb_mount_paths
        self.nfs_mount_path = nfs_mount_path
        self.path = path
        self.s_3_access_path = s_3_access_path
        self.share_name = share_name
        self.smb_mount_path = smb_mount_path
        self.tenant_id = tenant_id
        self.view_name = view_name


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
        all_smb_mount_paths = dictionary.get('allSmbMountPaths')
        nfs_mount_path = dictionary.get('nfsMountPath')
        path = dictionary.get('path')
        s_3_access_path = dictionary.get('s3AccessPath')
        share_name = dictionary.get('shareName')
        smb_mount_path = dictionary.get('smbMountPath')
        tenant_id = dictionary.get('tenantId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(all_smb_mount_paths,
                   nfs_mount_path,
                   path,
                   s_3_access_path,
                   share_name,
                   smb_mount_path,
                   tenant_id,
                   view_name)


