# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.public_folder
import cohesity_management_sdk.models.restore_object_details

class RootPublicFolder(object):

    """Implementation of the 'RootPublicFolder' model.

    Specifies the RootPublicFolder with restore details to support full or
    partial recovery.

    Attributes:
        public_folder_list (list of PublicFolder): Specifies the list of Public
            Folders to be restored incase user wishes not to restore entire
            RootPublicFolder.
        restore_entire_root_public_folder (bool): Notification list.
        root_public_folder_object (RestoreObjectDetails): Specifies the details
            of the RootPublicFolder object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "public_folder_list":'publicFolderList',
        "restore_entire_root_public_folder":'restoreEntireRootPublicFolder',
        "root_public_folder_object":'rootPublicFolderObject'
    }

    def __init__(self,
                 public_folder_list=None,
                 restore_entire_root_public_folder=None,
                 root_public_folder_object=None):
        """Constructor for the RootPublicFolder class"""

        # Initialize members of the class
        self.public_folder_list = public_folder_list
        self.restore_entire_root_public_folder = restore_entire_root_public_folder
        self.root_public_folder_object = root_public_folder_object


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
        public_folder_list = None
        if dictionary.get('publicFolderList') != None:
            public_folder_list = list()
            for structure in dictionary.get('publicFolderList'):
                restore_entire_root_public_folder.append(cohesity_management_sdk.models.public_folder.PublicFolder.from_dictionary(structure))

        restore_entire_root_public_folder = dictionary.get('restoreEntireRootPublicFolder')
        root_public_folder_object = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('rootPublicFolderObject')) if dictionary.get('rootPublicFolderObject') else None

        # Return an object of this model
        return cls(public_folder_list,
                   restore_entire_root_public_folder,
                   root_public_folder_object)


