# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class OneDriveBackupEnvParams(object):

    """Implementation of the 'OneDriveBackupEnvParams' model.

    Message to capture any additonal backup params for OneDrive within the
    Office365 environment.

    Attributes:
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
        should_backup_onedrive (bool): Specifies whether the OneDrive(s) for
            all the Office365 Users present in the protection job should be
            backed up.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filtering_policy":'filteringPolicy',
        "should_backup_onedrive":'shouldBackupOnedrive'
    }

    def __init__(self,
                 filtering_policy=None,
                 should_backup_onedrive=None):
        """Constructor for the OneDriveBackupEnvParams class"""

        # Initialize members of the class
        self.filtering_policy = filtering_policy
        self.should_backup_onedrive = should_backup_onedrive


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
        should_backup_onedrive = dictionary.get('shouldBackupOnedrive')

        # Return an object of this model
        return cls(filtering_policy,
                   should_backup_onedrive)


