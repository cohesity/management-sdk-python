# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_host_connector_params
import cohesity_management_sdk.models.script_path_and_params
import cohesity_management_sdk.models.script_execution_status

class RemoteScriptProto(object):

    """Implementation of the 'RemoteScriptProto' model.

    Message to encapsulate the information of script that can be executed
    either
    before or after the backup is taken.

    Attributes:
        remote_host_params (RemoteHostConnectorParams): Connector params for
            the remote host where script is located and is executed.
        script (ScriptPathAndParams): Contains script path and its optional
            params.
        status (ScriptExecutionStatus): Execution status of the script.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "remote_host_params":'remoteHostParams',
        "script":'script',
        "status":'status'
    }

    def __init__(self,
                 remote_host_params=None,
                 script=None,
                 status=None):
        """Constructor for the RemoteScriptProto class"""

        # Initialize members of the class
        self.remote_host_params = remote_host_params
        self.script = script
        self.status = status


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
        remote_host_params = cohesity_management_sdk.models.remote_host_connector_params.RemoteHostConnectorParams.from_dictionary(dictionary.get('remoteHostParams')) if dictionary.get('remoteHostParams') else None
        script = cohesity_management_sdk.models.script_path_and_params.ScriptPathAndParams.from_dictionary(dictionary.get('script')) if dictionary.get('script') else None
        status = cohesity_management_sdk.models.script_execution_status.ScriptExecutionStatus.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None

        # Return an object of this model
        return cls(remote_host_params,
                   script,
                   status)


