# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class NasBackupParams(object):

    """Implementation of the 'NasBackupParams' model.

    Message to capture any additional backup params for a NAS environment.

    Attributes:
        continue_on_error (bool): Whether the backup job should continue on
            errors for snapshot based backups. For non-snapshot-based generic
            NAS backup jobs, Magneto always continues on errors.
        filtering_policy (FilteringPolicyProto): Proto to encapsulate the
            filtering policy for backup objects like files or directories. If
            an object is not matched by any of the 'allow_filters', it will be
            excluded in the backup. If an object is matched by one of the
            'deny_filters', it will always be excluded in the backup.
            Basically 'deny_filters' overwrite 'allow_filters' if they both
            match the same object. Currently we only support two kinds of
            filter: prefix which always starts with '/', or postfix which
            always starts with '*' (cannot be "*" only). We don't support
            regular expression right now. A concrete example is: Allow
            filters: "/" Deny filters: "/tmp", "*.mp4" Using such a policy
            will include everything under the root directory except the /tmp
            directory and all the mp4 files.
        mixed_mode_preference (int): If the target entity is a mixed mode
            volume, which NAS protocol type the user prefer to backup. This
            does not apply to generic NAS and will be ignored.
        snapshot_change_enabled (bool): Whether this backup job should utilize
            changelist like API when available for faster incremental
            backups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continue_on_error":'continueOnError',
        "filtering_policy":'filteringPolicy',
        "mixed_mode_preference":'mixedModePreference',
        "snapshot_change_enabled":'snapshotChangeEnabled'
    }

    def __init__(self,
                 continue_on_error=None,
                 filtering_policy=None,
                 mixed_mode_preference=None,
                 snapshot_change_enabled=None):
        """Constructor for the NasBackupParams class"""

        # Initialize members of the class
        self.continue_on_error = continue_on_error
        self.filtering_policy = filtering_policy
        self.mixed_mode_preference = mixed_mode_preference
        self.snapshot_change_enabled = snapshot_change_enabled


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
        continue_on_error = dictionary.get('continueOnError')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        mixed_mode_preference = dictionary.get('mixedModePreference')
        snapshot_change_enabled = dictionary.get('snapshotChangeEnabled')

        # Return an object of this model
        return cls(continue_on_error,
                   filtering_policy,
                   mixed_mode_preference,
                   snapshot_change_enabled)


