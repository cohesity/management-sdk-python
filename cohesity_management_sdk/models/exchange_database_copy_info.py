# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExchangeDatabaseCopyInfo(object):

    """Implementation of the 'ExchangeDatabaseCopyInfo' model.

    Specifies the information about the copy of the Exchange Database on
    particular Exchange Application Server that is part of DAG.

    Attributes:
        activation_preference_number (int): Specifies the activation
            preference number assigned for this database copy.
        app_server_id (int): Specifies the entity id of the Exchange
            Application Server which has this database copy.
        backup_supported (bool): Specifies if backup is supported for the
            Exchange database copy.
        backup_unsupported_reasons (list of string): Specifies any reason(s)
            for Exchange database backup not supported.
        copy_guid (string): Specifies the Guid of the Exchange Database Copy.
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
        fqdn (string): Specifies the fully qualified domain name of the
            Exchange Server on which the database copy is hosted.
        is_active_copy (bool): Specifies if the Exchange database copy present
            on the Exchange Application server is active or passive.
        name (string): Specifes the name of the Exchange Database.
        owner_id (int): Specifies the owner entity id of the Exchange
            Application Server which has this database copy.
        server_name (string): Specifies the display name of the Exchange
            Application Server on which the database copy is hosted.
        utc_offset_min (int): Specifies UTC time offset of database creation
            time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "activation_preference_number":'activationPreferenceNumber',
        "app_server_id":'appServerId',
        "backup_supported":'backupSupported',
        "backup_unsupported_reasons":'backupUnsupportedReasons',
        "copy_guid":'copyGuid',
        "created_time_msecs":'createdTimeMsecs',
        "database_state":'databaseState',
        "db_size_bytes":'dbSizeBytes',
        "dbguid":'dbguid',
        "fqdn":'fqdn',
        "is_active_copy":'isActiveCopy',
        "name":'name',
        "owner_id":'ownerId',
        "server_name":'serverName',
        "utc_offset_min":'utcOffsetMin'
    }

    def __init__(self,
                 activation_preference_number=None,
                 app_server_id=None,
                 backup_supported=None,
                 backup_unsupported_reasons=None,
                 copy_guid=None,
                 created_time_msecs=None,
                 database_state=None,
                 db_size_bytes=None,
                 dbguid=None,
                 fqdn=None,
                 is_active_copy=None,
                 name=None,
                 owner_id=None,
                 server_name=None,
                 utc_offset_min=None):
        """Constructor for the ExchangeDatabaseCopyInfo class"""

        # Initialize members of the class
        self.activation_preference_number = activation_preference_number
        self.app_server_id = app_server_id
        self.backup_supported = backup_supported
        self.backup_unsupported_reasons = backup_unsupported_reasons
        self.copy_guid = copy_guid
        self.created_time_msecs = created_time_msecs
        self.database_state = database_state
        self.db_size_bytes = db_size_bytes
        self.dbguid = dbguid
        self.fqdn = fqdn
        self.is_active_copy = is_active_copy
        self.name = name
        self.owner_id = owner_id
        self.server_name = server_name
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
        activation_preference_number = dictionary.get('activationPreferenceNumber')
        app_server_id = dictionary.get('appServerId')
        backup_supported = dictionary.get('backupSupported')
        backup_unsupported_reasons = dictionary.get('backupUnsupportedReasons')
        copy_guid = dictionary.get('copyGuid')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        database_state = dictionary.get('databaseState')
        db_size_bytes = dictionary.get('dbSizeBytes')
        dbguid = dictionary.get('dbguid')
        fqdn = dictionary.get('fqdn')
        is_active_copy = dictionary.get('isActiveCopy')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        server_name = dictionary.get('serverName')
        utc_offset_min = dictionary.get('utcOffsetMin')

        # Return an object of this model
        return cls(activation_preference_number,
                   app_server_id,
                   backup_supported,
                   backup_unsupported_reasons,
                   copy_guid,
                   created_time_msecs,
                   database_state,
                   db_size_bytes,
                   dbguid,
                   fqdn,
                   is_active_copy,
                   name,
                   owner_id,
                   server_name,
                   utc_offset_min)


