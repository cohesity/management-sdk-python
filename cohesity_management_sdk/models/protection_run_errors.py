# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.request_error

class ProtectionRunErrors(object):

    """Implementation of the 'ProtectionRunErrors' model.

    TODO: type model description here.

    Attributes:
        errors (list of RequestError): Specifies the list of errors
            encountered by a task during a protection run.
        file_names (list of string): Specifies the list of filenames with
            errors encountered by a task during a protection run.
        pagination_cookie (string): Specifies the cookie for next set of
            results.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "errors":'errors',
        "file_names":'fileNames',
        "pagination_cookie":'paginationCookie'
    }

    def __init__(self,
                 errors=None,
                 file_names=None,
                 pagination_cookie=None):
        """Constructor for the ProtectionRunErrors class"""

        # Initialize members of the class
        self.errors = errors
        self.file_names = file_names
        self.pagination_cookie = pagination_cookie


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
        errors = None
        if dictionary.get('errors') != None:
            errors = list()
            for structure in dictionary.get('errors'):
                errors.append(cohesity_management_sdk.models.request_error.RequestError.from_dictionary(structure))
        file_names = dictionary.get('fileNames')
        pagination_cookie = dictionary.get('paginationCookie')

        # Return an object of this model
        return cls(errors,
                   file_names,
                   pagination_cookie)


