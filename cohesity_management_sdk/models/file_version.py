# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.snapshot_attempt

class FileVersion(object):

    """Implementation of the 'FileVersion' model.

    Specifies information about a single file or folder.

    Attributes:
        modified_time_usecs (long|int): Specifies the time when the file or
            folder was last modified. Specified as a Unix epoch Timestamp (in
            microseconds).
        size_bytes (long|int): Specifies the size of the file or folder (in
            bytes) from the most recent snapshot.
        snapshots (list of SnapshotAttempt): Array of Snapshots.  Specifies
            the available snapshots of the file or folder. When a Job Run
            executes, it captures a snapshot of object (such as a VM) that
            contains the file or folder.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "modified_time_usecs":'modifiedTimeUsecs',
        "size_bytes":'sizeBytes',
        "snapshots":'snapshots'
    }

    def __init__(self,
                 modified_time_usecs=None,
                 size_bytes=None,
                 snapshots=None):
        """Constructor for the FileVersion class"""

        # Initialize members of the class
        self.modified_time_usecs = modified_time_usecs
        self.size_bytes = size_bytes
        self.snapshots = snapshots


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
        modified_time_usecs = dictionary.get('modifiedTimeUsecs')
        size_bytes = dictionary.get('sizeBytes')
        snapshots = None
        if dictionary.get('snapshots') != None:
            snapshots = list()
            for structure in dictionary.get('snapshots'):
                snapshots.append(cohesity_management_sdk.models.snapshot_attempt.SnapshotAttempt.from_dictionary(structure))

        # Return an object of this model
        return cls(modified_time_usecs,
                   size_bytes,
                   snapshots)


