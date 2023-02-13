# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.throttling_policy_parameters

class ThrottlingPolicyOverride(object):

    """Implementation of the 'ThrottlingPolicyOverride' model.

    Specifies throttling policy override for a Datastore in a registered
    entity.

    Attributes:
        datastore_id (long|int): Specifies the Protection Source id of the
            Datastore.
        datastore_name (string): Specifies the display name of the Datastore.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy for a registered Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datastore_id":'datastoreId',
        "datastore_name":'datastoreName',
        "throttling_policy":'throttlingPolicy'
    }

    def __init__(self,
                 datastore_id=None,
                 datastore_name=None,
                 throttling_policy=None):
        """Constructor for the ThrottlingPolicyOverride class"""

        # Initialize members of the class
        self.datastore_id = datastore_id
        self.datastore_name = datastore_name
        self.throttling_policy = throttling_policy


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
        datastore_id = dictionary.get('datastoreId')
        datastore_name = dictionary.get('datastoreName')
        throttling_policy = cohesity_management_sdk.models.throttling_policy_parameters.ThrottlingPolicyParameters.from_dictionary(dictionary.get('throttlingPolicy')) if dictionary.get('throttlingPolicy') else None

        # Return an object of this model
        return cls(datastore_id,
                   datastore_name,
                   throttling_policy)


