# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UdaObject(object):

    """Implementation of the 'UdaObject' model.

    Specifies an Object containing information about a Universal Data Adapter
    object.


    Attributes:

        is_leaf (bool): Indicates whether this object is is a leaf object
        object_type (string): Type of this object
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_leaf":'isLeaf',
        "object_type":'objectType',
    }
    def __init__(self,
                 is_leaf=None,
                 object_type=None,
            ):

        """Constructor for the UdaObject class"""

        # Initialize members of the class
        self.is_leaf = is_leaf
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
        is_leaf = dictionary.get('isLeaf')
        object_type = dictionary.get('objectType')

        # Return an object of this model
        return cls(
            is_leaf,
            object_type
)