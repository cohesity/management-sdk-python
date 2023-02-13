# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RemoteScriptPathAndParams(object):

    """Implementation of the 'RemoteScriptPathAndParams' model.

    Specifies the path to the remote script and any parameters
    expected by the remote script.

    Attributes:
        continue_on_error (bool): Specifies if the script needs to continue
            even if there is an occurence of an error. If this flag is set to
            true, then backup job will start even if the pre backup script
            fails. Applicable only for pre backup scripts.
        is_active (bool): Specifies if the script is active. If set to false,
            this script will not be executed even if it is part of the backup
            job.
        script_params (string): Specifies the parameters and values to pass
            into the remote script. For example if the script expects values
            for the 'database' and 'user' parameters, specify the parameters
            and values using the following string: "database=myDatabase
            user=me".
        script_path (string): Specifies the path to the script on the remote
            host.
        timeout_secs (int): Specifies the timeout of the script in seconds.
            The script will be killed if it exceeds this value. If the value
            of the field is '-1' then timeout is not set for the script.

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
        """Constructor for the RemoteScriptPathAndParams class"""

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


