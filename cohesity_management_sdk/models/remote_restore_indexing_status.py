# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class RemoteRestoreIndexingStatus(object):

    """Implementation of the 'RemoteRestoreIndexingStatus' model.

    Specifies the status of an indexing task.

    Attributes:
        end_time_usecs (long|int): Specifies the end time of the time range
            that is being indexed. The indexing task is creating an index of
            the Job Runs that occurred between the startTimeUsecs and this
            endTimeUsecs. This field is recorded as a Unix epoch Timestamp (in
            microseconds).
        error (string): Specifies the error message if the indexing Job/task
            fails.
        indexing_task_end_time_usecs (long|int): Specifies when the indexing
            task completed. This time is recorded as a Unix epoch Timestamp
            (in microseconds). This field is not set if the indexing task is
            still in progress.
        indexing_task_start_time_usecs (long|int): Specifies when the indexing
            task started. This time is recorded as a Unix epoch Timestamp (in
            microseconds).
        indexing_task_status (IndexingTaskStatusEnum): Specifies the status of
            the indexing Job/task. 'kJobRunning' indicates that the Job/task
            is currently running. 'kJobFinished' indicates that the Job/task
            completed and finished. 'kJobFailed' indicates that the Job/task
            failed and did not complete. 'kJobCanceled' indicates that the
            Job/task was canceled. 'kJobPaused' indicates the Job/task is
            paused.
        indexing_task_uid (UniversalId): Specifies the unique id of the
            indexing task assigned by this Cluster.
        latest_expiry_time_usecs (long|int): For all the Snapshots retrieved
            by this Job, specifies the latest time when a Snapshot expires.
        progress_monitor_task (string): Specifies the path to progress monitor
            task to track the progress of building the index.
        start_time_usecs (long|int): Specifies the start time of the time
            range that is being indexed. The indexing task is creating an
            index of the Job Runs that occurred between this startTimeUsecs
            and the endTimeUsecs. This field is recorded as a Unix epoch
            Timestamp (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "indexing_task_end_time_usecs":'indexingTaskEndTimeUsecs',
        "indexing_task_start_time_usecs":'indexingTaskStartTimeUsecs',
        "indexing_task_status":'indexingTaskStatus',
        "indexing_task_uid":'indexingTaskUid',
        "latest_expiry_time_usecs":'latestExpiryTimeUsecs',
        "progress_monitor_task":'progressMonitorTask',
        "start_time_usecs":'startTimeUsecs'
    }

    def __init__(self,
                 end_time_usecs=None,
                 error=None,
                 indexing_task_end_time_usecs=None,
                 indexing_task_start_time_usecs=None,
                 indexing_task_status=None,
                 indexing_task_uid=None,
                 latest_expiry_time_usecs=None,
                 progress_monitor_task=None,
                 start_time_usecs=None):
        """Constructor for the RemoteRestoreIndexingStatus class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.indexing_task_end_time_usecs = indexing_task_end_time_usecs
        self.indexing_task_start_time_usecs = indexing_task_start_time_usecs
        self.indexing_task_status = indexing_task_status
        self.indexing_task_uid = indexing_task_uid
        self.latest_expiry_time_usecs = latest_expiry_time_usecs
        self.progress_monitor_task = progress_monitor_task
        self.start_time_usecs = start_time_usecs


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
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = dictionary.get('error')
        indexing_task_end_time_usecs = dictionary.get('indexingTaskEndTimeUsecs')
        indexing_task_start_time_usecs = dictionary.get('indexingTaskStartTimeUsecs')
        indexing_task_status = dictionary.get('indexingTaskStatus')
        indexing_task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('indexingTaskUid')) if dictionary.get('indexingTaskUid') else None
        latest_expiry_time_usecs = dictionary.get('latestExpiryTimeUsecs')
        progress_monitor_task = dictionary.get('progressMonitorTask')
        start_time_usecs = dictionary.get('startTimeUsecs')

        # Return an object of this model
        return cls(end_time_usecs,
                   error,
                   indexing_task_end_time_usecs,
                   indexing_task_start_time_usecs,
                   indexing_task_status,
                   indexing_task_uid,
                   latest_expiry_time_usecs,
                   progress_monitor_task,
                   start_time_usecs)


