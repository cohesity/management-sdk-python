# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_public_folders_params_root_public_folder
import cohesity_management_sdk.models.entity_proto

class RestoreO365PublicFoldersParams(object):

    """Implementation of the 'RestoreO365PublicFoldersParams' model.

    Attributes:
        root_public_folder_vec (list of
            RestoreO365PublicFoldersParams_RootPublicFolder): If
            is_entire_folder_required is set to false, user will then specify
            which particular sub-folders are to be restored.
        target_folder_path (string): TODO: Type description here.
            Public Folder including the sub-folders is to be restored.
        target_root_public_folder (EntityProto): All RootPublicFolders listed
            in the root_public_folder_vec will be
            restored to this traget RootPublicFolder with appropriate names.

            Let's say root_public_folder_vec is A and B; target_root_public_folder is
            C. The final folder-hierarchy after restore job is finished will look
            like this
            C/{target_folder_path}/A/{whatever is there in Public Folder A}
            B/{whatever is inside Public Folder B}


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "root_public_folder_vec":'rootPublicFolderVec',
        "target_folder_path":'targetFolderPath',
        "target_root_public_folder":'targetRootPublicFolder'
    }

    def __init__(self,
                 root_public_folder_vec=None,
                 target_folder_path=None,
                 target_root_public_folder=None):
        """Constructor for the RestoreO365PublicFoldersParams class"""

        # Initialize members of the class
        self.root_public_folder_vec = root_public_folder_vec
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
        root_public_folder_vec = None
        if dictionary.get('rootPublicFolderVec') != None:
            root_public_folder_vec = list()
            for structure in dictionary.get('rootPublicFolderVec'):
                root_public_folder_vec.append(cohesity_management_sdk.models.restore_o_365_public_folders_params_root_public_folder.RestoreO365PublicFoldersParams_RootPublicFolder.from_dictionary(structure))
        target_folder_path = dictionary.get('targetFolderPath')
        target_root_public_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetRootPublicFolder')) if dictionary.get('targetRootPublicFolder') else None

        # Return an object of this model
        return cls(root_public_folder_vec,
                   target_folder_path,
                   target_root_public_folder)


