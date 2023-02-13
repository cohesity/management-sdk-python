# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OverwriteViewParam(object):

    """Implementation of the 'OverwriteViewParam' model.

    Specifies the overwrite parameters for the view.

    Attributes:
        source_view_name (string): Specifies the source view name.
        target_view_name (string): Specifies the target view name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source_view_name":'sourceViewName',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 source_view_name=None,
                 target_view_name=None):
        """Constructor for the OverwriteViewParam class"""

        # Initialize members of the class
        self.source_view_name = source_view_name
        self.target_view_name = target_view_name


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
        source_view_name = dictionary.get('sourceViewName')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(source_view_name,
                   target_view_name)


