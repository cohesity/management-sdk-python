# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_script_path_and_params
import cohesity_management_sdk.models.remote_host

class RemoteJobScript(object):

    """Implementation of the 'RemoteJobScript' model.

    Provides details about the Remote Adapter associated with a
    'kPuppeteer' Protection Job.

    Attributes:
        full_backup_script (RemoteScriptPathAndParams): Specifies the script
            that should run for the Full (no CBT) backup schedule of a Remote
            Adapter 'kPuppeteer' Job. This field is mandatory if the Policy
            associated with this Job has a Full (no CBT) backup schedule and
            this is Remote Adapter 'kPuppeteer' Job.
        incremental_backup_script (RemoteScriptPathAndParams): Specifies the
            script that should run for the CBT-based backup schedule of a
            Remote Adapter 'kPuppeteer' Job. A CBT-based backup schedule is
            utilizing Change Block Tracking when capturing Snapshots. This
            field is mandatory if the Policy associated with this Job has a
            CBT-based backup schedule and this is Remote Adapter 'kPuppeteer'
            Job.
        log_backup_script (RemoteScriptPathAndParams): Specifies the script
            that should run for the Log backup schedule of a Remote Adapter
            'kPuppeteer' Job. This field is mandatory if the Policy associated
            with this Job has a Log backup schedule and this is Remote Adapter
            'kPuppeteer' Job.
        remote_host (RemoteHost): Specifies the remote host where the remote
            scripts are executed. This field must be set for Remote Adapter
            Jobs.
        username (string): Specifies the username that will be used to login
            to the remote host. For host type 'kLinux', it is expected that
            user has setup the password-less access. So only username field is
            required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_backup_script":'fullBackupScript',
        "incremental_backup_script":'incrementalBackupScript',
        "log_backup_script":'logBackupScript',
        "remote_host":'remoteHost',
        "username":'username'
    }

    def __init__(self,
                 full_backup_script=None,
                 incremental_backup_script=None,
                 log_backup_script=None,
                 remote_host=None,
                 username=None):
        """Constructor for the RemoteJobScript class"""

        # Initialize members of the class
        self.full_backup_script = full_backup_script
        self.incremental_backup_script = incremental_backup_script
        self.log_backup_script = log_backup_script
        self.remote_host = remote_host
        self.username = username


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
        full_backup_script = cohesity_management_sdk.models.remote_script_path_and_params.RemoteScriptPathAndParams.from_dictionary(dictionary.get('fullBackupScript')) if dictionary.get('fullBackupScript') else None
        incremental_backup_script = cohesity_management_sdk.models.remote_script_path_and_params.RemoteScriptPathAndParams.from_dictionary(dictionary.get('incrementalBackupScript')) if dictionary.get('incrementalBackupScript') else None
        log_backup_script = cohesity_management_sdk.models.remote_script_path_and_params.RemoteScriptPathAndParams.from_dictionary(dictionary.get('logBackupScript')) if dictionary.get('logBackupScript') else None
        remote_host = cohesity_management_sdk.models.remote_host.RemoteHost.from_dictionary(dictionary.get('remoteHost')) if dictionary.get('remoteHost') else None
        username = dictionary.get('username')

        # Return an object of this model
        return cls(full_backup_script,
                   incremental_backup_script,
                   log_backup_script,
                   remote_host,
                   username)


