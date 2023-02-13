# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_outlook_params_folder
import cohesity_management_sdk.models.restore_object

class RestoreOutlookParamsMailbox(object):

    """Implementation of the 'RestoreOutlookParams_Mailbox' model.

    TODO: type model description here.

    Attributes:
        folder_vec (list of RestoreOutlookParamsFolder): If
            is_entire_mailbox_required is set to false, user will then specify
            which particular folders are to be restored.
        is_entire_mailbox_required (bool): Specify if the entire mailbox is to
            be restored.
        object (RestoreObject): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folder_vec":'folderVec',
        "is_entire_mailbox_required":'isEntireMailboxRequired',
        "object":'object'
    }

    def __init__(self,
                 folder_vec=None,
                 is_entire_mailbox_required=None,
                 object=None):
        """Constructor for the RestoreOutlookParamsMailbox class"""

        # Initialize members of the class
        self.folder_vec = folder_vec
        self.is_entire_mailbox_required = is_entire_mailbox_required
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
                folder_vec.append(cohesity_management_sdk.models.restore_outlook_params_folder.RestoreOutlookParamsFolder.from_dictionary(structure))
        is_entire_mailbox_required = dictionary.get('isEntireMailboxRequired')
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None

        # Return an object of this model
        return cls(folder_vec,
                   is_entire_mailbox_required,
                   object)


