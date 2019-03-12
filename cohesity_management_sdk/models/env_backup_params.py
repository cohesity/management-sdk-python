# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.hyperv_backup_environment_parameters
import cohesity_management_sdk.models.nas_backup_parameters
import cohesity_management_sdk.models.outlook_backup_environment_parameters
import cohesity_management_sdk.models.physical_backup_environment_parameters
import cohesity_management_sdk.models.sql_backup_job_parameters
import cohesity_management_sdk.models.vmware_backup_environment_parameters

class EnvBackupParams(object):

    """Implementation of the 'EnvBackupParams' model.

    Message to capture any additional environment specific backup params at
    the
    job level.

    Attributes:
        hyperv_backup_params (HypervBackupEnvironmentParameters): Message to
            capture any additional backup params for a HyperV environment.
        nas_backup_params (NASBackupParameters): Message to capture any
            additional backup params for a NAS environment.
        outlook_backup_params (OutlookBackupEnvironmentParameters): Message to
            capture any additional backup params for an Outlook environment.
        physical_backup_params (PhysicalBackupEnvironmentParameters): Message
            to capture any additional backup params for a Physical
            environment.
        sql_backup_job_params (SQLBackupJobParameters): Message to capture
            additional backup job params specific to SQL.
        vmware_backup_params (VmwareBackupEnvironmentParameters): Message to
            capture any additional backup params for a VMware environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hyperv_backup_params":'hypervBackupParams',
        "nas_backup_params":'nasBackupParams',
        "outlook_backup_params":'outlookBackupParams',
        "physical_backup_params":'physicalBackupParams',
        "sql_backup_job_params":'sqlBackupJobParams',
        "vmware_backup_params":'vmwareBackupParams'
    }

    def __init__(self,
                 hyperv_backup_params=None,
                 nas_backup_params=None,
                 outlook_backup_params=None,
                 physical_backup_params=None,
                 sql_backup_job_params=None,
                 vmware_backup_params=None):
        """Constructor for the EnvBackupParams class"""

        # Initialize members of the class
        self.hyperv_backup_params = hyperv_backup_params
        self.nas_backup_params = nas_backup_params
        self.outlook_backup_params = outlook_backup_params
        self.physical_backup_params = physical_backup_params
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
        hyperv_backup_params = cohesity_management_sdk.models.hyperv_backup_environment_parameters.HypervBackupEnvironmentParameters.from_dictionary(dictionary.get('hypervBackupParams')) if dictionary.get('hypervBackupParams') else None
        nas_backup_params = cohesity_management_sdk.models.nas_backup_parameters.NASBackupParameters.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_environment_parameters.OutlookBackupEnvironmentParameters.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        physical_backup_params = cohesity_management_sdk.models.physical_backup_environment_parameters.PhysicalBackupEnvironmentParameters.from_dictionary(dictionary.get('physicalBackupParams')) if dictionary.get('physicalBackupParams') else None
        sql_backup_job_params = cohesity_management_sdk.models.sql_backup_job_parameters.SQLBackupJobParameters.from_dictionary(dictionary.get('sqlBackupJobParams')) if dictionary.get('sqlBackupJobParams') else None
        vmware_backup_params = cohesity_management_sdk.models.vmware_backup_environment_parameters.VmwareBackupEnvironmentParameters.from_dictionary(dictionary.get('vmwareBackupParams')) if dictionary.get('vmwareBackupParams') else None

        # Return an object of this model
        return cls(hyperv_backup_params,
                   nas_backup_params,
                   outlook_backup_params,
                   physical_backup_params,
                   sql_backup_job_params,
                   vmware_backup_params)


