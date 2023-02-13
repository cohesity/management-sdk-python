# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SiteDriveItem(object):

    """Implementation of the 'SiteDriveItem' model.

    Specifies details about a Site's Drive item.

    Attributes:
        is_file_item (bool): Specifies whether the current item is a file or
            not.
        item_id (string): Specifies the Id of the Drive item.
        item_path (string): Specifies the path of the Drive item within the
            drive.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_file_item":'isFileItem',
        "item_id":'itemId',
        "item_path":'itemPath'
    }

    def __init__(self,
                 is_file_item=None,
                 item_id=None,
                 item_path=None):
        """Constructor for the SiteDriveItem class"""

        # Initialize members of the class
        self.is_file_item = is_file_item
        self.item_id = item_id
        self.item_path = item_path


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
        is_file_item = dictionary.get('isFileItem')
        item_id = dictionary.get('itemId')
        item_path = dictionary.get('itemPath')

        # Return an object of this model
        return cls(is_file_item,
                   item_id,
                   item_path)


