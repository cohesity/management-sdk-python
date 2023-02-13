# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.root_public_folder
import cohesity_management_sdk.models.protection_source

class PublicFoldersRestoreParameters(object):

    """Implementation of the 'PublicFoldersRestoreParameters' model.

    Specifies information needed for recovering O365 Public Folders in
    O365Publicfolders environment.

    Attributes:
        root_public_folder_list (list of RootPublicFolder): Specifies the list of Public Folders
            to be restored.
        target_folder_path (string): Specifies the target folder path to restore
            the Public Folders.
        target_root_public_folder (ProtectionSource): Specifies the destination Public
            Folder where the Public Folders specified within RootPublicFolders
            will be restored with their appropriate paths. Unread Notification
            Count.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "root_public_folder_list":'rootPublicFolderList',
        "target_folder_path":'targetFolderPath',
        "target_root_public_folder":'targetRootPublicFolder'
    }

    def __init__(self,
                 root_public_folder_list=None,
                 target_folder_path=None,
                 target_root_public_folder=None):
        """Constructor for the PublicFoldersRestoreParameters class"""

        # Initialize members of the class
        self.root_public_folder_list = root_public_folder_list
        self.target_folder_path = target_folder_path
        self.target_root_public_folder = target_root_public_folder


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
        root_public_folder_list = None
        if dictionary.get('rootPublicFolderList') != None:
            root_public_folder_list = list()
            for structure in dictionary.get('rootPublicFolderList'):
                root_public_folder_list.append(cohesity_management_sdk.models.root_public_folder.RootPublicFolder.from_dictionary(structure))
        target_folder_path = dictionary.get('targetFolderPath')
        target_root_public_folder = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetRootPublicFolder')) if dictionary.get('targetRootPublicFolder') else None

        # Return an object of this model
        return cls(root_public_folder_list,
                   target_folder_path,
                   target_root_public_folder)


