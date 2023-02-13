# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_nlm_locks

class ListNlmLocksResponse(object):

    """Implementation of the 'ListNlmLocksResponse' model.

    Query response to list of NLM locks.

    Attributes:
        cookie (string): Specifies an opaque string to pass to get the next
            set of NLM locks. If null is returned, this response is the last
            set of NLM locks.
        files_nlm_locks (list of FileNlmLocks): Specifies the list of NLM
            locks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cookie":'cookie',
        "files_nlm_locks":'filesNlmLocks'
    }

    def __init__(self,
                 cookie=None,
                 files_nlm_locks=None):
        """Constructor for the ListNlmLocksResponse class"""

        # Initialize members of the class
        self.cookie = cookie
        self.files_nlm_locks = files_nlm_locks


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
        cookie = dictionary.get('cookie')
        files_nlm_locks = None
        if dictionary.get('filesNlmLocks') != None:
            files_nlm_locks = list()
            for structure in dictionary.get('filesNlmLocks'):
                files_nlm_locks.append(cohesity_management_sdk.models.file_nlm_locks.FileNlmLocks.from_dictionary(structure))

        # Return an object of this model
        return cls(cookie,
                   files_nlm_locks)


