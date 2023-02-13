# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.one_drive_owner
import cohesity_management_sdk.models.protection_source

class OneDriveRestoreParameters(object):

    """Implementation of the 'OneDriveRestoreParameters' model.

    Specifies information needed for recovering Drive(s) & Drive items.

    Attributes:
        drive_owner_list (list of OneDriveOwner): Specifies the list of Drive
            owners which are to be restored along with the details of their
            drives.
        restore_to_original_drive (bool): Specifies whether the objects are to
            be restored to the original drive.
        target_drive_id (string): Specifies the Drive Id of the target user
            where the OneDrive items are to be recovered.
        target_folder_path (string): Specifies the target folder path within
            the drive where recovery has to be done.
        target_user (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_owner_list":'driveOwnerList',
        "restore_to_original_drive":'restoreToOriginalDrive',
        "target_drive_id":'targetDriveId',
        "target_folder_path":'targetFolderPath',
        "target_user":'targetUser'
    }

    def __init__(self,
                 drive_owner_list=None,
                 restore_to_original_drive=None,
                 target_drive_id=None,
                 target_folder_path=None,
                 target_user=None):
        """Constructor for the OneDriveRestoreParameters class"""

        # Initialize members of the class
        self.drive_owner_list = drive_owner_list
        self.restore_to_original_drive = restore_to_original_drive
        self.target_drive_id = target_drive_id
        self.target_folder_path = target_folder_path
        self.target_user = target_user


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
        drive_owner_list = None
        if dictionary.get('driveOwnerList') != None:
            drive_owner_list = list()
            for structure in dictionary.get('driveOwnerList'):
                drive_owner_list.append(cohesity_management_sdk.models.one_drive_owner.OneDriveOwner.from_dictionary(structure))
        restore_to_original_drive = dictionary.get('restoreToOriginalDrive')
        target_drive_id = dictionary.get('targetDriveId')
        target_folder_path = dictionary.get('targetFolderPath')
        target_user = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetUser')) if dictionary.get('targetUser') else None

        # Return an object of this model
        return cls(drive_owner_list,
                   restore_to_original_drive,
                   target_drive_id,
                   target_folder_path,
                   target_user)


