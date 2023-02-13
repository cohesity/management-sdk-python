# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FlashBladeSmbInfo(object):

    """Implementation of the 'FlashBladeSmbInfo' model.

    Specifies information specific to SMB shares exposed by Pure Flash Blade
    file system.

    Attributes:
        acl_mode (AclModeEnum): ACL mode for this SMB share. 'kNative'
            specifies native ACL mode supports UNIX-like ACLs and Windows
            ACLs. In native mode, because SMB natively supports both ACLs
            while NFS only supports UNIX ACLs, ACLs will not be shared between
            SMB and NFS. 'kShared' shares UNIX-like ACL permissions with the
            NFS protocol. In shared mode both protocol ACL permissions are
            required to match. When one protocol creates files or modifies
            permissions, they must comply with the permission settings of the
            other protocol.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acl_mode":'aclMode'
    }

    def __init__(self,
                 acl_mode=None):
        """Constructor for the FlashBladeSmbInfo class"""

        # Initialize members of the class
        self.acl_mode = acl_mode


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
        acl_mode = dictionary.get('aclMode')

        # Return an object of this model
        return cls(acl_mode)


