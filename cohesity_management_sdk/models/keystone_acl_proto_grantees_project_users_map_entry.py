# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.keystone_acl_proto_grantees_project_users

class KeystoneACLProto_Grantees_ProjectUsersMapEntry(object):

    """Implementation of the 'KeystoneACLProto_Grantees_ProjectUsersMapEntry' model.

    Attributes:
        key (string): TODO: Type description here.
        value (KeystoneACLProto_Grantees_ProjectUsers): TODO: Type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the KeystoneACLProto_Grantees_ProjectUsersMapEntry class"""

        # Initialize members of the class
        self.key = key
        self.value = value


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
        key = dictionary.get('key', None)
        value = cohesity_management_sdk.models.keystone_acl_proto_grantees_project_users.KeystoneACLProto_Grantees_ProjectUsers.from_dictionary(dictionary.get('value', None)) if dictionary.get('value') else None

        # Return an object of this model
        return cls(key,
                   value)


