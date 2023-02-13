# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class CancelProtectionJobRunParam(object):

    """Implementation of the 'CancelProtectionJobRunParam' model.

    TODO: type model description here.

    Attributes:
        copy_task_uid (UniversalId): Specifies an id for an object that is
            unique across Cohesity Clusters. The id is composite of all the
            ids listed below.
        job_run_id (long|int): Run Id of a Protection Job Run that needs to be
            cancelled. If this Run id does not match the id of an active Run
            in the Protection job, the job Run is not cancelled and an error
            will be returned.
        task_id_list (list of long|int): List of entity ids for which we need to
            cancel the backup tasks. If this is provided it will not cancel the
            complete run but will cancel only subset of backup tasks (if backup
            tasks are cancelled correspoding copy task will also get cancelled).
            If the backup tasks are completed successfully it will not cancel
            those backup tasks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_task_uid":'copyTaskUid',
        "job_run_id":'jobRunId',
        "task_id_list":'taskIdList'
    }

    def __init__(self,
                 copy_task_uid=None,
                 job_run_id=None,
                 task_id_list=None):
        """Constructor for the CancelProtectionJobRunParam class"""

        # Initialize members of the class
        self.copy_task_uid = copy_task_uid
        self.job_run_id = job_run_id
        self.task_id_list = task_id_list


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
        copy_task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('copyTaskUid')) if dictionary.get('copyTaskUid') else None
        job_run_id = dictionary.get('jobRunId')
        task_id_list = dictionary.get('taskIdList')

        # Return an object of this model
        return cls(copy_task_uid,
                   job_run_id,
                   task_id_list)


