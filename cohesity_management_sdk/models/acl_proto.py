# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acl_proto_grant
import cohesity_management_sdk.models.common_acl_proto
import cohesity_management_sdk.models.keystone_acl_proto

class ACLProto(object):

    """Implementation of the 'ACLProto' model.

    Protobuf that describes the access control list (ACL) permissions for a
    bucket or for an object.

    Attributes:
        common_acl (CommonACLProto): CommonACL of the Swift container.
        grant_vec (list of ACLProto_Grant): TODO: Type description here.
        keystone_acl (KeystoneACLProto): KeystoneACL of the Swift container.
        swift_read_acl (string): Swift ACL strings.
        swift_write_acl (TypeACLProtoEnum): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "common_acl":'commonAcl',
        "grant_vec":'grantVec',
        "keystone_acl":'keystoneAcl',
        "swift_read_acl":'swiftReadAcl',
        "swift_write_acl":'swiftWriteAcl'
    }

    def __init__(self,
                 common_acl=None,
                 grant_vec=None,
                 keystone_acl=None,
                 swift_read_acl=None,
                 swift_write_acl=None):
        """Constructor for the ACLProto class"""

        # Initialize members of the class
        self.common_acl = common_acl
        self.grant_vec = grant_vec
        self.keystone_acl = keystone_acl
        self.swift_read_acl = swift_read_acl
        self.swift_write_acl = swift_write_acl


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
        common_acl = cohesity_management_sdk.models.common_acl_proto.CommonACLProto.from_dictionary(dictionary.get('commonAcl')) if dictionary.get('commonAcl') else None
        grant_vec = None
        if dictionary.get('grantVec') != None:
            grant_vec = list()
            for structure in dictionary.get('grantVec'):
                grant_vec.append(cohesity_management_sdk.models.acl_proto_grant.ACLProto_Grant.from_dictionary(structure))
        keystone_acl = cohesity_management_sdk.models.keystone_acl_proto.KeystoneACLProto.from_dictionary(dictionary.get('keystoneAcl')) if dictionary.get('keystoneAcl') else None
        swift_write_acl = dictionary.get('swiftWriteAcl')
        swift_read_acl = dictionary.get('swiftReadAcl')

        # Return an object of this model
        return cls(common_acl,
                   grant_vec,
                   keystone_acl,
                   swift_read_acl,
                   swift_write_acl)


