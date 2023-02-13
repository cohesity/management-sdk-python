# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id_proto

class BackupRunId(object):

    """Implementation of the 'BackupRunId' model.

    This captures information about identifying a backup run.

    Attributes:
        job_uid (UniversalIdProto): UID of the job.
        run_start_time_usecs (long|int): Start time of the backup run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_uid": 'jobUid',
        "run_start_time_usecs": 'runStartTimeUsecs'
    }

    def __init__(self,
                 job_uid=None,
                 run_start_time_usecs=None):
        """Constructor for the BackupRunId class"""

        # Initialize members of the class
        self.job_uid = job_uid
        self.run_start_time_usecs = run_start_time_usecs


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
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')

        # Return an object of this model
        return cls(job_uid,
                   run_start_time_usecs)


