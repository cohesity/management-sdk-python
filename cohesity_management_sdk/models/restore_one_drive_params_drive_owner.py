# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restore_one_drive_params_drive_owner_drive


class RestoreOneDriveParams_DriveOwner(object):

    """Implementation of the 'RestoreOneDriveParams_DriveOwner' model.

    TODO: type description here.


    Attributes:

        drive_vec (list of RestoreOneDriveParams_DriveOwner_Drive): The list of
            drives that are being restored.
        object (RestoreObject): This will store the details of the user whose
            drive is to be restored.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "drive_vec":'driveVec',
        "object":'object',
    }
    def __init__(self,
                 drive_vec=None,
                 object=None,
            ):

        """Constructor for the RestoreOneDriveParams_DriveOwner class"""

        # Initialize members of the class
        self.drive_vec = drive_vec
        self.object = object

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
        drive_vec = None
        if dictionary.get('driveVec') != None:
            drive_vec = list()
            for structure in dictionary.get('driveVec'):
                drive_vec.append(cohesity_management_sdk.models.restore_one_drive_params_drive_owner_drive.RestoreOneDriveParams_DriveOwner_Drive.from_dictionary(structure))
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None

        # Return an object of this model
        return cls(
            drive_vec,
            object
)