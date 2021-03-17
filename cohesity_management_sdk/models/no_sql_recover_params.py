# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.no_sql_restore_object
import cohesity_management_sdk.models.sequencer
import cohesity_management_sdk.models.no_sql_recover_params_entity_log

class NoSqlRecoverParams(object):

    """Implementation of the 'NoSqlRecoverParams' model.

    TODO: Type model description here.

    Attributes:
        end_seq_number (Sequencer): TODO: Type description here.
        entity_logs (list of NoSqlRecoverParams_EntityLog): List of leaf
            level entities with their corrosponding LogData.
        restore_objects (list of NoSqlRestoreObject): TODO: Type description
            here.
        start_seq_number (Sequencer): TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_seq_number":'endSequencer',
        "entity_logs":'entityLogs',
        "restore_objects":'restoreObjects',
        "start_seq_number":'startSequencer'
    }

    def __init__(self,
                 end_seq_number=None,
                 entity_logs=None,
                 restore_objects=None,
                 start_seq_number=None):
        """Constructor for the NoSqlRecoverParams class"""

        # Initialize members of the class
        self.end_seq_number = end_seq_number
        self.entity_logs = entity_logs
        self.restore_objects = restore_objects
        self.start_seq_number = start_seq_number


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
        end_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('endSequencer')) if dictionary.get('endSequencer') else None
        entity_logs = None
        if dictionary.get('entityLogs'):
            entity_logs = list()
            for structure in dictionary.get('entityLogs'):
                entity_logs.append(cohesity_management_sdk.models.no_sql_recover_params_entity_log.NoSqlRecoverParams_EntityLog.from_dictionary(structure))
        restore_objects = None
        if dictionary.get('restoreObjects') != None:
            restore_objects = list()
            for structure in dictionary.get('restoreObjects'):
                restore_objects.append(cohesity_management_sdk.models.no_sql_restore_object.NoSqlRestoreObject.from_dictionary(structure))
        start_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('startSequencer')) if dictionary.get('startSequencer') else None

        # Return an object of this model
        return cls(end_seq_number,
                   entity_logs,
                   restore_objects,
                   start_seq_number)


