# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PublicFolder(object):

    """Implementation of the 'PublicFolder' model.

    Specifies the O365 PublicFolder details.

    Attributes:
        folder_id (string): Specifies the unique ID of the folder.
            Folders to be restored incase user wishes not to restore entire
            PublicFolder.
        public_folder_item_id_list (list of string): Specifies the
            PublicFolder items within the folder to be restored incase
            the user wishes not to restore the entire folder.
        restore_entire_folder (bool): Specifies whether the entire
            folder is to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folder_id":'folderId',
        "public_folder_item_id_list":'publicFolderItemIdList',
        "restore_entire_folder":'restoreEntireFolder'
    }

    def __init__(self,
                 folder_id=None,
                 public_folder_item_id_list=None,
                 restore_entire_folder=None):
        """Constructor for the PublicFolder class"""

        # Initialize members of the class
        self.folder_id = folder_id
        self.public_folder_item_id_list = public_folder_item_id_list
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
        public_folder_item_id_list = dictionary.get('publicFolderItemIdList')
        restore_entire_folder = dictionary.get('restoreEntireFolder')

        # Return an object of this model
        return cls(folder_id,
                   public_folder_item_id_list,
                   restore_entire_folder)


