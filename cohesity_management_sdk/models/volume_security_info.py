# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VolumeSecurityInfo(object):

    """Implementation of the 'VolumeSecurityInfo' model.

    Specifies information about NetApp volume security settings.

    Attributes:
        group_id (int): Specifies the Unix group ID for this volume. 0
            indicates the root id.
        permissions (string): Specifies the Unix permission bits in octal
            string format.
        style (StyleEnum): Specifies the security style associated with this
            volume. Specifies the type of a NetApp Volume. 'kUnix' indicates
            Unix-style security. 'kNtfs' indicates Windows NTFS-style
            security. 'kMixed' indicates mixed-style security. 'kUnified'
            indicates Unified-style security.
        user_id (int): Specifies the Unix user id for this volume. 0 indicates
            the root id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_id":'groupId',
        "permissions":'permissions',
        "style":'style',
        "user_id":'userId'
    }

    def __init__(self,
                 group_id=None,
                 permissions=None,
                 style=None,
                 user_id=None):
        """Constructor for the VolumeSecurityInfo class"""

        # Initialize members of the class
        self.group_id = group_id
        self.permissions = permissions
        self.style = style
        self.user_id = user_id


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
        group_id = dictionary.get('groupId')
        permissions = dictionary.get('permissions')
        style = dictionary.get('style')
        user_id = dictionary.get('userId')

        # Return an object of this model
        return cls(group_id,
                   permissions,
                   style,
                   user_id)


