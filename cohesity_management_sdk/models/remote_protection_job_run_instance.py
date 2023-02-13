# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class RemoteProtectionJobRunInstance(object):

    """Implementation of the 'RemoteProtectionJobRunInstance' model.

    Specifies details about one Job Run (Snapshot) archived to a remote Vault
    that was captured by a Protection Job.

    Attributes:
        archive_task_uid (UniversalId): Specifies the globally unique id of
            the archival task that archived the Snapshot to the Vault.
        archive_version (int): Specifies the version of the archive.
        expiry_time_usecs (long|int): Specifies the time when the archive
            expires. This time is recorded as a Unix epoch Timestamp (in
            microseconds).
        index_size_bytes (long|int): Specifies the size of the index for the
            archive.
        job_run_id (long|int): Specifies the instance id of the Job Run task
            capturing the Snapshot.
        metadata_complete (bool): Specifies whether a full set of metadata is
            available now.
        snapshot_time_usecs (long|int): Specify the time the Snapshot was
            captured as a Unix epoch Timestamp (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archive_task_uid":'archiveTaskUid',
        "archive_version":'archiveVersion',
        "expiry_time_usecs":'expiryTimeUsecs',
        "index_size_bytes":'indexSizeBytes',
        "job_run_id":'jobRunId',
        "metadata_complete":'metadataComplete',
        "snapshot_time_usecs":'snapshotTimeUsecs'
    }

    def __init__(self,
                 archive_task_uid=None,
                 archive_version=None,
                 expiry_time_usecs=None,
                 index_size_bytes=None,
                 job_run_id=None,
                 metadata_complete=None,
                 snapshot_time_usecs=None):
        """Constructor for the RemoteProtectionJobRunInstance class"""

        # Initialize members of the class
        self.archive_task_uid = archive_task_uid
        self.archive_version = archive_version
        self.expiry_time_usecs = expiry_time_usecs
        self.index_size_bytes = index_size_bytes
        self.job_run_id = job_run_id
        self.metadata_complete = metadata_complete
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
        archive_version = dictionary.get('archiveVersion')
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        index_size_bytes = dictionary.get('indexSizeBytes')
        job_run_id = dictionary.get('jobRunId')
        metadata_complete = dictionary.get('metadataComplete')
        snapshot_time_usecs = dictionary.get('snapshotTimeUsecs')

        # Return an object of this model
        return cls(archive_task_uid,
                   archive_version,
                   expiry_time_usecs,
                   index_size_bytes,
                   job_run_id,
                   metadata_complete,
                   snapshot_time_usecs)


