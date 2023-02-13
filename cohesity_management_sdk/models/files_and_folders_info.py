# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilesAndFoldersInfo(object):

    """Implementation of the 'FilesAndFoldersInfo' model.

    FilesAndFolders specifies the metadata information about the files
    and(or)
    folders for creating a download task.

    Attributes:
        absolute_path (string): AbsolutePath specifies the absolute path of
            the specified file or folder.
        is_directory (bool): IsDirectory specifies if specified object is a
            directory or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "absolute_path":'absolutePath',
        "is_directory":'isDirectory'
    }

    def __init__(self,
                 absolute_path=None,
                 is_directory=None):
        """Constructor for the FilesAndFoldersInfo class"""

        # Initialize members of the class
        self.absolute_path = absolute_path
        self.is_directory = is_directory


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
        absolute_path = dictionary.get('absolutePath')
        is_directory = dictionary.get('isDirectory')

        # Return an object of this model
        return cls(absolute_path,
                   is_directory)


