# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object

class PerformRestoreJobStateProtoRestoreTask(object):

    """Implementation of the 'PerformRestoreJobStateProto_RestoreTask' model.

    Information of the object being restored along with the info of the task
    tracking the restore of that object.

    Attributes:
        object (RestoreObject): TODO: type description here.
        object_progress_monitor_task_path (string): The relative task path of
            the progress monitor for the restore of the above 'object'. Please
            note that this field will be set only after progress monitor is
            created for this restore job.
        task_id (long|int): Id of the task tracking the restore of the above
            'object'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object":'object',
        "object_progress_monitor_task_path":'objectProgressMonitorTaskPath',
        "task_id":'taskId'
    }

    def __init__(self,
                 object=None,
                 object_progress_monitor_task_path=None,
                 task_id=None):
        """Constructor for the PerformRestoreJobStateProtoRestoreTask class"""

        # Initialize members of the class
        self.object = object
        self.object_progress_monitor_task_path = object_progress_monitor_task_path
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
        task_id = dictionary.get('taskId')

        # Return an object of this model
        return cls(object,
                   object_progress_monitor_task_path,
                   task_id)


