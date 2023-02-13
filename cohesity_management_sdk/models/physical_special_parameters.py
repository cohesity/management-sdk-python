# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_parameters
import cohesity_management_sdk.models.file_path_parameters
import cohesity_management_sdk.models.windows_host_snapshot_parameters

class PhysicalSpecialParameters(object):

    """Implementation of the 'PhysicalSpecialParameters' model.

    Specifies additional special settings applicable for a Protection Source
    of 'kPhysical' type in a Protection Job.

    Attributes:
        application_parameters (ApplicationParameters): TODO: type description
            here.
        enable_system_backup (bool): Specifies whether to allow system backup
            using 3rd party tools installed on the Protection Host. System
            backups are used for doing bare metal recovery later. This field
            is applicable only for System backups.
        file_paths (list of FilePathParameters): Array of File Paths to Back
            Up.  Specifies a list of directories or files to protect in a
            Physical Server.
        metadata_file_path (string): Specifies metadata path on source. This
            file contains absolute paths of files that needs to be backed up
            on the same source. If this field is set, backup_path_info_vec
            will be ignored.
        skip_nested_volumes_vec (list of string): Specifies mounttypes of
            nested volumes to be skipped.
        uses_skip_nested_volumes_vec (bool): Specifies whether to use
            SkipNestedVolumes vec to skip nested mounts.
        volume_guid (list of string): Array of Mounted Volumes to Back Up.
            Specifies the subset of mounted volumes to protect in a Physical
            Server. If not specified, all mounted volumes on a Physical Server
            are protected.
        windows_parameters (WindowsHostSnapshotParameters): Specifies settings
            that are meaningful only on Windows hosts.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_parameters":'applicationParameters',
        "enable_system_backup":'enableSystemBackup',
        "file_paths":'filePaths',
        "metadata_file_path":'metadataFilePath',
        "skip_nested_volumes_vec":'skipNestedVolumesVec',
        "uses_skip_nested_volumes_vec":'usesSkipNestedVolumesVec',
        "volume_guid":'volumeGuid',
        "windows_parameters":'windowsParameters'
    }

    def __init__(self,
                 application_parameters=None,
                 enable_system_backup=None,
                 file_paths=None,
                 metadata_file_path=None,
                 skip_nested_volumes_vec=None,
                 uses_skip_nested_volumes_vec=None,
                 volume_guid=None,
                 windows_parameters=None):
        """Constructor for the PhysicalSpecialParameters class"""

        # Initialize members of the class
        self.application_parameters = application_parameters
        self.enable_system_backup = enable_system_backup
        self.file_paths = file_paths
        self.metadata_file_path = metadata_file_path
        self.skip_nested_volumes_vec = skip_nested_volumes_vec
        self.uses_skip_nested_volumes_vec = uses_skip_nested_volumes_vec
        self.volume_guid = volume_guid
        self.windows_parameters = windows_parameters


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
        application_parameters = cohesity_management_sdk.models.application_parameters.ApplicationParameters.from_dictionary(dictionary.get('applicationParameters')) if dictionary.get('applicationParameters') else None
        enable_system_backup = dictionary.get('enableSystemBackup')
        file_paths = None
        if dictionary.get('filePaths') != None:
            file_paths = list()
            for structure in dictionary.get('filePaths'):
                file_paths.append(cohesity_management_sdk.models.file_path_parameters.FilePathParameters.from_dictionary(structure))
        metadata_file_path = dictionary.get('metadataFilePath')
        skip_nested_volumes_vec = dictionary.get('skipNestedVolumesVec')
        uses_skip_nested_volumes_vec = dictionary.get('usesSkipNestedVolumesVec')
        volume_guid = dictionary.get('volumeGuid')
        windows_parameters = cohesity_management_sdk.models.windows_host_snapshot_parameters.WindowsHostSnapshotParameters.from_dictionary(dictionary.get('windowsParameters')) if dictionary.get('windowsParameters') else None

        # Return an object of this model
        return cls(application_parameters,
                   enable_system_backup,
                   file_paths,
                   metadata_file_path,
                   skip_nested_volumes_vec,
                   uses_skip_nested_volumes_vec,
                   volume_guid,
                   windows_parameters)


