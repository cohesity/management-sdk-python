# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.smb_permission
import cohesity_management_sdk.models.subnet

class ViewAlias(object):

    """Implementation of the 'ViewAlias' model.

    Specifies the parameters of a view alias.

    Attributes:
        alias_name (string): Alias name.
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
        view_name (string): View name.
        view_path (string): View path for the alias.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alias_name":'aliasName',
        "enable_smb_encryption":'enableSmbEncryption',
        "enable_smb_view_discovery":'enableSmbViewDiscovery',
        "enforce_smb_encryption":'enforceSmbEncryption',
        "share_permissions":'sharePermissions',
        "subnet_whitelist":'subnetWhitelist',
        "view_name":'viewName',
        "view_path":'viewPath'
    }

    def __init__(self,
                 alias_name=None,
                 enable_smb_encryption=None,
                 enable_smb_view_discovery=None,
                 enforce_smb_encryption=None,
                 share_permissions=None,
                 subnet_whitelist=None,
                 view_name=None,
                 view_path=None):
        """Constructor for the ViewAlias class"""

        # Initialize members of the class
        self.alias_name = alias_name
        self.enable_smb_encryption = enable_smb_encryption
        self.enable_smb_view_discovery = enable_smb_view_discovery
        self.enforce_smb_encryption = enforce_smb_encryption
        self.share_permissions = share_permissions
        self.subnet_whitelist = subnet_whitelist
        self.view_name = view_name
        self.view_path = view_path


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
        view_name = dictionary.get('viewName')
        view_path = dictionary.get('viewPath')

        # Return an object of this model
        return cls(alias_name,
                   enable_smb_encryption,
                   enable_smb_view_discovery,
                   enforce_smb_encryption,
                   share_permissions,
                   subnet_whitelist,
                   view_name,
                   view_path)


