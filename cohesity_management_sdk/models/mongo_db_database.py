# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MongoDBDatabase(object):

    """Implementation of the 'MongoDBDatabase' model.

    Specifies an Object containing information about a mongodb database.

    Attributes:
        size_bytes (int|long): Size of this Database.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 size_bytes=None):
        """Constructor for the MongoDBDatabase class"""

        # Initialize members of the class
        self.size_bytes = size_bytes


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
        size_bytes = dictionary.get('sizeBytes')

        # Return an object of this model
        return cls(size_bytes)


