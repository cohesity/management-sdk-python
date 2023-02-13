# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_script_proto
import cohesity_management_sdk.models.uptiering_run_once_params

class RestoreTaskAdditionalParams(object):

    """Implementation of the 'RestoreTaskAdditionalParams' model.

    Message to encapsulate the additional parameters associated with a restore
    task.

    Attributes:
        post_script (RemoteScriptProto): Post-script that must be executed
            after finishing the restore.
        pre_script (RemoteScriptProto): Pre-script that must be executed
            before starting the restore.
        uptier_params (UptieringRunOnceParams): Uptiering specific runonce
            params.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "post_script": 'postScript',
        "pre_script": 'preScript',
        "uptier_params":'uptierParams'
    }

    def __init__(self,
                 post_script=None,
                 pre_script=None,
                 uptier_params=None):
        """Constructor for the RestoreTaskAdditionalParams class"""

        # Initialize members of the class
        self.post_script = post_script
        self.pre_script = pre_script
        self.uptier_params = uptier_params


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
        post_script = cohesity_management_sdk.models.remote_script_proto.RemoteScriptProto.from_dictionary(dictionary.get('postScript')) if dictionary.get('postScript') else None
        pre_script = cohesity_management_sdk.models.remote_script_proto.RemoteScriptProto.from_dictionary(dictionary.get('preScript')) if dictionary.get('preScript') else None
        uptier_params = cohesity_management_sdk.models.uptiering_run_once_params.UptieringRunOnceParams.from_dictionary(dictionary.get('uptierParams')) if dictionary.get('uptierParams') else None

        # Return an object of this model
        return cls(post_script,
                   pre_script,
                   uptier_params)


