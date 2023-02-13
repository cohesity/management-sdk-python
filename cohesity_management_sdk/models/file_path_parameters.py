# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilePathParameters(object):

    """Implementation of the 'FilePathParameters' model.

    Specifies a file or a directory to protect in a Physical Server.
    If a directory is specified, all of its descendants are also backed up.
    Optionally, files or subdirectories can be explicitly excluded.

    Attributes:
        backup_file_path (string): Specifies absolute path to a file or a
            directory in a Physical Server to protect.
        excluded_file_paths (list of string): Array of Excluded File Paths.
            Specifies absolute paths to descendant files or subdirectories of
            backupFilePath that should not be protected.
        skip_nested_volumes (bool): Specifies if any subdirectories under
            backupFilePath, where local or network volumes are mounted, should
            be excluded from being protected. If true, the volumes are not
            protected. deprecated: true

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_file_path":'backupFilePath',
        "excluded_file_paths":'excludedFilePaths',
        "skip_nested_volumes":'skipNestedVolumes'
    }

    def __init__(self,
                 backup_file_path=None,
                 excluded_file_paths=None,
                 skip_nested_volumes=None):
        """Constructor for the FilePathParameters class"""

        # Initialize members of the class
        self.backup_file_path = backup_file_path
        self.excluded_file_paths = excluded_file_paths
        self.skip_nested_volumes = skip_nested_volumes


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
        backup_file_path = dictionary.get('backupFilePath')
        excluded_file_paths = dictionary.get('excludedFilePaths')
        skip_nested_volumes = dictionary.get('skipNestedVolumes')

        # Return an object of this model
        return cls(backup_file_path,
                   excluded_file_paths,
                   skip_nested_volumes)


