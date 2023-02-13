# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UdaObjects(object):

    """Implementation of the 'UdaObjects' model.

    Identifier for an individual object to be backed up. E.x. db1.

    Attributes:
        name (string): Name of the source
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name'
    }

    def __init__(self,
                 name=None):
        """Constructor for the UdaObjects class"""

        # Initialize members of the class
        self.name = name


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
        name = dictionary.get('name')

        # Return an object of this model
        return cls(name)


