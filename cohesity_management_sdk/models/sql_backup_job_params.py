# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


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
        full_backup_type (int): The type of SQL full backup to be used for
            this job.
        is_copy_only_full (bool): Whether full backups should be copy-only.
        use_aag_preferences_from_sql_server (bool): Set to true if we should
            use AAG preferences specified at the SQL server host.
        user_db_preference_type (int): Preference type for backing up user
            databases on the host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aag_backup_preference_type":'aagBackupPreferenceType',
        "backup_database_volumes_only":'backupDatabaseVolumesOnly',
        "backup_system_dbs":'backupSystemDbs',
        "full_backup_type":'fullBackupType',
        "is_copy_only_full":'isCopyOnlyFull',
        "use_aag_preferences_from_sql_server":'useAagPreferencesFromSqlServer',
        "user_db_preference_type":'userDbPreferenceType'
    }

    def __init__(self,
                 aag_backup_preference_type=None,
                 backup_database_volumes_only=None,
                 backup_system_dbs=None,
                 full_backup_type=None,
                 is_copy_only_full=None,
                 use_aag_preferences_from_sql_server=None,
                 user_db_preference_type=None):
        """Constructor for the SqlBackupJobParams class"""

        # Initialize members of the class
        self.aag_backup_preference_type = aag_backup_preference_type
        self.backup_database_volumes_only = backup_database_volumes_only
        self.backup_system_dbs = backup_system_dbs
        self.full_backup_type = full_backup_type
        self.is_copy_only_full = is_copy_only_full
        self.use_aag_preferences_from_sql_server = use_aag_preferences_from_sql_server
        self.user_db_preference_type = user_db_preference_type


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
        full_backup_type = dictionary.get('fullBackupType')
        is_copy_only_full = dictionary.get('isCopyOnlyFull')
        use_aag_preferences_from_sql_server = dictionary.get('useAagPreferencesFromSqlServer')
        user_db_preference_type = dictionary.get('userDbPreferenceType')

        # Return an object of this model
        return cls(aag_backup_preference_type,
                   backup_database_volumes_only,
                   backup_system_dbs,
                   full_backup_type,
                   is_copy_only_full,
                   use_aag_preferences_from_sql_server,
                   user_db_preference_type)


