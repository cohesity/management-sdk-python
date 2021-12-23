# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.aws_native_env_params
import cohesity_management_sdk.models.exchange_backup_job_params
import cohesity_management_sdk.models.externally_triggered_job_params
import cohesity_management_sdk.models.file_stubbing_params
import cohesity_management_sdk.models.file_uptiering_params
import cohesity_management_sdk.models.hyperv_backup_env_params
import cohesity_management_sdk.models.isilon_env_params
import cohesity_management_sdk.models.nas_backup_params
import cohesity_management_sdk.models.nas_analysis_job_params
import cohesity_management_sdk.models.no_sql_backup_job_params
import cohesity_management_sdk.models.o_365_backup_env_params
import cohesity_management_sdk.models.oracle_backup_job_params
import cohesity_management_sdk.models.outlook_backup_env_params
import cohesity_management_sdk.models.physical_backup_env_params
import cohesity_management_sdk.models.snapshot_manager_params
import cohesity_management_sdk.models.sql_backup_job_params
import cohesity_management_sdk.models.uda_backup_job_params
import cohesity_management_sdk.models.vmware_backup_env_params

class EnvBackupParams(object):

    """Implementation of the 'EnvBackupParams' model.

    Message to capture any additional environment specific backup params at
    the
    job level.

    Attributes:
        aws_native_env_params (AWSNativeEnvParams): This is applicable to AWS
            native backups.
        exchange_backup_job_params (ExchangeBackupJobParams): Message to
            capture additional backup job params specific to Exchange.
        externally_triggered_job_params (ExternallyTriggeredJobParams):
            This is applicable to externally triggered backups.
        file_stubbing_params (FileStubbingParams): File Stubbing Parameters
            Message to capture the additional stubbing params for a file-based
            environment.
        file_uptiering_params (FileUptieringParams): File Uptiering Parameters
            for NAS migration.
        hyperv_backup_params (HypervBackupEnvParams): Message to capture any
            additional backup params for a HyperV environment.
        isilon_env_params (IsilonEnvParams): This is applicable to Isilon type
            of environments.
        nas_analysis_job_params (NasAnalysisJobParams): This is applicable to
            analysis of NAS environments.
        nas_backup_params (NasBackupParams): Message to capture any additional
            backup params for a NAS environment.
        no_sql_backup_job_params (NoSqlBackupJobParams): Contains backup params
            at the job level applicable for nosql environment.
        o_365_backup_params (O365BackupEnvParams): Message to capture any
            additional backup params for Office365 environment. This
            encapsulates both Outlook & OneDrive backup parameters.
        oracle_backup_job_params (OracleBackupJobParams): Message to capture
            any additional backup params specific to Oracle.
        outlook_backup_params (OutlookBackupEnvParams): Message to capture any
            additional backup params for Outlook within Office365
            environment.
        physical_backup_params (PhysicalBackupEnvParams): Message to capture
            any additional backup params for a Physical environment.
        snapshot_manager_params (SnapshotManagerParams): TODO: type
            description here.
        sql_backup_job_params (SqlBackupJobParams): Message to capture
            additional backup job params specific to SQL.
        uda_backup_job_params (UdaBackupJobParams): This is applicable to UDA
            environments.
        vmware_backup_params (VmwareBackupEnvParams): Message to capture any
            additional backup params for a VMware environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_native_env_params": 'awsNativeEnvParams',
        "exchange_backup_job_params":'exchangeBackupJobParams',
        "externally_triggered_job_params":'externallyTriggeredJobParams',
        "file_stubbing_params":'fileStubbingParams',
        "file_uptiering_params":'fileUptieringParams',
        "hyperv_backup_params":'hypervBackupParams',
        "isilon_env_params":'isilonEnvParams',
        "nas_analysis_job_params":'nasAnalysisJobParams',
        "nas_backup_params":'nasBackupParams',
        "no_sql_backup_job_params": 'nosqlBackupJobParams',
        "o_365_backup_params":'o365BackupParams',
        "oracle_backup_job_params":'oracleBackupJobParams',
        "outlook_backup_params":'outlookBackupParams',
        "physical_backup_params":'physicalBackupParams',
        "snapshot_manager_params":'snapshotManagerParams',
        "sql_backup_job_params":'sqlBackupJobParams',
        "uda_backup_job_params":'udaBackupJobParams',
        "vmware_backup_params":'vmwareBackupParams'
    }

    def __init__(self,
                 aws_native_env_params=None,
                 exchange_backup_job_params=None,
                 externally_triggered_job_params=None,
                 file_stubbing_params=None,
                 file_uptiering_params=None,
                 hyperv_backup_params=None,
                 isilon_env_params=None,
                 nas_analysis_job_params=None,
                 nas_backup_params=None,
                 no_sql_backup_job_params=None,
                 o_365_backup_params=None,
                 oracle_backup_job_params=None,
                 outlook_backup_params=None,
                 physical_backup_params=None,
                 snapshot_manager_params=None,
                 sql_backup_job_params=None,
                 uda_backup_job_params=None,
                 vmware_backup_params=None):
        """Constructor for the EnvBackupParams class"""

        # Initialize members of the class
        self.aws_native_env_params = aws_native_env_params
        self.exchange_backup_job_params = exchange_backup_job_params
        self.externally_triggered_job_params = externally_triggered_job_params
        self.file_stubbing_params = file_stubbing_params
        self.file_uptiering_params = file_uptiering_params
        self.hyperv_backup_params = hyperv_backup_params
        self.isilon_env_params = isilon_env_params
        self.nas_analysis_job_params = nas_analysis_job_params
        self.nas_backup_params = nas_backup_params
        self.no_sql_backup_job_params = no_sql_backup_job_params
        self.o_365_backup_params = o_365_backup_params
        self.oracle_backup_job_params = oracle_backup_job_params
        self.outlook_backup_params = outlook_backup_params
        self.physical_backup_params = physical_backup_params
        self.snapshot_manager_params = snapshot_manager_params
        self.sql_backup_job_params = sql_backup_job_params
        self.uda_backup_job_params = uda_backup_job_params
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
        aws_native_env_params = cohesity_management_sdk.models.aws_native_env_params.AWSNativeEnvParams.from_dictionary(dict.get('awsNativeEnvParams')) if dictionary.get('awsNativeEnvParams') else None
        exchange_backup_job_params = cohesity_management_sdk.models.exchange_backup_job_params.ExchangeBackupJobParams.from_dictionary(dictionary.get('exchangeBackupJobParams')) if dictionary.get('exchangeBackupJobParams') else None
        externally_triggered_job_params = cohesity_management_sdk.models.externally_triggered_job_params.ExternallyTriggeredJobParams.from_dictionary(dictionary.get('externallyTriggeredJobParams')) if dictionary.get('externallyTriggeredJobParams') else None
        file_stubbing_params = cohesity_management_sdk.models.file_stubbing_params.FileStubbingParams.from_dictionary(dictionary.get('fileStubbingParams')) if dictionary.get('fileStubbingParams') else None
        file_uptiering_params = cohesity_management_sdk.models.file_uptiering_params.FileUptieringParams.from_dictionary(dictionary.get('fileUptieringParams')) if dictionary.get('fileUptieringParams') else None
        hyperv_backup_params = cohesity_management_sdk.models.hyperv_backup_env_params.HypervBackupEnvParams.from_dictionary(dictionary.get('hypervBackupParams')) if dictionary.get('hypervBackupParams') else None
        isilon_env_params = cohesity_management_sdk.models.isilon_env_params.IsilonEnvParams.from_dictionary(dictionary.get('isilonEnvParams')) if dictionary.get('isilonEnvParams') else None
        nas_analysis_job_params = cohesity_management_sdk.models.nas_analysis_job_params.NasAnalysisJobParams.from_dictionary(dictionary.get('nasAnalysisJobParams')) if dictionary.get('nasAnalysisJobParams') else None
        nas_backup_params = cohesity_management_sdk.models.nas_backup_params.NasBackupParams.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        no_sql_backup_job_params = cohesity_management_sdk.models.no_sql_backup_job_params.NoSqlBackupJobParams.from_dictionary(dictionary.get('nosqlBackupJobParams')) if dictionary.get('noSqlBackupJobParams') else None
        o_365_backup_params = cohesity_management_sdk.models.o_365_backup_env_params.O365BackupEnvParams.from_dictionary(dictionary.get('o365BackupParams')) if dictionary.get('o365BackupParams') else None
        oracle_backup_job_params = cohesity_management_sdk.models.oracle_backup_job_params.OracleBackupJobParams.from_dictionary(dictionary.get('oracleBackupJobParams')) if dictionary.get('oracleBackupJobParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_env_params.OutlookBackupEnvParams.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        physical_backup_params = cohesity_management_sdk.models.physical_backup_env_params.PhysicalBackupEnvParams.from_dictionary(dictionary.get('physicalBackupParams')) if dictionary.get('physicalBackupParams') else None
        snapshot_manager_params = cohesity_management_sdk.models.snapshot_manager_params.SnapshotManagerParams.from_dictionary(dictionary.get('snapshotManagerParams')) if dictionary.get('snapshotManagerParams') else None
        sql_backup_job_params = cohesity_management_sdk.models.sql_backup_job_params.SqlBackupJobParams.from_dictionary(dictionary.get('sqlBackupJobParams')) if dictionary.get('sqlBackupJobParams') else None
        uda_backup_job_params = cohesity_management_sdk.models.uda_backup_job_params.UdaBackupJobParams.from_dictionary(dictionary.get('udaBackupJobParams')) if dictionary.get('udaBackupJobParams') else None
        vmware_backup_params = cohesity_management_sdk.models.vmware_backup_env_params.VmwareBackupEnvParams.from_dictionary(dictionary.get('vmwareBackupParams')) if dictionary.get('vmwareBackupParams') else None

        # Return an object of this model
        return cls(aws_native_env_params,
                   exchange_backup_job_params,
                   externally_triggered_job_params,
                   file_stubbing_params,
                   file_uptiering_params,
                   hyperv_backup_params,
                   isilon_env_params,
                   nas_analysis_job_params,
                   nas_backup_params,
                   no_sql_backup_job_params,
                   o_365_backup_params,
                   oracle_backup_job_params,
                   outlook_backup_params,
                   physical_backup_params,
                   snapshot_manager_params,
                   sql_backup_job_params,
                   uda_backup_job_params,
                   vmware_backup_params)


