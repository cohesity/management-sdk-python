# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class PhysicalBackupEnvParams(object):

    """Implementation of the 'PhysicalBackupEnvParams' model.

    Message to capture any additional backup params for a Physical
    environment.

    Attributes:
        enable_incremental_backup_after_restart (bool): If this is set to
            true, then incremental backup will be performed after the server
            restarts, otherwise a full-backup will be done. NOTE: This is
            applicable to windows host environments.
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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_incremental_backup_after_restart":'enableIncrementalBackupAfterRestart',
        "filtering_policy":'filteringPolicy'
    }

    def __init__(self,
                 enable_incremental_backup_after_restart=None,
                 filtering_policy=None):
        """Constructor for the PhysicalBackupEnvParams class"""

        # Initialize members of the class
        self.enable_incremental_backup_after_restart = enable_incremental_backup_after_restart
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
        enable_incremental_backup_after_restart = dictionary.get('enableIncrementalBackupAfterRestart')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None

        # Return an object of this model
        return cls(enable_incremental_backup_after_restart,
                   filtering_policy)


