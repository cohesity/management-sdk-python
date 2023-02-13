# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AlertProperty(object):

    """Implementation of the 'AlertProperty' model.

    Specifies a key-value pair associated with an Alert.

    Attributes:
        key (string): Specifies name of the property.
        value (string): Specifies value of the property.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key":'key',
        "value":'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the AlertProperty class"""

        # Initialize members of the class
        self.key = key
        self.value = value


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
        key = dictionary.get('key')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(key,
                   value)


