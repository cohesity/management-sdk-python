# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SmbPrincipal(object):

    """Implementation of the 'SmbPrincipal' model.

    TODO: type model description here.

    Attributes:
        domain (string): Specifies domain name of the principal.
        name (string): Specifies name of the SMB principal which may be a
            group or user.
        sid (string): Specifies unique Security ID (SID) of the principal that
            look similar to windows domain SID.
        mtype (string): Specifies the type. This can be a user or a group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "name":'name',
        "sid":'sid',
        "mtype":'type'
    }

    def __init__(self,
                 domain=None,
                 name=None,
                 sid=None,
                 mtype=None):
        """Constructor for the SmbPrincipal class"""

        # Initialize members of the class
        self.domain = domain
        self.name = name
        self.sid = sid
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
        domain = dictionary.get('domain')
        name = dictionary.get('name')
        sid = dictionary.get('sid')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(domain,
                   name,
                   sid,
                   mtype)


