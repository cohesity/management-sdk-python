# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_host
import cohesity_management_sdk.models.oracle_container_database_info
import cohesity_management_sdk.models.oracle_data_guard_info

class OracleProtectionSource(object):

    """Implementation of the 'OracleProtectionSource' model.

    Specifies an Object representing one Oracle database.

    Attributes:
        archive_log_enabled (bool): Specifies whether the database is running
            in ARCHIVELOG mode. It enables the redo of log files into archived
            redo log files.
        bct_enabled (bool): Specifies whether the Block Change Tracking is
            enabled. BCT improves the performance of incremental backups by
            recording changed blocks into the block change tracking file. RMAN
            then uses this file to identify changed blocks to be backed up.
        container_database_info (OracleContainerDatabaseInfo): Specifies the
            Container Database Information including the Pluggable databases
            within the container.
        data_guard_info (OracleDataGuardInfo): Specifies the Data Gurad
            configuration information for the current DB entity.
        database_unique_name (string): Specifies the unique name of the Oracle
            entity.
        db_type (DbTypeEnum): Specifies the type of the database in Oracle
            Protection Source. 'kRACDatabase' indicates the database is a RAC
            DB. 'kSingleInstance' indicates that the databse is single
            instance.
        domain (string): Specifies the Oracle DB Domain.
        fra_size (long|int): Specifies Flash/Fast Recovery area size for the
            current DB entity.
        hosts (list of OracleHost): Specifies the list of hosts for the
            current DB entity.
        name (string): Specifies the instance name of the Oracle entity.
        owner_id (long|int): Specifies the entity id of the owner entity (such
            as a VM). This is only set if type is kDatabase.
        sga_target_size (string): Specifies System Global Area size for the
            current DB entity. A system global area (SGA) is a group of shared
            memory structures that contain data and control information for
            one Oracle database.
        shared_pool_size (string): Specifies Shared Pool Size for the current
            DB entity.
        size (long|int): Specifies database size.
        tde_encrypted_ts_count (int|long): Specifies the number of TDE
            encrypted tablespaces found in the database.
        temp_files_count (long|int): Specifies number of temporary files for
            the current DB entity.
        mtype (TypeOracleProtectionSourceEnum): Specifies the type of the
            managed Object in Oracle Protection Source. 'kRACRootContainer'
            indicates the entity is a root container to an Oracle Real
            Application clusters(Oracle RAC). 'kRootContainer' indicates the
            entity is a root container to an Oracle standalone server. 'kHost'
            indicates the entity is an Oracle host. 'kDatabase' indicates the
            entity is an Oracle Database. 'kTableSpace' indicates the entity
            is an Oracle table space. 'kTable' indicates the entity is an
            Oracle table.
        uuid (string): Specifies the UUID for the Oracle entity.
        version (string): Specifies the Oracle database instance version.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archive_log_enabled":'archiveLogEnabled',
        "bct_enabled":'bctEnabled',
        "container_database_info":'containerDatabaseInfo',
        "data_guard_info":'dataGuardInfo',
        "database_unique_name":'databaseUniqueName',
        "db_type":'dbType',
        "domain":'domain',
        "fra_size":'fraSize',
        "hosts":'hosts',
        "name":'name',
        "owner_id":'ownerId',
        "sga_target_size":'sgaTargetSize',
        "shared_pool_size":'sharedPoolSize',
        "size":'size',
        "tde_encrypted_ts_count":'tdeEncryptedTsCount',
        "temp_files_count":'tempFilesCount',
        "mtype":'type',
        "uuid":'uuid',
        "version":'version'
    }

    def __init__(self,
                 archive_log_enabled=None,
                 bct_enabled=None,
                 container_database_info=None,
                 data_guard_info=None,
                 database_unique_name=None,
                 db_type=None,
                 domain=None,
                 fra_size=None,
                 hosts=None,
                 name=None,
                 owner_id=None,
                 sga_target_size=None,
                 shared_pool_size=None,
                 size=None,
                 tde_encrypted_ts_count=None,
                 temp_files_count=None,
                 mtype=None,
                 uuid=None,
                 version=None):
        """Constructor for the OracleProtectionSource class"""

        # Initialize members of the class
        self.archive_log_enabled = archive_log_enabled
        self.bct_enabled = bct_enabled
        self.container_database_info = container_database_info
        self.data_guard_info = data_guard_info
        self.database_unique_name = database_unique_name
        self.db_type = db_type
        self.domain = domain
        self.fra_size = fra_size
        self.hosts = hosts
        self.name = name
        self.owner_id = owner_id
        self.sga_target_size = sga_target_size
        self.shared_pool_size = shared_pool_size
        self.size = size
        self.tde_encrypted_ts_count = tde_encrypted_ts_count
        self.temp_files_count = temp_files_count
        self.mtype = mtype
        self.uuid = uuid
        self.version = version


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
        archive_log_enabled = dictionary.get('archiveLogEnabled')
        bct_enabled = dictionary.get('bctEnabled')
        container_database_info = cohesity_management_sdk.models.oracle_container_database_info.OracleContainerDatabaseInfo.from_dictionary(dictionary.get('containerDatabaseInfo')) if dictionary.get('containerDatabaseInfo') else None
        data_guard_info = cohesity_management_sdk.models.oracle_data_guard_info.OracleDataGuardInfo.from_dictionary(dictionary.get('dataGuardInfo')) if dictionary.get('dataGuardInfo') else None
        database_unique_name = dictionary.get('databaseUniqueName')
        db_type = dictionary.get('dbType')
        domain = dictionary.get('domain')
        fra_size = dictionary.get('fraSize')
        hosts = None
        if dictionary.get('hosts') != None:
            hosts = list()
            for structure in dictionary.get('hosts'):
                hosts.append(cohesity_management_sdk.models.oracle_host.OracleHost.from_dictionary(structure))
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        sga_target_size = dictionary.get('sgaTargetSize')
        shared_pool_size = dictionary.get('sharedPoolSize')
        tde_encrypted_ts_count = dictionary.get('tdeEncryptedTsCount')
        size = dictionary.get('size')
        temp_files_count = dictionary.get('tempFilesCount')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(archive_log_enabled,
                   bct_enabled,
                   container_database_info,
                   data_guard_info,
                   database_unique_name,
                   db_type,
                   domain,
                   fra_size,
                   hosts,
                   name,
                   owner_id,
                   sga_target_size,
                   shared_pool_size,
                   size,
                   tde_encrypted_ts_count,
                   temp_files_count,
                   mtype,
                   uuid,
                   version)


