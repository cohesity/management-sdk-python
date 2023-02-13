# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GetJobRunInfoResult(object):

    """Implementation of the 'GetJobRunInfoResult' model.

    TODO: type model description here.

    Attributes:
        bytes_transferred (long|int): Specifies bytes transferred in the run.
        end_time_usecs (long|int): Specifies the end time of the run.
        failure_entities (long|int): Specifies the number of failed objects in
            the run.
        job_id (string): Specifies the job id.
        job_run_id (string): Specifies the job run id.
        job_type (string): Specifies the job type, protection, replication,
            archival, apollo, indexing etc.
        sla_violated (bool): Specifies if the sla was violated the run.
        start_time_usecs (long|int): Specifies the start time of the run.
        status (long|int): Specifies status of the run
        success_entities (long|int): Specifies the number successful objects
            in the run.
        total_entities (long|int): Specifies the number of objects in the
            run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_transferred":'bytesTransferred',
        "end_time_usecs":'endTimeUsecs',
        "failure_entities":'failureEntities',
        "job_id":'jobId',
        "job_run_id":'jobRunId',
        "job_type":'jobType',
        "sla_violated":'slaViolated',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "success_entities":'successEntities',
        "total_entities":'totalEntities'
    }

    def __init__(self,
                 bytes_transferred=None,
                 end_time_usecs=None,
                 failure_entities=None,
                 job_id=None,
                 job_run_id=None,
                 job_type=None,
                 sla_violated=None,
                 start_time_usecs=None,
                 status=None,
                 success_entities=None,
                 total_entities=None):
        """Constructor for the GetJobRunInfoResult class"""

        # Initialize members of the class
        self.bytes_transferred = bytes_transferred
        self.end_time_usecs = end_time_usecs
        self.failure_entities = failure_entities
        self.job_id = job_id
        self.job_run_id = job_run_id
        self.job_type = job_type
        self.sla_violated = sla_violated
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.success_entities = success_entities
        self.total_entities = total_entities


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
        bytes_transferred = dictionary.get('bytesTransferred')
        end_time_usecs = dictionary.get('endTimeUsecs')
        failure_entities = dictionary.get('failureEntities')
        job_id = dictionary.get('jobId')
        job_run_id = dictionary.get('jobRunId')
        job_type = dictionary.get('jobType')
        sla_violated = dictionary.get('slaViolated')
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        success_entities = dictionary.get('successEntities')
        total_entities = dictionary.get('totalEntities')

        # Return an object of this model
        return cls(bytes_transferred,
                   end_time_usecs,
                   failure_entities,
                   job_id,
                   job_run_id,
                   job_type,
                   sla_violated,
                   start_time_usecs,
                   status,
                   success_entities,
                   total_entities)


