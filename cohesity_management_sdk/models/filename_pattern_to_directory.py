# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilenamePatternToDirectory(object):

    """Implementation of the 'FilenamePatternToDirectory' model.

    Specifies a filename pattern and the directory path where to keep files
    matching that pattern.

    Attributes:
        directory (string): Specifies the directory where to keep the files
            matching the pattern.
        filename_pattern (string): Specifies a pattern to be matched with
            filenames. This can be a regex expression.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "directory":'directory',
        "filename_pattern":'filenamePattern'
    }

    def __init__(self,
                 directory=None,
                 filename_pattern=None):
        """Constructor for the FilenamePatternToDirectory class"""

        # Initialize members of the class
        self.directory = directory
        self.filename_pattern = filename_pattern


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
        directory = dictionary.get('directory')
        filename_pattern = dictionary.get('filenamePattern')

        # Return an object of this model
        return cls(directory,
                   filename_pattern)


