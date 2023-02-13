# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FixedUnixIdMapping(object):

    """Implementation of the 'FixedUnixIdMapping' model.

    Specifies the fields when mapping type is set to 'kFixed'. It maps all
    Active Directory users of a domain to a fixed Unix uid, and gid.

    Attributes:
        gid (long|int): Specifies the fixed Unix GID, when mapping type is set
            to kFixed.
        uid (long|int): Specifies the fixed Unix UID, when mapping type is set
            to kFixed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gid":'gid',
        "uid":'uid'
    }

    def __init__(self,
                 gid=None,
                 uid=None):
        """Constructor for the FixedUnixIdMapping class"""

        # Initialize members of the class
        self.gid = gid
        self.uid = uid


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
        gid = dictionary.get('gid')
        uid = dictionary.get('uid')

        # Return an object of this model
        return cls(gid,
                   uid)


