# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.oracle_db_channel_info_host_info

class OracleDBChannelInfo(object):

    """Implementation of the 'OracleDBChannelInfo' model.

    Note: The name of this proto message is out-dated. This proto can
    represent
    more than just the database channel information. It should be renamed
    in the future.

    Attributes:
        archivelog_keep_days (int): Archived log deletion policy for this
            unique Oracle database. 1: keep archived log forever 0: delete
            archived log immediately n>0: delete archived log after n days
        credentials (Credentials): The credentials to be used for this
            database.
        db_unique_name (string): The unique name of the database.
        db_uuid (string): Database id, internal field, is filled by magneto
            master based on corresponding app entity id.
        enable_dg_primary_backup (bool): If set to false, and if the DG database
            role is primary, we will not allow the backup of that database.
        host_info_vec (list of OracleDBChannelInfoHostInfo): Vector of Oracle
            hosts from which we are allowed to take the backup/restore. In
            case of RAC database it may be more than one.
        max_num_host (int): Maximum number of hosts from which we are allowed
            to take backup/restore parallely. This will be less than or equal
            to host_info_vec_size. If this is less than host_info_vec_size we
            will choose max_num_host from host_info_vec and take
            backup/restore from this number of host.
        num_channels (int): The default number of channels to use per host per
            db. This value is used on all hosts unless
            host_info_vec.num_channels is specified for that host. Default
            value for num_channels will be calculated as minimum number of
            nodes in cohesity cluster, and 2 * number of cpu on Oracle host.
            Preference order for number of channels per host for given db is:
            1. If user has specified host_info_vec.num_channels for host we
            will use that. 2. If user has not specified
            host_info_vec.num_channels but specified num_channels we will use
            this. 3. If user has neither specified host_info_vec.num_channels
            nor num_channels we will calculate default channels with above
            formula.
        rman_backup_type (int): Type of Oracle RMAN backup rquested (i.e
            ImageCopy, BackupSets).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archivelog_keep_days":'archivelogKeepDays',
        "credentials":'credentials',
        "db_unique_name":'dbUniqueName',
        "db_uuid":'dbUuid',
        "enable_dg_primary_backup":'enableDgPrimaryBackup',
        "host_info_vec":'hostInfoVec',
        "max_num_host":'maxNumHost',
        "num_channels":'numChannels',
        "rman_backup_type":'rmanBackupType'
    }

    def __init__(self,
                 archivelog_keep_days=None,
                 credentials=None,
                 db_unique_name=None,
                 db_uuid=None,
                 enable_dg_primary_backup=None,
                 host_info_vec=None,
                 max_num_host=None,
                 num_channels=None,
                 rman_backup_type=None):
        """Constructor for the OracleDBChannelInfo class"""

        # Initialize members of the class
        self.archivelog_keep_days = archivelog_keep_days
        self.credentials = credentials
        self.db_unique_name = db_unique_name
        self.db_uuid = db_uuid
        self.enable_dg_primary_backup = enable_dg_primary_backup
        self.host_info_vec = host_info_vec
        self.max_num_host = max_num_host
        self.num_channels = num_channels
        self.rman_backup_type = rman_backup_type


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
        archivelog_keep_days = dictionary.get('archivelogKeepDays')
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        db_unique_name = dictionary.get('dbUniqueName')
        db_uuid = dictionary.get('dbUuid')
        enable_dg_primary_backup = dictionary.get('enableDgPrimaryBackup')
        host_info_vec = None
        if dictionary.get('hostInfoVec') != None:
            host_info_vec = list()
            for structure in dictionary.get('hostInfoVec'):
                host_info_vec.append(cohesity_management_sdk.models.oracle_db_channel_info_host_info.OracleDBChannelInfoHostInfo.from_dictionary(structure))
        max_num_host = dictionary.get('maxNumHost')
        num_channels = dictionary.get('numChannels')
        rman_backup_type = dictionary.get('rmanBackupType')

        # Return an object of this model
        return cls(archivelog_keep_days,
                   credentials,
                   db_unique_name,
                   db_uuid,
                   enable_dg_primary_backup,
                   host_info_vec,
                   max_num_host,
                   num_channels,
                   rman_backup_type)


