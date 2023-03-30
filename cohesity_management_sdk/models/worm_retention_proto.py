# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class WormRetentionProto(object):

    """Implementation of the 'WormRetentionProto' model.

    Message that specifies the WORM attributes. WORM attributes can be
    associated with any of the following: 1. backup policy: compliance or
    administrative policy with worm retention. 2. backup runs: worm retention
    inherited from policy at successful backup run completion.. 3. backup tasks
    do not inherit WORM retention. Instead they check for WORM property on the
    corresponding backup run. There are no WORM attributes associated with the
    backup job.


    Attributes:

        enable_worm_on_external_target (bool): Whether objects in the external
            target associated with this policy need to be made immutable.
        policy_type (int): The type of WORM policy set on this run. This field
            is irrelevant while objects are on legal hold. Objects put on legal
            hold automatically raise the WORM level on the object behaviorally
            to the strictest level i.e. kCompliance.
        retention_secs (long|int): Retention time for datalock in seconds. This
            will be always relative time.
        version (int): Version number for this proto.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "enable_worm_on_external_target":'enableWormOnExternalTarget',
        "policy_type":'policyType',
        "retention_secs":'retentionSecs',
        "version":'version',
    }
    def __init__(self,
                 enable_worm_on_external_target=None,
                 policy_type=None,
                 retention_secs=None,
                 version=None,
            ):

        """Constructor for the WormRetentionProto class"""

        # Initialize members of the class
        self.enable_worm_on_external_target = enable_worm_on_external_target
        self.policy_type = policy_type
        self.retention_secs = retention_secs
        self.version = version

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
        enable_worm_on_external_target = dictionary.get('enableWormOnExternalTarget')
        policy_type = dictionary.get('policyType')
        retention_secs = dictionary.get('retentionSecs')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            enable_worm_on_external_target,
            policy_type,
            retention_secs,
            version
)