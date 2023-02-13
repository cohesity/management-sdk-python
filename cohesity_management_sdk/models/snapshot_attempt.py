# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SnapshotAttempt(object):

    """Implementation of the 'SnapshotAttempt' model.

    Specifies information about a single snapshot.

    Attributes:
        attempt_number (long|int): Specifies the number of the attempts made
            by the Job Run to capture a snapshot of the object. For example,
            if an snapshot is successfully captured after three attempts, this
            field equals 3.
        job_run_id (long|int): Specifies the id of the Job Run that captured
            the snapshot.
        started_time_usecs (long|int): Specifies the time when the Job Run
            starts capturing a snapshot. Specified as a Unix epoch Timestamp
            (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attempt_number":'attemptNumber',
        "job_run_id":'jobRunId',
        "started_time_usecs":'startedTimeUsecs'
    }

    def __init__(self,
                 attempt_number=None,
                 job_run_id=None,
                 started_time_usecs=None):
        """Constructor for the SnapshotAttempt class"""

        # Initialize members of the class
        self.attempt_number = attempt_number
        self.job_run_id = job_run_id
        self.started_time_usecs = started_time_usecs


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
        attempt_number = dictionary.get('attemptNumber')
        job_run_id = dictionary.get('jobRunId')
        started_time_usecs = dictionary.get('startedTimeUsecs')

        # Return an object of this model
        return cls(attempt_number,
                   job_run_id,
                   started_time_usecs)


