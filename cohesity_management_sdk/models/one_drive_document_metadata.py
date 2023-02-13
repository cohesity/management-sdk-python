
# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OneDriveDocumentMetadata(object):

    """Implementation of the 'OneDriveDocumentMetadata' model.

    Specifies the metadata for the OneDrive document.

    Attributes:
        document_type (DocumentTypeEnum): Specifies the type of OneDrive
            document(file/folder). Specifies the OneDrive document type.
            'kFile' specifies a file.
            'kFolder' specifies a folder.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_type":'documentType'
    }

    def __init__(self,
                 document_type=None):
        """Constructor for the OneDriveDocumentMetadata class"""

        # Initialize members of the class
        self.document_type = document_type


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
        document_type = dictionary.get('documentType')

        # Return an object of this model
        return cls(document_type)

