# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RoleUpdateParameters(object):

    """Implementation of the 'RoleUpdateParameters' model.

    Specifies parameters required to update a role.

    Attributes:
        description (string): Specifies a description about the role.
        privileges (list of string): Array of Privileges.  Specifies the list
            of privileges to assign to the role.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "privileges":'privileges'
    }

    def __init__(self,
                 description=None,
                 privileges=None):
        """Constructor for the RoleUpdateParameters class"""

        # Initialize members of the class
        self.description = description
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
        privileges = dictionary.get('privileges')

        # Return an object of this model
        return cls(description,
                   privileges)


