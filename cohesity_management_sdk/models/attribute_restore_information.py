# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AttributeRestoreInformation(object):

    """Implementation of the 'AttributeRestoreInformation' model.

    Represents the details about the restore of the AD attribute.

    Attributes:
        error_message (list of string): Specifes the error messages
            corresponding to restore of the attribute.
        name (string): Specifies the name of the attribute of the AD object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_message":'errorMessage',
        "name":'name'
    }

    def __init__(self,
                 error_message=None,
                 name=None):
        """Constructor for the AttributeRestoreInformation class"""

        # Initialize members of the class
        self.error_message = error_message
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
        error_message = dictionary.get('errorMessage')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(error_message,
                   name)


