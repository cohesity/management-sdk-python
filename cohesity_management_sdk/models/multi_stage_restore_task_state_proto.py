# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.update_restore_task_options


class MultiStageRestoreTaskStateProto(object):

    """Implementation of the 'MultiStageRestoreTaskStateProto' model.

    TODO: type description here.


    Attributes:

        multi_stage_restore_options (UpdateRestoreTaskOptions): Captures the
            options(parameters) corresponding to the multi-stage restore task.
        sync_size_bytes (long|int): Captures the size of the data being synced
            to the target by this restore task.
        sync_time_usecs (long|int): Captures the target entity's sync time in
            microseconds. This field usage depends on the type of the
            multi-stage restore.  For a VMware non-CDP multi-stage restore,
            this represents the start time of the backup run that the target VM
            is synced with.  For a VMware CDP multi-stage restore(yet to be
            implemented), this represents the time of the last applied IO on
            the target VM.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "multi_stage_restore_options":'multiStageRestoreOptions',
        "sync_size_bytes":'syncSizeBytes',
        "sync_time_usecs":'syncTimeUsecs',
    }
    def __init__(self,
                 multi_stage_restore_options=None,
                 sync_size_bytes=None,
                 sync_time_usecs=None,
            ):

        """Constructor for the MultiStageRestoreTaskStateProto class"""

        # Initialize members of the class
        self.multi_stage_restore_options = multi_stage_restore_options
        self.sync_size_bytes = sync_size_bytes
        self.sync_time_usecs = sync_time_usecs

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
        multi_stage_restore_options = cohesity_management_sdk.models.update_restore_task_options.UpdateRestoreTaskOptions.from_dictionary(dictionary.get('multiStageRestoreOptions')) if dictionary.get('multiStageRestoreOptions') else None
        sync_size_bytes = dictionary.get('syncSizeBytes')
        sync_time_usecs = dictionary.get('syncTimeUsecs')

        # Return an object of this model
        return cls(
            multi_stage_restore_options,
            sync_size_bytes,
            sync_time_usecs
)