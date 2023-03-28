# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_additional_params
import cohesity_management_sdk.models.cassandra_log_recover_job_params


class CassandraRecoverJobParams(object):

    """Implementation of the 'CassandraRecoverJobParams' model.

    Contains any additional cassandra environment specific params for the
    recover job.


    Attributes:

        cassandra_additional_info (CassandraAdditionalParams): Additional
            parameters required for Cassandra recovery. TODO (faizan.khan) :
            Remove this.
        finalise_restore_task_id (long|int): The task id which will be used by
            the finalise restore job.
        graph_handling_enabled (bool): whether special graph handling is
            enabled
        is_finalise_phase (bool): Whether the call is for the finalise restore
            phase.
        log_recover_params (CassandraLogRecoverJobParams): Additional params
            for log recovery.
        log_restore_directory (string): Logs will be restored to this location.
        restart_allowed (bool): Option to restart Cassandra services after
            point in time recovery.
        restart_command (string): Option command for restarting Cassandra
            services
        restart_immediately (bool): Option to restart Cassandra services
            immediately after the recovery.
        restart_time (long|int): Option to restart Cassandra services at the
            specified time
        selected_data_center_vec (list of string): The data centers selected
            for recovery.
        staging_directory_vec (list of string): Cassandra staging directory
        suffix (string): A suffix that is to be applied to all recovered
            entities TODO (faizan.khan) : Remove this.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_additional_info":'cassandraAdditionalInfo',
        "finalise_restore_task_id":'finaliseRestoreTaskId',
        "graph_handling_enabled":'graphHandlingEnabled',
        "is_finalise_phase":'isFinalisePhase',
        "log_recover_params":'logRecoverParams',
        "log_restore_directory":'logRestoreDirectory',
        "restart_allowed":'restartAllowed',
        "restart_command":'restartCommand',
        "restart_immediately":'restartImmediately',
        "restart_time":'restartTime',
        "selected_data_center_vec":'selectedDataCenterVec',
        "staging_directory_vec":'stagingDirectoryVec',
        "suffix":'suffix',
    }
    def __init__(self,
                 cassandra_additional_info=None,
                 finalise_restore_task_id=None,
                 graph_handling_enabled=None,
                 is_finalise_phase=None,
                 log_recover_params=None,
                 log_restore_directory=None,
                 restart_allowed=None,
                 restart_command=None,
                 restart_immediately=None,
                 restart_time=None,
                 selected_data_center_vec=None,
                 staging_directory_vec=None,
                 suffix=None,
            ):

        """Constructor for the CassandraRecoverJobParams class"""

        # Initialize members of the class
        self.cassandra_additional_info = cassandra_additional_info
        self.finalise_restore_task_id = finalise_restore_task_id
        self.graph_handling_enabled = graph_handling_enabled
        self.is_finalise_phase = is_finalise_phase
        self.log_recover_params = log_recover_params
        self.log_restore_directory = log_restore_directory
        self.restart_allowed = restart_allowed
        self.restart_command = restart_command
        self.restart_immediately = restart_immediately
        self.restart_time = restart_time
        self.selected_data_center_vec = selected_data_center_vec
        self.staging_directory_vec = staging_directory_vec
        self.suffix = suffix

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
        cassandra_additional_info = cohesity_management_sdk.models.cassandra_additional_params.CassandraAdditionalParams.from_dictionary(dictionary.get('cassandraAdditionalInfo')) if dictionary.get('cassandraAdditionalInfo') else None
        finalise_restore_task_id = dictionary.get('finaliseRestoreTaskId')
        graph_handling_enabled = dictionary.get('graphHandlingEnabled')
        is_finalise_phase = dictionary.get('isFinalisePhase')
        log_recover_params = cohesity_management_sdk.models.cassandra_log_recover_job_params.CassandraLogRecoverJobParams.from_dictionary(dictionary.get('logRecoverParams')) if dictionary.get('logRecoverParams') else None
        log_restore_directory = dictionary.get('logRestoreDirectory')
        restart_allowed = dictionary.get('restartAllowed')
        restart_command = dictionary.get('restartCommand')
        restart_immediately = dictionary.get('restartImmediately')
        restart_time = dictionary.get('restartTime')
        selected_data_center_vec = dictionary.get("selectedDataCenterVec")
        staging_directory_vec = dictionary.get("stagingDirectoryVec")
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(
            cassandra_additional_info,
            finalise_restore_task_id,
            graph_handling_enabled,
            is_finalise_phase,
            log_recover_params,
            log_restore_directory,
            restart_allowed,
            restart_command,
            restart_immediately,
            restart_time,
            selected_data_center_vec,
            staging_directory_vec,
            suffix
)