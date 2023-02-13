# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class SharepPointSiteBackupEnvParams(object):

    """Implementation of the 'SharepPointSiteBackupEnvParams' model.

    Message to capture any additional backup params for SharePoint within the
    Office365 environment.

    Attributes:
        doc_lib_filtering_policy (FilteringPolicyProto): The filtering policy
            describes which objects within a source should be excluded within
            the backup. If this is not specified, then all of the objects
            within the source will be backed up.
            NOTE: This filtering policy assumes the paths within a site. The
            first token will specify a doc library name.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "doc_lib_filtering_policy":'docLibFilteringPolicy'
    }

    def __init__(self,
                 doc_lib_filtering_policy=None):
        """Constructor for the SharepPointSiteBackupEnvParams class"""

        # Initialize members of the class
        self.doc_lib_filtering_policy = doc_lib_filtering_policy


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
        doc_lib_filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('docLibFilteringPolicy')) if dictionary.get('docLibFilteringPolicy') else None

        # Return an object of this model
        return cls(doc_lib_filtering_policy)


