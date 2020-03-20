# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.file_path_filter

class DataMigrationJobParameters(object):

    """Implementation of the 'DataMigrationJobParameters' model.

    Specifies parameters applicable for data migration jobs in NAS
    environment.

    Attributes:
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window are migrated.
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
        file_selection_policy (FileSelectionPolicyEnum): Specifies policy to
            select a file to migrate based on its creation, last access or
            modification time. eg. A file can be selected to migrate if it has
            not been accessed/modified in the ColdFileWindow. enum:
            kOlderThan, kLastAccessed, kLastModified. Specifies policy for
            file seletion in data migration jobs based on time. 'kOlderThan':
            Migrate the files that are older than cold file window.
            'kLastAccessed': Migrate the files thar are not accessed in cold
            file window. 'kLastModified': Migrate the files that have not been
            modified in cold file window.
        file_size_bytes (long|int): Gives the size criteria to be used for
            selecting the files to be migrated in bytes. The cold files that
            are equal and greater than this size are migrated.
        file_size_policy (FileSizePolicyEnum): Specifies policy to select a
            file to migrate based on its size. eg. A file can be selected to
            migrate if its size is greater than or smaller than the
            FileSizeBytes. enum: kGreaterThan, kSmallerThan. Specifies policy
            for file seletion in data migration jobs based on file size.
            'kGreaterThan': Migrate the files whose size are greater than
            specified file size. 'kSmallerThan': Migrate the files whose size
            are smaller than specified file size.
        target_view_name (string): The target view name to which the data will
            be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cold_file_window":'coldFileWindow',
        "file_path_filter":'filePathFilter',
        "file_selection_policy":'fileSelectionPolicy',
        "file_size_bytes":'fileSizeBytes',
        "file_size_policy":'fileSizePolicy',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 cold_file_window=None,
                 file_path_filter=None,
                 file_selection_policy=None,
                 file_size_bytes=None,
                 file_size_policy=None,
                 target_view_name=None):
        """Constructor for the DataMigrationJobParameters class"""

        # Initialize members of the class
        self.cold_file_window = cold_file_window
        self.file_path_filter = file_path_filter
        self.file_selection_policy = file_selection_policy
        self.file_size_bytes = file_size_bytes
        self.file_size_policy = file_size_policy
        self.target_view_name = target_view_name


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
        cold_file_window = dictionary.get('coldFileWindow')
        file_path_filter = cohesity_management_sdk.models.file_path_filter.FilePathFilter.from_dictionary(dictionary.get('filePathFilter')) if dictionary.get('filePathFilter') else None
        file_selection_policy = dictionary.get('fileSelectionPolicy')
        file_size_bytes = dictionary.get('fileSizeBytes')
        file_size_policy = dictionary.get('fileSizePolicy')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(cold_file_window,
                   file_path_filter,
                   file_selection_policy,
                   file_size_bytes,
                   file_size_policy,
                   target_view_name)


