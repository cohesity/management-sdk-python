# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_outlook_params
import cohesity_management_sdk.models.restore_site_params

class RestoreO365GroupsParams_GroupGranularParams(object):

    """Implementation of the 'RestoreO365GroupsParams_GroupGranularParams' model.

    Proto to capture the restore details of a Group.

    Attributes:
        group_id (string): The Unique ID of the group.
        group_mbx_params (RestoreOutlookParams): The restore details of the
            group mailbox.
        restore_site_params (RestoreSiteParams): Unread Notification group_id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_id":'groupId',
        "group_mbx_params":'groupMbxParams',
        "restore_site_params":'restoreSiteParams'
    }

    def __init__(self,
                 group_id=None,
                 group_mbx_params=None,
                 restore_site_params=None):
        """Constructor for the RestoreO365GroupsParams_GroupGranularParams class"""

        # Initialize members of the class
        self.group_id = group_id
        self.group_mbx_params = group_mbx_params
        self.restore_site_params = restore_site_params


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
        group_id = dictionary.get('groupId')
        group_mbx_params = cohesity_management_sdk.models.restore_outlook_params.RestoreOutlookParams.from_dictionary(dictionary.get('groupMbxParams')) if dictionary.get('groupMbxParams') else None
        restore_site_params = cohesity_management_sdk.models.restore_site_params.RestoreSiteParams.from_dictionary(dictionary.get('restoreSiteParams')) if dictionary.get('restoreSiteParams') else None

        # Return an object of this model
        return cls(group_id,
                   group_mbx_params,
                   restore_site_params)


