# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.physical_file_backup_params_backup_path_info

class PhysicalFileBackupParams(object):

    """Implementation of the 'PhysicalFileBackupParams' model.

    Message to capture params when backing up files on a Physical source.

    Attributes:
        backup_path_info_vec (list of PhysicalFileBackupParamsBackupPathInfo):
            Specifies the paths to backup on the Physical source.
        metadata_file_path (string): Specifies metadata path on source. This
            file contains absolute paths of files that needs to be backed up
            on the same source. If this field is set, backup_path_info_vec
            will be ignored.
        skip_nested_volumes_vec (list of string): Mount types of nested
            volumes to be skipped.
        symlink_follow_nas_target (bool): Specifies whether to follow nas target
            pointed by symlink.
            Set to true only for windows physical file based job.
        uses_skip_nested_volumes_vec (bool): Specifies whether to use
            skip_nested_volumes_vec to skip nested mounts. Before 6.4,
            BackupPathInfo.skip_nested_volumes boolean was used to skip nested
            volumes. So we use this boolean to support older jobs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_path_info_vec":'backupPathInfoVec',
        "metadata_file_path":'metadataFilePath',
        "skip_nested_volumes_vec":'skipNestedVolumesVec',
        "symlink_follow_nas_target":'symlinkFollowNasTarget',
        "uses_skip_nested_volumes_vec":'usesSkipNestedVolumesVec'
    }

    def __init__(self,
                 backup_path_info_vec=None,
                 metadata_file_path=None,
                 skip_nested_volumes_vec=None,
                 symlink_follow_nas_target=None,
                 uses_skip_nested_volumes_vec=None):
        """Constructor for the PhysicalFileBackupParams class"""

        # Initialize members of the class
        self.backup_path_info_vec = backup_path_info_vec
        self.metadata_file_path = metadata_file_path
        self.skip_nested_volumes_vec = skip_nested_volumes_vec
        self.symlink_follow_nas_target = symlink_follow_nas_target
        self.uses_skip_nested_volumes_vec = uses_skip_nested_volumes_vec


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
        backup_path_info_vec = None
        if dictionary.get('backupPathInfoVec') != None:
            backup_path_info_vec = list()
            for structure in dictionary.get('backupPathInfoVec'):
                backup_path_info_vec.append(cohesity_management_sdk.models.physical_file_backup_params_backup_path_info.PhysicalFileBackupParamsBackupPathInfo.from_dictionary(structure))
        metadata_file_path = dictionary.get('metadataFilePath')
        skip_nested_volumes_vec = dictionary.get('skipNestedVolumesVec')
        symlink_follow_nas_target = dictionary.get('symlinkFollowNasTarget')
        uses_skip_nested_volumes_vec = dictionary.get('usesSkipNestedVolumesVec')

        # Return an object of this model
        return cls(backup_path_info_vec,
                   metadata_file_path,
                   skip_nested_volumes_vec,
                   symlink_follow_nas_target,
                   uses_skip_nested_volumes_vec)


