# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RoleCreateParameters(object):

    """Implementation of the 'RoleCreateParameters' model.

    Specifies the parameters required to create a new custom role such
    as the name, description and the privileges to assign to the role.

    Attributes:
        description (string): Specifies a description about the role.
        name (string): Specifies the name of the custom role.
        privileges (list of string): Array of Privileges.  Specifies the list
            of privileges to assign to the role.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "name":'name',
        "privileges":'privileges'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 privileges=None):
        """Constructor for the RoleCreateParameters class"""

        # Initialize members of the class
        self.description = description
        self.name = name
        self.privileges = privileges


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
        description = dictionary.get('description')
        name = dictionary.get('name')
        privileges = dictionary.get('privileges')

        # Return an object of this model
        return cls(description,
                   name,
                   privileges)


