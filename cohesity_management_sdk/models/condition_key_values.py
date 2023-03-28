# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ConditionKeyValues(object):

    """Implementation of the 'ConditionKeyValues' model.

    TODO: type description here.


    Attributes:

        value_vec (list of string): This field specifies the values for the
            key.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "value_vec":'valueVec',
    }
    def __init__(self,
                 value_vec=None,
            ):

        """Constructor for the ConditionKeyValues class"""

        # Initialize members of the class
        self.value_vec = value_vec

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
        value_vec = dictionary.get("valueVec")

        # Return an object of this model
        return cls(
            value_vec
)