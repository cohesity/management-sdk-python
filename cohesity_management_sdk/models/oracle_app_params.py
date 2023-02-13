# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_database_node_channel

class OracleAppParams(object):

    """Implementation of the 'OracleAppParams' model.

    Specifies special settings applicable for a app entity i.e
    database/dataguard.

    Attributes:
        database_app_id (long|int): Specifies the source entity id of the
            selected app entity.
        node_channel_list (list of OracleDatabaseNodeChannel): Array of
            database node channel info.  Specifies the node channel info for
            all the databases of app entity. Length of this array will be 1
            for RAC and Standalone setups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_app_id":'databaseAppId',
        "node_channel_list":'nodeChannelList'
    }

    def __init__(self,
                 database_app_id=None,
                 node_channel_list=None):
        """Constructor for the OracleAppParams class"""

        # Initialize members of the class
        self.database_app_id = database_app_id
        self.node_channel_list = node_channel_list


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
        database_app_id = dictionary.get('databaseAppId')
        node_channel_list = None
        if dictionary.get('nodeChannelList') != None:
            node_channel_list = list()
            for structure in dictionary.get('nodeChannelList'):
                node_channel_list.append(cohesity_management_sdk.models.oracle_database_node_channel.OracleDatabaseNodeChannel.from_dictionary(structure))

        # Return an object of this model
        return cls(database_app_id,
                   node_channel_list)


