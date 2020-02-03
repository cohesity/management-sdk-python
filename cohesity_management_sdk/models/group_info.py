# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class GroupInfo(object):

    """Implementation of the 'GroupInfo' model.

    Specifies struct with basic group details.

    Attributes:
        domain (string): Specifies domain name of the user.
        group_name (string): Specifies group name of the group.
        sid (string): Specifies unique Security ID (SID) of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "group_name":'groupName',
        "sid":'sid'
    }

    def __init__(self,
                 domain=None,
                 group_name=None,
                 sid=None):
        """Constructor for the GroupInfo class"""

        # Initialize members of the class
        self.domain = domain
        self.group_name = group_name
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
        domain = dictionary.get('domain')
        group_name = dictionary.get('groupName')
        sid = dictionary.get('sid')

        # Return an object of this model
        return cls(domain,
                   group_name,
                   sid)


