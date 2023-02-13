# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DocError(object):

    """Implementation of the 'DocError' model.

    DocError are document error incurred in yoda service while tagging.

    Attributes:
        document_id (string): DocumentId is document which caused the error.
        error_string (string): ErrorString is the error converted to string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_id": 'documentId',
        "error_string": 'errorString'
    }

    def __init__(self,
                 document_id=None,
                 error_string=None):
        """Constructor for the DocError class"""

        # Initialize members of the class
        self.document_id = document_id
        self.error_string = error_string


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
        document_id = dictionary.get('documentId', None)
        error_string = dictionary.get('errorString', None)

        # Return an object of this model
        return cls(document_id,
                   error_string)


