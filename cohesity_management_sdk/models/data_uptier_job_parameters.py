# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class DataUptierJobParameters(object):

    """Implementation of the 'DataUptierJobParameters' model.

    Data Uptier Job Parameters.

    Attributes:
    file_selection_policy (FileSelectionPolicyEnum): Specifies policy to
        select a file to uptier based on file access or modification time.
        eg. A file can be selected to uptier if it has been accessed in the
        HotFileWindow or it is modified.
        enum: kLastAccessed, kLastModified.
        Specifies policy for file selection in data migration jobs based on
        time.
        'kOlderThan': Migrate the files that are older than cold file window.
        'kLastAccessed': Migrate the files that are not accessed in cold file
        window.
        'kLastModified': Migrate the files that have not been modified in cold
        file window.
    file_size_bytes (int): Gives the size criteria to be used for selecting the
        files to be uptiered in bytes. The hot files that are smaller or
        greater than this size are uptiered.
    file_size_policy (FileSizePolicyEnum): Specifies policy to select a file
        to uptier based on its size.
        eg. A file can be selected to uptier if its size is greater than or
        smaller than the FileSizeBytes.
        enum: kGreaterThan, kSmallerThan.
        Specifies policy for file selection in data migration jobs based on
        file size.
        'kGreaterThan': Migrate the files whose size are greater than specified
        file size.
        'kSmallerThan': Migrate the files whose size are smaller than specified
        file size.
    hot_file_window (int): Identifies the hot files in the NAS source. Files
        that have been modified in the last hot_file_window are uptiered.
        Applicable only when file_select_policy is kLastAccessed.
    num_file_access (int): Number of times file must be accessed within
        hot_file_window in order to qualify for uptiering. Applicable only
        when file_select_policy is kLastAccessed.
    source_view_name (string): The source view name from which the data will
        be uptiered.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_selection_policy":'fileSelectionPolicy',
        "file_size_bytes":'fileSizeBytes',
        "file_size_policy":'fileSizePolicy',
        "hot_file_window":'hotFileWindow',
        "num_file_access":'numFileAccess',
        "source_view_name":'sourceViewName'
    }

    def __init__(self,
                 file_selection_policy=None,
                 file_size_bytes=None,
                 file_size_policy=None,
                 hot_file_window=None,
                 num_file_access=None,
                 source_view_name=None):
        """Constructor for the DataUptierJobParameters class"""

        # Initialize members of the class
        self.file_selection_policy = file_selection_policy
        self.file_size_bytes = file_size_bytes
        self.file_size_policy = file_size_policy
        self.hot_file_window = hot_file_window
        self.num_file_access = num_file_access
        self.source_view_name = source_view_name


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
        file_selection_policy = dictionary.get('fileSelectionPolicy')
        file_size_bytes = dictionary.get('fileSizeBytes')
        file_size_policy = dictionary.get('fileSizePolicy')
        hot_file_window = dictionary.get('hotFileWindow')
        num_file_access = dictionary.get('numFileAccess')
        source_view_name = dictionary.get('sourceViewName')

        # Return an object of this model
        return cls(file_selection_policy,
                   file_size_bytes,
                   file_size_policy,
                   hot_file_window,
                   num_file_access,
                   source_view_name)


