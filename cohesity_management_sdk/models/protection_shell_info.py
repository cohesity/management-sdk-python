# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ProtectionShellInfo(object):

    """Implementation of the 'ProtectionShellInfo' model.

    Attributes:
        end_time_usecs (long|int): Specifies the end time of the Protection
            Run. The end time is specified as a Unix epoch Timestamp (in
            microseconds).
        error (string): Specifies if an error occurred (if any) while
           running this task. This field is populated when the status is equal
           to 'kFailure'.
        job_run_id (long|int): Specifies the id of the Job Run that ran the
            backup task and the copy tasks.
        run_type (RunTypeEnum): Specifies the type of backup such as
            'kRegular', 'kFull', 'kLog' or 'kSystem'.
            'kRegular' indicates a incremental (CBT) backup. Incremental
            backups utilizing CBT (if supported) are captured of the target
            protection objects.
            The first run of a kRegular schedule captures all the blocks.
            'kFull' indicates a full (no CBT) backup. A complete backup
            (all blocks) of the target protection objects are always captured
            and Change Block Tracking (CBT) is not utilized.
            'kLog' indicates a Database Log backup. Capture the database
            transaction logs to allow rolling back to a specific point in time.
            'kSystem' indicates a system backup. System backups are used to do
            bare metal recovery of the system to a specific point in time.
        start_time_usecs (long|int): Specifies the start time of the
            Protection Run. The start time is specified as a Unix epoch
            Timestamp (in microseconds).
            This time is when the task is queued to an internal queue where
            tasks are waiting to run.
        status (StatusCopyRunEnum): Specifies the status of Backup task such as
            'kRunning', 'kSuccess', 'kFailure' etc.
            'kAccepted' indicates the task is queued to run but not yet running.
            'kRunning' indicates the task is running.
            'kCanceling' indicates a request to cancel the task has occurred but
            the task is not yet canceled.
            'kCanceled' indicates the task has been canceled.
            'kSuccess' indicates the task was successful.
            'kFailure' indicates the task failed.
            'kWarning' indicates the task has finished with warning.
            'kOnHold' indicates the task is kept onHold.
            'kMissed' indicates the task is missed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs": 'endTimeUsecs',
        "error": 'error',
        "job_run_id":'jobRunId',
        "run_type":'runType',
        "start_time_usecs":'startTimeUsecs',
        "status":'status'
    }

    def __init__(self,
                 end_time_usecs=None,
                 error=None,
                 job_run_id=None,
                 run_type=None,
                 start_time_usecs=None,
                 status=None
                 ):
        """Constructor for the ProtectionShellInfo class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.job_run_id = job_run_id
        self.run_type = run_type
        self.start_time_usecs = start_time_usecs
        self.status = status

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
        job_run_id = dictionary.get('jobRunId')
        run_type = dictionary.get('runType')
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(end_time_usecs,
                   error,
                   job_run_id,
                   run_type,
                   start_time_usecs,
                   status)


