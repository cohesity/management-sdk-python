# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_permission

class AliasSmbConfig(object):

    """Implementation of the 'AliasSmbConfig' model.

    Message defining SMB config for IRIS. SMB config contains SMB encryption
    flags, SMB discoverable flag and Share level permissions.

    Attributes:
        caching_enabled (bool): Indicate if offline file caching is supported
        discovery_enabled (bool): Whether the share is discoverable.
        encryption_enabled (bool): Whether SMB encryption is enabled for this
            share. Encryption is supported only by SMB 3.x dialects. Dialects
            that do not support would still access data in unencrypted
            format.
        encryption_required (bool): Whether to enforce encryption for all the
            sessions for this view. When enabled all unencrypted sessions are
            disallowed.
        is_share_level_permission_empty (bool): Indicate if share level
            permission is cleared by user.
        permissions (list of SmbPermission): Share level permissions.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "caching_enabled":'cachingEnabled',
        "discovery_enabled":'discoveryEnabled',
        "encryption_enabled":'encryptionEnabled',
        "encryption_required":'encryptionRequired',
        "is_share_level_permission_empty":'isShareLevelPermissionEmpty',
        "permissions":'permissions'
    }

    def __init__(self,
                 caching_enabled=None,
                 discovery_enabled=None,
                 encryption_enabled=None,
                 encryption_required=None,
                 is_share_level_permission_empty=None,
                 permissions=None):
        """Constructor for the AliasSmbConfig class"""

        # Initialize members of the class
        self.caching_enabled = caching_enabled
        self.discovery_enabled = discovery_enabled
        self.encryption_enabled = encryption_enabled
        self.encryption_required = encryption_required
        self.is_share_level_permission_empty = is_share_level_permission_empty
        self.permissions = permissions


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
        caching_enabled = dictionary.get('cachingEnabled')
        discovery_enabled = dictionary.get('discoveryEnabled')
        encryption_enabled = dictionary.get('encryptionEnabled')
        encryption_required = dictionary.get('encryptionRequired')
        is_share_level_permission_empty = dictionary.get('isShareLevelPermissionEmpty')
        permissions = None
        if dictionary.get('permissions') != None:
            permissions = list()
            for structure in dictionary.get('permissions'):
                permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))

        # Return an object of this model
        return cls(caching_enabled,
                   discovery_enabled,
                   encryption_enabled,
                   encryption_required,
                   is_share_level_permission_empty,
                   permissions)


