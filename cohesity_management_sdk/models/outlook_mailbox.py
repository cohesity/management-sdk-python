# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.outlook_folder

class OutlookMailbox(object):

    """Implementation of the 'OutlookMailbox' model.

    Specifies the Outlook mailbox with restore details to support full or
    partial recovery.

    Attributes:
        mailbox_object (RestoreObjectDetails): Specifies an object to recover
            or clone or an object to restore files and folders from. A VM
            object can be recovered or cloned. A View object can be cloned. To
            specify a particular snapshot, you must specify a jobRunId and a
            startTimeUsecs. If jobRunId and startTimeUsecs are not specified,
            the last Job Run of the specified Job is used.
        outlook_folder_list (list of OutlookFolder): Specifies the list of
            folders to be restored incase user wishes not to restore entire
            mailbox.
        restore_entire_mailbox (bool): Specifies whether the enitre mailbox is
            to be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mailbox_object":'mailboxObject',
        "outlook_folder_list":'outlookFolderList',
        "restore_entire_mailbox":'restoreEntireMailbox'
    }

    def __init__(self,
                 mailbox_object=None,
                 outlook_folder_list=None,
                 restore_entire_mailbox=None):
        """Constructor for the OutlookMailbox class"""

        # Initialize members of the class
        self.mailbox_object = mailbox_object
        self.outlook_folder_list = outlook_folder_list
        self.restore_entire_mailbox = restore_entire_mailbox


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
        mailbox_object = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('mailboxObject')) if dictionary.get('mailboxObject') else None
        outlook_folder_list = None
        if dictionary.get('outlookFolderList') != None:
            outlook_folder_list = list()
            for structure in dictionary.get('outlookFolderList'):
                outlook_folder_list.append(cohesity_management_sdk.models.outlook_folder.OutlookFolder.from_dictionary(structure))
        restore_entire_mailbox = dictionary.get('restoreEntireMailbox')

        # Return an object of this model
        return cls(mailbox_object,
                   outlook_folder_list,
                   restore_entire_mailbox)


