# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class LabelSelector_MatchLabelsEntry(object):

    """Implementation of the 'LabelSelector_MatchLabelsEntry' model.

    Attributes:
        key (string): TODO: Type description here.
        value (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the LabelSelector_MatchLabelsEntry class"""

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


