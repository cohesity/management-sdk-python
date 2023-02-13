# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.snapshot_attempt
import cohesity_management_sdk.models.replica_info

class FileSnapshotInformation(object):

    """Implementation of the 'FileSnapshotInformation' model.

    Specifies the information about the snapshot that contains the file
    or folder. In addition, information about the file or folder is
    provided.

    Attributes:
        has_archival_copy (bool): If true, this snapshot is located on an
            archival target (such as a tape or AWS).
        has_local_copy (bool): If true, this snapshot is located on a local
            Cohesity Cluster.
        has_remote_copy (bool): If true, this snapshot is located on a Remote
            Cohesity Cluster.
        modified_time_usecs (long|int): Specifies the time when the file or
            folder was last modified. Specified as a Unix epoch Timestamp (in
            microseconds).
        replica_info_list (list of ReplicaInfo): Specifies the list of
            replication information about the current snapshot.
        size_bytes (long|int): Specifies the size of the file or folder in
            bytes.
        snapshot (SnapshotAttempt): Specifies information about a single
            snapshot.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_archival_copy":'hasArchivalCopy',
        "has_local_copy":'hasLocalCopy',
        "has_remote_copy":'hasRemoteCopy',
        "modified_time_usecs":'modifiedTimeUsecs',
        "replica_info_list":'replicaInfoList',
        "size_bytes":'sizeBytes',
        "snapshot":'snapshot'
    }

    def __init__(self,
                 has_archival_copy=None,
                 has_local_copy=None,
                 has_remote_copy=None,
                 modified_time_usecs=None,
                 replica_info_list=None,
                 size_bytes=None,
                 snapshot=None):
        """Constructor for the FileSnapshotInformation class"""

        # Initialize members of the class
        self.has_archival_copy = has_archival_copy
        self.has_local_copy = has_local_copy
        self.has_remote_copy = has_remote_copy
        self.modified_time_usecs = modified_time_usecs
        self.replica_info_list = replica_info_list
        self.size_bytes = size_bytes
        self.snapshot = snapshot


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
        has_archival_copy = dictionary.get('hasArchivalCopy')
        has_local_copy = dictionary.get('hasLocalCopy')
        has_remote_copy = dictionary.get('hasRemoteCopy')
        modified_time_usecs = dictionary.get('modifiedTimeUsecs')
        replica_info_list = None
        if dictionary.get('replicaInfoList') != None:
            replica_info_list = list()
            for structure in dictionary.get('replicaInfoList'):
                replica_info_list.append(cohesity_management_sdk.models.replica_info.ReplicaInfo.from_dictionary(structure))
        size_bytes = dictionary.get('sizeBytes')
        snapshot = cohesity_management_sdk.models.snapshot_attempt.SnapshotAttempt.from_dictionary(dictionary.get('snapshot')) if dictionary.get('snapshot') else None

        # Return an object of this model
        return cls(has_archival_copy,
                   has_local_copy,
                   has_remote_copy,
                   modified_time_usecs,
                   replica_info_list,
                   size_bytes,
                   snapshot)


