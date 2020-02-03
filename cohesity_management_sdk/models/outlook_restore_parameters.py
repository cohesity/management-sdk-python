# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.outlook_mailbox
import cohesity_management_sdk.models.protection_source

class OutlookRestoreParameters(object):

    """Implementation of the 'OutlookRestoreParameters' model.

    Specifies information needed for recovering Mailboxes in O365Outlook
    environment.

    Attributes:
        outlook_mailbox_list (list of OutlookMailbox): Specifies the list of
            mailboxes to be restored.
        target_folder_path (string): Specifies the target folder path to
            restore the mailboxes. This will always be specified whether the
            target mailbox is the original or an alternate one.
        target_mailbox (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "outlook_mailbox_list":'outlookMailboxList',
        "target_folder_path":'targetFolderPath',
        "target_mailbox":'targetMailbox'
    }

    def __init__(self,
                 outlook_mailbox_list=None,
                 target_folder_path=None,
                 target_mailbox=None):
        """Constructor for the OutlookRestoreParameters class"""

        # Initialize members of the class
        self.outlook_mailbox_list = outlook_mailbox_list
        self.target_folder_path = target_folder_path
        self.target_mailbox = target_mailbox


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
        outlook_mailbox_list = None
        if dictionary.get('outlookMailboxList') != None:
            outlook_mailbox_list = list()
            for structure in dictionary.get('outlookMailboxList'):
                outlook_mailbox_list.append(cohesity_management_sdk.models.outlook_mailbox.OutlookMailbox.from_dictionary(structure))
        target_folder_path = dictionary.get('targetFolderPath')
        target_mailbox = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetMailbox')) if dictionary.get('targetMailbox') else None

        # Return an object of this model
        return cls(outlook_mailbox_list,
                   target_folder_path,
                   target_mailbox)


