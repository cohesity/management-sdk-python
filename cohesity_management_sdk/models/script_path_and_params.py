# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ScriptPathAndParams(object):

    """Implementation of the 'ScriptPathAndParams' model.

    A message to encapsulate pre or post script associated with a backup job
    policy.

    Attributes:
        continue_on_error (bool): Applicable only for pre backup scripts. If
            this flag is set to true, then backup job will start even if the
            pre backup script fails.
        is_active (bool): Indicates if the script is active. If 'is_active' is
            set to false, this script will not be executed even if it is part
            of the backup job.
        script_params (string): Custom parameters that users want to pass to
            the script. For example, if user wants to pass following params:
            1. foo=bar 2. v=10. User can construct the param string as
            "far=bar v=10".
        script_path (string): For backup jobs of type 'kPuppeteer',
            'script_path' is full path of location of the script within the
            host. For Pre/Post scripts of agent-based backup jobs,
            'script_path' is just name of the script, not full path.
        timeout_secs (int): Timeout of the script. The script will be killed
            if it exceeds this value. '-1' indicates that the timeout is not
            set for the script.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continue_on_error":'continueOnError',
        "is_active":'isActive',
        "script_params":'scriptParams',
        "script_path":'scriptPath',
        "timeout_secs":'timeoutSecs'
    }

    def __init__(self,
                 continue_on_error=None,
                 is_active=None,
                 script_params=None,
                 script_path=None,
                 timeout_secs=None):
        """Constructor for the ScriptPathAndParams class"""

        # Initialize members of the class
        self.continue_on_error = continue_on_error
        self.is_active = is_active
        self.script_params = script_params
        self.script_path = script_path
        self.timeout_secs = timeout_secs


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
        continue_on_error = dictionary.get('continueOnError')
        is_active = dictionary.get('isActive')
        script_params = dictionary.get('scriptParams')
        script_path = dictionary.get('scriptPath')
        timeout_secs = dictionary.get('timeoutSecs')

        # Return an object of this model
        return cls(continue_on_error,
                   is_active,
                   script_params,
                   script_path,
                   timeout_secs)


