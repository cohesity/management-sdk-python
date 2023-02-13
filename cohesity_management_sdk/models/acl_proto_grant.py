# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.grantee_proto

class ACLProto_Grant(object):

    """Implementation of the 'ACLProto_Grant' model.

    IP Range for range of vip address addition.

    Attributes:
        grantee (GranteeProto): Identifier of a grantee. It can be either a
            registered user or one of Amazon S3 predefined group.
        permission_vec (list of int): Vector of permission granted to this
            grantee.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "grantee": 'grantee',
        "permission_vec": 'permissionVec'
    }

    def __init__(self,
                 grantee=None,
                 permission_vec=None):
        """Constructor for the ACLProto_Grant class"""

        # Initialize members of the class
        self.grantee = grantee
        self.permission_vec = permission_vec


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
        grantee = cohesity_management_sdk.models.grantee_proto.GranteeProto.from_dictionary(dictionary.get('grantee', None)) if dictionary.get('grantee', None) else None
        permission_vec = dictionary.get('permissionVec', None)

        # Return an object of this model
        return cls(grantee,
                   permission_vec)


