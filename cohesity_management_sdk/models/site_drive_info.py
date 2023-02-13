# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.site_drive_item

class SiteDriveInfo(object):

    """Implementation of the 'SiteDriveInfo' model.

    Specifies the Site's Document Library drive info.

    Attributes:
        drive_id (string): Specifies the Id of the Drive.
        drive_item_list (list of SiteDriveItem): Specifies the Drive items
            such as files/folders.
        drive_name (string): Specifies the drive name for the document
            repository. Incase of drive Id not present, this field must be
            populated to trigger restore.
        restore_entire_drive (bool): Specifies whether entire drive is to be
            restored. This should be set to false if specific drive items are
            to be restored within 'DriveItemList'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_id": 'driveId',
        "drive_item_list": 'driveItemList',
        "drive_name": 'driveName',
        "restore_entire_drive": 'restoreEntireDrive'
    }

    def __init__(self,
                 drive_id=None,
                 drive_item_list=None,
                 drive_name=None,
                 restore_entire_drive=None):
        """Constructor for the SiteDriveInfo class"""

        # Initialize members of the class
        self.drive_id = drive_id
        self.drive_item_list = drive_item_list
        self.drive_name = drive_name
        self.restore_entire_drive = restore_entire_drive

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
        drive_id = dictionary.get('driveId')
        drive_item_list = None
        if dictionary.get('driveItemList') != None:
            drive_item_list = list()
            for structure in dictionary.get('driveItemList'):
                drive_item_list.append(cohesity_management_sdk.models.site_drive_item.SiteDriveItem.from_dictionary(structure))
        drive_name = dictionary.get('driveName')
        restore_entire_drive = dictionary.get('restoreEntireDrive')

        # Return an object of this model
        return cls(drive_id,
                   drive_item_list,
                   drive_name,
                   restore_entire_drive)


