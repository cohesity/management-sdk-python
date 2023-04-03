# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_groups_params_group_granular_params
import cohesity_management_sdk.models.restore_object


class RestoreO365GroupsParams_MSGroupInfo(object):

    """Implementation of the 'RestoreO365GroupsParams_MSGroupInfo' model.

    TODO: type description here.


    Attributes:

        group_granular_params (RestoreO365GroupsParams_GroupGranularParams):
            Details of the mailbox and site contents that need to be restored
            for this group.
        is_full_group_required (bool): Specify if the entire Group (mailbox +
            site) is to be restored.
        mailbox_restore_type (int): Whether mailbox restore is full or
            granular.
        object (RestoreObject): This will store the details of the MS groups to
            be restored.
        site_restore_type (int): Whether site restore is full or granular.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "group_granular_params":'groupGranularParams',
        "is_full_group_required":'isFullGroupRequired',
        "mailbox_restore_type":'mailboxRestoreType',
        "object":'object',
        "site_restore_type":'siteRestoreType',
    }
    def __init__(self,
                 group_granular_params=None,
                 is_full_group_required=None,
                 mailbox_restore_type=None,
                 object=None,
                 site_restore_type=None,
            ):

        """Constructor for the RestoreO365GroupsParams_MSGroupInfo class"""

        # Initialize members of the class
        self.group_granular_params = group_granular_params
        self.is_full_group_required = is_full_group_required
        self.mailbox_restore_type = mailbox_restore_type
        self.object = object
        self.site_restore_type = site_restore_type

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
        group_granular_params = cohesity_management_sdk.models.restore_o_365_groups_params_group_granular_params.RestoreO365GroupsParams_GroupGranularParams.from_dictionary(dictionary.get('groupGranularParams')) if dictionary.get('groupGranularParams') else None
        is_full_group_required = dictionary.get('isFullGroupRequired')
        mailbox_restore_type = dictionary.get('mailboxRestoreType')
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None
        site_restore_type = dictionary.get('siteRestoreType')

        # Return an object of this model
        return cls(
            group_granular_params,
            is_full_group_required,
            mailbox_restore_type,
            object,
            site_restore_type
)