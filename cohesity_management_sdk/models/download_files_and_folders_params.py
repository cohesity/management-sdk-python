# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.files_and_folders_info
import cohesity_management_sdk.models.restore_object_details

class DownloadFilesAndFoldersParams(object):

    """Implementation of the 'DownloadFilesAndFoldersParams' model.

    DownloadFilesAndFoldersParams holds the information to create a task for
    downloading list of files or folders

    Attributes:
        files_and_folders_info (list of FilesAndFoldersInfo): Specifies the
            absolute paths for list of files and folders to download.
        name (string): Specifies the name of the Download Task. This field
            must be set and must be a unique name.
        source_object_info (RestoreObjectDetails): Specifies an object to
            recover or clone or an object to restore files and folders from. A
            VM object can be recovered or cloned. A View object can be cloned.
            To specify a particular snapshot, you must specify a jobRunId and
            a startTimeUsecs. If jobRunId and startTimeUsecs are not
            specified, the last Job Run of the specified Job is used.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "files_and_folders_info":'filesAndFoldersInfo',
        "source_object_info":'sourceObjectInfo'
    }

    def __init__(self,
                 name=None,
                 files_and_folders_info=None,
                 source_object_info=None):
        """Constructor for the DownloadFilesAndFoldersParams class"""

        # Initialize members of the class
        self.files_and_folders_info = files_and_folders_info
        self.name = name
        self.source_object_info = source_object_info


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
        name = dictionary.get('name')
        files_and_folders_info = None
        if dictionary.get('filesAndFoldersInfo') != None:
            files_and_folders_info = list()
            for structure in dictionary.get('filesAndFoldersInfo'):
                files_and_folders_info.append(cohesity_management_sdk.models.files_and_folders_info.FilesAndFoldersInfo.from_dictionary(structure))
        source_object_info = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('sourceObjectInfo')) if dictionary.get('sourceObjectInfo') else None

        # Return an object of this model
        return cls(name,
                   files_and_folders_info,
                   source_object_info)


