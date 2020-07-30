# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class FileUptieringParams(object):

    """Implementation of the 'FileUptieringParams' model.

    File Uptiering Parameters for NAS migration.

    Attributes:
        file_select_policy (int): File uptier policy based on file
            access/modify time.
        file_size (int): Gives the size criteria to be used for selecting the
            files to be uptiered.
            The hot files, which are greater or smaller than file_size, are
            uptiered.
        file_size_policy (int): File size policy for selecting files to
            uptier.
        hot_file_window (int): Identifies the hot files in the view. Files,
            which are accessed in the last hot_file_window msecs, are
            uptiered. It is only applicable when file_select_policy is
            kLastAccessed.
        num_file_access (int): Number of times file must be accessed within
            hot_file_window in order to qualify for uptiering. Applicable only
            when file_select_policy is kLastAccessed.
        source_view_name (string): The source view name from which the data will
            be uptiered.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_select_policy": 'fileSelectPolicy',
        "file_size": 'fileSize',
        "file_size_policy": 'fileSizePolicy',
        "hot_file_window": 'hotFileWindow',
        "num_file_access":'numFileAccess',
        "source_view_name":'sourceViewName'
    }

    def __init__(self,
                 file_select_policy=None,
                 file_size=None,
                 file_size_policy=None,
                 hot_file_window=None,
                 num_file_access=None,
                 source_view_name=None):
        """Constructor for the FileUptieringParams class"""

        # Initialize members of the class
        self.file_select_policy = file_select_policy
        self.file_size = file_size
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
        file_select_policy = dictionary.get('fileSelectPolicy')
        file_size = dictionary.get('fileSize')
        file_size_policy = dictionary.get('fileSizePolicy')
        hot_file_window = dictionary.get('hotFileWindow')
        num_file_access = dictionary.get('numFileAccess')
        source_view_name = dictionary.get('sourceViewName')

        # Return an object of this model
        return cls(file_select_policy,
                   file_size,
                   file_size_policy,
                   hot_file_window,
                   num_file_access,
                   source_view_name)


