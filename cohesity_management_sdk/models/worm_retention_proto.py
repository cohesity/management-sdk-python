# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class WormRetentionProto(object):

    """Implementation of the 'WormRetentionProto' model.

    Message that specifies the WORM attributes. WORM attributes can be
    associated with any of the following:
    1. backup policy: compliance or administrative policy with worm
    retention.
    2. backup runs: worm retention inherited from policy at successful backup
    run completion..
    3. backup tasks do not inherit WORM retention. Instead they check for
    WORM
    property on the corresponding backup run.
    There are no WORM attributes associated with the backup job.

    Attributes:
        policy_type (int): The type of WORM policy set on this run. This field
            is irrelevant while objects are on legal hold. Objects put on
            legal hold automatically raise the WORM level on the object
            behaviorally to the strictest level i.e. kCompliance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy_type":'policyType'
    }

    def __init__(self,
                 policy_type=None):
        """Constructor for the WormRetentionProto class"""

        # Initialize members of the class
        self.policy_type = policy_type


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
        policy_type = dictionary.get('policyType')

        # Return an object of this model
        return cls(policy_type)


