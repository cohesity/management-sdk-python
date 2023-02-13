# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_restore_indexing_status
import cohesity_management_sdk.models.remote_restore_snapshot_status
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.remote_protection_job_information

class RemoteVaultRestoreTaskStatus(object):

    """Implementation of the 'RemoteVaultRestoreTaskStatus' model.

    Specifies the status of a remote Vault restore task.

    Attributes:
        current_indexing_status (RemoteRestoreIndexingStatus): Specifies the
            status of an indexing task that builds an index from the
            Protection Job metadata retrieved from the remote Vault. The index
            contains information about Job Runs (Snapshots) for a Protection
            Job and is required to restore Snapshots to this local Cluster.
        current_snapshot_status (RemoteRestoreSnapshotStatus): Specifies the
            status of the Snapshot restore task. The Snapshot restore task
            restores the specified archived Snapshots from a remote Vault to
            this Cluster.
        local_protection_job_uid (UniversalId): Specifies the globally unique
            id of the new inactive Protection Job created on the local Cluster
            as part of the restoration of archived data.
        parent_job_uid (UniversalId): Specifies the unique id of the parent
            Job/task that spawned the indexing and Snapshot restore tasks.
        remote_protection_job_information (RemoteProtectionJobInformation):
            Specifies details about the original Protection Job and its
            Snapshots, that were archived to a remote Vault.
        search_job_uid (UniversalId): Specifies the unique id of the search
            Job that searched the remote Vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_indexing_status":'currentIndexingStatus',
        "current_snapshot_status":'currentSnapshotStatus',
        "local_protection_job_uid":'localProtectionJobUid',
        "parent_job_uid":'parentJobUid',
        "remote_protection_job_information":'remoteProtectionJobInformation',
        "search_job_uid":'searchJobUid'
    }

    def __init__(self,
                 current_indexing_status=None,
                 current_snapshot_status=None,
                 local_protection_job_uid=None,
                 parent_job_uid=None,
                 remote_protection_job_information=None,
                 search_job_uid=None):
        """Constructor for the RemoteVaultRestoreTaskStatus class"""

        # Initialize members of the class
        self.current_indexing_status = current_indexing_status
        self.current_snapshot_status = current_snapshot_status
        self.local_protection_job_uid = local_protection_job_uid
        self.parent_job_uid = parent_job_uid
        self.remote_protection_job_information = remote_protection_job_information
        self.search_job_uid = search_job_uid


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
        current_indexing_status = cohesity_management_sdk.models.remote_restore_indexing_status.RemoteRestoreIndexingStatus.from_dictionary(dictionary.get('currentIndexingStatus')) if dictionary.get('currentIndexingStatus') else None
        current_snapshot_status = cohesity_management_sdk.models.remote_restore_snapshot_status.RemoteRestoreSnapshotStatus.from_dictionary(dictionary.get('currentSnapshotStatus')) if dictionary.get('currentSnapshotStatus') else None
        local_protection_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('localProtectionJobUid')) if dictionary.get('localProtectionJobUid') else None
        parent_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('parentJobUid')) if dictionary.get('parentJobUid') else None
        remote_protection_job_information = cohesity_management_sdk.models.remote_protection_job_information.RemoteProtectionJobInformation.from_dictionary(dictionary.get('remoteProtectionJobInformation')) if dictionary.get('remoteProtectionJobInformation') else None
        search_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None

        # Return an object of this model
        return cls(current_indexing_status,
                   current_snapshot_status,
                   local_protection_job_uid,
                   parent_job_uid,
                   remote_protection_job_information,
                   search_job_uid)


