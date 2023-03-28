# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_path_filter


class OneDriveEnvJobParameters(object):

    """Implementation of the 'OneDriveEnvJobParameters' model.

    Specifies OneDrive job parameters applicable for all Office365 Environment
    type Protection Sources in a Protection Job.


    Attributes:

        file_path_filter (FilePathFilter): The filtering policy describes which
            paths within the onedrive should be excluded within the backup. If
            this is not specified, then the entire onedrive will be backed up.
        should_backup_onedrive (bool): Specifies whether OneDrive(s) of each
            Office365 Users/Groups within the job, should be backed up or not.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "file_path_filter":'filePathFilter',
        "should_backup_onedrive":'shouldBackupOnedrive',
    }
    def __init__(self,
                 file_path_filter=None,
                 should_backup_onedrive=None,
            ):

        """Constructor for the OneDriveEnvJobParameters class"""

        # Initialize members of the class
        self.file_path_filter = file_path_filter
        self.should_backup_onedrive = should_backup_onedrive

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
        file_path_filter = cohesity_management_sdk.models.file_path_filter.FilePathFilter.from_dictionary(dictionary.get('filePathFilter')) if dictionary.get('filePathFilter') else None
        should_backup_onedrive = dictionary.get('shouldBackupOnedrive')

        # Return an object of this model
        return cls(
            file_path_filter,
            should_backup_onedrive
)