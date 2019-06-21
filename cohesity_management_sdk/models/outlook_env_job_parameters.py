# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.file_path_filter

class OutlookEnvJobParameters(object):

    """Implementation of the 'OutlookEnvJobParameters' model.

    Specifies job parameters applicable for all 'kO365Outlook' Environment
    type Protection Sources in a Protection Job.

    Attributes:
        file_path_filter (FilePathFilter): Specifies filters to match files
            and directories on a Server. Two kinds of filters are supported.
            a) prefix which always starts with '/'. b) posix which always
            starts with '*' (cannot be "*" only). Regular expressions are not
            supported. If a directory is matched, the action is applicable to
            all of its descendants. File paths not matching any protectFilters
            are not backed up.  An example is: Protect Filters: "/" Exclude
            Filters: "/tmp", "*.mp4" Using such a policy will include
            everything under the root directory except the /tmp directory and
            all the mp4 files.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_path_filter":'filePathFilter'
    }

    def __init__(self,
                 file_path_filter=None):
        """Constructor for the OutlookEnvJobParameters class"""

        # Initialize members of the class
        self.file_path_filter = file_path_filter


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
        file_path_filter = cohesity_management_sdk.models.file_path_filter.FilePathFilter.from_dictionary(dictionary.get('filePathFilter')) if dictionary.get('filePathFilter') else None

        # Return an object of this model
        return cls(file_path_filter)


