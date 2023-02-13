# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class IndexAndSnapshots(object):

    """Implementation of the 'IndexAndSnapshots' model.

    Specifies settings required to restore the index and Snapshots of
    a Protection Job.

    Attributes:
        archive_task_uid (UniversalId): Specifies a unique id of the Archive
            task that originally archived the object to the Vault.
        end_time_usecs (long|int): Specifies the end time as a Unix epoch
            Timestamp (in microseconds). If set, only index and Snapshots for
            Protection Job Runs that started before the specified end time are
            restored.
        remote_protection_job_uid (UniversalId): Specifies a unique id
            assigned to the original Protection Job by the original Cluster
            that archived data to the remote Vault.
        start_time_usecs (long|int): Specifies the start time as a Unix epoch
            Timestamp (in microseconds). If set, only the index and Snapshots
            for Protection Job Runs that started after the specified start
            time are restored.
        view_box_id (long|int): Specifies the id of the local Storage Domain
            (View Box) where the index and the Snapshot will be restored to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archive_task_uid":'archiveTaskUid',
        "end_time_usecs":'endTimeUsecs',
        "remote_protection_job_uid":'remoteProtectionJobUid',
        "start_time_usecs":'startTimeUsecs',
        "view_box_id":'viewBoxId'
    }

    def __init__(self,
                 archive_task_uid=None,
                 end_time_usecs=None,
                 remote_protection_job_uid=None,
                 start_time_usecs=None,
                 view_box_id=None):
        """Constructor for the IndexAndSnapshots class"""

        # Initialize members of the class
        self.archive_task_uid = archive_task_uid
        self.end_time_usecs = end_time_usecs
        self.remote_protection_job_uid = remote_protection_job_uid
        self.start_time_usecs = start_time_usecs
        self.view_box_id = view_box_id


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
        end_time_usecs = dictionary.get('endTimeUsecs')
        remote_protection_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('remoteProtectionJobUid')) if dictionary.get('remoteProtectionJobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(archive_task_uid,
                   end_time_usecs,
                   remote_protection_job_uid,
                   start_time_usecs,
                   view_box_id)


