# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.physical_file_backup_params_backup_path_info

class PhysicalFileBackupParams(object):

    """Implementation of the 'PhysicalFileBackupParams' model.

    Message to capture params when backing up files on a Physical source.

    Attributes:
        backup_path_info_vec (list of PhysicalFileBackupParamsBackupPathInfo):
            Specifies the paths to backup on the Physical source.
        metadata_file_path (string): Specifies file list path on source. This
            file  contains absolute path of files that needs to be backed up
            on the same source. If this field is set, backup_path_info_vec
            will be ignored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_path_info_vec":'backupPathInfoVec',
        "metadata_file_path":'metadataFilePath'
    }

    def __init__(self,
                 backup_path_info_vec=None,
                 metadata_file_path=None):
        """Constructor for the PhysicalFileBackupParams class"""

        # Initialize members of the class
        self.backup_path_info_vec = backup_path_info_vec
        self.metadata_file_path = metadata_file_path


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

        # Return an object of this model
        return cls(backup_path_info_vec,
                   metadata_file_path)


