# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_db_config_redo_log_group_conf
import cohesity_management_sdk.models.oracle_db_config_pfile_parameter_map_entry

class OracleDBConfig(object):

    """Implementation of the 'OracleDBConfig' model.

    This proto captures the oracle database configuration for alternate DB
    restore.

    Attributes:
        audit_log_dest (string): Audit log destination.
        bct_file_path (string): BCT file path.
        control_file_path_vec (list of string): List of paths where the
            control file needs to be multiplexed.
        db_config_file_path (string): Path to the file on oracle host which
            decides the configuration of restored DB.
        diag_dest (string): Diag destination.
        enable_archive_log_mode (bool): If set to false, archive log mode is
            disabled.
        fra_dest (string): FRA path.
        fra_size_mb (int): FRA Size in MBs.
        num_tempfiles (int): How many tempfiles to use for the recovered
            database.
        pfile_parameter_map (list of OracleDBConfig_PfileParameterMapEntry):
            Map of pfile parameters to its values.
        redo_log_conf (OracleDBConfigRedoLogGroupConf): GROUP1 :
            {DST1/CH1.log, DST2/CH1.log} GROUP2 : {DST1/CH2.log, DST2/CH2.log}
            GROUP3 : {DST1/CH3.log, DST2/CH3.log}
        sga_target_size (string): SGA_TARGET_SIZE size [ Default value same as
            Source DB ].
        shared_pool_size (string): Shared pool size [ Default value same as
            Source DB ].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audit_log_dest":'auditLogDest',
        "bct_file_path":'bctFilePath',
        "control_file_path_vec":'controlFilePathVec',
        "db_config_file_path":'dbConfigFilePath',
        "diag_dest":'diagDest',
        "enable_archive_log_mode":'enableArchiveLogMode',
        "fra_dest":'fraDest',
        "fra_size_mb":'fraSizeMb',
        "num_tempfiles":'numTempfiles',
        "pfile_parameter_map":'pfileParameterMap',
        "redo_log_conf":'redoLogConf',
        "sga_target_size":'sgaTargetSize',
        "shared_pool_size":'sharedPoolSize'
    }

    def __init__(self,
                 audit_log_dest=None,
                 bct_file_path=None,
                 control_file_path_vec=None,
                 db_config_file_path=None,
                 diag_dest=None,
                 enable_archive_log_mode=None,
                 fra_dest=None,
                 fra_size_mb=None,
                 num_tempfiles=None,
                 pfile_parameter_map=None,
                 redo_log_conf=None,
                 sga_target_size=None,
                 shared_pool_size=None):
        """Constructor for the OracleDBConfig class"""

        # Initialize members of the class
        self.audit_log_dest = audit_log_dest
        self.bct_file_path = bct_file_path
        self.control_file_path_vec = control_file_path_vec
        self.db_config_file_path = db_config_file_path
        self.diag_dest = diag_dest
        self.enable_archive_log_mode = enable_archive_log_mode
        self.fra_dest = fra_dest
        self.fra_size_mb = fra_size_mb
        self.num_tempfiles = num_tempfiles
        self.pfile_parameter_map = pfile_parameter_map
        self.redo_log_conf = redo_log_conf
        self.sga_target_size = sga_target_size
        self.shared_pool_size = shared_pool_size


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
        audit_log_dest = dictionary.get('auditLogDest')
        bct_file_path = dictionary.get('bctFilePath')
        control_file_path_vec = dictionary.get('controlFilePathVec')
        db_config_file_path = dictionary.get('dbConfigFilePath')
        diag_dest = dictionary.get('diagDest')
        enable_archive_log_mode = dictionary.get('enableArchiveLogMode')
        fra_dest = dictionary.get('fraDest')
        fra_size_mb = dictionary.get('fraSizeMb')
        num_tempfiles = dictionary.get('numTempfiles')
        pfile_parameter_map = None
        if dictionary.get('pfileParameterMap') != None:
            pfile_parameter_map = list()
            for structure in dictionary.get('pfileParameterMap'):
                pfile_parameter_map.append(cohesity_management_sdk.models.oracle_db_config_pfile_parameter_map_entry.OracleDBConfig_PfileParameterMapEntry.from_dictionary(structure))
        redo_log_conf = cohesity_management_sdk.models.oracle_db_config_redo_log_group_conf.OracleDBConfigRedoLogGroupConf.from_dictionary(dictionary.get('redoLogConf')) if dictionary.get('redoLogConf') else None
        sga_target_size = dictionary.get('sgaTargetSize')
        shared_pool_size = dictionary.get('sharedPoolSize')

        # Return an object of this model
        return cls(audit_log_dest,
                   bct_file_path,
                   control_file_path_vec,
                   db_config_file_path,
                   diag_dest,
                   enable_archive_log_mode,
                   fra_dest,
                   fra_size_mb,
                   num_tempfiles,
                   pfile_parameter_map,
                   redo_log_conf,
                   sga_target_size,
                   shared_pool_size)


