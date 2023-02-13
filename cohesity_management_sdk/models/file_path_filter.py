# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilePathFilter(object):

    """Implementation of the 'FilePathFilter' model.

    Specifies filters to match files and directories on a Server.
    Two kinds of filters are supported. a) prefix which always starts
    with '/'. b) posix which always starts with '*' (cannot be "*" only).
    Regular expressions are not supported.
    If a directory is matched, the action is applicable to all of its
    descendants. File paths not matching any protectFilters are not backed
    up.
    An example is:
    Protect Filters: "/"
    Exclude Filters: "/tmp", "*.mp4"
    Using such a policy will include everything under the root directory
    except
    the /tmp directory and all the mp4 files.

    Attributes:
        exclude_filters (list of string): Array of Excluded File Path Filters.
            Specifies filters to match files or directories that should be
            removed from the list of objects matching ProtectFilters.
        protect_filters (list of string): Array of Protected File Path
            Filters.  Specifies filters to match files or directories that
            should be protected.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exclude_filters":'excludeFilters',
        "protect_filters":'protectFilters'
    }

    def __init__(self,
                 exclude_filters=None,
                 protect_filters=None):
        """Constructor for the FilePathFilter class"""

        # Initialize members of the class
        self.exclude_filters = exclude_filters
        self.protect_filters = protect_filters


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
        exclude_filters = dictionary.get('excludeFilters')
        protect_filters = dictionary.get('protectFilters')

        # Return an object of this model
        return cls(exclude_filters,
                   protect_filters)


