# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Preferences(object):

    """Implementation of the 'Preferences' model.

    TODO: type model description here.

    Attributes:
        locale (string): Locale reflects the language settings of the user.
            Populate using the user preferences stored in Scribe for the user
            wherever needed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "locale":'locale'
    }

    def __init__(self,
                 locale=None):
        """Constructor for the Preferences class"""

        # Initialize members of the class
        self.locale = locale


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
        locale = dictionary.get('locale')

        # Return an object of this model
        return cls(locale)


