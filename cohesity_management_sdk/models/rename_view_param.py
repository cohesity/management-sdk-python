# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RenameViewParam(object):

    """Implementation of the 'RenameViewParam' model.

    Specifies the rename parameters for the view.

    Attributes:
        new_view_name (string): Specifies the new name of the View.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "new_view_name":'newViewName'
    }

    def __init__(self,
                 new_view_name=None):
        """Constructor for the RenameViewParam class"""

        # Initialize members of the class
        self.new_view_name = new_view_name


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
        new_view_name = dictionary.get('newViewName')

        # Return an object of this model
        return cls(new_view_name)


