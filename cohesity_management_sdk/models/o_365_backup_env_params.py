# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto
import cohesity_management_sdk.models.group_backup_env_params
import cohesity_management_sdk.models.one_drive_backup_env_params
import cohesity_management_sdk.models.outlook_backup_env_params
import cohesity_management_sdk.models.public_folders_backup_env_params
import cohesity_management_sdk.models.sharep_point_site_backup_env_params
import cohesity_management_sdk.models.teams_backup_env_params


class O365BackupEnvParams(object):

    """Implementation of the 'O365BackupEnvParams' model.

    Message to capture any additional backup params for Office365 environment.
    This encapsulates both Outlook & OneDrive backup parameters.


    Attributes:

        filtering_policy (FilteringPolicyProto): This field has been
            deprecated. Use 'filtering_policy' specified within
            'outlook_backup_params' for Outlook exclusions filter and
            'onedrive_backup_params' for OneDrive exclusions filter
            respectively.
        group_backup_params (GroupBackupEnvParams): Group specific backup
            parameters. Refer 'GroupBackupEnvParams' for details.
        onedrive_backup_params (OneDriveBackupEnvParams): OneDrive specific
            backup parameters. Refer 'OneDriveBackupEnvParams' for details.
        outlook_backup_params (OutlookBackupEnvParams): Outlook specific backup
            parameters. Refer 'OutlookBackupEnvParams' for details.
        public_folders_backup_params (PublicFoldersBackupEnvParams):
            PublicFolders specific backup parameters. Refer
            'PublicFoldersEnvParams' for details.
        site_backup_params (SharepPointSiteBackupEnvParams): SharePoint
            specific backup parameters. Refer 'SharepPointSiteBackupEnvParams'
            for details.
        teams_backup_params (TeamsBackupEnvParams): Teams specific backup
            parameters. Refer 'TeamsBackupEnvParams' for details.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "filtering_policy":'filteringPolicy',
        "group_backup_params":'groupBackupParams',
        "onedrive_backup_params":'onedriveBackupParams',
        "outlook_backup_params":'outlookBackupParams',
        "public_folders_backup_params":'publicFoldersBackupParams',
        "site_backup_params":'siteBackupParams',
        "teams_backup_params":'teamsBackupParams',
    }
    def __init__(self,
                 filtering_policy=None,
                 group_backup_params=None,
                 onedrive_backup_params=None,
                 outlook_backup_params=None,
                 public_folders_backup_params=None,
                 site_backup_params=None,
                 teams_backup_params=None,
            ):

        """Constructor for the O365BackupEnvParams class"""

        # Initialize members of the class
        self.filtering_policy = filtering_policy
        self.group_backup_params = group_backup_params
        self.onedrive_backup_params = onedrive_backup_params
        self.outlook_backup_params = outlook_backup_params
        self.public_folders_backup_params = public_folders_backup_params
        self.site_backup_params = site_backup_params
        self.teams_backup_params = teams_backup_params

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
        group_backup_params = cohesity_management_sdk.models.group_backup_env_params.GroupBackupEnvParams.from_dictionary(dictionary.get('groupBackupParams')) if dictionary.get('groupBackupParams') else None
        onedrive_backup_params = cohesity_management_sdk.models.one_drive_backup_env_params.OneDriveBackupEnvParams.from_dictionary(dictionary.get('onedriveBackupParams')) if dictionary.get('onedriveBackupParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_env_params.OutlookBackupEnvParams.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        public_folders_backup_params = cohesity_management_sdk.models.public_folders_backup_env_params.PublicFoldersBackupEnvParams.from_dictionary(dictionary.get('publicFoldersBackupParams')) if dictionary.get('publicFoldersBackupParams') else None
        site_backup_params = cohesity_management_sdk.models.sharep_point_site_backup_env_params.SharepPointSiteBackupEnvParams.from_dictionary(dictionary.get('siteBackupParams')) if dictionary.get('siteBackupParams') else None
        teams_backup_params = cohesity_management_sdk.models.teams_backup_env_params.TeamsBackupEnvParams.from_dictionary(dictionary.get('teamsBackupParams')) if dictionary.get('teamsBackupParams') else None

        # Return an object of this model
        return cls(
            filtering_policy,
            group_backup_params,
            onedrive_backup_params,
            outlook_backup_params,
            public_folders_backup_params,
            site_backup_params,
            teams_backup_params
)