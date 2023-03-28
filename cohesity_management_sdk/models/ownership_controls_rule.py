# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OwnershipControlsRule(object):

    """Implementation of the 'OwnershipControlsRule' model.

    TODO: type description here.


    Attributes:

        object_ownership (int): Defines type of object ownership control.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object_ownership":'objectOwnership',
    }
    def __init__(self,
                 object_ownership=None,
            ):

        """Constructor for the OwnershipControlsRule class"""

        # Initialize members of the class
        self.object_ownership = object_ownership

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
        object_ownership = dictionary.get('objectOwnership')

        # Return an object of this model
        return cls(
            object_ownership
)