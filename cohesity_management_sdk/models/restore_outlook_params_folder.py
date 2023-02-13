# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreOutlookParamsFolder(object):

    """Implementation of the 'RestoreOutlookParams_Folder' model.

    This will be set in case of partial mailbox recovery.

    Attributes:
        folder_id (string): The Unique ID of the folder.
        folder_key (long|int): The Unique key of the folder.
        is_entire_folder_required (bool): Specify if the entire folder is to
            be restored.
        item_id_vec (list of string): If is_entire_folder_required is set to
            false, user will then specify which particular items are to be
            restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folder_id":'folderId',
        "folder_key":'folderKey',
        "is_entire_folder_required":'isEntireFolderRequired',
        "item_id_vec":'itemIdVec'
    }

    def __init__(self,
                 folder_id=None,
                 folder_key=None,
                 is_entire_folder_required=None,
                 item_id_vec=None):
        """Constructor for the RestoreOutlookParamsFolder class"""

        # Initialize members of the class
        self.folder_id = folder_id
        self.folder_key = folder_key
        self.is_entire_folder_required = is_entire_folder_required
        self.item_id_vec = item_id_vec


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
        is_entire_folder_required = dictionary.get('isEntireFolderRequired')
        item_id_vec = dictionary.get('itemIdVec')

        # Return an object of this model
        return cls(folder_id,
                   folder_key,
                   is_entire_folder_required,
                   item_id_vec)


