# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreSiteParams_DriveItem(object):

    """Implementation of the 'RestoreSiteParams_DriveItem' model.

    This will be set in case of partial drive recovery.

    Attributes:
        drive_item_path (string): The path of the drive item relative to root.
        id (string): The unique identifier of the item within the Drive.
        is_file_item (bool): Specify if the item is a file or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_item_path":'driveItemPath',
        "id":'id',
        "is_file_item":'isFileItem'
    }

    def __init__(self,
                 drive_item_path=None,
                 id=None,
                 is_file_item=None):
        """Constructor for the RestoreSiteParams_DriveItem class"""

        # Initialize members of the class
        self.drive_item_path = drive_item_path
        self.id = id
        self.is_file_item = is_file_item


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
        drive_item_path = dictionary.get('driveItemPath')
        id = dictionary.get('id')
        is_file_item = dictionary.get('isFileItem')

        # Return an object of this model
        return cls(drive_item_path,
                   id,
                   is_file_item)


