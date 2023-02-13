# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class RemoteRestoreSnapshotStatus(object):

    """Implementation of the 'RemoteRestoreSnapshotStatus' model.

    Specifies the status of a restore Snapshot task.

    Attributes:
        archive_task_uid (UniversalId): Specifies the globally unique id of
            the archival task that archived the Snapshots to the remote
            Vault.
        error (string): Specifies the error message if the indexing task
            fails.
        expiry_time_usecs (long|int): Specifies the time when the Snapshot
            expires on the remote Vault. This field is recorded as a Unix
            epoch Timestamp (in microseconds).
        job_run_id (long|int): Specifies the id of the Job Run that originally
            captured the Snapshot.
        progress_monitor_task (string): Specifies the path to the progress
            monitor task that tracks the progress of building the index.
        snapshot_task_status (SnapshotTaskStatusEnum): Specifies the status of
            the indexing task. 'kJobRunning' indicates that the Job/task is
            currently running. 'kJobFinished' indicates that the Job/task
            completed and finished. 'kJobFailed' indicates that the Job/task
            failed and did not complete. 'kJobCanceled' indicates that the
            Job/task was canceled. 'kJobPaused' indicates the Job/task is
            paused.
        snapshot_task_uid (UniversalId): Specifies the globally unique id of
            the task capturing the Snapshot.
        snapshot_time_usecs (long|int): Specify the time the Snapshot was
            captured. This time is recorded as a Unix epoch Timestamp (in
            microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archive_task_uid":'archiveTaskUid',
        "error":'error',
        "expiry_time_usecs":'expiryTimeUsecs',
        "job_run_id":'jobRunId',
        "progress_monitor_task":'progressMonitorTask',
        "snapshot_task_status":'snapshotTaskStatus',
        "snapshot_task_uid":'snapshotTaskUid',
        "snapshot_time_usecs":'snapshotTimeUsecs'
    }

    def __init__(self,
                 archive_task_uid=None,
                 error=None,
                 expiry_time_usecs=None,
                 job_run_id=None,
                 progress_monitor_task=None,
                 snapshot_task_status=None,
                 snapshot_task_uid=None,
                 snapshot_time_usecs=None):
        """Constructor for the RemoteRestoreSnapshotStatus class"""

        # Initialize members of the class
        self.archive_task_uid = archive_task_uid
        self.error = error
        self.expiry_time_usecs = expiry_time_usecs
        self.job_run_id = job_run_id
        self.progress_monitor_task = progress_monitor_task
        self.snapshot_task_status = snapshot_task_status
        self.snapshot_task_uid = snapshot_task_uid
        self.snapshot_time_usecs = snapshot_time_usecs


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
        archive_task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('archiveTaskUid')) if dictionary.get('archiveTaskUid') else None
        error = dictionary.get('error')
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        job_run_id = dictionary.get('jobRunId')
        progress_monitor_task = dictionary.get('progressMonitorTask')
        snapshot_task_status = dictionary.get('snapshotTaskStatus')
        snapshot_task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('snapshotTaskUid')) if dictionary.get('snapshotTaskUid') else None
        snapshot_time_usecs = dictionary.get('snapshotTimeUsecs')

        # Return an object of this model
        return cls(archive_task_uid,
                   error,
                   expiry_time_usecs,
                   job_run_id,
                   progress_monitor_task,
                   snapshot_task_status,
                   snapshot_task_uid,
                   snapshot_time_usecs)


