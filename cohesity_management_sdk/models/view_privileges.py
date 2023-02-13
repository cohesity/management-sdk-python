# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ViewPrivileges(object):

    """Implementation of the 'ViewPrivileges' model.

    ViewPrivileges specifies which views are allowed to be accessed by an app
    instance.

    Attributes:
        privileges_type (PrivilegesTypeViewPrivilegesEnum): Specifies if all,
            none or specific views are allowed to be accessed.
            Specifies if all, none or specific views are allowed to be
            accessed.
            kNone - None of the views have access.
            kAll - All the views have access.
            kSpecific - Only specific views have access.
        view_ids (list of int): Specifies the ids of the views which are
            allowed to be accessed in case the privilege type is kSpecific.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "privileges_type": 'privilegesType',
        "view_ids": 'viewIds'
    }

    def __init__(self,
                 privileges_type=None,
                 view_ids=None):
        """Constructor for the ViewPrivileges class"""

        # Initialize members of the class
        self.privileges_type = privileges_type
        self.view_ids = view_ids


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
        privileges_type = dictionary.get('privilegesType', None)
        view_ids = dictionary.get('viewIds', None)

        # Return an object of this model
        return cls(privileges_type,
                   view_ids)


