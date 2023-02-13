# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreCountByObjectType(object):

    """Implementation of the 'RestoreCountByObjectType' model.

    Number of restore operations by object type.

    Attributes:
        object_count (int): Specifies the number of restores of the object
            type.
        object_type (string): Specifies the type of the restored object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object_count":'objectCount',
        "object_type":'objectType'
    }

    def __init__(self,
                 object_count=None,
                 object_type=None):
        """Constructor for the RestoreCountByObjectType class"""

        # Initialize members of the class
        self.object_count = object_count
        self.object_type = object_type


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
        object_count = dictionary.get('objectCount')
        object_type = dictionary.get('objectType')

        # Return an object of this model
        return cls(object_count,
                   object_type)


