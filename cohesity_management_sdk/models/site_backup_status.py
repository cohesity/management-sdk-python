# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.site_backup_file
import cohesity_management_sdk.models.site_info


class SiteBackupStatus(object):

    """Implementation of the 'SiteBackupStatus' model.

    TODO: type description here.


    Attributes:

        backup_file_vec (list of SiteBackupFile): List of backuped files. Its
            PnP package and any other files required to recover the site.
        option_flags (int): Actual options with which this site was backed up
            (BackupSiteArg.BackupSiteOptionFlags).
        site_info (SiteInfo): This site info is used during recovery to recover
            a full site.
        warning_vec (list of string): Backup succeeded, but there were some
            warnings for user. For example we could not backup term store due
            to lack of permissions.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_file_vec":'backupFileVec',
        "option_flags":'optionFlags',
        "site_info":'siteInfo',
        "warning_vec":'warningVec',
    }
    def __init__(self,
                 backup_file_vec=None,
                 option_flags=None,
                 site_info=None,
                 warning_vec=None,
            ):

        """Constructor for the SiteBackupStatus class"""

        # Initialize members of the class
        self.backup_file_vec = backup_file_vec
        self.option_flags = option_flags
        self.site_info = site_info
        self.warning_vec = warning_vec

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
        backup_file_vec = None
        if dictionary.get('backupFileVec') != None:
            backup_file_vec = list()
            for structure in dictionary.get('backupFileVec'):
                backup_file_vec.append(cohesity_management_sdk.models.site_backup_file.SiteBackupFile.from_dictionary(structure))
        option_flags = dictionary.get('optionFlags')
        site_info = cohesity_management_sdk.models.site_info.SiteInfo.from_dictionary(dictionary.get('siteInfo')) if dictionary.get('siteInfo') else None
        warning_vec = dictionary.get("warningVec")

        # Return an object of this model
        return cls(
            backup_file_vec,
            option_flags,
            site_info,
            warning_vec
)