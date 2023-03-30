# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.no_sql_recover_params_entity_log
import cohesity_management_sdk.models.no_sql_restore_object
import cohesity_management_sdk.models.sequencer


class NoSqlRecoverParams(object):

    """Implementation of the 'NoSqlRecoverParams' model.

    TODO: type description here.


    Attributes:

        end_sequencer (Sequencer): TODO: Type description here.
        entity_logs (list of NoSqlRecoverParams_EntityLog): List of leaf level
            entities with their corrosponding LogData.
        job_end_time_usecs (long|int): The end time for the base snapshot in
            this recovery.
        restore_objects (list of NoSqlRestoreObject): TODO: Type description
            here.
        start_sequencer (Sequencer): The range of sequencer between which to
            apply logs present in the atom view to achive the point in time
            recovery.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_sequencer":'endSequencer',
        "entity_logs":'entityLogs',
        "job_end_time_usecs":'jobEndTimeUsecs',
        "restore_objects":'restoreObjects',
        "start_sequencer":'startSequencer',
    }
    def __init__(self,
                 end_sequencer=None,
                 entity_logs=None,
                 job_end_time_usecs=None,
                 restore_objects=None,
                 start_sequencer=None,
            ):

        """Constructor for the NoSqlRecoverParams class"""

        # Initialize members of the class
        self.end_sequencer = end_sequencer
        self.entity_logs = entity_logs
        self.job_end_time_usecs = job_end_time_usecs
        self.restore_objects = restore_objects
        self.start_sequencer = start_sequencer

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
        end_sequencer = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('endSequencer')) if dictionary.get('endSequencer') else None
        entity_logs = None
        if dictionary.get('entityLogs') != None:
            entity_logs = list()
            for structure in dictionary.get('entityLogs'):
                entity_logs.append(cohesity_management_sdk.models.no_sql_recover_params_entity_log.NoSqlRecoverParams_EntityLog.from_dictionary(structure))
        job_end_time_usecs = dictionary.get('jobEndTimeUsecs')
        restore_objects = None
        if dictionary.get('restoreObjects') != None:
            restore_objects = list()
            for structure in dictionary.get('restoreObjects'):
                restore_objects.append(cohesity_management_sdk.models.no_sql_restore_object.NoSqlRestoreObject.from_dictionary(structure))
        start_sequencer = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('startSequencer')) if dictionary.get('startSequencer') else None

        # Return an object of this model
        return cls(
            end_sequencer,
            entity_logs,
            job_end_time_usecs,
            restore_objects,
            start_sequencer
)