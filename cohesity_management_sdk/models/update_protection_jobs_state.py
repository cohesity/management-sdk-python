# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateProtectionJobsState(object):

    """Implementation of the 'UpdateProtectionJobsState' model.

    TODO: type model description here.

    Attributes:
        failed_job_ids (list of long|int): Specifies a list of Protection Job
            ids for which updation of state failed.
        successful_job_ids (list of long|int): Specifies a list of Protection
            Job ids for which updation of state is successful.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failed_job_ids":'failedJobIds',
        "successful_job_ids":'successfulJobIds'
    }

    def __init__(self,
                 failed_job_ids=None,
                 successful_job_ids=None):
        """Constructor for the UpdateProtectionJobsState class"""

        # Initialize members of the class
        self.failed_job_ids = failed_job_ids
        self.successful_job_ids = successful_job_ids


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
        failed_job_ids = dictionary.get('failedJobIds')
        successful_job_ids = dictionary.get('successfulJobIds')

        # Return an object of this model
        return cls(failed_job_ids,
                   successful_job_ids)


