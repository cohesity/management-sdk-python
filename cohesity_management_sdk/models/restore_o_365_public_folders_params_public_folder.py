# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreO365PublicFoldersParams_PublicFolder(object):

    """Implementation of the 'RestoreO365PublicFoldersParams_PublicFolder' model.

    Proto to capture the restore details of a Public Folder

    Attributes:
        absolute_folder_path (string): The absolute path of the folder.
        folder_id (string): The Unique ID of the folder.
        is_entire_folder_required (bool): Specify if the entire Public Folder
            is to be restored.
        item_id_vec (list of string): If is_entire_folder_required is set to
            false, users will then specify which particular items are to be
            restored.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "absolute_folder_path":'absoluteFolderPath',
        "folder_id":'folderId',
        "is_entire_folder_required":'isEntireFolderRequired',
        "item_id_vec":'itemIdVec'
    }

    def __init__(self,
                 absolute_folder_path=None,
                 folder_id=None,
                 is_entire_folder_required=None,
                 item_id_vec=None):
        """Constructor for the RestoreO365PublicFoldersParams_PublicFolder class"""

        # Initialize members of the class
        self.absolute_folder_path = absolute_folder_path
        self.folder_id = folder_id
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
        absolute_folder_path = dictionary.get('absoluteFolderPath')
        folder_id = dictionary.get('folderId')
        is_entire_folder_required = dictionary.get('isEntireFolderRequired')
        item_id_vec = dictionary.get('itemIdVec')

        # Return an object of this model
        return cls(absolute_folder_path,
                   folder_id,
                   is_entire_folder_required,
                   item_id_vec)


