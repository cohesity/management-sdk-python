# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.source_backup_status
import cohesity_management_sdk.models.copy_run
import cohesity_management_sdk.models.run_uid

class LatestProtectionRun(object):

    """Implementation of the 'LatestProtectionRun' model.

    Specifies the information about the latest Protection Run.

    Attributes:
        backup_run (SourceBackupStatus): Specifies the source object to
            protect and the current backup status.
        change_event_id (long|int): Specifies the event id which caused last
            update on this object.
        copy_run (CopyRun): Specifies details about the Copy Run for a backup
            run of a Job Run. A Copy task copies snapshots resulted from a
            backup run to a snapshot target which could be 'kLocal',
            'kArchival', or 'kRemote'.
        job_run_id (long|int): Specifies job run id of the latest successful
            Protection Job Run.
        protection_job_run_uid (RunUid): Specifies the universal id of the
            latest successful Protection Job Run.
        snapshot_target (string): Specifies the cluster id in case of local or
            replication snapshots and name of location in case of archival
            snapshots.
        snapshot_target_type (int): Specifies the snapshot target type of the
            latest snapshot.
        task_status (int): Specifies the task status of the Protection Job Run
            in the final attempt.
        uuid (string): Specifies the unique id of the Protection Source for
            which a snapshot is taken.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_run":'backupRun',
        "change_event_id":'changeEventId',
        "copy_run":'copyRun',
        "job_run_id":'jobRunId',
        "protection_job_run_uid":'protectionJobRunUid',
        "snapshot_target":'snapshotTarget',
        "snapshot_target_type":'snapshotTargetType',
        "task_status":'taskStatus',
        "uuid":'uuid'
    }

    def __init__(self,
                 backup_run=None,
                 change_event_id=None,
                 copy_run=None,
                 job_run_id=None,
                 protection_job_run_uid=None,
                 snapshot_target=None,
                 snapshot_target_type=None,
                 task_status=None,
                 uuid=None):
        """Constructor for the LatestProtectionRun class"""

        # Initialize members of the class
        self.backup_run = backup_run
        self.change_event_id = change_event_id
        self.copy_run = copy_run
        self.job_run_id = job_run_id
        self.protection_job_run_uid = protection_job_run_uid
        self.snapshot_target = snapshot_target
        self.snapshot_target_type = snapshot_target_type
        self.task_status = task_status
        self.uuid = uuid


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
        backup_run = cohesity_management_sdk.models.source_backup_status.SourceBackupStatus.from_dictionary(dictionary.get('backupRun')) if dictionary.get('backupRun') else None
        change_event_id = dictionary.get('changeEventId')
        copy_run = cohesity_management_sdk.models.copy_run.CopyRun.from_dictionary(dictionary.get('copyRun')) if dictionary.get('copyRun') else None
        job_run_id = dictionary.get('jobRunId')
        protection_job_run_uid = cohesity_management_sdk.models.run_uid.RunUid.from_dictionary(dictionary.get('protectionJobRunUid')) if dictionary.get('protectionJobRunUid') else None
        snapshot_target = dictionary.get('snapshotTarget')
        snapshot_target_type = dictionary.get('snapshotTargetType')
        task_status = dictionary.get('taskStatus')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(backup_run,
                   change_event_id,
                   copy_run,
                   job_run_id,
                   protection_job_run_uid,
                   snapshot_target,
                   snapshot_target_type,
                   task_status,
                   uuid)


