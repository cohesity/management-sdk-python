# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.keystone_acl_proto_grantees_project_users_map_entry

class KeystoneACLProto_Grantees(object):

    """Implementation of the 'KeystoneACLProto_Grantees' model.

    Attributes:
        all_users (bool):This field indicates if all users are granted ACL
            permission.
        project_id_vec (list of string): Specifies the instance name of the
            Universal Data Adapter entity.
        project_users_map (
            list of KeystoneACLProto_Grantees_ProjectUsersMapEntry):
        role_name_vec (list of string): This field holds a list of Keystone
            roles for which any Keystone user with one (or more) of the roles
            on the project containing the swift container holding this
            KeystoneACLProto is granted ACL permission.
        user_id_vec (list of string): This field holds a list of keystone
            user ids who are granted ACL permission.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_users":'allUsers',
        "project_id_vec":'projectIdVec',
        "project_users_map":'projectUsersMap',
        "role_name_vec":'roleNameVec',
        "user_id_vec":'userIdVec'
    }

    def __init__(self,
                 all_users=None,
                 project_id_vec=None,
                 project_users_map=None,
                 role_name_vec=None,
                 user_id_vec=None):
        """Constructor for the KeystoneACLProto_Grantees class"""

        # Initialize members of the class
        self.all_users = all_users
        self.project_id_vec = project_id_vec
        self.project_users_map = project_users_map
        self.role_name_vec = role_name_vec
        self.user_id_vec = user_id_vec


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
        all_users = dictionary.get('allUsers')
        project_id_vec = dictionary.get('projectIdVec')
        project_users_map = None
        if dictionary.get('projectUsersMap') != None:
            project_id_vec = list()
            for structure in dictionary.get('projectUsersMap'):
                project_id_vec.append(cohesity_management_sdk.models.keystone_acl_proto_grantees_project_users_map_entry.KeystoneACLProto_Grantees_ProjectUsersMapEntry.from_dictionary(structure))
        user_id_vec = dictionary.get('userIdVec')
        role_name_vec = dictionary.get('roleNameVec')

        # Return an object of this model
        return cls(all_users,
                   project_id_vec,
                   project_users_map,
                   role_name_vec,
                   user_id_vec)


