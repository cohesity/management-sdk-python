# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class ScriptExecutionStatus(object):

    """Implementation of the 'ScriptExecutionStatus' model.

    TODO: type model description here.

    Attributes:
        error (ErrorProto): Error that occurred during execution.
        executing (bool): Indicates if a script is executing. This is
            particularly useful when there is a cancellation request and
            Magneto crashes at that point before cleaning up the running
            script.
        exit_code (int): Exit code of the script.
        state (int): Execution state of the script.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "executing":'executing',
        "exit_code":'exitCode',
        "state":'state'
    }

    def __init__(self,
                 error=None,
                 executing=None,
                 exit_code=None,
                 state=None):
        """Constructor for the ScriptExecutionStatus class"""

        # Initialize members of the class
        self.error = error
        self.executing = executing
        self.exit_code = exit_code
        self.state = state


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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        executing = dictionary.get('executing')
        exit_code = dictionary.get('exitCode')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(error,
                   executing,
                   exit_code,
                   state)


