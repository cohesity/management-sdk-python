# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.oracle_db_channel_info_host_info

class OracleDBChannelInfo(object):

    """Implementation of the 'OracleDBChannelInfo' model.

    Message to capture channel information for Oracle database backup or
    restore information.

    Attributes:
        db_unique_name (string): The unique name of the database.
        db_uuid (string): Database id, internal field, is filled by magneto
            master based on corresponding app entity id.
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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "db_unique_name":'dbUniqueName',
        "db_uuid":'dbUuid',
        "host_info_vec":'hostInfoVec',
        "max_num_host":'maxNumHost',
        "num_channels":'numChannels'
    }

    def __init__(self,
                 db_unique_name=None,
                 db_uuid=None,
                 host_info_vec=None,
                 max_num_host=None,
                 num_channels=None):
        """Constructor for the OracleDBChannelInfo class"""

        # Initialize members of the class
        self.db_unique_name = db_unique_name
        self.db_uuid = db_uuid
        self.host_info_vec = host_info_vec
        self.max_num_host = max_num_host
        self.num_channels = num_channels


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
        db_unique_name = dictionary.get('dbUniqueName')
        db_uuid = dictionary.get('dbUuid')
        host_info_vec = None
        if dictionary.get('hostInfoVec') != None:
            host_info_vec = list()
            for structure in dictionary.get('hostInfoVec'):
                host_info_vec.append(cohesity_management_sdk.models.oracle_db_channel_info_host_info.OracleDBChannelInfoHostInfo.from_dictionary(structure))
        max_num_host = dictionary.get('maxNumHost')
        num_channels = dictionary.get('numChannels')

        # Return an object of this model
        return cls(db_unique_name,
                   db_uuid,
                   host_info_vec,
                   max_num_host,
                   num_channels)


