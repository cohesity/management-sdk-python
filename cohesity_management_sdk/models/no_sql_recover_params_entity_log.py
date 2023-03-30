# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.no_sql_log_data


class NoSqlRecoverParams_EntityLog(object):

    """Implementation of the 'NoSqlRecoverParams_EntityLog' model.

    TODO: type description here.


    Attributes:

        entity (EntityProto): Entity for a leaf level entity.
        log_data_vec (list of NoSqlLogData): List of log file and time range to
            applied for hydrated backup or for recovery. Each data event has a
            path of log file and the valid sequencer range within that log
            file.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity":'entity',
        "log_data_vec":'logDataVec',
    }
    def __init__(self,
                 entity=None,
                 log_data_vec=None,
            ):

        """Constructor for the NoSqlRecoverParams_EntityLog class"""

        # Initialize members of the class
        self.entity = entity
        self.log_data_vec = log_data_vec

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
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        log_data_vec = None
        if dictionary.get('logDataVec') != None:
            log_data_vec = list()
            for structure in dictionary.get('logDataVec'):
                log_data_vec.append(cohesity_management_sdk.models.no_sql_log_data.NoSqlLogData.from_dictionary(structure))

        # Return an object of this model
        return cls(
            entity,
            log_data_vec
)