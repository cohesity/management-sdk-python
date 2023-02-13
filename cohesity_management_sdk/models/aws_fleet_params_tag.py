# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AWSFleetParams_Tag(object):

    """Implementation of the 'AWSFleetParams_Tag' model.

    Tag information.

    Attributes:
        key (string): Key for the tag.
        value (string): Value for the tag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the AWSFleetParams_Tag class"""

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
        key = dictionary.get('key', None)
        value = dictionary.get('value', None)

        # Return an object of this model
        return cls(key,
                   value)


