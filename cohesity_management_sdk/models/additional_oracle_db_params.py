# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_db_channel_info

class AdditionalOracleDBParams(object):

    """Implementation of the 'AdditionalOracleDBParams' model.

    TODO: type model description here.

    Attributes:
        app_entity_id (long|int): Database app id.
        db_info_channel_vec (list of OracleDBChannelInfo): The following proto
            message should be renamed to a more general message to represent
            parameters pertaining to a single unique Oracle database.
            Uniqueness of an Oracle database should be strictly determined by
            its database unique name. i.e. all backup parameters needed for a
            unique Oracle database should be expressed in the following proto.
            It is a vector for future support of backing up Data Guard
            sources. We may or may not need this to be vector to support Data
            Guard sources. For now, the size of this vector is always 1. When
            we rename this proto in the future, if we determine there is no
            need to use a vector for Data Guard support, we can choose to
            remove 'repeated'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_entity_id":'appEntityId',
        "db_info_channel_vec":'dbInfoChannelVec'
    }

    def __init__(self,
                 app_entity_id=None,
                 db_info_channel_vec=None):
        """Constructor for the AdditionalOracleDBParams class"""

        # Initialize members of the class
        self.app_entity_id = app_entity_id
        self.db_info_channel_vec = db_info_channel_vec


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
        app_entity_id = dictionary.get('appEntityId')
        db_info_channel_vec = None
        if dictionary.get('dbInfoChannelVec') != None:
            db_info_channel_vec = list()
            for structure in dictionary.get('dbInfoChannelVec'):
                db_info_channel_vec.append(cohesity_management_sdk.models.oracle_db_channel_info.OracleDBChannelInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(app_entity_id,
                   db_info_channel_vec)


