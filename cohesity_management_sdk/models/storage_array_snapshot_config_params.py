# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.storage_array_snapshot_max_space_config_params
import cohesity_management_sdk.models.storage_array_snapshot_throttling_policy


class StorageArraySnapshotConfigParams(object):

    """Implementation of the 'StorageArraySnapshotConfigParams' model.

    TODO: type description here.


    Attributes:

        is_max_snapshots_config_enabled (bool): Specifies if the storage array
            snapshot max snapshots config is enabled or not.
        is_max_space_config_enabled (bool): Specifies if the storage array
            snapshot max space config is enabled or not.
        storage_array_snapshot_max_space_config
            (StorageArraySnapshotMaxSpaceConfigParams): Specifies the storage
            array snapshot free space config for this volume/lun.
        storage_array_snapshot_throttling_policies (list of
            StorageArraySnapshotThrottlingPolicy): Specifies throttling
            policies configured for individual volume/lun.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_max_snapshots_config_enabled":'isMaxSnapshotsConfigEnabled',
        "is_max_space_config_enabled":'isMaxSpaceConfigEnabled',
        "storage_array_snapshot_max_space_config":'storageArraySnapshotMaxSpaceConfig',
        "storage_array_snapshot_throttling_policies":'storageArraySnapshotThrottlingPolicies',
    }
    def __init__(self,
                 is_max_snapshots_config_enabled=None,
                 is_max_space_config_enabled=None,
                 storage_array_snapshot_max_space_config=None,
                 storage_array_snapshot_throttling_policies=None,
            ):

        """Constructor for the StorageArraySnapshotConfigParams class"""

        # Initialize members of the class
        self.is_max_snapshots_config_enabled = is_max_snapshots_config_enabled
        self.is_max_space_config_enabled = is_max_space_config_enabled
        self.storage_array_snapshot_max_space_config = storage_array_snapshot_max_space_config
        self.storage_array_snapshot_throttling_policies = storage_array_snapshot_throttling_policies

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
        is_max_snapshots_config_enabled = dictionary.get('isMaxSnapshotsConfigEnabled')
        is_max_space_config_enabled = dictionary.get('isMaxSpaceConfigEnabled')
        storage_array_snapshot_max_space_config = cohesity_management_sdk.models.storage_array_snapshot_max_space_config_params.StorageArraySnapshotMaxSpaceConfigParams.from_dictionary(dictionary.get('storageArraySnapshotMaxSpaceConfig')) if dictionary.get('storageArraySnapshotMaxSpaceConfig') else None
        storage_array_snapshot_throttling_policies = None
        if dictionary.get('storageArraySnapshotThrottlingPolicies') != None:
            storage_array_snapshot_throttling_policies = list()
            for structure in dictionary.get('storageArraySnapshotThrottlingPolicies'):
                storage_array_snapshot_throttling_policies.append(cohesity_management_sdk.models.storage_array_snapshot_throttling_policy.StorageArraySnapshotThrottlingPolicy.from_dictionary(structure))

        # Return an object of this model
        return cls(
            is_max_snapshots_config_enabled,
            is_max_space_config_enabled,
            storage_array_snapshot_max_space_config,
            storage_array_snapshot_throttling_policies
)