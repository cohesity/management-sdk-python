# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_permission
import cohesity_management_sdk.models.subnet

class UpdateViewAliasParam(object):

    """Implementation of the 'UpdateViewAliasParam' model.

    Specifies the parameters of updating view alias op.

    Attributes:
        alias_name (string): Name of the alias to be updated.
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
        share_permissions (list of SmbPermission): Specifies a list of share
            level permissions.
        subnet_whitelist (list of Subnet): Specifies a list of Subnets with IP
            addresses that have permissions to access the View Alias.
            (Overrides the Subnets specified at the global Cohesity Cluster
            level and View level.)
        super_user_sids (list of string): Specifies a list of user sids who
            have Superuser access to this alias.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alias_name":'aliasName',
        "enable_filer_audit_log":'enableFilerAuditLog',
        "enable_smb_encryption":'enableSmbEncryption',
        "enable_smb_view_discovery":'enableSmbViewDiscovery',
        "enforce_smb_encryption":'enforceSmbEncryption',
        "share_permissions":'sharePermissions',
        "subnet_whitelist":'subnetWhitelist',
        "super_user_sids":'superUserSids'
    }

    def __init__(self,
                 alias_name=None,
                 enable_filer_audit_log=None,
                 enable_smb_encryption=None,
                 enable_smb_view_discovery=None,
                 enforce_smb_encryption=None,
                 share_permissions=None,
                 subnet_whitelist=None,
                 super_user_sids=None):
        """Constructor for the UpdateViewAliasParam class"""

        # Initialize members of the class
        self.alias_name = alias_name
        self.enable_filer_audit_log = enable_filer_audit_log
        self.enable_smb_encryption = enable_smb_encryption
        self.enable_smb_view_discovery = enable_smb_view_discovery
        self.enforce_smb_encryption = enforce_smb_encryption
        self.share_permissions = share_permissions
        self.subnet_whitelist = subnet_whitelist
        self.super_user_sids = super_user_sids


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
        alias_name = dictionary.get('aliasName')
        enable_filer_audit_log = dictionary.get('enableFilerAuditLog')
        enable_smb_encryption = dictionary.get('enableSmbEncryption')
        enable_smb_view_discovery = dictionary.get('enableSmbViewDiscovery')
        enforce_smb_encryption = dictionary.get('enforceSmbEncryption')
        share_permissions = None
        if dictionary.get('sharePermissions') != None:
            share_permissions = list()
            for structure in dictionary.get('sharePermissions'):
                share_permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        super_user_sids = dictionary.get('superUserSids')

        # Return an object of this model
        return cls(alias_name,
                   enable_filer_audit_log,
                   enable_smb_encryption,
                   enable_smb_view_discovery,
                   enforce_smb_encryption,
                   share_permissions,
                   subnet_whitelist,
                   super_user_sids)


