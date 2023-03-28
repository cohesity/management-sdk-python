# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.copy_run_stats
import cohesity_management_sdk.models.protection_source


class CopySnapshotTaskStatus(object):

    """Implementation of the 'CopySnapshotTaskStatus' model.

    Specifies the status of the copy task that copies the snapshot of a
    Protection Source object to a target.


    Attributes:

        error (string): Specifies if an error occurred (if any) while running
            this task. This field is populated when the status is equal to
            'kFailure'.
        source (ProtectionSource): Specifies the source object whose snapshot
            is replicated. This is specified for replication targets.
        stats (CopyRunStats): Specifies the stats of the replication or the
            archival task.
        status (StatusCopySnapshotTaskStatusEnum): Specifies the status of the
            source object being protected. 'kAccepted' indicates the task is
            queued to run but not yet running. 'kRunning' indicates the task is
            running. 'kCanceling' indicates a request to cancel the task has
            occurred but the task is not yet canceled. 'kCanceled' indicates
            the task has been canceled. 'kSuccess' indicates the task was
            successful. 'kFailure' indicates the task failed. 'kWarning'
            indicates the task has finished with warning. 'kOnHold' indicates
            the task is kept onHold. 'kMissed' indicates the task is missed.
            'Finalizing' indicates the task is finalizing.
        task_end_time_usecs (long|int): Specifies the end time of the copy
            task. The end time is specified as a Unix epoch Timestamp (in
            microseconds).
        task_start_time_usecs (long|int): Specifies the start time of the copy
            task. The start time is specified as a Unix epoch Timestamp (in
            microseconds). Copy run task is started after completing backup
            tasks. It may spawn sub-tasks to copy or replicate individual
            snapshots.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "source":'source',
        "stats":'stats',
        "status":'status',
        "task_end_time_usecs":'taskEndTimeUsecs',
        "task_start_time_usecs":'taskStartTimeUsecs',
    }
    def __init__(self,
                 error=None,
                 source=None,
                 stats=None,
                 status=None,
                 task_end_time_usecs=None,
                 task_start_time_usecs=None,
            ):

        """Constructor for the CopySnapshotTaskStatus class"""

        # Initialize members of the class
        self.error = error
        self.source = source
        self.stats = stats
        self.status = status
        self.task_end_time_usecs = task_end_time_usecs
        self.task_start_time_usecs = task_start_time_usecs

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
        error = dictionary.get('error')
        source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('source')) if dictionary.get('source') else None
        stats = cohesity_management_sdk.models.copy_run_stats.CopyRunStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        status = dictionary.get('status')
        task_end_time_usecs = dictionary.get('taskEndTimeUsecs')
        task_start_time_usecs = dictionary.get('taskStartTimeUsecs')

        # Return an object of this model
        return cls(
            error,
            source,
            stats,
            status,
            task_end_time_usecs,
            task_start_time_usecs
)