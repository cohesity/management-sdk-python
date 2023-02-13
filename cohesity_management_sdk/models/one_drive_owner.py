# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.one_drive_info
import cohesity_management_sdk.models.restore_object_details

class OneDriveOwner(object):

    """Implementation of the 'OneDriveOwner' model.

    Specifies OneDrive owner details.

    Attributes:
        drive_info_list (list of OneDriveInfo): Specifies the Drives that a
            user owns which are to be restored.
        user_detail_object (RestoreObjectDetails): Specifies an object to
            recover or clone or an object to restore files and folders from. A
            VM object can be recovered or cloned. A View object can be cloned.
            To specify a particular snapshot, you must specify a jobRunId and
            a startTimeUsecs. If jobRunId and startTimeUsecs are not
            specified, the last Job Run of the specified Job is used.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_info_list":'driveInfoList',
        "user_detail_object":'userDetailObject'
    }

    def __init__(self,
                 drive_info_list=None,
                 user_detail_object=None):
        """Constructor for the OneDriveOwner class"""

        # Initialize members of the class
        self.drive_info_list = drive_info_list
        self.user_detail_object = user_detail_object


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
        drive_info_list = None
        if dictionary.get('driveInfoList') != None:
            drive_info_list = list()
            for structure in dictionary.get('driveInfoList'):
                drive_info_list.append(cohesity_management_sdk.models.one_drive_info.OneDriveInfo.from_dictionary(structure))
        user_detail_object = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('userDetailObject')) if dictionary.get('userDetailObject') else None

        # Return an object of this model
        return cls(drive_info_list,
                   user_detail_object)


