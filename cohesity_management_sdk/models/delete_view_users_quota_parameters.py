# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.user_id

class DeleteViewUsersQuotaParameters(object):

    """Implementation of the 'DeleteViewUsersQuotaParameters' model.

    Specifies the user ids to remove the corresponding quota overrides in
    view.

    Attributes:
        delete_all (bool): Delete all existing user quota override policies.
        user_ids (list of UserId): The user ids whose policy needs to be
            deleted.
        view_name (string): View name of input view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delete_all":'deleteAll',
        "user_ids":'userIds',
        "view_name":'viewName'
    }

    def __init__(self,
                 delete_all=None,
                 user_ids=None,
                 view_name=None):
        """Constructor for the DeleteViewUsersQuotaParameters class"""

        # Initialize members of the class
        self.delete_all = delete_all
        self.user_ids = user_ids
        self.view_name = view_name


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
        delete_all = dictionary.get('deleteAll')
        user_ids = None
        if dictionary.get('userIds') != None:
            user_ids = list()
            for structure in dictionary.get('userIds'):
                user_ids.append(cohesity_management_sdk.models.user_id.UserId.from_dictionary(structure))
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(delete_all,
                   user_ids,
                   view_name)


