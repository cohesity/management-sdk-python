# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.storage_array_snapshot_max_snapshot_config_params
import cohesity_management_sdk.models.storage_array_snapshot_max_space_config_params


class StorageArraySnapshotThrottlingPolicy(object):

    """Implementation of the 'StorageArraySnapshotThrottlingPolicy' model.

    TODO: type description here.


    Attributes:

        id (long|int): Specifies the volume id of the storage array snapshot
            config.
        is_max_snapshots_config_enabled (bool): Specifies if the storage array
            snapshot max snapshots config is enabled or not.
        is_max_space_config_enabled (bool): Specifies if the storage array
            snapshot max space config is enabled or not.
        max_snapshot_config (StorageArraySnapshotMaxSnapshotConfigParams):
            Specifies the storage array snapshot max snapshot config for this
            volume/lun. Valid only when IsMaxSnapshotsConfigEnabled is true.
        max_space_config (StorageArraySnapshotMaxSpaceConfigParams): Specifies
            the storage array snapshot free space config for this volume/lun.
            Valid only when IsMaxSpaceConfigEnabled is true.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "is_max_snapshots_config_enabled":'isMaxSnapshotsConfigEnabled',
        "is_max_space_config_enabled":'isMaxSpaceConfigEnabled',
        "max_snapshot_config":'maxSnapshotConfig',
        "max_space_config":'maxSpaceConfig',
    }
    def __init__(self,
                 id=None,
                 is_max_snapshots_config_enabled=None,
                 is_max_space_config_enabled=None,
                 max_snapshot_config=None,
                 max_space_config=None,
            ):

        """Constructor for the StorageArraySnapshotThrottlingPolicy class"""

        # Initialize members of the class
        self.id = id
        self.is_max_snapshots_config_enabled = is_max_snapshots_config_enabled
        self.is_max_space_config_enabled = is_max_space_config_enabled
        self.max_snapshot_config = max_snapshot_config
        self.max_space_config = max_space_config

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
        id = dictionary.get('id')
        is_max_snapshots_config_enabled = dictionary.get('isMaxSnapshotsConfigEnabled')
        is_max_space_config_enabled = dictionary.get('isMaxSpaceConfigEnabled')
        max_snapshot_config = cohesity_management_sdk.models.storage_array_snapshot_max_snapshot_config_params.StorageArraySnapshotMaxSnapshotConfigParams.from_dictionary(dictionary.get('maxSnapshotConfig')) if dictionary.get('maxSnapshotConfig') else None
        max_space_config = cohesity_management_sdk.models.storage_array_snapshot_max_space_config_params.StorageArraySnapshotMaxSpaceConfigParams.from_dictionary(dictionary.get('maxSpaceConfig')) if dictionary.get('maxSpaceConfig') else None

        # Return an object of this model
        return cls(
            id,
            is_max_snapshots_config_enabled,
            is_max_space_config_enabled,
            max_snapshot_config,
            max_space_config
)