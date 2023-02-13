# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilesToDirectoryMapping(object):

    """Implementation of the 'FilesToDirectoryMapping' model.

    TODO: type model description here.

    Attributes:
        file_pattern (string): Source file name. The file name can be a regex
            matching source files.
        target_directory (string): Target directtory for the source file
            pattern.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_pattern":'filePattern',
        "target_directory":'targetDirectory'
    }

    def __init__(self,
                 file_pattern=None,
                 target_directory=None):
        """Constructor for the FilesToDirectoryMapping class"""

        # Initialize members of the class
        self.file_pattern = file_pattern
        self.target_directory = target_directory


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
        file_pattern = dictionary.get('filePattern')
        target_directory = dictionary.get('targetDirectory')

        # Return an object of this model
        return cls(file_pattern,
                   target_directory)


