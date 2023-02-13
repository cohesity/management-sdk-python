# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.view_alias

class ActivateViewAliasesResult(object):

    """Implementation of the 'ActivateViewAliasesResult' model.

    Specifies the information of activated alias views created
    for a view.

    Attributes:
        aliases (list of ViewAlias): Aliases created for the view. A view
            alias allows a directory path inside a view to be mounted using
            the alias name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aliases":'aliases'
    }

    def __init__(self,
                 aliases=None):
        """Constructor for the ActivateViewAliasesResult class"""

        # Initialize members of the class
        self.aliases = aliases


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
        aliases = None
        if dictionary.get('aliases') != None:
            aliases = list()
            for structure in dictionary.get('aliases'):
                aliases.append(cohesity_management_sdk.models.view_alias.ViewAlias.from_dictionary(structure))

        # Return an object of this model
        return cls(aliases)


