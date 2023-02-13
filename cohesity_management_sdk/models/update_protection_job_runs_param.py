# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.update_protection_job_run

class UpdateProtectionJobRunsParam(object):

    """Implementation of the 'UpdateProtectionJobRunsParam' model.

    Specifies the Job Runs to update with a new expiration times.

    Attributes:
        job_runs (list of UpdateProtectionJobRun): Array of Job Runs.
            Specifies the Job Runs to update with a new expiration times.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_runs":'jobRuns'
    }

    def __init__(self,
                 job_runs=None):
        """Constructor for the UpdateProtectionJobRunsParam class"""

        # Initialize members of the class
        self.job_runs = job_runs


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
        job_runs = None
        if dictionary.get('jobRuns') != None:
            job_runs = list()
            for structure in dictionary.get('jobRuns'):
                job_runs.append(cohesity_management_sdk.models.update_protection_job_run.UpdateProtectionJobRun.from_dictionary(structure))

        # Return an object of this model
        return cls(job_runs)


