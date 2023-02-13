# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class KmsDeleteParams(object):

    """Implementation of the 'KmsDeleteParams' model.

    Params to delete a KMS with specified server name.

    Attributes:
        id (long|int): Specifies a unique id of the KMS config.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id'
    }

    def __init__(self,
                 id=None):
        """Constructor for the KmsDeleteParams class"""

        # Initialize members of the class
        self.id = id


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
        id = dictionary.get('id')

        # Return an object of this model
        return cls(id)


