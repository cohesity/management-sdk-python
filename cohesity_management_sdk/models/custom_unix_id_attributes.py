# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CustomUnixIdAttributes(object):

    """Implementation of the 'CustomUnixIdAttributes' model.

    Specifies the custom attributes when mapping type is set to
    'kCustomAttributes'. It defines the attribute names to derive the mapping
    for a user of an Active Directory domain.

    Attributes:
        gid_attr_name (string): Specifies the custom field name in Active
            Directory user properties to get the GID.
        uid_attr_name (string): Specifies the custom field name in Active
            Directory user properties to get the UID.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gid_attr_name":'gidAttrName',
        "uid_attr_name":'uidAttrName'
    }

    def __init__(self,
                 gid_attr_name=None,
                 uid_attr_name=None):
        """Constructor for the CustomUnixIdAttributes class"""

        # Initialize members of the class
        self.gid_attr_name = gid_attr_name
        self.uid_attr_name = uid_attr_name


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
        gid_attr_name = dictionary.get('gidAttrName')
        uid_attr_name = dictionary.get('uidAttrName')

        # Return an object of this model
        return cls(gid_attr_name,
                   uid_attr_name)


