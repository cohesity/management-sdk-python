# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OwnerInfo(object):

    """Implementation of the 'OwnerInfo' model.

    Information about a resource (i.e., bucket or object) owner.

    Attributes:
        user_id (string): Unique identifier of the owner.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id":'userId'
    }

    def __init__(self,
                 user_id=None):
        """Constructor for the OwnerInfo class"""

        # Initialize members of the class
        self.user_id = user_id


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
        user_id = dictionary.get('userId')

        # Return an object of this model
        return cls(user_id)


