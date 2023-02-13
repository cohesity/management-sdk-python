# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_wrapper_proto

class RestoreTaskWrapper(object):

    """Implementation of the 'RestoreTaskWrapper' model.

    TODO: type model description here.

    Attributes:
        restore_task (RestoreWrapperProto): If this message is a checkpoint
            record in WAL-logging or if this message is used to send restore
            task info back to the user, it will contain the info of the
            restore job/task and the list of all destroy tasks (only when the
            record is for a restore task of type clone) associated with it. If
            this message is delta record, it will contain the state mutation
            for one of individual restore job, restore task and individual
            destroy task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_task":'restoreTask'
    }

    def __init__(self,
                 restore_task=None):
        """Constructor for the RestoreTaskWrapper class"""

        # Initialize members of the class
        self.restore_task = restore_task


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
        restore_task = cohesity_management_sdk.models.restore_wrapper_proto.RestoreWrapperProto.from_dictionary(dictionary.get('restoreTask')) if dictionary.get('restoreTask') else None

        # Return an object of this model
        return cls(restore_task)


