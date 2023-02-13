# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SqlBackupJobParams(object):

    """Implementation of the 'SqlBackupJobParams' model.

    Message to capture additional backup job params specific to SQL.

    Attributes:
        aag_backup_preference_type (int): Preference type for backing up
            databases that are part of an AAG. Only applicable if
            'use_aag_preferences_from_sql_server' is set to false.
        backup_database_volumes_only (bool): If set to true, only the volumes
            associated with databases should be backed up. The user cannot
            select additional volumes at host level for backup.  If set to
            false, all the volumes on the host machine will be backed up. In
            this case, the user can further select the exact set of volumes
            using host level params.  Note that the volumes associated with
            selected databases will always be included in the backup.
        backup_system_dbs (bool): Set to true if system databases should be
            backed up.
        continue_after_error (bool): Whether backup should continue after
            encountering a page checksum error.
        enable_checksum (bool): Whether backup checksums are enabled.
        enable_incremental_backup_after_restart (bool): If this is set to
            true, then incremental backup will be performed after the server
            restarts, otherwise a full-backup will be done.
        full_backup_type (int): The type of SQL full backup to be used for
            this job.
        is_copy_only_full (bool): Whether full backups should be copy-only.
        is_copy_only_log (bool): Whether log backups should be copy-only.
        num_dbs_per_batch (int): The number of databases to be backed up per
            batch. This is only applicable for file based sql backup. If this
            is not specified, we use the value specified in
            magneto_vss_sql_app_file_batch_size gflag.
        num_streams (int): The number of streams to be used in native sql
            backup command. This is only applicable for native sql backup. If
            this is not specified, we use the value specified in
            magneto_sql_num_streams_for_each_db_backup gflag.
        use_aag_preferences_from_sql_server (bool): Set to true if we should
            use AAG preferences specified at the SQL server host.
        user_db_preference_type (int): Preference type for backing up user
            databases on the host.
        with_clause (string): 'with_clause' contains 'with clause' to be used
            in native sql backup command. This is only applicable for native
            sql backup. Here user can specify multiple backup options.
            Example: "WITH BUFFERCOUNT = 575, MAXTRANSFERSIZE = 2097152". If
            this is not specified, we use the value specified in
            magneto_sql_native_backup_with_clause gflag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aag_backup_preference_type":'aagBackupPreferenceType',
        "backup_database_volumes_only":'backupDatabaseVolumesOnly',
        "backup_system_dbs":'backupSystemDbs',
        "continue_after_error":'continueAfterError',
        "enable_checksum":'enableChecksum',
        "enable_incremental_backup_after_restart":'enableIncrementalBackupAfterRestart',
        "full_backup_type":'fullBackupType',
        "is_copy_only_full":'isCopyOnlyFull',
        "is_copy_only_log":'isCopyOnlyLog',
        "num_dbs_per_batch":'numDbsPerBatch',
        "num_streams":'numStreams',
        "use_aag_preferences_from_sql_server":'useAagPreferencesFromSqlServer',
        "user_db_preference_type":'userDbPreferenceType',
        "with_clause":'withClause'
    }

    def __init__(self,
                 aag_backup_preference_type=None,
                 backup_database_volumes_only=None,
                 backup_system_dbs=None,
                 continue_after_error=None,
                 enable_checksum=None,
                 enable_incremental_backup_after_restart=None,
                 full_backup_type=None,
                 is_copy_only_full=None,
                 is_copy_only_log=None,
                 num_dbs_per_batch=None,
                 num_streams=None,
                 use_aag_preferences_from_sql_server=None,
                 user_db_preference_type=None,
                 with_clause=None):
        """Constructor for the SqlBackupJobParams class"""

        # Initialize members of the class
        self.aag_backup_preference_type = aag_backup_preference_type
        self.backup_database_volumes_only = backup_database_volumes_only
        self.backup_system_dbs = backup_system_dbs
        self.continue_after_error = continue_after_error
        self.enable_checksum = enable_checksum
        self.enable_incremental_backup_after_restart = enable_incremental_backup_after_restart
        self.full_backup_type = full_backup_type
        self.is_copy_only_full = is_copy_only_full
        self.is_copy_only_log = is_copy_only_log
        self.num_dbs_per_batch = num_dbs_per_batch
        self.num_streams = num_streams
        self.use_aag_preferences_from_sql_server = use_aag_preferences_from_sql_server
        self.user_db_preference_type = user_db_preference_type
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
        aag_backup_preference_type = dictionary.get('aagBackupPreferenceType')
        backup_database_volumes_only = dictionary.get('backupDatabaseVolumesOnly')
        backup_system_dbs = dictionary.get('backupSystemDbs')
        continue_after_error = dictionary.get('continueAfterError')
        enable_checksum = dictionary.get('enableChecksum')
        enable_incremental_backup_after_restart = dictionary.get('enableIncrementalBackupAfterRestart')
        full_backup_type = dictionary.get('fullBackupType')
        is_copy_only_full = dictionary.get('isCopyOnlyFull')
        is_copy_only_log = dictionary.get('isCopyOnlyLog')
        num_dbs_per_batch = dictionary.get('numDbsPerBatch')
        num_streams = dictionary.get('numStreams')
        use_aag_preferences_from_sql_server = dictionary.get('useAagPreferencesFromSqlServer')
        user_db_preference_type = dictionary.get('userDbPreferenceType')
        with_clause = dictionary.get('withClause')

        # Return an object of this model
        return cls(aag_backup_preference_type,
                   backup_database_volumes_only,
                   backup_system_dbs,
                   continue_after_error,
                   enable_checksum,
                   enable_incremental_backup_after_restart,
                   full_backup_type,
                   is_copy_only_full,
                   is_copy_only_log,
                   num_dbs_per_batch,
                   num_streams,
                   use_aag_preferences_from_sql_server,
                   user_db_preference_type,
                   with_clause)


