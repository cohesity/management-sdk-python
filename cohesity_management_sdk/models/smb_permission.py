# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SmbPermission(object):

    """Implementation of the 'SmbPermission' model.

    Specifies information about a single SMB permission.

    Attributes:
        access (AccessEnum): Specifies the read/write access to the SMB share.
            'kReadyOnly' indicates read only access to the SMB share.
            'kReadWrite' indicates read and write access to the SMB share.
            'kFullControl' indicates full administrative control of the SMB
            share. 'kSpecialAccess' indicates custom permissions to the SMB
            share using access masks structures.
        mode (ModeEnum): Specifies how the permission should be applied to
            folders and/or files. 'kFolderSubFoldersAndFiles' indicates that
            permissions are applied to a Folder and it's sub folders and
            files. 'kFolderAndSubFolders' indicates that permissions are
            applied to a Folder and it's sub folders. 'kFolderAndSubFiles'
            indicates that permissions are applied to a Folder and it's sub
            files. 'kFolderOnly' indicates that permsission are applied to
            folder only. 'kSubFoldersAndFilesOnly' indicates that permissions
            are applied to sub folders and files only. 'kSubFoldersOnly'
            indicates that permissiona are applied to sub folders only.
            'kFilesOnly' indicates that permissions are applied to files
            only.
        sid (string): Specifies the security identifier (SID) of the
            principal.
        special_access_mask (int): Specifies custom access permissions. When
            the access mask from the Access Control Entry (ACE) cannot be
            mapped to one of the enums in 'access', this field is populated
            with the custom mask derived from the ACE and 'access' is set to
            kSpecialAccess. This is a placeholder for storing an unmapped
            access permission and should not be set when creating and editing
            a View.
        special_type (int): Specifies a custom type. When the type from the
            Access Control Entry (ACE) cannot be mapped to one of the enums in
            'type', this field is populated with the custom type derived from
            the ACE and 'type' is set to kSpecialType. This is a placeholder
            for storing an unmapped type and should not be set when creating
            and editing a View.
        mtype (TypeSmbPermissionEnum): Specifies the type of permission.
            'kAllow' indicates access is allowed. 'kDeny' indicates access is
            denied. 'kSpecialType' indicates a type defined in the Access
            Control Entry (ACE) does not map to 'kAllow' or 'kDeny'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access":'access',
        "mode":'mode',
        "sid":'sid',
        "special_access_mask":'specialAccessMask',
        "special_type":'specialType',
        "mtype":'type'
    }

    def __init__(self,
                 access=None,
                 mode=None,
                 sid=None,
                 special_access_mask=None,
                 special_type=None,
                 mtype=None):
        """Constructor for the SmbPermission class"""

        # Initialize members of the class
        self.access = access
        self.mode = mode
        self.sid = sid
        self.special_access_mask = special_access_mask
        self.special_type = special_type
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
        access = dictionary.get('access')
        mode = dictionary.get('mode')
        sid = dictionary.get('sid')
        special_access_mask = dictionary.get('specialAccessMask')
        special_type = dictionary.get('specialType')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(access,
                   mode,
                   sid,
                   special_access_mask,
                   special_type,
                   mtype)


