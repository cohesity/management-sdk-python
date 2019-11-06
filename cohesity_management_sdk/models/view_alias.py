# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class ViewAlias(object):

    """Implementation of the 'ViewAlias' model.

    TODO: type model description here.

    Attributes:
        alias_name (string): Alias name.
        view_name (string): View name.
        view_path (string): View path for the alias.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alias_name":'aliasName',
        "view_name":'viewName',
        "view_path":'viewPath'
    }

    def __init__(self,
                 alias_name=None,
                 view_name=None,
                 view_path=None):
        """Constructor for the ViewAlias class"""

        # Initialize members of the class
        self.alias_name = alias_name
        self.view_name = view_name
        self.view_path = view_path


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
        alias_name = dictionary.get('aliasName')
        view_name = dictionary.get('viewName')
        view_path = dictionary.get('viewPath')

        # Return an object of this model
        return cls(alias_name,
                   view_name,
                   view_path)


