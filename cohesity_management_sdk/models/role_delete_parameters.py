# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RoleDeleteParameters(object):

    """Implementation of the 'RoleDeleteParameters' model.

    Specifies the parameters required for deleting one or more roles.

    Attributes:
        names (list of string): Array of Role Names.  Specifies the list of
            roles to delete which are specified by role names.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "names":'names'
    }

    def __init__(self,
                 names=None):
        """Constructor for the RoleDeleteParameters class"""

        # Initialize members of the class
        self.names = names


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
        names = dictionary.get('names')

        # Return an object of this model
        return cls(names)


