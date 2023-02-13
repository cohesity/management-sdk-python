# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreFileCopyStats(object):

    """Implementation of the 'RestoreFileCopyStats' model.

    This message captures the progress information regarding restore of
    file/directory.

    Attributes:
        estimation_skipped (bool): This will be set to true if the estimation
            step was skipped. NOTE: If estimation is skipped, then progress
            info will not be available.
        num_bytes_copied (long|int): Number of bytes copied so far.
        num_directories_copied (int): Number of directories copied so far.
            NOTE: This just means the creation of directory (not the contents
            of the directory).
        num_files_copied (int): Number of files copied so far.
        total_bytes_to_copy (long|int): Total number of bytes to copy.
        total_directories_to_copy (int): Total number of directories to copy.
            NOTE: This just means the creation of directory (not the contents
            of the directory).
        total_files_to_copy (int): Total number of files to copy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "estimation_skipped":'estimationSkipped',
        "num_bytes_copied":'numBytesCopied',
        "num_directories_copied":'numDirectoriesCopied',
        "num_files_copied":'numFilesCopied',
        "total_bytes_to_copy":'totalBytesToCopy',
        "total_directories_to_copy":'totalDirectoriesToCopy',
        "total_files_to_copy":'totalFilesToCopy'
    }

    def __init__(self,
                 estimation_skipped=None,
                 num_bytes_copied=None,
                 num_directories_copied=None,
                 num_files_copied=None,
                 total_bytes_to_copy=None,
                 total_directories_to_copy=None,
                 total_files_to_copy=None):
        """Constructor for the RestoreFileCopyStats class"""

        # Initialize members of the class
        self.estimation_skipped = estimation_skipped
        self.num_bytes_copied = num_bytes_copied
        self.num_directories_copied = num_directories_copied
        self.num_files_copied = num_files_copied
        self.total_bytes_to_copy = total_bytes_to_copy
        self.total_directories_to_copy = total_directories_to_copy
        self.total_files_to_copy = total_files_to_copy


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
        estimation_skipped = dictionary.get('estimationSkipped')
        num_bytes_copied = dictionary.get('numBytesCopied')
        num_directories_copied = dictionary.get('numDirectoriesCopied')
        num_files_copied = dictionary.get('numFilesCopied')
        total_bytes_to_copy = dictionary.get('totalBytesToCopy')
        total_directories_to_copy = dictionary.get('totalDirectoriesToCopy')
        total_files_to_copy = dictionary.get('totalFilesToCopy')

        # Return an object of this model
        return cls(estimation_skipped,
                   num_bytes_copied,
                   num_directories_copied,
                   num_files_copied,
                   total_bytes_to_copy,
                   total_directories_to_copy,
                   total_files_to_copy)


