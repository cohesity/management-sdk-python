# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_permission

class SmbPermissionsInfo(object):

    """Implementation of the 'SmbPermissionsInfo' model.

    Specifies information about SMB permissions.

    Attributes:
        owner_sid (string): Specifies the security identifier (SID) of the
            owner of the SMB share.
        permissions (list of SmbPermission): Array of SMB Permissions.
            Specifies a list of SMB permissions.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "owner_sid":'ownerSid',
        "permissions":'permissions'
    }

    def __init__(self,
                 owner_sid=None,
                 permissions=None):
        """Constructor for the SmbPermissionsInfo class"""

        # Initialize members of the class
        self.owner_sid = owner_sid
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
        owner_sid = dictionary.get('ownerSid')
        permissions = None
        if dictionary.get('permissions') != None:
            permissions = list()
            for structure in dictionary.get('permissions'):
                permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))

        # Return an object of this model
        return cls(owner_sid,
                   permissions)


