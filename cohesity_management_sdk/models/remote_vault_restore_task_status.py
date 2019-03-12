# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.status_of_indexing_task
import cohesity_management_sdk.models.status_of_restore_snapshot_task
import cohesity_management_sdk.models.unique_global_id
import cohesity_management_sdk.models.remote_protection_job_information

class RemoteVaultRestoreTaskStatus(object):

    """Implementation of the 'Remote Vault Restore Task Status.' model.

    Specifies the status of a remote Vault restore task.

    Attributes:
        current_indexing_status (StatusOfIndexingTask): Specifies the status
            of an indexing task that builds an index from the Protection Job
            metadata retrieved from the remote Vault. The index contains
            information about Job Runs (Snapshots) for a Protection Job and is
            required to restore Snapshots to this local Cluster.
        current_snapshot_status (StatusOfRestoreSnapshotTask): Specifies the
            status of the Snapshot restore task. The Snapshot restore task
            restores the specified archived Snapshots from a remote Vault to
            this Cluster.
        local_protection_job_uid (UniqueGlobalId): Specifies the globally
            unique id of the new inactive Protection Job created on the local
            Cluster as part of the restoration of archived data.
        parent_job_uid (UniqueGlobalId): Specifies the unique id of the parent
            Job/task that spawned the indexing and Snapshot restore tasks.
        remote_protection_job_information (RemoteProtectionJobInformation):
            Specifies details about the original Protection Job and its
            Snapshots, that were archived to a remote Vault.
        search_job_uid (UniqueGlobalId): Specifies the unique id of the search
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
        current_indexing_status = cohesity_management_sdk.models.status_of_indexing_task.StatusOfIndexingTask.from_dictionary(dictionary.get('currentIndexingStatus')) if dictionary.get('currentIndexingStatus') else None
        current_snapshot_status = cohesity_management_sdk.models.status_of_restore_snapshot_task.StatusOfRestoreSnapshotTask.from_dictionary(dictionary.get('currentSnapshotStatus')) if dictionary.get('currentSnapshotStatus') else None
        local_protection_job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('localProtectionJobUid')) if dictionary.get('localProtectionJobUid') else None
        parent_job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('parentJobUid')) if dictionary.get('parentJobUid') else None
        remote_protection_job_information = cohesity_management_sdk.models.remote_protection_job_information.RemoteProtectionJobInformation.from_dictionary(dictionary.get('remoteProtectionJobInformation')) if dictionary.get('remoteProtectionJobInformation') else None
        search_job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None

        # Return an object of this model
        return cls(current_indexing_status,
                   current_snapshot_status,
                   local_protection_job_uid,
                   parent_job_uid,
                   remote_protection_job_information,
                   search_job_uid)


