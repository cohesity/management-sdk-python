# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduler_proto_scheduler_job

class SchedulerProto(object):

    """Implementation of the 'SchedulerProto' model.

    Specifies the scheduler structure which holds the various schedule jobs.

    Attributes:
        scheduler_jobs (list of SchedulerProto_SchedulerJob):  The array of
            the various scheduler jobs.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheduler_jobs":'schedulerJobs'
    }

    def __init__(self,
                 scheduler_jobs=None):
        """Constructor for the SchedulerProto class"""

        # Initialize members of the class
        self.scheduler_jobs = scheduler_jobs


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
        scheduler_jobs = None
        if dictionary.get('schedulerJobs') != None:
            scheduler_jobs = list()
            for structure in dictionary.get('schedulerJobs'):
                scheduler_jobs.append(cohesity_management_sdk.models.scheduler_proto_scheduler_job.SchedulerProto_SchedulerJob.from_dictionary(structure))

        # Return an object of this model
        return cls(scheduler_jobs)


