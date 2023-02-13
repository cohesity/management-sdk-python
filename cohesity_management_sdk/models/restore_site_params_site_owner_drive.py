# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_site_params_drive_item

class RestoreSiteParams_SiteOwner_Drive(object):

    """Implementation of the 'RestoreSiteParams_SiteOwner_Drive' model.

    TODO: Type model description here.

    Attributes:
        is_entire_drive_required (bool): Specify if the entire drive is to be
            restored. This field should be false if restore_item_vec size > 0.
        restore_drive_id (string): Id of the drive whose items are being
            restored.
        restore_drive_name (string): Specifies the name of the drive whos
            items are being restored.
            NOTE: For restore either the drive Id or the name must be
            populated.
        restore_path_vec (list of RestoreSiteParams_DriveItem): List of drive
            paths that need to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_entire_drive_required":'isEntireDriveRequired',
        "restore_drive_id":'restoreDriveId',
        "restore_drive_name":'restoreDriveName',
        "restore_path_vec":'restorePathVec'
    }

    def __init__(self,
                 is_entire_drive_required=None,
                 restore_drive_id=None,
                 restore_drive_name=None,
                 restore_path_vec=None):
        """Constructor for the RestoreSiteParams_SiteOwner_Drive class"""

        # Initialize members of the class
        self.is_entire_drive_required = is_entire_drive_required
        self.restore_drive_id = restore_drive_id
        self.restore_drive_name = restore_drive_name
        self.restore_path_vec = restore_path_vec


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
        restore_drive_name = dictionary.get('restoreDriveName')
        restore_path_vec = None
        if dictionary.get('restorePathVec') != None:
            restore_path_vec = list()
            for structure in dictionary.get('restorePathVec'):
                restore_path_vec.append(cohesity_management_sdk.models.restore_site_params_drive_item.RestoreSiteParams_DriveItem.from_dictionary(structure))

        # Return an object of this model
        return cls(is_entire_drive_required,
                   restore_drive_id,
                   restore_drive_name,
                   restore_path_vec)


