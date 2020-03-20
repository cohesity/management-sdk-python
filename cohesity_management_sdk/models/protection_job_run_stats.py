# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class ProtectionJobRunStats(object):

    """Implementation of the 'ProtectionJobRunStats' model.

    Specifies statistics about a Protection Job Run.
    This contains the Job Run level statistics.

    Attributes:
        admitted_time_usecs (long|int): Specifies the time the task was
            unqueued from the queue to start running. This field can be used
            to determine the following times: initial-wait-time =
            admittedTimeUsecs - startTimeUsecs run-time = endTimeUsecs -
            admittedTimeUsecs If the task ends up waiting in other queues,
            then actual run-time will be smaller than the run-time computed
            this way. This field is only populated for Backup tasks
            currently.
        end_time_usecs (long|int): Specifies the end time of the Protection
            Run. The end time is specified as a Unix epoch Timestamp (in
            microseconds).
        num_app_instances (int): Specifies the number of application instances
            backed up by this Run. For example if the environment type is
            kSQL, this field contains the number of SQL Server instances.
        num_canceled_tasks (long|int): Specifies the number of backup tasks
            that were canceled.
        num_failed_app_objects (int): Specifies the number of application
            objects that were cancelled in this Run.
        num_failed_tasks (long|int): Specifies the number of backup tasks that
            failed.
        num_successful_app_objects (int): Specifies the number of application
            objects successfully backed up by this Run. For example, if the
            environment type is kSQL, this number is for all of the SQL server
            databases.
        num_successful_tasks (long|int): Specifies the number of backup tasks
            that completed successfully.
        start_time_usecs (long|int): Specifies the start time of the
            Protection Run. The start time is specified as a Unix epoch
            Timestamp (in microseconds). This time is when the task is queued
            to an internal queue where tasks are waiting to run.
        time_taken_usecs (long|int): Specifies the actual execution time for
            the protection run to complete the backup task and the copy tasks.
            This time will not include the time waited in various internal
            queues. This field is only populated for Backup tasks currently.
        total_bytes_read_from_source (long|int): Specifies the total amount of
            data read from the source (so far).
        total_bytes_to_read_from_source (long|int): Specifies the total amount
            of data expected to be read from the source.
        total_logical_backup_size_bytes (long|int): Specifies the size of the
            source object (such as a VM) protected by this task on the primary
            storage after the snapshot is taken. The logical size of the data
            on the source if the data is fully hydrated or expanded and not
            reduced by change-block tracking, compression and deduplication.
        total_physical_backup_size_bytes (long|int): Specifies the total
            amount of physical space used on the Cohesity Cluster to store the
            protected object after being reduced by change-block tracking,
            compression and deduplication. For example, if the logical backup
            size is 1GB, but only 1MB was used on the Cohesity Cluster to
            store it, this field be equal to 1MB.
        total_source_size_bytes (long|int): Specifies the size of the source
            object (such as a VM) protected by this task on the primary
            storage before the snapshot is taken. The logical size of the data
            on the source if the data is fully hydrated or expanded and not
            reduced by change-block tracking, compression and deduplication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "admitted_time_usecs":'admittedTimeUsecs',
        "end_time_usecs":'endTimeUsecs',
        "num_app_instances":'numAppInstances',
        "num_canceled_tasks":'numCanceledTasks',
        "num_failed_app_objects":'numFailedAppObjects',
        "num_failed_tasks":'numFailedTasks',
        "num_successful_app_objects":'numSuccessfulAppObjects',
        "num_successful_tasks":'numSuccessfulTasks',
        "start_time_usecs":'startTimeUsecs',
        "time_taken_usecs":'timeTakenUsecs',
        "total_bytes_read_from_source":'totalBytesReadFromSource',
        "total_bytes_to_read_from_source":'totalBytesToReadFromSource',
        "total_logical_backup_size_bytes":'totalLogicalBackupSizeBytes',
        "total_physical_backup_size_bytes":'totalPhysicalBackupSizeBytes',
        "total_source_size_bytes":'totalSourceSizeBytes'
    }

    def __init__(self,
                 admitted_time_usecs=None,
                 end_time_usecs=None,
                 num_app_instances=None,
                 num_canceled_tasks=None,
                 num_failed_app_objects=None,
                 num_failed_tasks=None,
                 num_successful_app_objects=None,
                 num_successful_tasks=None,
                 start_time_usecs=None,
                 time_taken_usecs=None,
                 total_bytes_read_from_source=None,
                 total_bytes_to_read_from_source=None,
                 total_logical_backup_size_bytes=None,
                 total_physical_backup_size_bytes=None,
                 total_source_size_bytes=None):
        """Constructor for the ProtectionJobRunStats class"""

        # Initialize members of the class
        self.admitted_time_usecs = admitted_time_usecs
        self.end_time_usecs = end_time_usecs
        self.num_app_instances = num_app_instances
        self.num_canceled_tasks = num_canceled_tasks
        self.num_failed_app_objects = num_failed_app_objects
        self.num_failed_tasks = num_failed_tasks
        self.num_successful_app_objects = num_successful_app_objects
        self.num_successful_tasks = num_successful_tasks
        self.start_time_usecs = start_time_usecs
        self.time_taken_usecs = time_taken_usecs
        self.total_bytes_read_from_source = total_bytes_read_from_source
        self.total_bytes_to_read_from_source = total_bytes_to_read_from_source
        self.total_logical_backup_size_bytes = total_logical_backup_size_bytes
        self.total_physical_backup_size_bytes = total_physical_backup_size_bytes
        self.total_source_size_bytes = total_source_size_bytes


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
        admitted_time_usecs = dictionary.get('admittedTimeUsecs')
        end_time_usecs = dictionary.get('endTimeUsecs')
        num_app_instances = dictionary.get('numAppInstances')
        num_canceled_tasks = dictionary.get('numCanceledTasks')
        num_failed_app_objects = dictionary.get('numFailedAppObjects')
        num_failed_tasks = dictionary.get('numFailedTasks')
        num_successful_app_objects = dictionary.get('numSuccessfulAppObjects')
        num_successful_tasks = dictionary.get('numSuccessfulTasks')
        start_time_usecs = dictionary.get('startTimeUsecs')
        time_taken_usecs = dictionary.get('timeTakenUsecs')
        total_bytes_read_from_source = dictionary.get('totalBytesReadFromSource')
        total_bytes_to_read_from_source = dictionary.get('totalBytesToReadFromSource')
        total_logical_backup_size_bytes = dictionary.get('totalLogicalBackupSizeBytes')
        total_physical_backup_size_bytes = dictionary.get('totalPhysicalBackupSizeBytes')
        total_source_size_bytes = dictionary.get('totalSourceSizeBytes')

        # Return an object of this model
        return cls(admitted_time_usecs,
                   end_time_usecs,
                   num_app_instances,
                   num_canceled_tasks,
                   num_failed_app_objects,
                   num_failed_tasks,
                   num_successful_app_objects,
                   num_successful_tasks,
                   start_time_usecs,
                   time_taken_usecs,
                   total_bytes_read_from_source,
                   total_bytes_to_read_from_source,
                   total_logical_backup_size_bytes,
                   total_physical_backup_size_bytes,
                   total_source_size_bytes)


