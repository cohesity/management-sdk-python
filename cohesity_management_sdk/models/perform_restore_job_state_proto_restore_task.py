# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.restore_object


class PerformRestoreJobStateProto_RestoreTask(object):

    """Implementation of the 'PerformRestoreJobStateProto_RestoreTask' model.

    Information of the object being restored along with the info of the task
    tracking the restore of that object.


    Attributes:

        object (RestoreObject): Information of the object being restored (along
            with the snapshot it is being restored from).
        object_progress_monitor_task_path (string): The relative task path of
            the progress monitor for the restore of the above 'object'. Please
            note that this field will be set only after progress monitor is
            created for this restore job.
        preprocessing_error (ErrorProto): Error encountered for the object in
            the preprocessing step. If set, the task will not be scheduled on
            the slave for restore. Ex: This is set in case of VCD recovery when
            VM with the same name exist in the vapp.
        task_id (long|int): Id of the task tracking the restore of the above
            'object'.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object":'object',
        "object_progress_monitor_task_path":'objectProgressMonitorTaskPath',
        "preprocessing_error":'preprocessingError',
        "task_id":'taskId',
    }
    def __init__(self,
                 object=None,
                 object_progress_monitor_task_path=None,
                 preprocessing_error=None,
                 task_id=None,
            ):

        """Constructor for the PerformRestoreJobStateProto_RestoreTask class"""

        # Initialize members of the class
        self.object = object
        self.object_progress_monitor_task_path = object_progress_monitor_task_path
        self.preprocessing_error = preprocessing_error
        self.task_id = task_id

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
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None
        object_progress_monitor_task_path = dictionary.get('objectProgressMonitorTaskPath')
        preprocessing_error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('preprocessingError')) if dictionary.get('preprocessingError') else None
        task_id = dictionary.get('taskId')

        # Return an object of this model
        return cls(
            object,
            object_progress_monitor_task_path,
            preprocessing_error,
            task_id
)