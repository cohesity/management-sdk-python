# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.outlook_mailbox
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.pst_parameters

class OutlookRestoreParameters(object):

    """Implementation of the 'OutlookRestoreParameters' model.

    Specifies information needed for recovering Mailboxes in O365Outlook
    environment.

    Attributes:
        outlook_mailbox_list (list of OutlookMailbox): Specifies the list of
            mailboxes to be restored.
        pst_params (PstParameters): Specifies the PST conversion specific
            parameters. This should always be specified when need to convert
            selected items to PST.
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
        "pst_params":'pstParams',
        "target_folder_path":'targetFolderPath',
        "target_mailbox":'targetMailbox'
    }

    def __init__(self,
                 outlook_mailbox_list=None,
                 pst_params=None,
                 target_folder_path=None,
                 target_mailbox=None):
        """Constructor for the OutlookRestoreParameters class"""

        # Initialize members of the class
        self.outlook_mailbox_list = outlook_mailbox_list
        self.pst_params = pst_params
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
        pst_params = cohesity_management_sdk.models.pst_parameters.PstParameters.from_dictionary(dictionary.get('pstParams'))if dictionary.get('pstParams') else None
        if dictionary.get('outlookMailboxList') != None:
            outlook_mailbox_list = list()
            for structure in dictionary.get('outlookMailboxList'):
                outlook_mailbox_list.append(cohesity_management_sdk.models.outlook_mailbox.OutlookMailbox.from_dictionary(structure))
        target_folder_path = dictionary.get('targetFolderPath')
        target_mailbox = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetMailbox')) if dictionary.get('targetMailbox') else None

        # Return an object of this model
        return cls(outlook_mailbox_list,
                   pst_params,
                   target_folder_path,
                   target_mailbox)


