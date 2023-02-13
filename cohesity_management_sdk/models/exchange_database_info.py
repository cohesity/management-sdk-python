# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExchangeDatabaseInfo(object):

    """Implementation of the 'ExchangeDatabaseInfo' model.

    Specifies the information about the Exchange Database.

    Attributes:
        app_server_id (int): Specifies the entity id of the Exchange
            Application Server which has this database copy.
        backup_supported (bool): Specifies if backup is supported for the
            Exchange database copy.
        backup_unsupported_reasons (list of string): Specifies any reason(s)
            for Exchange database backup not supported.
        created_time_msecs (int): Specifies the time when the database is
            created in Unix epoch time in milliseconds.
        database_state (DatabaseStateEnum): Specifies the state of the
            Exchange database copy.
            Specifies the state of Exchange Database Copy.

            'kUnknown' indicates the status is not known.
            'kMounted' indicates the exchange database copy is mounted and
            healthy.
            'kError' indicates  the  exchange  database  copy  is unmounted or
            partially mounted or is in error state.
        db_size_bytes (int): Specifies the size of the Exchange database copy
            in bytes.
        dbguid (string): Specifies the guid of the Exchange Database.
        name (string): Specifes the name of the Exchange Database.
        owner_id (int): Specifies the owner entity id of the Exchange
            Application Server which has this database copy.
        utc_offset_min (int): Specifies UTC time offset of database creation
            time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_server_id":'appServerId',
        "backup_supported":'backupSupported',
        "backup_unsupported_reasons":'backupUnsupportedReasons',
        "created_time_msecs":'createdTimeMsecs',
        "database_state":'databaseState',
        "db_size_bytes":'dbSizeBytes',
        "dbguid":'dbguid',
        "name":'name',
        "owner_id":'ownerId',
        "utc_offset_min":'utcOffsetMin'
    }

    def __init__(self,
                 app_server_id=None,
                 backup_supported=None,
                 backup_unsupported_reasons=None,
                 created_time_msecs=None,
                 database_state=None,
                 db_size_bytes=None,
                 dbguid=None,
                 name=None,
                 owner_id=None,
                 utc_offset_min=None):
        """Constructor for the ExchangeDatabaseInfo class"""

        # Initialize members of the class
        self.app_server_id = app_server_id
        self.backup_supported = backup_supported
        self.backup_unsupported_reasons = backup_unsupported_reasons
        self.created_time_msecs = created_time_msecs
        self.db_size_bytes = db_size_bytes
        self.dbguid = dbguid
        self.name = name
        self.owner_id = owner_id
        self.utc_offset_min = utc_offset_min


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
        app_server_id = dictionary.get('appServerId')
        backup_supported = dictionary.get('backupSupported')
        backup_unsupported_reasons = dictionary.get('backupUnsupportedReasons')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        database_state = dictionary.get('databaseState')
        db_size_bytes = dictionary.get('dbSizeBytes')
        dbguid = dictionary.get('dbguid')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        utc_offset_min = dictionary.get('utcOffsetMin')

        # Return an object of this model
        return cls(app_server_id,
                   backup_supported,
                   backup_unsupported_reasons,
                   created_time_msecs,
                   database_state,
                   db_size_bytes,
                   dbguid,
                   name,
                   owner_id,
                   utc_offset_min)


