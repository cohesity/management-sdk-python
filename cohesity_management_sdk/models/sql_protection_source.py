# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.db_file_info
import cohesity_management_sdk.models.sql_source_id
import cohesity_management_sdk.models.sql_server_instance_version

class SqlProtectionSource(object):

    """Implementation of the 'SqlProtectionSource' model.

    Specifies an Object representing one SQL Server instance or database.

    Attributes:
        is_available_for_vss_backup (bool): Specifies whether the database is
            marked as available for backup according to the SQL Server VSS
            writer. This may be false if either the state of the databases is
            not online, or if the VSS writer is not online. This field is set
            only for type 'kDatabase'.
        created_timestamp (string): Specifies the time when the database was
            created. It is displayed in the timezone of the SQL server on
            which this database is running.
        database_name (string): Specifies the database name of the SQL
            Protection Source, if the type is database.
        db_aag_entity_id (long|int): Specifies the AAG entity id if the
            database is part of an AAG. This field is set only for type
            'kDatabase'.
        db_aag_name (string): Specifies the name of the AAG if the database is
            part of an AAG. This field is set only for type 'kDatabase'.
        db_compatibility_level (long|int): Specifies the versions of SQL
            server that the database is compatible with.
        db_file_groups (list of string): Specifies the information about the
            set of file groups for this db on the host. This is only set if
            the type is kDatabase.
        db_files (list of DbFileInfo): Specifies the last known information
            about the set of database files on the host. This field is set
            only for type 'kDatabase'.
        default_database_location (string):  Specifies the default path for
            data files for DBs in an instance
        default_log_location (string): Specifies the default path for log
            files for DBs in an instance
        db_owner_username (string): Specifies the name of the database owner.
        id (SqlSourceId): Specifies a unique id for a SQL Protection Source.
        name (string): Specifies the instance name of the SQL Protection
            Source
        owner_id (long|int): Specifies the id of the container VM for the SQL
            Protection Source.
        recovery_model (RecoveryModelEnum): Specifies the Recovery Model for
            the database in SQL environment. Only meaningful for the
            'kDatabase' SQL Protection Source. Specifies the Recovery Model
            set for the Microsoft SQL Server. 'kSimpleRecoveryModel' indicates
            the Simple SQL Recovery Model which does not utilize log backups.
            'kFullRecoveryModel' indicates the Full SQL Recovery Model which
            requires log backups and allows recovery to a single point in
            time. 'kBulkLoggedRecoveryModel' indicates the Bulk Logged SQL
            Recovery Model which requires log backups and allows
            high-performance bulk copy operations.
        sql_server_db_state (SqlServerDbStateEnum): The state of the database
            as returned by SQL Server. Indicates the state of the database.
            The values correspond to the 'state' field in the system table
            sys.databases. See https://goo.gl/P66XqM. 'kOnline' indicates that
            database is in online state. 'kRestoring' indicates that database
            is in restore state. 'kRecovering' indicates that database is in
            recovery state. 'kRecoveryPending' indicates that database
            recovery is in pending state. 'kSuspect' indicates that primary
            filegroup is suspect and may be damaged. 'kEmergency' indicates
            that manually forced emergency state. 'kOffline' indicates that
            database is in offline state. 'kCopying' indicates that database
            is in copying state. 'kOfflineSecondary' indicates that secondary
            database is in offline state.
        sql_server_instance_version (SQLServerInstanceVersion): Specifies the
            Server Instance Version.
        mtype (TypeSqlProtectionSourceEnum): Specifies the type of the managed
            Object in a SQL Protection Source. Examples of SQL Objects include
            'kInstance' and 'kDatabase'. 'kInstance' indicates that SQL server
            instance is being protected. 'kDatabase' indicates that SQL server
            database is being protected. 'kAAG' indicates that SQL AAG
            (AlwaysOn Availability Group) is being protected.
            'kAAGRootContainer' indicates that SQL AAG's root container is
            being protected. 'kRootContainer' indicates root container for SQL
            sources.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_available_for_vss_backup":'IsAvailableForVssBackup',
        "created_timestamp":'createdTimestamp',
        "database_name":'databaseName',
        "db_aag_entity_id":'dbAagEntityId',
        "db_aag_name":'dbAagName',
        "db_compatibility_level":'dbCompatibilityLevel',
        "db_file_groups":'dbFileGroups',
        "db_files":'dbFiles',
        "default_database_location":'defaultDatabaseLocation',
        "default_log_location":'defaultLogLocation',
        "db_owner_username":'dbOwnerUsername',
        "id":'id',
        "name":'name',
        "owner_id":'ownerId',
        "recovery_model":'recoveryModel',
        "sql_server_db_state":'sqlServerDbState',
        "sql_server_instance_version":'sqlServerInstanceVersion',
        "mtype":'type'
    }

    def __init__(self,
                 is_available_for_vss_backup=None,
                 created_timestamp=None,
                 database_name=None,
                 db_aag_entity_id=None,
                 db_aag_name=None,
                 db_compatibility_level=None,
                 db_file_groups=None,
                 db_files=None,
                 default_database_location=None,
                 default_log_location=None,
                 db_owner_username=None,
                 id=None,
                 name=None,
                 owner_id=None,
                 recovery_model=None,
                 sql_server_db_state=None,
                 sql_server_instance_version=None,
                 mtype=None):
        """Constructor for the SqlProtectionSource class"""

        # Initialize members of the class
        self.is_available_for_vss_backup = is_available_for_vss_backup
        self.created_timestamp = created_timestamp
        self.database_name = database_name
        self.db_aag_entity_id = db_aag_entity_id
        self.db_aag_name = db_aag_name
        self.db_compatibility_level = db_compatibility_level
        self.db_file_groups = db_file_groups
        self.db_files = db_files
        self.default_database_location = default_database_location
        self.default_log_location = default_log_location
        self.db_owner_username = db_owner_username
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.recovery_model = recovery_model
        self.sql_server_db_state = sql_server_db_state
        self.sql_server_instance_version = sql_server_instance_version
        self.mtype = mtype


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
        is_available_for_vss_backup = dictionary.get('IsAvailableForVssBackup')
        created_timestamp = dictionary.get('createdTimestamp')
        database_name = dictionary.get('databaseName')
        db_aag_entity_id = dictionary.get('dbAagEntityId')
        db_aag_name = dictionary.get('dbAagName')
        db_compatibility_level = dictionary.get('dbCompatibilityLevel')
        db_file_groups = dictionary.get('dbFileGroups')
        db_files = None
        if dictionary.get('dbFiles') != None:
            db_files = list()
            for structure in dictionary.get('dbFiles'):
                db_files.append(cohesity_management_sdk.models.db_file_info.DbFileInfo.from_dictionary(structure))
        default_database_location = dictionary.get('defaultDatabaseLocation')
        default_log_location = dictionary.get('defaultLogLocation')
        db_owner_username = dictionary.get('dbOwnerUsername')
        id = cohesity_management_sdk.models.sql_source_id.SqlSourceId.from_dictionary(dictionary.get('id')) if dictionary.get('id') else None
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        recovery_model = dictionary.get('recoveryModel')
        sql_server_db_state = dictionary.get('sqlServerDbState')
        sql_server_instance_version = cohesity_management_sdk.models.sql_server_instance_version.SQLServerInstanceVersion.from_dictionary(dictionary.get('sqlServerInstanceVersion')) if dictionary.get('sqlServerInstanceVersion') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(is_available_for_vss_backup,
                   created_timestamp,
                   database_name,
                   db_aag_entity_id,
                   db_aag_name,
                   db_compatibility_level,
                   db_file_groups,
                   db_files,
                   default_database_location,
                   default_log_location,
                   db_owner_username,
                   id,
                   name,
                   owner_id,
                   recovery_model,
                   sql_server_db_state,
                   sql_server_instance_version,
                   mtype)


