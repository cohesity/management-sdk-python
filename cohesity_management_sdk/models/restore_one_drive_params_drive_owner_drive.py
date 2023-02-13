# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_one_drive_params_drive_item

class RestoreOneDriveParamsDriveOwnerDrive(object):

    """Implementation of the 'RestoreOneDriveParams_DriveOwner_Drive' model.

    TODO: type model description here.

    Attributes:
        is_entire_drive_required (bool): Specify if the entire drive is to be
            restored. This field should be false if restore_item_vec size >
            0.
        restore_drive_id (string): Id of the drive whose items are being
            restored.
        restore_item_vec (list of RestoreOneDriveParamsDriveItem): List of
            drive paths that need to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_entire_drive_required":'isEntireDriveRequired',
        "restore_drive_id":'restoreDriveId',
        "restore_item_vec":'restoreItemVec'
    }

    def __init__(self,
                 is_entire_drive_required=None,
                 restore_drive_id=None,
                 restore_item_vec=None):
        """Constructor for the RestoreOneDriveParamsDriveOwnerDrive class"""

        # Initialize members of the class
        self.is_entire_drive_required = is_entire_drive_required
        self.restore_drive_id = restore_drive_id
        self.restore_item_vec = restore_item_vec


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
        is_entire_drive_required = dictionary.get('isEntireDriveRequired')
        restore_drive_id = dictionary.get('restoreDriveId')
        restore_item_vec = None
        if dictionary.get('restoreItemVec') != None:
            restore_item_vec = list()
            for structure in dictionary.get('restoreItemVec'):
                restore_item_vec.append(cohesity_management_sdk.models.restore_one_drive_params_drive_item.RestoreOneDriveParamsDriveItem.from_dictionary(structure))

        # Return an object of this model
        return cls(is_entire_drive_required,
                   restore_drive_id,
                   restore_item_vec)


