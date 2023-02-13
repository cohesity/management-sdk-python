# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DatastoreInfo(object):

    """Implementation of the 'DatastoreInfo' model.

    TODO: type model description here.

    Attributes:
        capacity (int): Specifies the capacity of the datastore in bytes.
        free_space (int): Specifies the available space on the datastore in
            bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity":'capacity',
        "free_space":'freeSpace'
    }

    def __init__(self,
                 capacity=None,
                 free_space=None):
        """Constructor for the DatastoreInfo class"""

        # Initialize members of the class
        self.capacity = capacity
        self.free_space = free_space


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
        capacity = dictionary.get('capacity')
        free_space = dictionary.get('freeSpace')

        # Return an object of this model
        return cls(capacity,
                   free_space)


