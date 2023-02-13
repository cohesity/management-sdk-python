# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.common_acl_proto_grantees

class CommonACLProto(object):

    """Implementation of the 'CommonACLProto' model.

    Protobuf that describes the Common access control list (ACL) permissions
    for a swift container.
    TODO (avinash_aita): Verify the '.rlistings' write ACL behavior. If
    necessary, remove persisting 'write_rlistings' field and fail such
    requests.

    Attributes:
        read_grantees (CommonACLProto_Grantees): Read permissions granted to
            grantees.
        write_r_listings (bool): Write permissions granted to grantees.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "read_grantees": 'readGrantees',
        "write_r_listings": 'writeRlistings'
    }

    def __init__(self,
                 read_grantees=None,
                 write_r_listings=None):
        """Constructor for the CommonACLProto class"""

        # Initialize members of the class
        self.read_grantees = read_grantees
        self.write_r_listings = write_r_listings


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
        read_grantees = cohesity_management_sdk.models.common_acl_proto_grantees.CommonACLProto_Grantees.from_dictionary(dictionary.get('readGrantees')) if dictionary.get('readGrantees') else None
        write_r_listings = dictionary.get('writeRlistings', None)

        # Return an object of this model
        return cls(read_grantees,
                   write_r_listings)


