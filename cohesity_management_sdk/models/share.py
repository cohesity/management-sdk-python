# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_permission
import cohesity_management_sdk.models.subnet

class Share(object):

    """Implementation of the 'Share' model.

    Specifies the share details when request is made for list of shares
    filtered by ShareName parameter.

    Attributes:
        all_smb_mount_paths (list of string): Array of SMB Paths.  Specifies
            the possible paths that can be used to mount this Share as a SMB
            share. If Active Directory has multiple account names; each
            machine account has its own path.
        enable_filer_audit_log (bool): Specifies whether to enable filer audit
            log on this view alias.
        enable_smb_encryption (bool): Specifies the SMB encryption for the
            View Alias. If set, it enables the SMB encryption for the View
            Alias. Encryption is supported only by SMB 3.x dialects. Dialects
            that do not support would still access data in unencrypted
            format.
        enable_smb_view_discovery (bool): If set, it enables discovery of view
            alias for SMB.
        enforce_smb_encryption (bool): Specifies the SMB encryption for all
            the sessions for the View Alias. If set, encryption is enforced
            for all the sessions for the View Alias. When enabled all future
            and existing unencrypted sessions are disallowed.
        nfs_mount_path (string): Specifies the path for mounting this Share as
            an NFS share.
        path (string): Specifies the path information for this share.
        s_3_access_path (string): Specifies the path to access this View as an
            S3 share.
        share_name (string): The name of the share.
        share_permissions (list of SmbPermission): Specifies a list of share
            level permissions.
        smb_mount_path (string): Specifies the main path for mounting this
            Share as an SMB share.
        subnet_whitelist (list of Subnet): Specifies a list of Subnets with IP
            addresses that have permissions to access the View Alias.
            (Overrides the Subnets specified at the global Cohesity Cluster
            level and View level.)
        super_user_sids (list of string): Specifies a list of user sids who:
            ave Superuser access to this share.
        tenant_id (string): Specifies the unique id of the tenant.
        view_name (string): Specifies the view name this share belongs to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_smb_mount_paths":'allSmbMountPaths',
        "enable_filer_audit_log":'enableFilerAuditLog',
        "enable_smb_encryption":'enableSmbEncryption',
        "enable_smb_view_discovery":'enableSmbViewDiscovery',
        "enforce_smb_encryption":'enforceSmbEncryption',
        "nfs_mount_path":'nfsMountPath',
        "path":'path',
        "s_3_access_path":'s3AccessPath',
        "share_name":'shareName',
        "share_permissions":'sharePermissions',
        "smb_mount_path":'smbMountPath',
        "subnet_whitelist":'subnetWhitelist',
        "super_user_sids":'superUserSids',
        "tenant_id":'tenantId',
        "view_name":'viewName'
    }

    def __init__(self,
                 all_smb_mount_paths=None,
                 enable_filer_audit_log=None,
                 enable_smb_encryption=None,
                 enable_smb_view_discovery=None,
                 enforce_smb_encryption=None,
                 nfs_mount_path=None,
                 path=None,
                 s_3_access_path=None,
                 share_name=None,
                 share_permissions=None,
                 smb_mount_path=None,
                 subnet_whitelist=None,
                 super_user_sids=None,
                 tenant_id=None,
                 view_name=None):
        """Constructor for the Share class"""

        # Initialize members of the class
        self.all_smb_mount_paths = all_smb_mount_paths
        self.enable_filer_audit_log = enable_filer_audit_log
        self.enable_smb_encryption = enable_smb_encryption
        self.enable_smb_view_discovery = enable_smb_view_discovery
        self.enforce_smb_encryption = enforce_smb_encryption
        self.nfs_mount_path = nfs_mount_path
        self.path = path
        self.s_3_access_path = s_3_access_path
        self.share_name = share_name
        self.share_permissions = share_permissions
        self.smb_mount_path = smb_mount_path
        self.subnet_whitelist = subnet_whitelist
        self.super_user_sids = super_user_sids
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
        enable_filer_audit_log = dictionary.get('enableFilerAuditLog')
        enable_smb_encryption = dictionary.get('enableSmbEncryption')
        enable_smb_view_discovery = dictionary.get('enableSmbViewDiscovery')
        enforce_smb_encryption = dictionary.get('enforceSmbEncryption')
        nfs_mount_path = dictionary.get('nfsMountPath')
        path = dictionary.get('path')
        s_3_access_path = dictionary.get('s3AccessPath')
        share_name = dictionary.get('shareName')
        share_permissions = None
        if dictionary.get('sharePermissions') != None:
            share_permissions = list()
            for structure in dictionary.get('sharePermissions'):
                share_permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))
        smb_mount_path = dictionary.get('smbMountPath')
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        super_user_sids = dictionary.get('superUserSids')
        tenant_id = dictionary.get('tenantId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(all_smb_mount_paths,
                   enable_filer_audit_log,
                   enable_smb_encryption,
                   enable_smb_view_discovery,
                   enforce_smb_encryption,
                   nfs_mount_path,
                   path,
                   s_3_access_path,
                   share_name,
                   share_permissions,
                   smb_mount_path,
                   subnet_whitelist,
                   super_user_sids,
                   tenant_id,
                   view_name)


