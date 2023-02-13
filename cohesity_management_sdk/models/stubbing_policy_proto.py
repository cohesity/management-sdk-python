# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.retention_policy_proto
import cohesity_management_sdk.models.scheduling_policy_proto

class StubbingPolicyProto(object):

    """Implementation of the 'StubbingPolicyProto' model.

    Stubbing jobs do not use protection policies. Instead, schedule and
    retention policy will be embedded in the BackupJobProto.

    Attributes:
        retention_policy (RetentionPolicyProto): Message that specifies the
            retention policy for backup snapshots.
        scheduling_policy (SchedulingPolicyProto): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "retention_policy":'retentionPolicy',
        "scheduling_policy":'schedulingPolicy'
    }

    def __init__(self,
                 retention_policy=None,
                 scheduling_policy=None):
        """Constructor for the StubbingPolicyProto class"""

        # Initialize members of the class
        self.retention_policy = retention_policy
        self.scheduling_policy = scheduling_policy


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
        retention_policy = cohesity_management_sdk.models.retention_policy_proto.RetentionPolicyProto.from_dictionary(dictionary.get('retentionPolicy')) if dictionary.get('retentionPolicy') else None
        scheduling_policy = cohesity_management_sdk.models.scheduling_policy_proto.SchedulingPolicyProto.from_dictionary(dictionary.get('schedulingPolicy')) if dictionary.get('schedulingPolicy') else None

        # Return an object of this model
        return cls(retention_policy,
                   scheduling_policy)


