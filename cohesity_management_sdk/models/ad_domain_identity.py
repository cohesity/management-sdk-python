# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AdDomainIdentity(object):

    """Implementation of the 'AdDomainIdentity' model.

    AD domain identity information.

    Attributes:
        dn (string): Specifies distinguished name of the domain.
        guid (string): Specifies Unique objectGUID for an AD domain.
        name (string): Specifies display name of the domain.
        sid (string): Specifies domain SID.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dn":'dn',
        "guid":'guid',
        "name":'name',
        "sid":'sid'
    }

    def __init__(self,
                 dn=None,
                 guid=None,
                 name=None,
                 sid=None):
        """Constructor for the AdDomainIdentity class"""

        # Initialize members of the class
        self.dn = dn
        self.guid = guid
        self.name = name
        self.sid = sid


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
        dn = dictionary.get('dn')
        guid = dictionary.get('guid')
        name = dictionary.get('name')
        sid = dictionary.get('sid')

        # Return an object of this model
        return cls(dn,
                   guid,
                   name,
                   sid)


