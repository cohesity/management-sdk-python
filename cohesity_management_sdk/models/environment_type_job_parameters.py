# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_snapshot_manager_parameters
import cohesity_management_sdk.models.exchange_env_job_parameters
import cohesity_management_sdk.models.externally_triggered_env_job_parameters
import cohesity_management_sdk.models.hyperv_env_job_parameters
import cohesity_management_sdk.models.nas_env_job_parameters
import cohesity_management_sdk.models.office_365_env_job_parameters
import cohesity_management_sdk.models.oracle_env_job_parameters
import cohesity_management_sdk.models.physical_env_job_parameters
import cohesity_management_sdk.models.san_env_job_parameters
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
        exchange_parameters (ExchangeEnvJobParameters): Specifies additional
            special parameters that are applicable only to Types of
            'kExchange' type.
        externally_triggered_job_parameters (ExternallyTriggeredEnvJobParameters):
            Specifies additional special parameters that are applicable only to
            externally triggered backup jobs of 'kView' type.
        hyperv_parameters (HypervEnvJobParameters): Specifies job parameters
            applicable for all 'kHyperV' Environment type Protection Sources
            in a Protection Job.
        nas_parameters (NasEnvJobParameters): Specifies job parameters
            applicable for all 'kGenericNas' Environment type Protection
            Sources in a Protection Job.
        office_365_parameters (Office365EnvJobParameters): Specifies Office365
            parameters applicable for all Office365 Environment type
            Protection Sources in a Protection Job. This encapsulates both
            OneDrive & Mailbox parameters.
        oracle_parameters (OracleEnvJobParameters): Specifies job parameters
            applicable for all 'kOracle' Environment type Protection Sources
            in a Protection Job.
        physical_parameters (PhysicalEnvJobParameters): Protection Job
            parameters applicable to 'kPhysical' Environment type. Specifies
            job parameters applicable for all 'kPhysical' Environment type
            Protection Sources in a Protection Job.
        pure_parameters (SanEnvJobParameters): Specifies job parameters
            applicable for all SAN Environment types Protection Sources in a
            Protection Job.
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
        "exchange_parameters":'exchangeParameters',
        "externally_triggered_job_parameters":'externallyTriggeredJobParameters',
        "hyperv_parameters":'hypervParameters',
        "nas_parameters":'nasParameters',
        "office_365_parameters":'office365Parameters',
        "oracle_parameters": 'oracleParameters',
        "physical_parameters":'physicalParameters',
        "pure_parameters":'pureParameters',
        "sql_parameters":'sqlParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 aws_snapshot_parameters=None,
                 exchange_parameters=None,
                 externally_triggered_job_parameters=None,
                 hyperv_parameters=None,
                 nas_parameters=None,
                 office_365_parameters=None,
                 oracle_parameters=None,
                 physical_parameters=None,
                 pure_parameters=None,
                 sql_parameters=None,
                 vmware_parameters=None):
        """Constructor for the EnvironmentTypeJobParameters class"""

        # Initialize members of the class
        self.aws_snapshot_parameters = aws_snapshot_parameters
        self.exchange_parameters = exchange_parameters
        self.externally_triggered_job_parameters = externally_triggered_job_parameters
        self.hyperv_parameters = hyperv_parameters
        self.nas_parameters = nas_parameters
        self.office_365_parameters = office_365_parameters
        self.oracle_parameters = oracle_parameters
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
        exchange_parameters = cohesity_management_sdk.models.exchange_env_job_parameters.ExchangeEnvJobParameters.from_dictionary(dictionary.get('exchangeParameters')) if dictionary.get('exchangeParameters') else None
        externally_triggered_job_parameters = cohesity_management_sdk.models.externally_triggered_env_job_parameters.ExternallyTriggeredEnvJobParameters.from_dictionary(dictionary.get('externallyTriggeredJobParameters')) if dictionary.get('externallyTriggeredJobParameters') else None
        hyperv_parameters = cohesity_management_sdk.models.hyperv_env_job_parameters.HypervEnvJobParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        nas_parameters = cohesity_management_sdk.models.nas_env_job_parameters.NasEnvJobParameters.from_dictionary(dictionary.get('nasParameters')) if dictionary.get('nasParameters') else None
        office_365_parameters = cohesity_management_sdk.models.office_365_env_job_parameters.Office365EnvJobParameters.from_dictionary(dictionary.get('office365Parameters')) if dictionary.get('office365Parameters') else None
        oracle_parameters = cohesity_management_sdk.models.oracle_env_job_parameters.OracleEnvJobParameters.from_dictionary(dictionary.get('oracleParameters')) if dictionary.get('oracleParameters') else None
        physical_parameters = cohesity_management_sdk.models.physical_env_job_parameters.PhysicalEnvJobParameters.from_dictionary(dictionary.get('physicalParameters')) if dictionary.get('physicalParameters') else None
        pure_parameters = cohesity_management_sdk.models.san_env_job_parameters.SanEnvJobParameters.from_dictionary(dictionary.get('pureParameters')) if dictionary.get('pureParameters') else None
        sql_parameters = cohesity_management_sdk.models.sql_env_job_parameters.SqlEnvJobParameters.from_dictionary(dictionary.get('sqlParameters')) if dictionary.get('sqlParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_env_job_parameters.VmwareEnvJobParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(aws_snapshot_parameters,
                   exchange_parameters,
                   externally_triggered_job_parameters,
                   hyperv_parameters,
                   nas_parameters,
                   office_365_parameters,
                   oracle_parameters,
                   physical_parameters,
                   pure_parameters,
                   sql_parameters,
                   vmware_parameters)


