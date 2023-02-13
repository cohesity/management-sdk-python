# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.keystone_acl_proto_grantees

class KeystoneACLProto(object):

    """Implementation of the 'KeystoneACLProto' model.

    Protobuf that describes the Keystone access control list (ACL) permissions
    for a swift container.
    Note: Keystone ACL is applicable for only keystone authenticated users.

    Attributes:
        read_grantees (KeystoneACLProto_Grantees): Grantees with read permission.
        write_grantees (KeystoneACLProto_Grantees): Grantees with write permission.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "read_grantees": 'readGrantees',
        "write_grantees": 'writeGrantees'
    }

    def __init__(self,
                 read_grantees=None,
                 write_grantees=None):
        """Constructor for the KeystoneACLProto class"""

        # Initialize members of the class
        self.read_grantees = read_grantees
        self.write_grantees = write_grantees


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
        read_grantees = cohesity_management_sdk.models.keystone_acl_proto_grantees.KeystoneACLProto_Grantees.from_dictionary(dictionary.get('readGrantees')) if dictionary.get('readGrantees') else None
        write_grantees = cohesity_management_sdk.models.keystone_acl_proto_grantees.KeystoneACLProto_Grantees.from_dictionary(dictionary.get('writeGrantees')) if dictionary.get('writeGrantees') else None

        # Return an object of this model
        return cls(read_grantees,
                   write_grantees)


