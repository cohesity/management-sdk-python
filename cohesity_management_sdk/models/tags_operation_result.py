# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.doc_error

class TagsOperationResult(object):

    """Implementation of the 'TagsOperationResult' model.

    TagsOperationResult specifies the result of tagging operation.

    Attributes:
    doc_errors (list of DocError):  DocErrors are document errors incurred in
        yoda service while tagging.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "doc_errors":'docErrors'
    }

    def __init__(self,
                 doc_errors=None):
        """Constructor for the TagsOperationResult class"""

        # Initialize members of the class
        self.doc_errors = doc_errors


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
        doc_errors = None
        if dictionary.get('docErrors') != None:
            doc_errors = list()
            for structure in dictionary.get('docErrors'):
                doc_errors.append(cohesity_management_sdk.models.doc_error.DocError.from_dictionary(structure))

        # Return an object of this model
        return cls(doc_errors)


