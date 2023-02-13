# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MagnetoInstanceId(object):

    """Implementation of the 'MagnetoInstanceId' model.

    TODO: type model description here.

    Attributes:
        attempt_num (long|int): The attempt of the job instance that took the
            snapshot.
        job_instance_id (long|int): Instance of the job that took the
            snapshot.
        job_start_time_usecs (long|int): Start time of the job instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attempt_num":'attemptNum',
        "job_instance_id":'jobInstanceId',
        "job_start_time_usecs":'jobStartTimeUsecs'
    }

    def __init__(self,
                 attempt_num=None,
                 job_instance_id=None,
                 job_start_time_usecs=None):
        """Constructor for the MagnetoInstanceId class"""

        # Initialize members of the class
        self.attempt_num = attempt_num
        self.job_instance_id = job_instance_id
        self.job_start_time_usecs = job_start_time_usecs


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
        attempt_num = dictionary.get('attemptNum')
        job_instance_id = dictionary.get('jobInstanceId')
        job_start_time_usecs = dictionary.get('jobStartTimeUsecs')

        # Return an object of this model
        return cls(attempt_num,
                   job_instance_id,
                   job_start_time_usecs)


