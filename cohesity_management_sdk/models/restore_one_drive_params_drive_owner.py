# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_one_drive_params_drive_owner_drive
import cohesity_management_sdk.models.restore_object

class RestoreOneDriveParamsDriveOwner(object):

    """Implementation of the 'RestoreOneDriveParams_DriveOwner' model.

    TODO: type model description here.

    Attributes:
        drive_vec (list of RestoreOneDriveParamsDriveOwnerDrive): The list of
            drives that are being restored.
        object (RestoreObject): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_vec":'driveVec',
        "object":'object'
    }

    def __init__(self,
                 drive_vec=None,
                 object=None):
        """Constructor for the RestoreOneDriveParamsDriveOwner class"""

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
                drive_vec.append(cohesity_management_sdk.models.restore_one_drive_params_drive_owner_drive.RestoreOneDriveParamsDriveOwnerDrive.from_dictionary(structure))
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None

        # Return an object of this model
        return cls(drive_vec,
                   object)


