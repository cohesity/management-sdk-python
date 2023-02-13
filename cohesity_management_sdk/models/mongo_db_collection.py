# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MongoDBCollection(object):

    """Implementation of the 'MongoDBCollection' model.

    Specifies an Object containing information about a mongodb collection.

    Attributes:
        is_capped_collection (bool): Set to true if this is a capped
            Collection.
        is_mongo_view (bool): Set to true if this Collection is a view.
        size_bytes (int|long): Size of this Collection.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_capped_collection":'isCappedCollection',
        "is_mongo_view":'isMongoView',
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 is_capped_collection=None,
                 is_mongo_view=None,
                 size_bytes=None):
        """Constructor for the MongoDBCollection class"""

        # Initialize members of the class
        self.is_capped_collection = is_capped_collection
        self.is_mongo_view = is_mongo_view
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
        is_capped_collection = dictionary.get('isCappedCollection')
        is_mongo_view = dictionary.get('isMongoView')
        size_bytes = dictionary.get('sizeBytes')

        # Return an object of this model
        return cls(is_capped_collection,
                   is_mongo_view,
                   size_bytes)


