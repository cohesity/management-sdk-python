# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProtoSID(object):

    """Implementation of the 'ClusterConfigProto_SID' model.

    Represents the security identifier that uniquely defines a security
    principal. SIDs are associated with users and groups.
    Reference: https://msdn.microsoft.com/en-us/library/aa379597.aspx

    Attributes:
        identifier_authority (list of int): The authority under which the SID
            was created. This is always 6 bytes long.
        revision_level (int): The revision level of the SID.
        sub_authority (list of int): List of ids relative to the
            identifier_authority that uniquely identify a principal. The last
            entry in this list is the RID, which uniquely identifies the
            principal within a domain.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "identifier_authority":'identifierAuthority',
        "revision_level":'revisionLevel',
        "sub_authority":'subAuthority'
    }

    def __init__(self,
                 identifier_authority=None,
                 revision_level=None,
                 sub_authority=None):
        """Constructor for the ClusterConfigProtoSID class"""

        # Initialize members of the class
        self.identifier_authority = identifier_authority
        self.revision_level = revision_level
        self.sub_authority = sub_authority


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
        identifier_authority = dictionary.get('identifierAuthority')
        revision_level = dictionary.get('revisionLevel')
        sub_authority = dictionary.get('subAuthority')

        # Return an object of this model
        return cls(identifier_authority,
                   revision_level,
                   sub_authority)


