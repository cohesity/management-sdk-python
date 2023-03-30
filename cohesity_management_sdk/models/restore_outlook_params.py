# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.ews_to_pst_conversion_params
import cohesity_management_sdk.models.restore_outlook_params_mailbox


class RestoreOutlookParams(object):

    """Implementation of the 'RestoreOutlookParams' model.

    TODO: type description here.


    Attributes:

        mailbox_vec (list of RestoreOutlookParams_Mailbox): In a RestoreJob ,
            user will provide the list of mailboxes to be restored. Provision
            is there for restoring full AND partial mailbox recovery.
        pst_params (EwsToPstConversionParams): These are the parameters that
            user can provide for converting/recovering selected EWS items to
            PST format.
        skip_mbx_permit_for_pst (bool): Indicates whether PST conversion should
            skip mailbox entity permit.
        target_folder_path (string): User will type the target folder path.
            This will always be specified (whether target_mailbox is original
            mailbox or alternate). If multiple folders are selected, they will
            all be restored to this folder. The appropriate hierarchy along
            with the folder names will be preserved.
        target_mailbox (EntityProto): This is the destination mailbox. All
            mailboxes listed in the mailbox_vec will be restored to this
            mailbox with appropriate names. Let's say mailbox_vec is A and B;
            target_mailbox is C. The final folder-hierarchy after restore job
            is finished will look like this : C : {target_folder_path}/|
            |A/{whatever is there in mailbox A} |B/{whatever is inside B
            mailbox B}
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "mailbox_vec":'mailboxVec',
        "pst_params":'pstParams',
        "skip_mbx_permit_for_pst":'skipMbxPermitForPst',
        "target_folder_path":'targetFolderPath',
        "target_mailbox":'targetMailbox',
    }
    def __init__(self,
                 mailbox_vec=None,
                 pst_params=None,
                 skip_mbx_permit_for_pst=None,
                 target_folder_path=None,
                 target_mailbox=None,
            ):

        """Constructor for the RestoreOutlookParams class"""

        # Initialize members of the class
        self.mailbox_vec = mailbox_vec
        self.pst_params = pst_params
        self.skip_mbx_permit_for_pst = skip_mbx_permit_for_pst
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
        mailbox_vec = None
        if dictionary.get('mailboxVec') != None:
            mailbox_vec = list()
            for structure in dictionary.get('mailboxVec'):
                mailbox_vec.append(cohesity_management_sdk.models.restore_outlook_params_mailbox.RestoreOutlookParams_Mailbox.from_dictionary(structure))
        pst_params = cohesity_management_sdk.models.ews_to_pst_conversion_params.EwsToPstConversionParams.from_dictionary(dictionary.get('pstParams')) if dictionary.get('pstParams') else None
        skip_mbx_permit_for_pst = dictionary.get('skipMbxPermitForPst')
        target_folder_path = dictionary.get('targetFolderPath')
        target_mailbox = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetMailbox')) if dictionary.get('targetMailbox') else None

        # Return an object of this model
        return cls(
            mailbox_vec,
            pst_params,
            skip_mbx_permit_for_pst,
            target_folder_path,
            target_mailbox
)