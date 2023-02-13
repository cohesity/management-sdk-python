# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.physical_file_backup_params
import cohesity_management_sdk.models.physical_snapshot_params
import cohesity_management_sdk.models.source_app_params

class PhysicalBackupSourceParams(object):

    """Implementation of the 'PhysicalBackupSourceParams' model.

    Message to capture additional backup params for a Physical type source.

    Attributes:
        enable_system_backup (bool): Allows Magneto to drive a "system" backup
            using a 3rd-party tool installed on the Agent host.
        file_backup_params (PhysicalFileBackupParams): Message to capture
            params when backing up files on a Physical source.
        snapshot_params (PhysicalSnapshotParams): This message contains params
            that controls the snapshot process for a physical host.
        source_app_params (SourceAppParams): This message contains params
            specific to application running on the source such as a VM or a
            physical host.
        volume_guid_vec (list of string): If this list is non-empty, then only
            volumes in this will be protected, otherwise all volumes belonging
            to the host will be protected.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_system_backup":'enableSystemBackup',
        "file_backup_params":'fileBackupParams',
        "snapshot_params":'snapshotParams',
        "source_app_params":'sourceAppParams',
        "volume_guid_vec":'volumeGuidVec'
    }

    def __init__(self,
                 enable_system_backup=None,
                 file_backup_params=None,
                 snapshot_params=None,
                 source_app_params=None,
                 volume_guid_vec=None):
        """Constructor for the PhysicalBackupSourceParams class"""

        # Initialize members of the class
        self.enable_system_backup = enable_system_backup
        self.file_backup_params = file_backup_params
        self.snapshot_params = snapshot_params
        self.source_app_params = source_app_params
        self.volume_guid_vec = volume_guid_vec


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
        enable_system_backup = dictionary.get('enableSystemBackup')
        file_backup_params = cohesity_management_sdk.models.physical_file_backup_params.PhysicalFileBackupParams.from_dictionary(dictionary.get('fileBackupParams')) if dictionary.get('fileBackupParams') else None
        snapshot_params = cohesity_management_sdk.models.physical_snapshot_params.PhysicalSnapshotParams.from_dictionary(dictionary.get('snapshotParams')) if dictionary.get('snapshotParams') else None
        source_app_params = cohesity_management_sdk.models.source_app_params.SourceAppParams.from_dictionary(dictionary.get('sourceAppParams')) if dictionary.get('sourceAppParams') else None
        volume_guid_vec = dictionary.get('volumeGuidVec')

        # Return an object of this model
        return cls(enable_system_backup,
                   file_backup_params,
                   snapshot_params,
                   source_app_params,
                   volume_guid_vec)


