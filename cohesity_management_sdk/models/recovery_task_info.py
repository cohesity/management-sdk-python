# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RecoveryTaskInfo(object):

    """Implementation of the 'RecoveryTaskInfo' model.

    Parameters for a recovery op.

    Attributes:
        name (string): Name of the recovery task.
        task_id (string): Id of the recovery task.
        mtype (TypeRecoveryTaskInfoEnum): Denotes if the recovery task has an
            archival target. This param is used to reflect if the recovery op
            has an archival target to work with. 'local' indicates no archival
            target. 'archive' indicates that objects restored using an
            archival target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "task_id":'taskId',
        "mtype":'type'
    }

    def __init__(self,
                 name=None,
                 task_id=None,
                 mtype=None):
        """Constructor for the RecoveryTaskInfo class"""

        # Initialize members of the class
        self.name = name
        self.task_id = task_id
        self.mtype = mtype


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
        name = dictionary.get('name')
        task_id = dictionary.get('taskId')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(name,
                   task_id,
                   mtype)


