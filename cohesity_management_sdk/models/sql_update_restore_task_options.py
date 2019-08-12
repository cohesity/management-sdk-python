# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class SqlUpdateRestoreTaskOptions(object):

    """Implementation of the 'SqlUpdateRestoreTaskOptions' model.

    TODO: type model description here.

    Attributes:
        multi_stage_restore_action (int): This field is set if we are
            performing an action on a multi-stage SQL restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "multi_stage_restore_action":'multiStageRestoreAction'
    }

    def __init__(self,
                 multi_stage_restore_action=None):
        """Constructor for the SqlUpdateRestoreTaskOptions class"""

        # Initialize members of the class
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
        multi_stage_restore_action = dictionary.get('multiStageRestoreAction')

        # Return an object of this model
        return cls(multi_stage_restore_action)


