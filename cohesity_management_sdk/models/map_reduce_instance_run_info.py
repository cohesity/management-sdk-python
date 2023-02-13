# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MapReduceInstance_RunInfo(object):

    """Implementation of the 'MapReduceInstance_RunInfo' model.

    Stores the progress of run of this instance.

    Attributes:
        end_time (long|int): Time when map redcue job completed.
        error_message (string): If this run failed, then error message for
            failure.
        execution_start_time_usecs (long|int):  Time (in usecs) when job was
            picked up for execution.
        files_processed (long|int): Number of files processed in this run.
        map_done_time_usecs (long|int): Time (in usecs) when map tasks were
            done.
        map_input_bytes (long|int): Total size of data processed by this run
            in bytes.
        mappers_spawned (long|int):Number of mappers spawned till now.
        num_map_outputs (long|int): Number of outputs from mappers.
        num_reduce_outputs (long|int): Number of outputs from reducers.
        percentage_completion (float): Percentage completion of this run so
            far.
        percentage_mapper_completion (float): Percentage of mapper phase
            completed.
        percentage_reducer_completion (float): Percentage of reducer phase
            completed.
        reducers_spawned (int|long): Number of reducers spawned till now.
        remaining_time_mins (int|long):  Expected remaining time in minutes
            for completion of this run.
        start_time (int|long): Time when map reduce job was started by user.
        status (int|long): Status of this run.
        total_num_mappers (int|long): Total number of mappers to be spawned.
        total_num_reducers (int|long): Specifies the View name where this
            object is stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time":'endTime',
        "error_message":'errorMessage',
        "execution_start_time_usecs":'executionStartTimeUsecs',
        "files_processed":'filesProcessed',
        "map_done_time_usecs":'mapDoneTimeUsecs',
        "map_input_bytes":'mapInputBytes',
        "mappers_spawned":'mappersSpawned',
        "num_map_outputs":'numMapOutputs',
        "num_reduce_outputs":'numReduceOutputs',
        "percentage_completion":'percentageCompletion',
        "percentage_mapper_completion":'percentageMapperCompletion',
        "percentage_reducer_completion":'percentageReducerCompletion',
        "reducers_spawned":'reducersSpawned',
        "remaining_time_mins":'remainingTimeMins',
        "start_time":'startTime',
        "status":'status',
        "total_num_mappers":'totalNumMappers',
        "total_num_reducers":'totalNumReducers'
    }

    def __init__(self,
                 end_time=None,
                 error_message=None,
                 execution_start_time_usecs=None,
                 files_processed=None,
                 map_done_time_usecs=None,
                 map_input_bytes=None,
                 mappers_spawned=None,
                 num_map_outputs=None,
                 num_reduce_outputs=None,
                 percentage_completion=None,
                 percentage_mapper_completion=None,
                 percentage_reducer_completion=None,
                 reducers_spawned=None,
                 remaining_time_mins=None,
                 start_time=None,
                 status=None,
                 total_num_mappers=None,
                 total_num_reducers=None):
        """Constructor for the MapReduceInstance_RunInfo class"""

        # Initialize members of the class
        self.end_time = end_time
        self.error_message = error_message
        self.execution_start_time_usecs = execution_start_time_usecs
        self.files_processed = files_processed
        self.map_done_time_usecs = map_done_time_usecs
        self.map_input_bytes = map_input_bytes
        self.mappers_spawned = mappers_spawned
        self.num_map_outputs = num_map_outputs
        self.num_reduce_outputs = num_reduce_outputs
        self.percentage_completion = percentage_completion
        self.percentage_mapper_completion = percentage_mapper_completion
        self.percentage_reducer_completion = percentage_reducer_completion
        self.reducers_spawned = reducers_spawned
        self.remaining_time_mins = remaining_time_mins
        self.start_time = start_time
        self.status = status
        self.total_num_mappers = total_num_mappers
        self.total_num_reducers = total_num_reducers


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
        end_time = dictionary.get('endTime')
        error_message = dictionary.get('errorMessage')
        execution_start_time_usecs = dictionary.get('executionStartTimeUsecs')
        files_processed = dictionary.get('filesProcessed')
        map_done_time_usecs = dictionary.get('mapDoneTimeUsecs')
        map_input_bytes = dictionary.get('mapInputBytes')
        mappers_spawned = dictionary.get('mappersSpawned')
        num_map_outputs = dictionary.get('numMapOutputs')
        num_reduce_outputs = dictionary.get('numReduceOutputs')
        percentage_completion = dictionary.get('percentageCompletion')
        percentage_mapper_completion = dictionary.get('percentageMapperCompletion')
        percentage_reducer_completion = dictionary.get('percentageReducerCompletion')
        reducers_spawned = dictionary.get('reducersSpawned')
        remaining_time_mins = dictionary.get('remainingTimeMins')
        start_time = dictionary.get('startTime')
        status = dictionary.get('status')
        total_num_mappers = dictionary.get('totalNumMappers')
        total_num_reducers = dictionary.get('totalNumReducers')

        # Return an object of this model
        return cls(end_time,
                   error_message,
                   execution_start_time_usecs,
                   files_processed,
                   map_done_time_usecs,
                   map_input_bytes,
                   mappers_spawned,
                   num_map_outputs,
                   num_reduce_outputs,
                   percentage_completion,
                   percentage_mapper_completion,
                   percentage_reducer_completion,
                   reducers_spawned,
                   remaining_time_mins,
                   start_time,
                   status,
                   total_num_mappers,
                   total_num_reducers)


