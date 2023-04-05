# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto


class S3BucketParamsProto(object):

    """Implementation of the 'S3BucketParamsProto' model.

    TODO: type description here.


    Attributes:

        filtering_policies (list of FilteringPolicyProto): The filtering policy
            to decide which objects within a source should be backed up. If
            this is not specified, then all of the objects within the source
            will be backed up.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "filtering_policies":'filteringPolicies',
    }
    def __init__(self,
                 filtering_policies=None,
            ):

        """Constructor for the S3BucketParamsProto class"""

        # Initialize members of the class
        self.filtering_policies = filtering_policies

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
        filtering_policies = None
        if dictionary.get('filteringPolicies') != None:
            filtering_policies = list()
            for structure in dictionary.get('filteringPolicies'):
                filtering_policies.append(cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(structure))

        # Return an object of this model
        return cls(
            filtering_policies
)