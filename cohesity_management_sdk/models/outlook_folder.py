# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OutlookFolder(object):

    """Implementation of the 'OutlookFolder' model.

    Specifies the Outlook folder details.

    Attributes:
        folder_id (string): Specifies the unique ID of the folder.
        folder_key (long|int): Specifies the key unique within the mailbox of
            the folder.
        outlook_item_id_list (list of string): Specifies the outlook items
            within the folder to be restored incase the user wishes not to
            restore the entire folder.
        restore_entire_folder (bool): Specifies whether the entire folder is
            to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folder_id":'folderId',
        "folder_key":'folderKey',
        "outlook_item_id_list":'outlookItemIdList',
        "restore_entire_folder":'restoreEntireFolder'
    }

    def __init__(self,
                 folder_id=None,
                 folder_key=None,
                 outlook_item_id_list=None,
                 restore_entire_folder=None):
        """Constructor for the OutlookFolder class"""

        # Initialize members of the class
        self.folder_id = folder_id
        self.folder_key = folder_key
        self.outlook_item_id_list = outlook_item_id_list
        self.restore_entire_folder = restore_entire_folder


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
        folder_id = dictionary.get('folderId')
        folder_key = dictionary.get('folderKey')
        outlook_item_id_list = dictionary.get('outlookItemIdList')
        restore_entire_folder = dictionary.get('restoreEntireFolder')

        # Return an object of this model
        return cls(folder_id,
                   folder_key,
                   outlook_item_id_list,
                   restore_entire_folder)


