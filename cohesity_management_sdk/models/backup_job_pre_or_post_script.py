# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_host_connector_params
import cohesity_management_sdk.models.script_path_and_params


class BackupJobPreOrPostScript(object):

    """Implementation of the 'BackupJobPreOrPostScript' model.

    A message to encapsulate the pre and post scripts associated with a backup
    job. Pre script is executed before backup run of a job starts. Post script
    is executed after backup run of a job finishes. Currently, pre and post
    script is only supported for backup job of type 'kPuppeteer' and
    agent-based backup jobs.


    Attributes:

        backup_script (ScriptPathAndParams): Script specific to the
            incremental/regular backup. If the script is not specified,
            incremental backup run will fail. For agent-based backup jobs, only
            following script is considered. The script file will be looked in
            the agent installation directory. If the file is not present, then
            it will be logged in Pulse and backup job continues without
            throwing any error/warning.
        full_backup_script (ScriptPathAndParams): Script specific to the full
            backup. If the script is not specified, full backup run will fail.
        log_backup_script (ScriptPathAndParams): Script specific to the log
            backup. If the script is not specified, log backup run will fail.
        remote_host_params (RemoteHostConnectorParams): Connector params for
            the host on which script is executed. This field is mandatory for
            job of type kPuppeteer and optional for other job types.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_script":'backupScript',
        "full_backup_script":'fullBackupScript',
        "log_backup_script":'logBackupScript',
        "remote_host_params":'remoteHostParams',
    }
    def __init__(self,
                 backup_script=None,
                 full_backup_script=None,
                 log_backup_script=None,
                 remote_host_params=None,
            ):

        """Constructor for the BackupJobPreOrPostScript class"""

        # Initialize members of the class
        self.backup_script = backup_script
        self.full_backup_script = full_backup_script
        self.log_backup_script = log_backup_script
        self.remote_host_params = remote_host_params

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
        backup_script = cohesity_management_sdk.models.script_path_and_params.ScriptPathAndParams.from_dictionary(dictionary.get('backupScript')) if dictionary.get('backupScript') else None
        full_backup_script = cohesity_management_sdk.models.script_path_and_params.ScriptPathAndParams.from_dictionary(dictionary.get('fullBackupScript')) if dictionary.get('fullBackupScript') else None
        log_backup_script = cohesity_management_sdk.models.script_path_and_params.ScriptPathAndParams.from_dictionary(dictionary.get('logBackupScript')) if dictionary.get('logBackupScript') else None
        remote_host_params = cohesity_management_sdk.models.remote_host_connector_params.RemoteHostConnectorParams.from_dictionary(dictionary.get('remoteHostParams')) if dictionary.get('remoteHostParams') else None

        # Return an object of this model
        return cls(
            backup_script,
            full_backup_script,
            log_backup_script,
            remote_host_params
)