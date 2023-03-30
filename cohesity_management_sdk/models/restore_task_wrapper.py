# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_wrapper_proto


class RestoreTaskWrapper(object):

    """Implementation of the 'RestoreTaskWrapper' model.

    TODO: type description here.


    Attributes:

        restore_task (RestoreWrapperProto): RestoreTask is the struct for
            RestoreWrapperProto used by magneto. It wraps either a
            Restore/Clone task, or a Destroy clone task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "restore_task":'restoreTask',
    }
    def __init__(self,
                 restore_task=None,
            ):

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
        return cls(
            restore_task
)