# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_groups_params_ms_group_info

class RestoreO365GroupsParams(object):

    """Implementation of the 'RestoreO365GroupsParams' model.

    Attributes:
        ms_groups_vec (list of RestoreO365GroupsParams_MSGroupInfo): List of
            groups getting restored.
        restore_to_original (bool): Whether or not all groups are restored to
            original location.
        target_group (string): Target group in case restore_to_original is
            false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ms_groups_vec":'msGroupsVec',
        "restore_to_original":'restoreToOriginal',
        "target_group":'targetGroup'
    }

    def __init__(self,
                 ms_groups_vec=None,
                 restore_to_original=None,
                 target_group=None):
        """Constructor for the RestoreO365GroupsParams class"""

        # Initialize members of the class
        self.ms_groups_vec = ms_groups_vec
        self.restore_to_original = restore_to_original
        self.target_group = target_group


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
        ms_groups_vec = None
        if dictionary.get('msGroupsVec') != None:
            ms_groups_vec = list()
            for structure in dictionary.get('msGroupsVec'):
                ms_groups_vec.append(cohesity_management_sdk.models.restore_o_365_groups_params_ms_group_info.RestoreO365GroupsParams_MSGroupInfo.from_dictionary(structure))
        restore_to_original = dictionary.get('restoreToOriginal')
        target_group = dictionary.get('targetGroup')

        # Return an object of this model
        return cls(ms_groups_vec,
                   restore_to_original,
                   target_group)


