# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_archive_run

class CloudArchiveSummary(object):

    """Implementation of the 'CloudArchiveSummary' model.

    Specifies statistics about the transfer of data from this Cohesity
    Cluster to a Vault.

    Attributes:
        job_id (long|int): Specifies the id of the job.
        job_name (string): Specifies the name of the Protection Job.
        job_type (JobTypeEnum): Specifies the type of the Protection Job.
        number_of_failed_runs (int): Specifies the number of failed runs for a
            Protection Job.
        number_of_queued_runs (int): Specifies the number of queued runs for a
            Protection Job.
        number_of_successful_runs (int): Specifies the number of successful
            runs for a Protection Job.
        runs (list of CloudArchiveRun): Specifies the list of cloud archive
            runs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id": 'jobId',
        "job_name": 'jobName',
        "job_type": 'jobType',
        "number_of_failed_runs":'numberOfFailedRuns',
        "number_of_queued_runs":'numberOfQueuedRuns',
        "number_of_successful_runs":'numberOfSuccessfulRuns',
        "runs":'runs'
    }

    def __init__(self,
                 job_id=None,
                 job_name=None,
                 job_type=None,
                 number_of_failed_runs=None,
                 number_of_queued_runs=None,
                 number_of_successful_runs=None,
                 runs=None
                 ):
        """Constructor for the CloudArchiveSummary class"""

        # Initialize members of the class
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.number_of_failed_runs = number_of_failed_runs
        self.number_of_queued_runs = number_of_queued_runs
        self.number_of_successful_runs = number_of_successful_runs
        self.runs = runs

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
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_type = dictionary.get('jobType')
        number_of_failed_runs = dictionary.get('numberOfFailedRuns')
        number_of_queued_runs = dictionary.get('numberOfQueuedRuns')
        number_of_successful_runs = dictionary.get('numberOfSuccessfulRuns')
        runs = None
        if dictionary.get('runs') != None:
            runs = list()
            for structure in dictionary.get('runs'):
                runs.append(cohesity_management_sdk.models.cloud_archive_run.CloudArchiveRun.from_dictionary(structure))

        # Return an object of this model
        return cls(job_id,
                   job_name,
                   job_type,
                   number_of_failed_runs,
                   number_of_queued_runs,
                   number_of_successful_runs,
                   runs)


