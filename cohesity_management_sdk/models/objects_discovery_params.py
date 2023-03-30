# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.users_discovery_params


class ObjectsDiscoveryParams(object):

    """Implementation of the 'ObjectsDiscoveryParams' model.

    Specifies the parameters used for discovering the office 365 objects
    selectively during source registration or refresh.


    Attributes:

        discoverable_object_type_list (list of string): Specifies the list of
            object types that will be discovered as part of source registration
            or refresh.
        users_discovery_params (UsersDiscoveryParams): Specifies the discovery
            params for kUser entities.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "discoverable_object_type_list":'discoverableObjectTypeList',
        "users_discovery_params":'usersDiscoveryParams',
    }
    def __init__(self,
                 discoverable_object_type_list=None,
                 users_discovery_params=None,
            ):

        """Constructor for the ObjectsDiscoveryParams class"""

        # Initialize members of the class
        self.discoverable_object_type_list = discoverable_object_type_list
        self.users_discovery_params = users_discovery_params

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
        discoverable_object_type_list = dictionary.get("discoverableObjectTypeList")
        users_discovery_params = cohesity_management_sdk.models.users_discovery_params.UsersDiscoveryParams.from_dictionary(dictionary.get('usersDiscoveryParams')) if dictionary.get('usersDiscoveryParams') else None

        # Return an object of this model
        return cls(
            discoverable_object_type_list,
            users_discovery_params
)