# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto

class RetrieveArchiveInfoRetrievedEntity(object):

    """Implementation of the 'RetrieveArchiveInfo_RetrievedEntity' model.

    Proto to define the info about the entity that was retrieved from an
    archive.

    Attributes:
        bytes_transferred (long|int): Number of physical bytes transferred
            over wire for this entity.
        end_timestamp_usecs (long|int): Time in microseconds when retrieve of
            this entity finished or failed.
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        error (ErrorProto): If the retrieve of the 'entity' failed, this
            field may contain the cause of the failure.
        logical_bytes_transferred (long|int): Number of logical bytes
            transferred so far.
        logical_size_bytes (long|int): Total logical size of this entity.
        progress_monitor_task_path (string): The path relative to the root
            path of the retrieval task progress monitor of this entity
            progress monitor.
        relative_snapshot_dir (string): The path relative to the root of the
            file system where the snapshot of this entity was retrieved/copied
            to.
        start_timestamp_usecs (long|int): Time in microseconds when retrieve
            of this entity started.
        status (int): The retrieval status of this entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_transferred":'bytesTransferred',
        "end_timestamp_usecs":'endTimestampUsecs',
        "entity":'entity',
        "error":'error',
        "logical_bytes_transferred":'logicalBytesTransferred',
        "logical_size_bytes":'logicalSizeBytes',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "relative_snapshot_dir":'relativeSnapshotDir',
        "start_timestamp_usecs":'startTimestampUsecs',
        "status":'status'
    }

    def __init__(self,
                 bytes_transferred=None,
                 end_timestamp_usecs=None,
                 entity=None,
                 error=None,
                 logical_bytes_transferred=None,
                 logical_size_bytes=None,
                 progress_monitor_task_path=None,
                 relative_snapshot_dir=None,
                 start_timestamp_usecs=None,
                 status=None):
        """Constructor for the RetrieveArchiveInfoRetrievedEntity class"""

        # Initialize members of the class
        self.bytes_transferred = bytes_transferred
        self.end_timestamp_usecs = end_timestamp_usecs
        self.entity = entity
        self.error = error
        self.logical_bytes_transferred = logical_bytes_transferred
        self.logical_size_bytes = logical_size_bytes
        self.progress_monitor_task_path = progress_monitor_task_path
        self.relative_snapshot_dir = relative_snapshot_dir
        self.start_timestamp_usecs = start_timestamp_usecs
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
        bytes_transferred = dictionary.get('bytesTransferred')
        end_timestamp_usecs = dictionary.get('endTimestampUsecs')
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        logical_bytes_transferred = dictionary.get('logicalBytesTransferred')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        relative_snapshot_dir = dictionary.get('relativeSnapshotDir')
        start_timestamp_usecs = dictionary.get('startTimestampUsecs')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(bytes_transferred,
                   end_timestamp_usecs,
                   entity,
                   error,
                   logical_bytes_transferred,
                   logical_size_bytes,
                   progress_monitor_task_path,
                   relative_snapshot_dir,
                   start_timestamp_usecs,
                   status)


