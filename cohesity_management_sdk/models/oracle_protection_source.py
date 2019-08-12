# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.oracle_host

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
        db_type (DbTypeEnum): Specifies the type of the database in Oracle
            Protection Source. 'kRACDatabase' indicates the database is a RAC
            DB. 'kSingleInstance' indicates that the databse is single
            instance.
        fra_size (long|int): Specfies Flash/Fast Recovery area size for the
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
        "db_type":'dbType',
        "fra_size":'fraSize',
        "hosts":'hosts',
        "name":'name',
        "owner_id":'ownerId',
        "sga_target_size":'sgaTargetSize',
        "shared_pool_size":'sharedPoolSize',
        "size":'size',
        "temp_files_count":'tempFilesCount',
        "mtype":'type',
        "uuid":'uuid',
        "version":'version'
    }

    def __init__(self,
                 archive_log_enabled=None,
                 bct_enabled=None,
                 db_type=None,
                 fra_size=None,
                 hosts=None,
                 name=None,
                 owner_id=None,
                 sga_target_size=None,
                 shared_pool_size=None,
                 size=None,
                 temp_files_count=None,
                 mtype=None,
                 uuid=None,
                 version=None):
        """Constructor for the OracleProtectionSource class"""

        # Initialize members of the class
        self.archive_log_enabled = archive_log_enabled
        self.bct_enabled = bct_enabled
        self.db_type = db_type
        self.fra_size = fra_size
        self.hosts = hosts
        self.name = name
        self.owner_id = owner_id
        self.sga_target_size = sga_target_size
        self.shared_pool_size = shared_pool_size
        self.size = size
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
        db_type = dictionary.get('dbType')
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
        size = dictionary.get('size')
        temp_files_count = dictionary.get('tempFilesCount')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(archive_log_enabled,
                   bct_enabled,
                   db_type,
                   fra_size,
                   hosts,
                   name,
                   owner_id,
                   sga_target_size,
                   shared_pool_size,
                   size,
                   temp_files_count,
                   mtype,
                   uuid,
                   version)


