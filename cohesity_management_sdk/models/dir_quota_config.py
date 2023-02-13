# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DirQuotaConfig(object):

    """Implementation of the 'DirQuotaConfig' model.

    Specifies the configuration object of a directory quota.

    Attributes:
        enabled (bool): Specifies whether the directory quota is enabled on
            the view.
        view_name (string): Specifies the name of the view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "view_name":'viewName'
    }

    def __init__(self,
                 enabled=None,
                 view_name=None):
        """Constructor for the DirQuotaConfig class"""

        # Initialize members of the class
        self.enabled = enabled
        self.view_name = view_name


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
        enabled = dictionary.get('enabled')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(enabled,
                   view_name)


