# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto
import cohesity_management_sdk.models.one_drive_backup_env_params
import cohesity_management_sdk.models.outlook_backup_env_params
import cohesity_management_sdk.models.sharep_point_site_backup_env_params

class O365BackupEnvParams(object):

    """Implementation of the 'O365BackupEnvParams' model.

    Message to capture any additional backup params for Office365
    environment.
    This encapsulates both Outlook & OneDrive backup parameters.

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
        onedrive_backup_params (OneDriveBackupEnvParams): Message to capture
            any additonal backup params for OneDrive within the Office365
            environment.
        outlook_backup_params (OutlookBackupEnvParams): Message to capture any
            additional backup params for Outlook within Office365
            environment.
        site_backup_params (SharepPointSiteBackupEnvParams): SharePoint
            specific backup parameters. Refer 'SharepPointSiteBackupEnvParams'
            for details.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filtering_policy":'filteringPolicy',
        "onedrive_backup_params":'onedriveBackupParams',
        "outlook_backup_params":'outlookBackupParams',
        "site_backup_params":'siteBackupParams'
    }

    def __init__(self,
                 filtering_policy=None,
                 onedrive_backup_params=None,
                 outlook_backup_params=None,
                 site_backup_params=None):
        """Constructor for the O365BackupEnvParams class"""

        # Initialize members of the class
        self.filtering_policy = filtering_policy
        self.onedrive_backup_params = onedrive_backup_params
        self.outlook_backup_params = outlook_backup_params
        self.site_backup_params = site_backup_params


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
        onedrive_backup_params = cohesity_management_sdk.models.one_drive_backup_env_params.OneDriveBackupEnvParams.from_dictionary(dictionary.get('onedriveBackupParams')) if dictionary.get('onedriveBackupParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_env_params.OutlookBackupEnvParams.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        site_backup_params = cohesity_management_sdk.models.sharep_point_site_backup_env_params.SharepPointSiteBackupEnvParams.from_dictionary(dictionary.get('siteBackupParams')) if dictionary.get('siteBackupParams') else None

        # Return an object of this model
        return cls(filtering_policy,
                   onedrive_backup_params,
                   outlook_backup_params,
                   site_backup_params)


