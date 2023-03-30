# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.worm_retention_proto


class RetentionPolicyProto(object):

    """Implementation of the 'RetentionPolicyProto' model.

    Message that specifies the retention policy for backup snapshots.


    Attributes:

        num_days_to_keep (long|int): The number of days to keep the snapshots
            for a backup run.
        num_secs_to_keep (int): The number of seconds to keep the snapshots for
            a backup run.
        worm_retention (WormRetentionProto): If the WORM lock is enabled on
            this policy, details of WORM policy. Absence of this field
            indicates WORM is not enabled on this policy. Also, presence of
            this field doesn't necessarily imply WORM protection. This is
            because the field could be present but the retention could have
            expired. If the policy has WORM enabled, We do not propagate it to
            attached backup jobs and further down the hierarchy here. Instead,
            any update on the backup run performs WORM checks based on the
            currently attached policy. Backup runs, when finished, inherit the
            WORM property from the corresponding attached policy at the
            completion time.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "num_days_to_keep":'numDaysToKeep',
        "num_secs_to_keep":'numSecsToKeep',
        "worm_retention":'wormRetention',
    }
    def __init__(self,
                 num_days_to_keep=None,
                 num_secs_to_keep=None,
                 worm_retention=None,
            ):

        """Constructor for the RetentionPolicyProto class"""

        # Initialize members of the class
        self.num_days_to_keep = num_days_to_keep
        self.num_secs_to_keep = num_secs_to_keep
        self.worm_retention = worm_retention

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
        num_days_to_keep = dictionary.get('numDaysToKeep')
        num_secs_to_keep = dictionary.get('numSecsToKeep')
        worm_retention = cohesity_management_sdk.models.worm_retention_proto.WormRetentionProto.from_dictionary(dictionary.get('wormRetention')) if dictionary.get('wormRetention') else None

        # Return an object of this model
        return cls(
            num_days_to_keep,
            num_secs_to_keep,
            worm_retention
)