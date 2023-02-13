# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.request_error
import cohesity_management_sdk.models.filesystem_volume

class FileRestoreInfo(object):

    """Implementation of the 'FileRestoreInfo' model.

    Specifies restore information of a file or a folder.

    Attributes:
        error (RequestError): Details about the Error.
        filename (string): Specifies the path of the file/directory.
        filesystem_volume (FilesystemVolume): Specifies information about a
            filesystem volume.
        is_folder (bool): Specifies whether the file path is a folder.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "filename":'filename',
        "filesystem_volume":'filesystemVolume',
        "is_folder":'isFolder'
    }

    def __init__(self,
                 error=None,
                 filename=None,
                 filesystem_volume=None,
                 is_folder=None):
        """Constructor for the FileRestoreInfo class"""

        # Initialize members of the class
        self.error = error
        self.filename = filename
        self.filesystem_volume = filesystem_volume
        self.is_folder = is_folder


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
        error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        filename = dictionary.get('filename')
        filesystem_volume = cohesity_management_sdk.models.filesystem_volume.FilesystemVolume.from_dictionary(dictionary.get('filesystemVolume')) if dictionary.get('filesystemVolume') else None
        is_folder = dictionary.get('isFolder')

        # Return an object of this model
        return cls(error,
                   filename,
                   filesystem_volume,
                   is_folder)


