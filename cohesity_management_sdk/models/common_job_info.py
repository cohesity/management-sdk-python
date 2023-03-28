# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id


class CommonJobInfo(object):

    """Implementation of the 'CommonJobInfo' model.

    CommonJobInfo specifies the basic metadata used in all types of job.


    Attributes:

        end_time_usecs (long|int): Specifies the Timestamp in microseconds when
            this job was finished.
        error (string): Specifies the error message reported when a search
            fails.
        job_name (string): Specifies the name of the job.
        job_uid (UniversalId): Specifies the Job Uid.
        start_time_usecs (long|int): Specifies the Timestamp in microseconds
            when this job was started.
        status (StatusCommonJobInfoEnum): Specifies the status of the job.
            'kJobRunning' indicates that the Job/task is currently running.
            'kJobFinished' indicates that the Job/task completed and finished.
            'kJobFailed' indicates that the Job/task failed and did not
            complete. 'kJobCanceled' indicates that the Job/task was canceled.
            'kJobPaused' indicates the Job/task is paused.
        vault_id (long|int): Specifies the Vault Id associated with the job.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "job_name":'jobName',
        "job_uid":'jobUid',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "vault_id":'vaultId',
    }
    def __init__(self,
                 end_time_usecs=None,
                 error=None,
                 job_name=None,
                 job_uid=None,
                 start_time_usecs=None,
                 status=None,
                 vault_id=None,
            ):

        """Constructor for the CommonJobInfo class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.job_name = job_name
        self.job_uid = job_uid
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.vault_id = vault_id

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
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = dictionary.get('error')
        job_name = dictionary.get('jobName')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        vault_id = dictionary.get('vaultId')

        # Return an object of this model
        return cls(
            end_time_usecs,
            error,
            job_name,
            job_uid,
            start_time_usecs,
            status,
            vault_id
)