# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class PublicFoldersBackupEnvParams(object):

    """Implementation of the 'PublicFoldersBackupEnvParams' model.

    Message to capture any additional backup params for Public Folders within
    Office365 environment.

    Attributes:
        filtering_policy (FilteringPolicyProto): The filtering policy describes
            which paths within a Public Folder should be excluded within the
            backup. If this is not specified, then the entire Public Folders
            will be backed up.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filtering_policy":'filteringPolicy'
    }

    def __init__(self,
                 filtering_policy=None):
        """Constructor for the PublicFoldersBackupEnvParams class"""

        # Initialize members of the class
        self.filtering_policy = filtering_policy


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
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None

        # Return an object of this model
        return cls(filtering_policy)


