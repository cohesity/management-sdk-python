# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MongoDBRecoverJobParams(object):

    """Implementation of the 'MongoDBRecoverJobParams' model.

    Contains any additional mongodb environment specific params for the
    recover job.

    Attributes:
        suffix (string): A suffix that is to be applied to all recovered
            entities

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "suffix": 'suffix'
    }

    def __init__(self,
                 suffix=None):
        """Constructor for the MongoDBRecoverJobParams class"""

        # Initialize members of the class
        self.suffix = suffix


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
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(suffix)


