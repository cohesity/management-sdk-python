# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.oracle_database_node

class OracleDatabaseNodeChannel(object):

    """Implementation of the 'OracleDatabaseNodeChannel' model.

    Specifies node and channel info required for the backup and restore of
    a database.

    Attributes:
        archive_log_keep_days (int): Specifies the number of days archive log
            should be stored.
        database_node_list (list of OracleDatabaseNode): Array of nodes of a
            database.  Specifies the Node info from where we are allowed to
            take the backup/restore.
        database_unique_name (string): Specifies the unique Name of the
            database.
        database_uuid (string): Specifies the database unique id. This is an
            internal field and is filled by magneto master based on
            corresponding app entity id.
        default_channel_count (int): Specifies the default number of channels
            to use per node per database. The default number of channels to
            use per host per db. This value is used on all
            OracleDatabaseNode's unless databaseNodeList item's channelCount
            is specified for the node.
        max_node_count (int): Specifies the maximum number of nodes from which
            we are allowed to take backup/restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archive_log_keep_days":'archiveLogKeepDays',
        "database_node_list":'databaseNodeList',
        "database_unique_name":'databaseUniqueName',
        "database_uuid":'databaseUuid',
        "default_channel_count":'defaultChannelCount',
        "max_node_count":'maxNodeCount'
    }

    def __init__(self,
                 archive_log_keep_days=None,
                 database_node_list=None,
                 database_unique_name=None,
                 database_uuid=None,
                 default_channel_count=None,
                 max_node_count=None):
        """Constructor for the OracleDatabaseNodeChannel class"""

        # Initialize members of the class
        self.archive_log_keep_days = archive_log_keep_days
        self.database_node_list = database_node_list
        self.database_unique_name = database_unique_name
        self.database_uuid = database_uuid
        self.default_channel_count = default_channel_count
        self.max_node_count = max_node_count


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
        archive_log_keep_days = dictionary.get('archiveLogKeepDays')
        database_node_list = None
        if dictionary.get('databaseNodeList') != None:
            database_node_list = list()
            for structure in dictionary.get('databaseNodeList'):
                database_node_list.append(cohesity_management_sdk.models.oracle_database_node.OracleDatabaseNode.from_dictionary(structure))
        database_unique_name = dictionary.get('databaseUniqueName')
        database_uuid = dictionary.get('databaseUuid')
        default_channel_count = dictionary.get('defaultChannelCount')
        max_node_count = dictionary.get('maxNodeCount')

        # Return an object of this model
        return cls(archive_log_keep_days,
                   database_node_list,
                   database_unique_name,
                   database_uuid,
                   default_channel_count,
                   max_node_count)


