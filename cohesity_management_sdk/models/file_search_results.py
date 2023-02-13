# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_search_result

class FileSearchResults(object):

    """Implementation of the 'FileSearchResults' model.

    Specifies an array of found files and folders. In addition, a count is
    provided to indicate if additional requests must be made to get
    the full result.

    Attributes:
        files (list of FileSearchResult): Array of Files and Folders.
            Specifies the list of files and folders returned by this request
            that match the specified search and filter criteria. The number of
            files returned is limited by the pageCount field.
        pagination_cookie (string): Specifies cookie for resuming search if
            pagination is being used. For Librarian queries only.
        total_count (long|int): Specifies the total number of files and
            folders that match the filter and search criteria. Use this value
            to determine how many additional requests are required to get the
            full result.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "files":'files',
        "pagination_cookie":'paginationCookie',
        "total_count":'totalCount'
    }

    def __init__(self,
                 files=None,
                 pagination_cookie=None,
                 total_count=None):
        """Constructor for the FileSearchResults class"""

        # Initialize members of the class
        self.files = files
        self.pagination_cookie = pagination_cookie
        self.total_count = total_count


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
        files = None
        if dictionary.get('files') != None:
            files = list()
            for structure in dictionary.get('files'):
                files.append(cohesity_management_sdk.models.file_search_result.FileSearchResult.from_dictionary(structure))
        pagination_cookie = dictionary.get('paginationCookie', None)
        total_count = dictionary.get('totalCount')

        # Return an object of this model
        return cls(files,
                   pagination_cookie,
                   total_count)


