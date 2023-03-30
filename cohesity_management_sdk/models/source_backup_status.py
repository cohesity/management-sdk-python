# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.app_entity_backup_status_info
import cohesity_management_sdk.models.backup_source_stats
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.snapshot_info


class SourceBackupStatus(object):

    """Implementation of the 'SourceBackupStatus' model.

    Specifies the source object to protect and the current backup status.


    Attributes:

        apps_backup_status (list of AppEntityBackupStatusInfo): Specifies the
            backup status at app/DB level.
        current_snapshot_info (SnapshotInfo): Specifies details about the
            snapshot captured to backup the source object (such as a VM).
        error (string): Specifies if an error occurred (if any) while running
            this task. This field is populated when the status is equal to
            'kFailure'.
        is_full_backup (bool): Specifies whether this is a 'kFull' or
            'kRegular' backup of the Run. This may be true even if the
            scheduled backup type is 'kRegular'. This will happen when this run
            corresponds to the first backup run of the Job or if no previous
            snapshot information is found.
        num_restarts (int): Specifies the number of times the task was
            restarted because of the changes on the backup source host.
        parent_source_id (long|int): Specifies the id of the registered
            Protection Source that is the parent of the Objects that are
            protected by this Job Run.
        progress_monitor_task_path (string): Specifies the yoda progress
            monitor task path which is used to get pulse information about the
            source that is being backed up.
        quiesced (bool): Specifies if app-consistent snapshot was captured.
            This field is set to true, if an app-consistent snapshot was taken
            by quiescing applications and the file system before taking a
            backup.
        sla_violated (bool): Specifies if the SLA was violated for the Job Run.
            This field is set to true, if time to complete the Job Run is
            longer than the SLA specified. This field is populated when the
            status is set to 'kSuccess' or 'kFailure'.
        source (ProtectionSource): Specifies the source object to protect.
        stats (BackupSourceStats): Specifies the stats of the Backup Run task
            for the Protection Source.
        status (StatusSourceBackupStatusEnum): Specifies the status of the
            source object being protected. 'kAccepted' indicates the task is
            queued to run but not yet running. 'kRunning' indicates the task is
            running. 'kCanceling' indicates a request to cancel the task has
            occurred but the task is not yet canceled. 'kCanceled' indicates
            the task has been canceled. 'kSuccess' indicates the task was
            successful. 'kFailure' indicates the task failed. 'kWarning'
            indicates the task has finished with warning. 'kOnHold' indicates
            the task is kept onHold. 'kMissed' indicates the task is missed.
            'Finalizing' indicates the task is finalizing.
        warnings (list of string): Array of Warnings.  Specifies the warnings
            that occurred (if any) while running this task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "apps_backup_status":'appsBackupStatus',
        "current_snapshot_info":'currentSnapshotInfo',
        "error":'error',
        "is_full_backup":'isFullBackup',
        "num_restarts":'numRestarts',
        "parent_source_id":'parentSourceId',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "quiesced":'quiesced',
        "sla_violated":'slaViolated',
        "source":'source',
        "stats":'stats',
        "status":'status',
        "warnings":'warnings',
    }
    def __init__(self,
                 apps_backup_status=None,
                 current_snapshot_info=None,
                 error=None,
                 is_full_backup=None,
                 num_restarts=None,
                 parent_source_id=None,
                 progress_monitor_task_path=None,
                 quiesced=None,
                 sla_violated=None,
                 source=None,
                 stats=None,
                 status=None,
                 warnings=None,
            ):

        """Constructor for the SourceBackupStatus class"""

        # Initialize members of the class
        self.apps_backup_status = apps_backup_status
        self.current_snapshot_info = current_snapshot_info
        self.error = error
        self.is_full_backup = is_full_backup
        self.num_restarts = num_restarts
        self.parent_source_id = parent_source_id
        self.progress_monitor_task_path = progress_monitor_task_path
        self.quiesced = quiesced
        self.sla_violated = sla_violated
        self.source = source
        self.stats = stats
        self.status = status
        self.warnings = warnings

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
        apps_backup_status = None
        if dictionary.get('appsBackupStatus') != None:
            apps_backup_status = list()
            for structure in dictionary.get('appsBackupStatus'):
                apps_backup_status.append(cohesity_management_sdk.models.app_entity_backup_status_info.AppEntityBackupStatusInfo.from_dictionary(structure))
        current_snapshot_info = cohesity_management_sdk.models.snapshot_info.SnapshotInfo.from_dictionary(dictionary.get('currentSnapshotInfo')) if dictionary.get('currentSnapshotInfo') else None
        error = dictionary.get('error')
        is_full_backup = dictionary.get('isFullBackup')
        num_restarts = dictionary.get('numRestarts')
        parent_source_id = dictionary.get('parentSourceId')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        quiesced = dictionary.get('quiesced')
        sla_violated = dictionary.get('slaViolated')
        source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('source')) if dictionary.get('source') else None
        stats = cohesity_management_sdk.models.backup_source_stats.BackupSourceStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        status = dictionary.get('status')
        warnings = dictionary.get("warnings")

        # Return an object of this model
        return cls(
            apps_backup_status,
            current_snapshot_info,
            error,
            is_full_backup,
            num_restarts,
            parent_source_id,
            progress_monitor_task_path,
            quiesced,
            sla_violated,
            source,
            stats,
            status,
            warnings
)