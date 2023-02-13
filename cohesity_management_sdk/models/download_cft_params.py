# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DownloadCftParams(object):

    """Implementation of the 'DownloadCftParams' model.

    TODO: Type model description here.

    Attributes:
        file_name (string): Specifies the file name of the cloud formation
            template.
        file_path (string): Specifies the file path of the template. If passed
            null, "/home/cohesity/bin" will be considered as file path.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_name": 'fileName',
        "file_path": 'filePath'
    }

    def __init__(self,
                 file_name=None,
                 file_path=None):
        """Constructor for the DownloadCftParams class"""

        # Initialize members of the class
        self.file_name = file_name
        self.file_path = file_path


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
        file_name = dictionary.get('fileName', None)
        file_path = dictionary.get('filePath', None)

        # Return an object of this model
        return cls(file_name,
                   file_path)


