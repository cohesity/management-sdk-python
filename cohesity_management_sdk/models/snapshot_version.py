# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class SnapshotVersion(object):

    """Implementation of the 'SnapshotVersion' model.

    Specifies information about snapshots of a backup object.

    Attributes:
        attempt_number (long|int): Specifies the number of the attempts made
            by the Job Run to capture a snapshot of the object. For example,
            if an snapshot is successfully captured after three attempts, this
            field equals 3.
        delta_size_bytes (long|int): Specifies the size of the data captured
            from the source object. For a full backup (where Change Block
            Tracking is not utilized) this field is equal to logicalSizeBytes.
            For an incremental backup (where Change Block Tracking is
            utilized), this field specifies the size of the data that has
            changed since the last backup.
        is_app_consistent (bool): Specifies if an app-consistent snapshot was
            captured. For example, was the VM was quiesced before the snapshot
            was captured.
        is_full_backup (bool): Specifies if the snapshot is a full backup. For
            example, all blocks of the VM is captured and Change Block
            Tracking is not utilized.
        job_run_id (long|int): Specifies the id of the Job Run that captured
            the snapshot.
        local_mount_path (string): Specifies the local path relative to the
            View, without the ViewBox/View prefix.
        logical_size_bytes (long|int): Specifies the size of the snapshot if
            the data is fully hydrated or expanded and not reduced by
            change-block tracking, compression and deduplication. For example
            if a VMDK of size 100GB is created with thin provisioning and the
            disk size to store the VMDK is 20GB. The logical size of this
            object is 100GB and the physical size is 20GB.
        physical_size_bytes (long|int): Specifies the amount of data actually
            used on the disk to store this object after being reduced by
            change-block tracking, compression and deduplication.
        primary_physical_size_bytes (long|int): Specifies the total amount of
            disk space used to store this object on the primary storage. For
            example the total amount of disk space used to store the VM files
            (such as the VMDK files) on the primary datastore.
        started_time_usecs (long|int): Specifies the time when the Job Run
            starts capturing a snapshot. Specified as a Unix epoch Timestamp
            (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attempt_number":'attemptNumber',
        "delta_size_bytes":'deltaSizeBytes',
        "is_app_consistent":'isAppConsistent',
        "is_full_backup":'isFullBackup',
        "job_run_id":'jobRunId',
        "local_mount_path":'localMountPath',
        "logical_size_bytes":'logicalSizeBytes',
        "physical_size_bytes":'physicalSizeBytes',
        "primary_physical_size_bytes":'primaryPhysicalSizeBytes',
        "started_time_usecs":'startedTimeUsecs'
    }

    def __init__(self,
                 attempt_number=None,
                 delta_size_bytes=None,
                 is_app_consistent=None,
                 is_full_backup=None,
                 job_run_id=None,
                 local_mount_path=None,
                 logical_size_bytes=None,
                 physical_size_bytes=None,
                 primary_physical_size_bytes=None,
                 started_time_usecs=None):
        """Constructor for the SnapshotVersion class"""

        # Initialize members of the class
        self.attempt_number = attempt_number
        self.delta_size_bytes = delta_size_bytes
        self.is_app_consistent = is_app_consistent
        self.is_full_backup = is_full_backup
        self.job_run_id = job_run_id
        self.local_mount_path = local_mount_path
        self.logical_size_bytes = logical_size_bytes
        self.physical_size_bytes = physical_size_bytes
        self.primary_physical_size_bytes = primary_physical_size_bytes
        self.started_time_usecs = started_time_usecs


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
        attempt_number = dictionary.get('attemptNumber')
        delta_size_bytes = dictionary.get('deltaSizeBytes')
        is_app_consistent = dictionary.get('isAppConsistent')
        is_full_backup = dictionary.get('isFullBackup')
        job_run_id = dictionary.get('jobRunId')
        local_mount_path = dictionary.get('localMountPath')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        physical_size_bytes = dictionary.get('physicalSizeBytes')
        primary_physical_size_bytes = dictionary.get('primaryPhysicalSizeBytes')
        started_time_usecs = dictionary.get('startedTimeUsecs')

        # Return an object of this model
        return cls(attempt_number,
                   delta_size_bytes,
                   is_app_consistent,
                   is_full_backup,
                   job_run_id,
                   local_mount_path,
                   logical_size_bytes,
                   physical_size_bytes,
                   primary_physical_size_bytes,
                   started_time_usecs)


