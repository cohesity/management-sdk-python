# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.aws_snapshot_manager_parameters
import cohesity_management_sdk.models.hyperv_env_job_parameters
import cohesity_management_sdk.models.nas_env_job_parameters
import cohesity_management_sdk.models.outlook_env_job_parameters
import cohesity_management_sdk.models.physical_env_job_parameters
import cohesity_management_sdk.models.pure_env_job_parameters
import cohesity_management_sdk.models.sql_env_job_parameters
import cohesity_management_sdk.models.vmware_env_job_parameters

class EnvironmentTypeJobParameters(object):

    """Implementation of the 'EnvironmentTypeJobParameters' model.

    Specifies additional parameters that are common to all Protection
    Sources in a Protection Job created for a particular environment type.

    Attributes:
        aws_snapshot_parameters (AwsSnapshotManagerParameters): Protection Job
            parameters applicable to 'kAWSSnapshotManager' Environment type.
            Specifies additional job parameters applicable for
            'kAWSSnapshotManager' Environment type Protection Sources in a
            Protection Job.
        hyperv_parameters (HypervEnvJobParameters): Specifies job parameters
            applicable for all 'kHyperV' Environment type Protection Sources
            in a Protection Job.
        nas_parameters (NasEnvJobParameters): Specifies job parameters
            applicable for all 'kGenericNas' Environment type Protection
            Sources in a Protection Job.
        outlook_parameters (OutlookEnvJobParameters): Specifies job parameters
            applicable for all 'kO365Outlook' Environment type Protection
            Sources in a Protection Job.
        physical_parameters (PhysicalEnvJobParameters): Protection Job
            parameters applicable to 'kPhysical' Environment type. Specifies
            job parameters applicable for all 'kPhysical' Environment type
            Protection Sources in a Protection Job.
        pure_parameters (PureEnvJobParameters): Specifies job parameters
            applicable for all 'kPure' Environment type Protection Sources in
            a Protection Job.
        sql_parameters (SqlEnvJobParameters): Specifies job parameters
            applicable for all 'kSQL' Environment type Protection Sources in a
            Protection Job.
        vmware_parameters (VmwareEnvJobParameters): Specifies job parameters
            applicable for all 'kVMware' Environment type Protection Sources
            in a Protection Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_snapshot_parameters":'awsSnapshotParameters',
        "hyperv_parameters":'hypervParameters',
        "nas_parameters":'nasParameters',
        "outlook_parameters":'outlookParameters',
        "physical_parameters":'physicalParameters',
        "pure_parameters":'pureParameters',
        "sql_parameters":'sqlParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 aws_snapshot_parameters=None,
                 hyperv_parameters=None,
                 nas_parameters=None,
                 outlook_parameters=None,
                 physical_parameters=None,
                 pure_parameters=None,
                 sql_parameters=None,
                 vmware_parameters=None):
        """Constructor for the EnvironmentTypeJobParameters class"""

        # Initialize members of the class
        self.aws_snapshot_parameters = aws_snapshot_parameters
        self.hyperv_parameters = hyperv_parameters
        self.nas_parameters = nas_parameters
        self.outlook_parameters = outlook_parameters
        self.physical_parameters = physical_parameters
        self.pure_parameters = pure_parameters
        self.sql_parameters = sql_parameters
        self.vmware_parameters = vmware_parameters


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
        aws_snapshot_parameters = cohesity_management_sdk.models.aws_snapshot_manager_parameters.AwsSnapshotManagerParameters.from_dictionary(dictionary.get('awsSnapshotParameters')) if dictionary.get('awsSnapshotParameters') else None
        hyperv_parameters = cohesity_management_sdk.models.hyperv_env_job_parameters.HypervEnvJobParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        nas_parameters = cohesity_management_sdk.models.nas_env_job_parameters.NasEnvJobParameters.from_dictionary(dictionary.get('nasParameters')) if dictionary.get('nasParameters') else None
        outlook_parameters = cohesity_management_sdk.models.outlook_env_job_parameters.OutlookEnvJobParameters.from_dictionary(dictionary.get('outlookParameters')) if dictionary.get('outlookParameters') else None
        physical_parameters = cohesity_management_sdk.models.physical_env_job_parameters.PhysicalEnvJobParameters.from_dictionary(dictionary.get('physicalParameters')) if dictionary.get('physicalParameters') else None
        pure_parameters = cohesity_management_sdk.models.pure_env_job_parameters.PureEnvJobParameters.from_dictionary(dictionary.get('pureParameters')) if dictionary.get('pureParameters') else None
        sql_parameters = cohesity_management_sdk.models.sql_env_job_parameters.SqlEnvJobParameters.from_dictionary(dictionary.get('sqlParameters')) if dictionary.get('sqlParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_env_job_parameters.VmwareEnvJobParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(aws_snapshot_parameters,
                   hyperv_parameters,
                   nas_parameters,
                   outlook_parameters,
                   physical_parameters,
                   pure_parameters,
                   sql_parameters,
                   vmware_parameters)


