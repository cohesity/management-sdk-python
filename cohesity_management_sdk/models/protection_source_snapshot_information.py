# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.snapshot_copy_task

class ProtectionSourceSnapshotInformation(object):

    """Implementation of the 'ProtectionSourceSnapshotInformation' model.

    Specifies details about a Snapshot that backups up a leaf
    Protection Source Object.

    Attributes:
        copy_tasks (list of SnapshotCopyTask): Array of Snapshot Copy Tasks.
            Specifies a list of copy tasks (such as replication and archival
            tasks).
        job_id (long|int): Specifies the id of the Protection Job.
        job_name (string):  Specifies the name of the Protection Job.
        job_run_id (long|int): Specifies the id of the Job Run.
        job_run_start_time_usecs (long|int): Specifies the start time of the
            Job which this object is part of.
            The time is specified in Unix epoch Timestamp (in microseconds).
        last_run_end_time_usecs (long|int): Specifies the end time of the last
            Run of this object's snapshot.
            The time is specified in Unix epoch Timestamp (in microseconds).
        last_run_start_time_usecs (long|int): Specifies the start time of the
            last Run of this object's snapshot.
            The time is specified in Unix epoch Timestamp (in microseconds).
        message (string): Specifies warning or error information when the Job
            Run is not successful..
        num_bytes_read (int|long):  Specifies the total number of bytes read.
        num_logical_bytes_protected (int|long): Specifies the total number of
            logical bytes that are protected. The logical size is when the
            data is fully hydrated or expanded.
        pagination_cookie (long|int): Specifies an opaque string to pass into
            the next request to get the next set of Snapshots for pagination
            purposes. If null, this is the last set of Snapshots or the number
            of Snapshots returned is equal to or less than the specified
            pageCount.
        run_status (RunStatusEnum):  Specifies the type of the Job Run.
            'kSuccess' indicates that the Job Run was successful.
            'kRunning' indicates that the Job Run is currently running.
            'kWarning' indicates that the Job Run was successful but warnings
            were issued.
            'kCancelled' indicates that the Job Run was canceled.
            'kError' indicates the Job Run encountered an error and did not
            run to completion.
        run_type (RunTypeEnum): Specifies the status of the Job Run.
            'kRegular' indicates an incremental (CBT) backup. Incremental
            backups utilizing CBT (if supported) are captured of the target
            protection objects.
            The first run of a kRegular schedule captures all the blocks.
            'kFull' indicates a full (no CBT) backup. A complete backup
            (all blocks) of the target protection objects are always captured
            and Change Block Tracking (CBT) is not utilized.
            'kLog' indicates a Database Log backup. Capture the database
            transaction logs to allow rolling back to a specific point in
            time.
            'kSystem' indicates system volume backup. It produces an image
            for bare metal recovery.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_tasks":'copyTasks',
        "job_id":'jobId',
        "job_name":'jobName',
        "job_run_id":'jobRunId',
        "job_run_start_time_usecs":'jobRunStartTimeUsecs',
        "last_run_end_time_usecs":'lastRunEndTimeUsecs',
        "last_run_start_time_usecs":'lastRunStartTimeUsecs',
        "message":'message',
        "num_bytes_read":'numBytesRead',
        "num_logical_bytes_protected":'numLogicalBytesProtected',
        "pagination_cookie":'paginationCookie',
        "run_status":'runStatus',
        "run_type":'runType'
    }

    def __init__(self,
                 copy_tasks=None,
                 job_id=None,
                 job_name=None,
                 job_run_id=None,
                 job_run_start_time_usecs=None,
                 last_run_end_time_usecs=None,
                 last_run_start_time_usecs=None,
                 message=None,
                 num_bytes_read=None,
                 num_logical_bytes_protected=None,
                 pagination_cookie=None,
                 run_status=None,
                 run_type=None):
        """Constructor for the ProtectionSourceSnapshotInformation class"""

        # Initialize members of the class
        self.copy_tasks = copy_tasks
        self.job_id = job_id
        self.job_name = job_name
        self.job_run_id = job_run_id
        self.job_run_start_time_usecs = job_run_start_time_usecs
        self.last_run_end_time_usecs = last_run_end_time_usecs
        self.last_run_start_time_usecs = last_run_start_time_usecs
        self.message = message
        self.num_bytes_read = num_bytes_read
        self.num_logical_bytes_protected = num_logical_bytes_protected
        self.pagination_cookie = pagination_cookie
        self.run_status = run_status
        self.run_type = run_type


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
        copy_tasks = None
        if dictionary.get('copyTasks') != None:
            copy_tasks = list()
            for structure in dictionary.get('copyTasks'):
                copy_tasks.append(cohesity_management_sdk.models.snapshot_copy_task.SnapshotCopyTask.from_dictionary(structure))
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_run_id = dictionary.get('jobRunId')
        job_run_start_time_usecs = dictionary.get('jobRunStartTimeUsecs')
        last_run_end_time_usecs = dictionary.get('lastRunEndTimeUsecs')
        last_run_start_time_usecs = dictionary.get('lastRunStartTimeUsecs')
        message = dictionary.get('message')
        num_bytes_read = dictionary.get('numBytesRead')
        num_logical_bytes_protected = dictionary.get('numLogicalBytesProtected')
        pagination_cookie = dictionary.get('paginationCookie')
        run_status = dictionary.get('runStatus')
        run_type = dictionary.get('runType')

        # Return an object of this model
        return cls(copy_tasks,
                   job_id,
                   job_name,
                   job_run_id,
                   job_run_start_time_usecs,
                   last_run_end_time_usecs,
                   last_run_start_time_usecs,
                   message,
                   num_bytes_read,
                   num_logical_bytes_protected,
                   pagination_cookie,
                   run_status,
                   run_type)



