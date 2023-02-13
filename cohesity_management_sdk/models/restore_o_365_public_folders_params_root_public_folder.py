# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_public_folders_params_public_folder
import cohesity_management_sdk.models.restore_object

class RestoreO365PublicFoldersParams_RootPublicFolder(object):

    """Implementation of the 'RestoreO365PublicFoldersParams_RootPublicFolder' model.

    Attributes:
        folder_vec (list of RestoreO365PublicFoldersParams_PublicFolder): If
            is_entire_folder_required is set to false, user will then specify
            which particular sub-folders are to be restored.
        is_entire_root_folder_required (bool): Specify if the entire Root
            Public Folder including the sub-folders is to be restored.
        object (RestoreObject): This will store the details of the Root Public
            Folder to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folder_vec":'folderVec',
        "is_entire_root_folder_required":'isEntireRootFolderRequired',
        "object":'object'
    }

    def __init__(self,
                 folder_vec=None,
                 is_entire_root_folder_required=None,
                 object=None):
        """Constructor for the RestoreO365PublicFoldersParams_RootPublicFolder class"""

        # Initialize members of the class
        self.folder_vec = folder_vec
        self.is_entire_root_folder_required = is_entire_root_folder_required
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
        folder_vec = None
        if dictionary.get('folderVec') != None:
            folder_vec = list()
            for structure in dictionary.get('folderVec'):
                folder_vec.append(cohesity_management_sdk.models.restore_o_365_public_folders_params_public_folder.RestoreO365PublicFoldersParams_PublicFolder.from_dictionary(structure))
        is_entire_root_folder_required = dictionary.get('isEntireRootFolderRequired')
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None

        # Return an object of this model
        return cls(folder_vec,
                   is_entire_root_folder_required,
                   object)


