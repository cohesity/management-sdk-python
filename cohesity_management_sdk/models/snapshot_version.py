# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.replica_info

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
        indexing_status (IndexingStatusEnum): Specifies the indexing status of
            the snapshot. 'kStarted' indicates that indexing has started.
            'kDone' indicates that indexing has been completed according to
            the type of object. 'kNoIndex' indicates that the snapshot cannot
            be indexed. This is the case during archival restore.
            'kIceboxRestoreStarted' indicates that indexing is started from an
            archive. 'kIceboxRestoreError' indicates that an error occurred
            during restore from archiveand there is no index present.
            'kSkipped' indicates that indexing is skipped due to indexing
            backlog.
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
        replica_info_list (list of ReplicaInfo): Specifies the list of
            replication information about the current snapshot.
        started_time_usecs (long|int): Specifies the time when the Job Run
            starts capturing a snapshot. Specified as a Unix epoch Timestamp
            (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attempt_number":'attemptNumber',
        "delta_size_bytes":'deltaSizeBytes',
        "indexing_status":'indexingStatus',
        "is_app_consistent":'isAppConsistent',
        "is_full_backup":'isFullBackup',
        "job_run_id":'jobRunId',
        "local_mount_path":'localMountPath',
        "logical_size_bytes":'logicalSizeBytes',
        "physical_size_bytes":'physicalSizeBytes',
        "primary_physical_size_bytes":'primaryPhysicalSizeBytes',
        "replica_info_list":'replicaInfoList',
        "started_time_usecs":'startedTimeUsecs'
    }

    def __init__(self,
                 attempt_number=None,
                 delta_size_bytes=None,
                 indexing_status=None,
                 is_app_consistent=None,
                 is_full_backup=None,
                 job_run_id=None,
                 local_mount_path=None,
                 logical_size_bytes=None,
                 physical_size_bytes=None,
                 primary_physical_size_bytes=None,
                 replica_info_list=None,
                 started_time_usecs=None):
        """Constructor for the SnapshotVersion class"""

        # Initialize members of the class
        self.attempt_number = attempt_number
        self.delta_size_bytes = delta_size_bytes
        self.indexing_status = indexing_status
        self.is_app_consistent = is_app_consistent
        self.is_full_backup = is_full_backup
        self.job_run_id = job_run_id
        self.local_mount_path = local_mount_path
        self.logical_size_bytes = logical_size_bytes
        self.physical_size_bytes = physical_size_bytes
        self.primary_physical_size_bytes = primary_physical_size_bytes
        self.replica_info_list = replica_info_list
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
        indexing_status = dictionary.get('indexingStatus')
        is_app_consistent = dictionary.get('isAppConsistent')
        is_full_backup = dictionary.get('isFullBackup')
        job_run_id = dictionary.get('jobRunId')
        local_mount_path = dictionary.get('localMountPath')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        physical_size_bytes = dictionary.get('physicalSizeBytes')
        primary_physical_size_bytes = dictionary.get('primaryPhysicalSizeBytes')
        replica_info_list = None
        if dictionary.get('replicaInfoList') != None:
            replica_info_list = list()
            for structure in dictionary.get('replicaInfoList'):
                replica_info_list.append(cohesity_management_sdk.models.replica_info.ReplicaInfo.from_dictionary(structure))
        started_time_usecs = dictionary.get('startedTimeUsecs')

        # Return an object of this model
        return cls(attempt_number,
                   delta_size_bytes,
                   indexing_status,
                   is_app_consistent,
                   is_full_backup,
                   job_run_id,
                   local_mount_path,
                   logical_size_bytes,
                   physical_size_bytes,
                   primary_physical_size_bytes,
                   replica_info_list,
                   started_time_usecs)


