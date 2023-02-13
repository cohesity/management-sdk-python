# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.objects_protected_by_policy

class JobRunsTile(object):

    """Implementation of the 'JobRunsTile' model.

    Jon Runs information.

    Attributes:
        last_day_num_job_errors (int): Number of Error runs in the last 24
            hours.
        last_day_num_job_runs (int): Number of Job Runs in the last 24 hours.
        last_day_num_job_sla_violations (int): Number of SLA Violations in the
            last 24 hours.
        num_job_running (int): Number of Jobs currently running.
        objects_protected_by_policy (list of ObjectsProtectedByPolicy):
            Objects Protected By Policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_day_num_job_errors":'lastDayNumJobErrors',
        "last_day_num_job_runs":'lastDayNumJobRuns',
        "last_day_num_job_sla_violations":'lastDayNumJobSlaViolations',
        "num_job_running":'numJobRunning',
        "objects_protected_by_policy":'objectsProtectedByPolicy'
    }

    def __init__(self,
                 last_day_num_job_errors=None,
                 last_day_num_job_runs=None,
                 last_day_num_job_sla_violations=None,
                 num_job_running=None,
                 objects_protected_by_policy=None):
        """Constructor for the JobRunsTile class"""

        # Initialize members of the class
        self.last_day_num_job_errors = last_day_num_job_errors
        self.last_day_num_job_runs = last_day_num_job_runs
        self.last_day_num_job_sla_violations = last_day_num_job_sla_violations
        self.num_job_running = num_job_running
        self.objects_protected_by_policy = objects_protected_by_policy


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
        last_day_num_job_errors = dictionary.get('lastDayNumJobErrors')
        last_day_num_job_runs = dictionary.get('lastDayNumJobRuns')
        last_day_num_job_sla_violations = dictionary.get('lastDayNumJobSlaViolations')
        num_job_running = dictionary.get('numJobRunning')
        objects_protected_by_policy = None
        if dictionary.get('objectsProtectedByPolicy') != None:
            objects_protected_by_policy = list()
            for structure in dictionary.get('objectsProtectedByPolicy'):
                objects_protected_by_policy.append(cohesity_management_sdk.models.objects_protected_by_policy.ObjectsProtectedByPolicy.from_dictionary(structure))

        # Return an object of this model
        return cls(last_day_num_job_errors,
                   last_day_num_job_runs,
                   last_day_num_job_sla_violations,
                   num_job_running,
                   objects_protected_by_policy)


