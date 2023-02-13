# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sql_update_restore_task_options
import cohesity_management_sdk.models.files_to_directory_mapping

class RestoreSqlAppObjectParams(object):

    """Implementation of the 'RestoreSqlAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        capture_tail_logs (bool): Set to true if tail logs are to be captured
            before the restore operation. This is only applicable if we are
            restoring the SQL database to its original source, and the
            database is not being renamed.
        continue_after_error (bool): Whether restore should continue after
            encountering a page checksum error.
        data_file_destination (string): Which directory to put the database
            data files. Missing directory will be automatically created.
            Cannot be empty if not restoring to the original SQL instance.
        db_restore_overwrite_policy (int): Policy to overwrite an existing DB
            during a restore operation.
        enable_checksum (bool): Whether restore checksums are enabled.
        instance_name (string): The name of the SQL instance that we restore
            database to. If target_host is not empty, this also cannot be
            empty.
        is_auto_sync_enabled (bool): The following field is set if auto_sync
            for multi-stage SQL restore task is enabled. This field is valid
            only if is_multi_state_restore is set to true.
        is_multi_stage_restore (bool): The following field is set if we are
            creating a multi-stage SQL restore task needed for features such
            as Hot-Standby.
        keep_cdc (bool): Set to true to keep cdc on restored database.
        log_file_destination (string): Which directory to put the database log
            files. Missing directory will be automatically created. Cannot be
            empty if not restoring to the original SQL instance.
        multi_stage_restore_options (SqlUpdateRestoreTaskOptions): TODO: type
            description here.
        new_database_name (string): The new name of the database, if it is
            going to be renamed. app_entity in RestoreAppObject has to be
            non-empty for the renaming, otherwise it does not make sense to
            rename all databases in the owner.
        restore_time_secs (long|int): The time to which the SQL database needs
            to be restored. This allows for granular recovery of SQL
            databases. If this is not set, the SQL database will be recovered
            to the full/incremental snapshot (specified in the owner's restore
            object in AppOwnerRestoreInfo).
        resume_restore (bool): Resume restore if sql instance/database exist
            in restore/recovering state. The database might be in
            restore/recovering state if previous restore failed or previous
            restore was attempted  with norecovery option.
        secondary_data_file_destination (string): Which directory to put the
            secondary data files of the database. Secondary data files are
            optional and are user defined. The recommended file name extension
            for these is ".ndf".  If this option is specified, the directory
            will be automatically created if its missing.
        secondary_data_file_destination_vec (list of FilesToDirectoryMapping):
            Specify the secondary data files and corresponding direcories of
            the DB. Secondary data files are optional and are user defined.
            The recommended file extension for secondary files is ".ndf".  If
            this option is specified and the destination folders do not exist
            they will be automatically created.
        with_clause (string): 'with_clause' contains 'with clause' to be used
            in native sql restore command. This is only applicable for db
            restore of native sql backup. Here user can specify multiple
            restore options. Example: "WITH BUFFERCOUNT = 575, MAXTRANSFERSIZE
            = 2097152". If this is not specified, we use the value specified
            in magneto_sql_native_restore_with_clause gflag.
        with_no_recovery (bool): Set to true if we want to recover the
            database in "NO_RECOVERY" mode which does not bring it online
            after restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capture_tail_logs":'captureTailLogs',
        "continue_after_error":'continueAfterError',
        "data_file_destination":'dataFileDestination',
        "db_restore_overwrite_policy":'dbRestoreOverwritePolicy',
        "enable_checksum":'enableChecksum',
        "instance_name":'instanceName',
        "is_auto_sync_enabled":'isAutoSyncEnabled',
        "is_multi_stage_restore":'isMultiStageRestore',
        "keep_cdc":'keepCdc',
        "log_file_destination":'logFileDestination',
        "multi_stage_restore_options":'multiStageRestoreOptions',
        "new_database_name":'newDatabaseName',
        "restore_time_secs":'restoreTimeSecs',
        "resume_restore":'resumeRestore',
        "secondary_data_file_destination":'secondaryDataFileDestination',
        "secondary_data_file_destination_vec":'secondaryDataFileDestinationVec',
        "with_clause":'withClause',
        "with_no_recovery":'withNoRecovery'
    }

    def __init__(self,
                 capture_tail_logs=None,
                 continue_after_error=None,
                 data_file_destination=None,
                 db_restore_overwrite_policy=None,
                 enable_checksum=None,
                 instance_name=None,
                 is_auto_sync_enabled=None,
                 is_multi_stage_restore=None,
                 keep_cdc=None,
                 log_file_destination=None,
                 multi_stage_restore_options=None,
                 new_database_name=None,
                 restore_time_secs=None,
                 resume_restore=None,
                 secondary_data_file_destination=None,
                 secondary_data_file_destination_vec=None,
                 with_clause=None,
                 with_no_recovery=None):
        """Constructor for the RestoreSqlAppObjectParams class"""

        # Initialize members of the class
        self.capture_tail_logs = capture_tail_logs
        self.continue_after_error = continue_after_error
        self.data_file_destination = data_file_destination
        self.db_restore_overwrite_policy = db_restore_overwrite_policy
        self.enable_checksum = enable_checksum
        self.instance_name = instance_name
        self.is_auto_sync_enabled = is_auto_sync_enabled
        self.is_multi_stage_restore = is_multi_stage_restore
        self.keep_cdc = keep_cdc
        self.log_file_destination = log_file_destination
        self.multi_stage_restore_options = multi_stage_restore_options
        self.new_database_name = new_database_name
        self.restore_time_secs = restore_time_secs
        self.resume_restore = resume_restore
        self.secondary_data_file_destination = secondary_data_file_destination
        self.secondary_data_file_destination_vec = secondary_data_file_destination_vec
        self.with_clause = with_clause
        self.with_no_recovery = with_no_recovery


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
        capture_tail_logs = dictionary.get('captureTailLogs')
        continue_after_error = dictionary.get('continueAfterError')
        data_file_destination = dictionary.get('dataFileDestination')
        db_restore_overwrite_policy = dictionary.get('dbRestoreOverwritePolicy')
        enable_checksum = dictionary.get('enableChecksum')
        instance_name = dictionary.get('instanceName')
        is_auto_sync_enabled = dictionary.get('isAutoSyncEnabled')
        is_multi_stage_restore = dictionary.get('isMultiStageRestore')
        keep_cdc = dictionary.get('keepCdc')
        log_file_destination = dictionary.get('logFileDestination')
        multi_stage_restore_options = cohesity_management_sdk.models.sql_update_restore_task_options.SqlUpdateRestoreTaskOptions.from_dictionary(dictionary.get('multiStageRestoreOptions')) if dictionary.get('multiStageRestoreOptions') else None
        new_database_name = dictionary.get('newDatabaseName')
        restore_time_secs = dictionary.get('restoreTimeSecs')
        resume_restore = dictionary.get('resumeRestore')
        secondary_data_file_destination = dictionary.get('secondaryDataFileDestination')
        secondary_data_file_destination_vec = None
        if dictionary.get('secondaryDataFileDestinationVec') != None:
            secondary_data_file_destination_vec = list()
            for structure in dictionary.get('secondaryDataFileDestinationVec'):
                secondary_data_file_destination_vec.append(cohesity_management_sdk.models.files_to_directory_mapping.FilesToDirectoryMapping.from_dictionary(structure))
        with_clause = dictionary.get('withClause')
        with_no_recovery = dictionary.get('withNoRecovery')

        # Return an object of this model
        return cls(capture_tail_logs,
                   continue_after_error,
                   data_file_destination,
                   db_restore_overwrite_policy,
                   enable_checksum,
                   instance_name,
                   is_auto_sync_enabled,
                   is_multi_stage_restore,
                   keep_cdc,
                   log_file_destination,
                   multi_stage_restore_options,
                   new_database_name,
                   restore_time_secs,
                   resume_restore,
                   secondary_data_file_destination,
                   secondary_data_file_destination_vec,
                   with_clause,
                   with_no_recovery)


