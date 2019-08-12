# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.file_stubbing_params
import cohesity_management_sdk.models.hyperv_backup_env_params
import cohesity_management_sdk.models.nas_backup_params
import cohesity_management_sdk.models.o_365_backup_env_params
import cohesity_management_sdk.models.outlook_backup_env_params
import cohesity_management_sdk.models.physical_backup_env_params
import cohesity_management_sdk.models.snapshot_manager_params
import cohesity_management_sdk.models.sql_backup_job_params
import cohesity_management_sdk.models.vmware_backup_env_params

class EnvBackupParams(object):

    """Implementation of the 'EnvBackupParams' model.

    Message to capture any additional environment specific backup params at
    the
    job level.

    Attributes:
        file_stubbing_params (FileStubbingParams): File Stubbing Parameters
            Message to capture the additional stubbing params for a file-based
            environment.
        hyperv_backup_params (HypervBackupEnvParams): Message to capture any
            additional backup params for a HyperV environment.
        nas_backup_params (NasBackupParams): Message to capture any additional
            backup params for a NAS environment.
        o_365_backup_params (O365BackupEnvParams): TODO: type description
            here.
        outlook_backup_params (OutlookBackupEnvParams): Message to capture any
            additional backup params for an Outlook environment.
        physical_backup_params (PhysicalBackupEnvParams): Message to capture
            any additional backup params for a Physical environment.
        snapshot_manager_params (SnapshotManagerParams): TODO: type
            description here.
        sql_backup_job_params (SqlBackupJobParams): Message to capture
            additional backup job params specific to SQL.
        vmware_backup_params (VmwareBackupEnvParams): Message to capture any
            additional backup params for a VMware environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_stubbing_params":'fileStubbingParams',
        "hyperv_backup_params":'hypervBackupParams',
        "nas_backup_params":'nasBackupParams',
        "o_365_backup_params":'o365BackupParams',
        "outlook_backup_params":'outlookBackupParams',
        "physical_backup_params":'physicalBackupParams',
        "snapshot_manager_params":'snapshotManagerParams',
        "sql_backup_job_params":'sqlBackupJobParams',
        "vmware_backup_params":'vmwareBackupParams'
    }

    def __init__(self,
                 file_stubbing_params=None,
                 hyperv_backup_params=None,
                 nas_backup_params=None,
                 o_365_backup_params=None,
                 outlook_backup_params=None,
                 physical_backup_params=None,
                 snapshot_manager_params=None,
                 sql_backup_job_params=None,
                 vmware_backup_params=None):
        """Constructor for the EnvBackupParams class"""

        # Initialize members of the class
        self.file_stubbing_params = file_stubbing_params
        self.hyperv_backup_params = hyperv_backup_params
        self.nas_backup_params = nas_backup_params
        self.o_365_backup_params = o_365_backup_params
        self.outlook_backup_params = outlook_backup_params
        self.physical_backup_params = physical_backup_params
        self.snapshot_manager_params = snapshot_manager_params
        self.sql_backup_job_params = sql_backup_job_params
        self.vmware_backup_params = vmware_backup_params


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
        file_stubbing_params = cohesity_management_sdk.models.file_stubbing_params.FileStubbingParams.from_dictionary(dictionary.get('fileStubbingParams')) if dictionary.get('fileStubbingParams') else None
        hyperv_backup_params = cohesity_management_sdk.models.hyperv_backup_env_params.HypervBackupEnvParams.from_dictionary(dictionary.get('hypervBackupParams')) if dictionary.get('hypervBackupParams') else None
        nas_backup_params = cohesity_management_sdk.models.nas_backup_params.NasBackupParams.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        o_365_backup_params = cohesity_management_sdk.models.o_365_backup_env_params.O365BackupEnvParams.from_dictionary(dictionary.get('o365BackupParams')) if dictionary.get('o365BackupParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_env_params.OutlookBackupEnvParams.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        physical_backup_params = cohesity_management_sdk.models.physical_backup_env_params.PhysicalBackupEnvParams.from_dictionary(dictionary.get('physicalBackupParams')) if dictionary.get('physicalBackupParams') else None
        snapshot_manager_params = cohesity_management_sdk.models.snapshot_manager_params.SnapshotManagerParams.from_dictionary(dictionary.get('snapshotManagerParams')) if dictionary.get('snapshotManagerParams') else None
        sql_backup_job_params = cohesity_management_sdk.models.sql_backup_job_params.SqlBackupJobParams.from_dictionary(dictionary.get('sqlBackupJobParams')) if dictionary.get('sqlBackupJobParams') else None
        vmware_backup_params = cohesity_management_sdk.models.vmware_backup_env_params.VmwareBackupEnvParams.from_dictionary(dictionary.get('vmwareBackupParams')) if dictionary.get('vmwareBackupParams') else None

        # Return an object of this model
        return cls(file_stubbing_params,
                   hyperv_backup_params,
                   nas_backup_params,
                   o_365_backup_params,
                   outlook_backup_params,
                   physical_backup_params,
                   snapshot_manager_params,
                   sql_backup_job_params,
                   vmware_backup_params)


