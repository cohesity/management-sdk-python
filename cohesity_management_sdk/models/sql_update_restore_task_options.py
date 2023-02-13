# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SqlUpdateRestoreTaskOptions(object):

    """Implementation of the 'SqlUpdateRestoreTaskOptions' model.

    TODO: type model description here.

    Attributes:
        enable_auto_sync (bool): Enable/Disable auto_sync for db migration
        multi_stage_restore_action (int): This field is set if we are
            performing an action on a multi-stage SQL restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_auto_sync":'enableAutoSync',
        "multi_stage_restore_action":'multiStageRestoreAction'
    }

    def __init__(self,
                 enable_auto_sync=None,
                 multi_stage_restore_action=None):
        """Constructor for the SqlUpdateRestoreTaskOptions class"""

        # Initialize members of the class
        self.enable_auto_sync = enable_auto_sync
        self.multi_stage_restore_action = multi_stage_restore_action


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
        enable_auto_sync = dictionary.get('enableAutoSync')
        multi_stage_restore_action = dictionary.get('multiStageRestoreAction')

        # Return an object of this model
        return cls(enable_auto_sync, multi_stage_restore_action)


