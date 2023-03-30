# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filename_pattern_to_directory


class SqlRestoreParameters(object):

    """Implementation of the 'SqlRestoreParameters' model.

    Specifies the parameters specific the Application Server instance.


    Attributes:

        capture_tail_logs (bool): Set this to true if tail logs are to be
            captured before the restore operation. This is only applicable if
            we are restoring the SQL database to its hosting Protection Source,
            and the database is not being renamed.
        is_auto_sync_enabled (bool): This field determines if Auto Sync
            enabled/disabled for SQL Multi-stage Restore task
        keep_cdc (bool): This field prevents "change data capture" settings
            from being reomved when a database or log backup is restored on
            another server and database is recovered.
        keep_offline (bool): Set this to true if we want to restore the
            database and do not want to bring it online after restore.  This is
            only applicable if we are restoring the database back to its
            original location.
        new_database_name (string): Specifies optionally a new name for the
            restored database.
        new_instance_name (string): Specifies an instance name of the SQL
            Server that should be restored. SQL application has many instances.
            Each instance has a unique name. One of the instances that should
            be restored must be set in this field.
        overwrite_policy (OverwritePolicyEnum): Overwrite Policy specifies a
            policy to be used while recovering existing databases. Specifies
            the policy to be used while recovering existing databases.
            'kFailIfExists' refers to a policy to fail if DB exists already.
            'kOverwrite' refres to the policy to overwrite existing DB.
        restore_time_secs (long|int): Specifies the time in the past to which
            the SQL database needs to be restored. This allows for granular
            recovery of SQL databases. If this is not set, the SQL database
            will be restored from the full/incremental snapshot.
        target_data_files_directory (string): Specifies the directory where to
            put the database data files. Missing directory will be
            automatically created. This field must be set if restoring to a
            different target host.
        target_log_files_directory (string): Specifies the directory where to
            put the database log files. Missing directory will be automatically
            created. This field must be set if restoring to a different target
            host.
        target_secondary_data_files_directory_list (list of
            FilenamePatternToDirectory): Specifies the secondary data filename
            pattern and corresponding directories of the DB. Secondary data
            files are optional and are user defined. The recommended file
            extension for secondary files is ".ndf".  If this option is
            specified and the destination folders do not exist they will be
            automatically created.
        with_clause (string): WithClause allows you to specify clauses to be
            used in native sql restore task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "capture_tail_logs":'captureTailLogs',
        "is_auto_sync_enabled":'isAutoSyncEnabled',
        "keep_cdc":'keepCdc',
        "keep_offline":'keepOffline',
        "new_database_name":'newDatabaseName',
        "new_instance_name":'newInstanceName',
        "overwrite_policy":'overwritePolicy',
        "restore_time_secs":'restoreTimeSecs',
        "target_data_files_directory":'targetDataFilesDirectory',
        "target_log_files_directory":'targetLogFilesDirectory',
        "target_secondary_data_files_directory_list":'targetSecondaryDataFilesDirectoryList',
        "with_clause":'withClause',
    }
    def __init__(self,
                 capture_tail_logs=None,
                 is_auto_sync_enabled=None,
                 keep_cdc=None,
                 keep_offline=None,
                 new_database_name=None,
                 new_instance_name=None,
                 overwrite_policy=None,
                 restore_time_secs=None,
                 target_data_files_directory=None,
                 target_log_files_directory=None,
                 target_secondary_data_files_directory_list=None,
                 with_clause=None,
            ):

        """Constructor for the SqlRestoreParameters class"""

        # Initialize members of the class
        self.capture_tail_logs = capture_tail_logs
        self.is_auto_sync_enabled = is_auto_sync_enabled
        self.keep_cdc = keep_cdc
        self.keep_offline = keep_offline
        self.new_database_name = new_database_name
        self.new_instance_name = new_instance_name
        self.overwrite_policy = overwrite_policy
        self.restore_time_secs = restore_time_secs
        self.target_data_files_directory = target_data_files_directory
        self.target_log_files_directory = target_log_files_directory
        self.target_secondary_data_files_directory_list = target_secondary_data_files_directory_list
        self.with_clause = with_clause

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
        is_auto_sync_enabled = dictionary.get('isAutoSyncEnabled')
        keep_cdc = dictionary.get('keepCdc')
        keep_offline = dictionary.get('keepOffline')
        new_database_name = dictionary.get('newDatabaseName')
        new_instance_name = dictionary.get('newInstanceName')
        overwrite_policy = dictionary.get('overwritePolicy')
        restore_time_secs = dictionary.get('restoreTimeSecs')
        target_data_files_directory = dictionary.get('targetDataFilesDirectory')
        target_log_files_directory = dictionary.get('targetLogFilesDirectory')
        target_secondary_data_files_directory_list = None
        if dictionary.get('targetSecondaryDataFilesDirectoryList') != None:
            target_secondary_data_files_directory_list = list()
            for structure in dictionary.get('targetSecondaryDataFilesDirectoryList'):
                target_secondary_data_files_directory_list.append(cohesity_management_sdk.models.filename_pattern_to_directory.FilenamePatternToDirectory.from_dictionary(structure))
        with_clause = dictionary.get('withClause')

        # Return an object of this model
        return cls(
            capture_tail_logs,
            is_auto_sync_enabled,
            keep_cdc,
            keep_offline,
            new_database_name,
            new_instance_name,
            overwrite_policy,
            restore_time_secs,
            target_data_files_directory,
            target_log_files_directory,
            target_secondary_data_files_directory_list,
            with_clause
)