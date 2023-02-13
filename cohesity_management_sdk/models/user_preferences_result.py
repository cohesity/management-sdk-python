# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UserPreferencesResult(object):

    """Implementation of the 'UserPreferencesResult' model.

    Specifies the result of user preference.

    Attributes:
        preferences (dict<object, string>): Preferences is a key-value map of
            preferences.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "preferences":'preferences'
    }

    def __init__(self,
                 preferences=None):
        """Constructor for the UserPreferencesResult class"""

        # Initialize members of the class
        self.preferences = preferences


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
        preferences = dictionary.get('preferences')

        # Return an object of this model
        return cls(preferences)


