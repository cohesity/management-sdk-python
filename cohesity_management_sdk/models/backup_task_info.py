# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BackupTaskInfo(object):

    """Implementation of the 'BackupTaskInfo' model.

    TODO: type model description here.

    Attributes:
        instance_id (string): Id of that particular instance
        name (string): Name of the recovery task.
        start_time_usecs (string): Denotes the start time of the backuptask,
            needed for deeplinking.
        task_id (string): Id of the recovery task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "instance_id":'instanceId',
        "name":'name',
        "start_time_usecs":'startTimeUsecs',
        "task_id":'taskId'
    }

    def __init__(self,
                 instance_id=None,
                 name=None,
                 start_time_usecs=None,
                 task_id=None):
        """Constructor for the BackupTaskInfo class"""

        # Initialize members of the class
        self.instance_id = instance_id
        self.name = name
        self.start_time_usecs = start_time_usecs
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
        instance_id = dictionary.get('instanceId')
        name = dictionary.get('name')
        start_time_usecs = dictionary.get('startTimeUsecs')
        task_id = dictionary.get('taskId')

        # Return an object of this model
        return cls(instance_id,
                   name,
                   start_time_usecs,
                   task_id)


