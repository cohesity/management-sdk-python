# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SourceForPrincipalParam(object):

    """Implementation of the 'SourceForPrincipalParam' model.

    Set Access Permissions for a Principal.
    For the specified principal, grant access permissions to the
    the specified Protection Sources and View names.

    Attributes:
        protection_source_ids (list of long|int): Array of Protection Source
            Ids.  For the specified principal, grant access permissions to the
            Protection Sources listed in this array.
        sid (string): Specifies the SID of the principal to grant access
            permissions to.
        view_names (list of string): Array of View names.  For the specified
            principal, grant access permissions to the Views names listed in
            this array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_source_ids":'protectionSourceIds',
        "sid":'sid',
        "view_names":'viewNames'
    }

    def __init__(self,
                 protection_source_ids=None,
                 sid=None,
                 view_names=None):
        """Constructor for the SourceForPrincipalParam class"""

        # Initialize members of the class
        self.protection_source_ids = protection_source_ids
        self.sid = sid
        self.view_names = view_names


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
        protection_source_ids = dictionary.get('protectionSourceIds')
        sid = dictionary.get('sid')
        view_names = dictionary.get('viewNames')

        # Return an object of this model
        return cls(protection_source_ids,
                   sid,
                   view_names)


