# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NewS3SecretAccessKey(object):

    """Implementation of the 'NewS3SecretAccessKey' model.

    TODO: type model description here.

    Attributes:
        new_key (string): Specifies the new S3 Secret Access key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "new_key":'newKey'
    }

    def __init__(self,
                 new_key=None):
        """Constructor for the NewS3SecretAccessKey class"""

        # Initialize members of the class
        self.new_key = new_key


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
        new_key = dictionary.get('newKey')

        # Return an object of this model
        return cls(new_key)


