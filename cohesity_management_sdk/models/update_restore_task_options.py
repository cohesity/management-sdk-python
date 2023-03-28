# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.multi_stage_restore_finalize_action_params


class UpdateRestoreTaskOptions(object):

    """Implementation of the 'UpdateRestoreTaskOptions' model.

    UpdateRestoreTaskOptions holds the common information needed for updating a
    restore task.


    Attributes:

        multi_stage_finalize_params (MultiStageRestoreFinalizeActionParams):
            Specifies generic options to update the restore task.
        multi_stage_restore_action (MultiStageRestoreActionEnum): Specifies the
            multi-stage options to update the Restore Task with. Specifies the
            action type of multi stage restore.  'kCreate' specifies the create
            action for a restore. 'kUpdate' specifies the user action to update
            an ongoing restore. 'kFinalize' specifies the user action to
            finalize a restore.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "multi_stage_finalize_params":'multiStageFinalizeParams',
        "multi_stage_restore_action":'multiStageRestoreAction',
    }
    def __init__(self,
                 multi_stage_finalize_params=None,
                 multi_stage_restore_action=None,
            ):

        """Constructor for the UpdateRestoreTaskOptions class"""

        # Initialize members of the class
        self.multi_stage_finalize_params = multi_stage_finalize_params
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
        multi_stage_finalize_params = cohesity_management_sdk.models.multi_stage_restore_finalize_action_params.MultiStageRestoreFinalizeActionParams.from_dictionary(dictionary.get('multiStageFinalizeParams')) if dictionary.get('multiStageFinalizeParams') else None
        multi_stage_restore_action = dictionary.get('multiStageRestoreAction')

        # Return an object of this model
        return cls(
            multi_stage_finalize_params,
            multi_stage_restore_action
)