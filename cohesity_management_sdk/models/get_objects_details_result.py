# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GetObjectsDetailsResult(object):

    """Implementation of the 'GetObjectsDetailsResult' model.

    TODO: type model description here.

    Attributes:
        end_time_msecs (long|int): Specifies the end time of the run.
        entity_env (long|int): Specifies the entity environment of the
            object.
        entity_id (long|int): Specifies the entity id of the object.
        entity_name (string): Specifies the name of the entity.
        job_id (string): Specifies the job id.
        job_run_id (string): Specifies the job run id.
        job_type (string): Specifies the job type, protection, replication,
            archival, apollo, indexing etc.
        start_time_msecs (long|int): Specifies the start time of the run.
        status (long|int): Specifies status of the object run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_msecs":'endTimeMsecs',
        "entity_env":'entityEnv',
        "entity_id":'entityId',
        "entity_name":'entityName',
        "job_id":'jobId',
        "job_run_id":'jobRunId',
        "job_type":'jobType',
        "start_time_msecs":'startTimeMsecs',
        "status":'status'
    }

    def __init__(self,
                 end_time_msecs=None,
                 entity_env=None,
                 entity_id=None,
                 entity_name=None,
                 job_id=None,
                 job_run_id=None,
                 job_type=None,
                 start_time_msecs=None,
                 status=None):
        """Constructor for the GetObjectsDetailsResult class"""

        # Initialize members of the class
        self.end_time_msecs = end_time_msecs
        self.entity_env = entity_env
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.job_id = job_id
        self.job_run_id = job_run_id
        self.job_type = job_type
        self.start_time_msecs = start_time_msecs
        self.status = status


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
        end_time_msecs = dictionary.get('endTimeMsecs')
        entity_env = dictionary.get('entityEnv')
        entity_id = dictionary.get('entityId')
        entity_name = dictionary.get('entityName')
        job_id = dictionary.get('jobId')
        job_run_id = dictionary.get('jobRunId')
        job_type = dictionary.get('jobType')
        start_time_msecs = dictionary.get('startTimeMsecs')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(end_time_msecs,
                   entity_env,
                   entity_id,
                   entity_name,
                   job_id,
                   job_run_id,
                   job_type,
                   start_time_msecs,
                   status)


