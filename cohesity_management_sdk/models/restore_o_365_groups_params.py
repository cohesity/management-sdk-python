# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_groups_params_ms_group_info


class RestoreO365GroupsParams(object):

    """Implementation of the 'RestoreO365GroupsParams' model.

    TODO: type description here.


    Attributes:

        create_new_group (bool): Bool which specifies, if we have to create a
            new group if it doesn't exist.
        ms_groups_vec (list of RestoreO365GroupsParams_MSGroupInfo): List of
            groups getting restored.
        restore_original_owners_members (bool): Bool which specifies, if the
            original members/owners should be part of the newly created target
            group.
        restore_to_original (bool): Whether or not all groups are restored to
            original location.
        target_group (string): Target group in case restore_to_original is
            false.
        target_group_name (string): Target group name in case
            restore_to_original is false. This will be ignored if restoring to
            alternate existing group.
        target_group_owner (string): The string which contains the owner smtp
            address for the target group.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "create_new_group":'createNewGroup',
        "ms_groups_vec":'msGroupsVec',
        "restore_original_owners_members":'restoreOriginalOwnersMembers',
        "restore_to_original":'restoreToOriginal',
        "target_group":'targetGroup',
        "target_group_name":'targetGroupName',
        "target_group_owner":'targetGroupOwner',
    }
    def __init__(self,
                 create_new_group=None,
                 ms_groups_vec=None,
                 restore_original_owners_members=None,
                 restore_to_original=None,
                 target_group=None,
                 target_group_name=None,
                 target_group_owner=None,
            ):

        """Constructor for the RestoreO365GroupsParams class"""

        # Initialize members of the class
        self.create_new_group = create_new_group
        self.ms_groups_vec = ms_groups_vec
        self.restore_original_owners_members = restore_original_owners_members
        self.restore_to_original = restore_to_original
        self.target_group = target_group
        self.target_group_name = target_group_name
        self.target_group_owner = target_group_owner

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
        create_new_group = dictionary.get('createNewGroup')
        ms_groups_vec = None
        if dictionary.get('msGroupsVec') != None:
            ms_groups_vec = list()
            for structure in dictionary.get('msGroupsVec'):
                ms_groups_vec.append(cohesity_management_sdk.models.restore_o_365_groups_params_ms_group_info.RestoreO365GroupsParams_MSGroupInfo.from_dictionary(structure))
        restore_original_owners_members = dictionary.get('restoreOriginalOwnersMembers')
        restore_to_original = dictionary.get('restoreToOriginal')
        target_group = dictionary.get('targetGroup')
        target_group_name = dictionary.get('targetGroupName')
        target_group_owner = dictionary.get('targetGroupOwner')

        # Return an object of this model
        return cls(
            create_new_group,
            ms_groups_vec,
            restore_original_owners_members,
            restore_to_original,
            target_group,
            target_group_name,
            target_group_owner
)