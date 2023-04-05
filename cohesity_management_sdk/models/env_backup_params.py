# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_backup_job_params
import cohesity_management_sdk.models.aws_native_env_params
import cohesity_management_sdk.models.exchange_backup_job_params
import cohesity_management_sdk.models.externally_triggered_job_params
import cohesity_management_sdk.models.file_stubbing_params
import cohesity_management_sdk.models.file_uptiering_params
import cohesity_management_sdk.models.gcp_native_job_params
import cohesity_management_sdk.models.hyperv_backup_env_params
import cohesity_management_sdk.models.isilon_env_params
import cohesity_management_sdk.models.kubernetes_env_params
import cohesity_management_sdk.models.nas_analysis_job_params
import cohesity_management_sdk.models.nas_backup_params
import cohesity_management_sdk.models.no_sql_backup_job_params
import cohesity_management_sdk.models.o_365_backup_env_params
import cohesity_management_sdk.models.oracle_backup_job_params
import cohesity_management_sdk.models.outlook_backup_env_params
import cohesity_management_sdk.models.physical_backup_env_params
import cohesity_management_sdk.models.s3_backup_job_params
import cohesity_management_sdk.models.sfdc_backup_job_params
import cohesity_management_sdk.models.snapshot_manager_params
import cohesity_management_sdk.models.sql_backup_job_params
import cohesity_management_sdk.models.uda_backup_job_params
import cohesity_management_sdk.models.vmware_backup_env_params


class EnvBackupParams(object):

    """Implementation of the 'EnvBackupParams' model.

    Message to capture any additional environment specific backup params at the
    job level.


    Attributes:

        acropolis_backup_job_params (AcropolisBackupJobParams): This is
            applicable to Acropolis environment.
        aws_native_env_params (AWSNativeEnvParams): This is applicable to AWS
            native backups.
        exchange_backup_job_params (ExchangeBackupJobParams): This is
            applicable to Exchange environments.
        externally_triggered_job_params (ExternallyTriggeredJobParams): This is
            applicable to externally triggered backups.
        file_stubbing_params (FileStubbingParams): This is applicable to
            stubbing in NAS environments.
        file_uptiering_params (FileUptieringParams): This is applicable to
            uptiering in NAS environments.
        gcp_native_job_params (GCPNativeJobParams): This is applicable to GCP
            native backups.
        hyperv_backup_params (HyperVBackupEnvParams): This is applicable to
            HyperV type of environments.
        isilon_env_params (IsilonEnvParams): This is applicable to Isilon type
            of environments.
        kubernetes_env_params (KubernetesEnvParams): This is applicable to
            Kubernetes type of environments.
        nas_analysis_job_params (NasAnalysisJobParams): This is applicable to
            analysis of NAS environments.
        nas_backup_params (NasBackupParams): This is applicable to NAS type of
            environments.
        nosql_backup_job_params (NoSqlBackupJobParams): This is applicable to
            NoSql DB environments.
        o_365_backup_params (O365BackupEnvParams): This is applicable to
            stubbing in o365 environments.
        oracle_backup_job_params (OracleBackupJobParams): This is applicable to
            Oracle environments.
        outlook_backup_params (OutlookBackupEnvParams): This is applicable to
            Outlook type of environments.
        physical_backup_params (PhysicalBackupEnvParams): This is applicable to
            Physical type of environments.
        s3_backup_job_params (S3BackupJobParams): This is applicable to kAwsS3
            job type.
        sfdc_backup_job_params (SfdcBackupJobParams): This is applicable to
            SFDC type of environments.
        snapshot_manager_params (SnapshotManagerParams): This is applicable to
            snapshot manager jobs.
        sql_backup_job_params (SqlBackupJobParams): This is applicable to SQL
            environments.
        uda_backup_job_params (UdaBackupJobParams): This is applicable to UDA
            environments.
        vmware_backup_params (VMwareBackupEnvParams): This is applicable to
            VMware type of environments.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "acropolis_backup_job_params":'acropolisBackupJobParams',
        "aws_native_env_params":'awsNativeEnvParams',
        "exchange_backup_job_params":'exchangeBackupJobParams',
        "externally_triggered_job_params":'externallyTriggeredJobParams',
        "file_stubbing_params":'fileStubbingParams',
        "file_uptiering_params":'fileUptieringParams',
        "gcp_native_job_params":'gcpNativeJobParams',
        "hyperv_backup_params":'hypervBackupParams',
        "isilon_env_params":'isilonEnvParams',
        "kubernetes_env_params":'kubernetesEnvParams',
        "nas_analysis_job_params":'nasAnalysisJobParams',
        "nas_backup_params":'nasBackupParams',
        "nosql_backup_job_params":'nosqlBackupJobParams',
        "o_365_backup_params":'o365BackupParams',
        "oracle_backup_job_params":'oracleBackupJobParams',
        "outlook_backup_params":'outlookBackupParams',
        "physical_backup_params":'physicalBackupParams',
        "s3_backup_job_params":'s3BackupJobParams',
        "sfdc_backup_job_params":'sfdcBackupJobParams',
        "snapshot_manager_params":'snapshotManagerParams',
        "sql_backup_job_params":'sqlBackupJobParams',
        "uda_backup_job_params":'udaBackupJobParams',
        "vmware_backup_params":'vmwareBackupParams',
    }
    def __init__(self,
                 acropolis_backup_job_params=None,
                 aws_native_env_params=None,
                 exchange_backup_job_params=None,
                 externally_triggered_job_params=None,
                 file_stubbing_params=None,
                 file_uptiering_params=None,
                 gcp_native_job_params=None,
                 hyperv_backup_params=None,
                 isilon_env_params=None,
                 kubernetes_env_params=None,
                 nas_analysis_job_params=None,
                 nas_backup_params=None,
                 nosql_backup_job_params=None,
                 o_365_backup_params=None,
                 oracle_backup_job_params=None,
                 outlook_backup_params=None,
                 physical_backup_params=None,
                 s3_backup_job_params=None,
                 sfdc_backup_job_params=None,
                 snapshot_manager_params=None,
                 sql_backup_job_params=None,
                 uda_backup_job_params=None,
                 vmware_backup_params=None,
            ):

        """Constructor for the EnvBackupParams class"""

        # Initialize members of the class
        self.acropolis_backup_job_params = acropolis_backup_job_params
        self.aws_native_env_params = aws_native_env_params
        self.exchange_backup_job_params = exchange_backup_job_params
        self.externally_triggered_job_params = externally_triggered_job_params
        self.file_stubbing_params = file_stubbing_params
        self.file_uptiering_params = file_uptiering_params
        self.gcp_native_job_params = gcp_native_job_params
        self.hyperv_backup_params = hyperv_backup_params
        self.isilon_env_params = isilon_env_params
        self.kubernetes_env_params = kubernetes_env_params
        self.nas_analysis_job_params = nas_analysis_job_params
        self.nas_backup_params = nas_backup_params
        self.nosql_backup_job_params = nosql_backup_job_params
        self.o_365_backup_params = o_365_backup_params
        self.oracle_backup_job_params = oracle_backup_job_params
        self.outlook_backup_params = outlook_backup_params
        self.physical_backup_params = physical_backup_params
        self.s3_backup_job_params = s3_backup_job_params
        self.sfdc_backup_job_params = sfdc_backup_job_params
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
        acropolis_backup_job_params = cohesity_management_sdk.models.acropolis_backup_job_params.AcropolisBackupJobParams.from_dictionary(dictionary.get('acropolisBackupJobParams')) if dictionary.get('acropolisBackupJobParams') else None
        aws_native_env_params = cohesity_management_sdk.models.aws_native_env_params.AWSNativeEnvParams.from_dictionary(dictionary.get('awsNativeEnvParams')) if dictionary.get('awsNativeEnvParams') else None
        exchange_backup_job_params = cohesity_management_sdk.models.exchange_backup_job_params.ExchangeBackupJobParams.from_dictionary(dictionary.get('exchangeBackupJobParams')) if dictionary.get('exchangeBackupJobParams') else None
        externally_triggered_job_params = cohesity_management_sdk.models.externally_triggered_job_params.ExternallyTriggeredJobParams.from_dictionary(dictionary.get('externallyTriggeredJobParams')) if dictionary.get('externallyTriggeredJobParams') else None
        file_stubbing_params = cohesity_management_sdk.models.file_stubbing_params.FileStubbingParams.from_dictionary(dictionary.get('fileStubbingParams')) if dictionary.get('fileStubbingParams') else None
        file_uptiering_params = cohesity_management_sdk.models.file_uptiering_params.FileUptieringParams.from_dictionary(dictionary.get('fileUptieringParams')) if dictionary.get('fileUptieringParams') else None
        gcp_native_job_params = cohesity_management_sdk.models.gcp_native_job_params.GCPNativeJobParams.from_dictionary(dictionary.get('gcpNativeJobParams')) if dictionary.get('gcpNativeJobParams') else None
        hyperv_backup_params = cohesity_management_sdk.models.hyperv_backup_env_params.HyperVBackupEnvParams.from_dictionary(dictionary.get('hypervBackupParams')) if dictionary.get('hypervBackupParams') else None
        isilon_env_params = cohesity_management_sdk.models.isilon_env_params.IsilonEnvParams.from_dictionary(dictionary.get('isilonEnvParams')) if dictionary.get('isilonEnvParams') else None
        kubernetes_env_params = cohesity_management_sdk.models.kubernetes_env_params.KubernetesEnvParams.from_dictionary(dictionary.get('kubernetesEnvParams')) if dictionary.get('kubernetesEnvParams') else None
        nas_analysis_job_params = cohesity_management_sdk.models.nas_analysis_job_params.NasAnalysisJobParams.from_dictionary(dictionary.get('nasAnalysisJobParams')) if dictionary.get('nasAnalysisJobParams') else None
        nas_backup_params = cohesity_management_sdk.models.nas_backup_params.NasBackupParams.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        nosql_backup_job_params = cohesity_management_sdk.models.no_sql_backup_job_params.NoSqlBackupJobParams.from_dictionary(dictionary.get('nosqlBackupJobParams')) if dictionary.get('nosqlBackupJobParams') else None
        o_365_backup_params = cohesity_management_sdk.models.o_365_backup_env_params.O365BackupEnvParams.from_dictionary(dictionary.get('o365BackupParams')) if dictionary.get('o365BackupParams') else None
        oracle_backup_job_params = cohesity_management_sdk.models.oracle_backup_job_params.OracleBackupJobParams.from_dictionary(dictionary.get('oracleBackupJobParams')) if dictionary.get('oracleBackupJobParams') else None
        outlook_backup_params = cohesity_management_sdk.models.outlook_backup_env_params.OutlookBackupEnvParams.from_dictionary(dictionary.get('outlookBackupParams')) if dictionary.get('outlookBackupParams') else None
        physical_backup_params = cohesity_management_sdk.models.physical_backup_env_params.PhysicalBackupEnvParams.from_dictionary(dictionary.get('physicalBackupParams')) if dictionary.get('physicalBackupParams') else None
        s3_backup_job_params = cohesity_management_sdk.models.s3_backup_job_params.S3BackupJobParams.from_dictionary(dictionary.get('s3BackupJobParams')) if dictionary.get('s3BackupJobParams') else None
        sfdc_backup_job_params = cohesity_management_sdk.models.sfdc_backup_job_params.SfdcBackupJobParams.from_dictionary(dictionary.get('sfdcBackupJobParams')) if dictionary.get('sfdcBackupJobParams') else None
        snapshot_manager_params = cohesity_management_sdk.models.snapshot_manager_params.SnapshotManagerParams.from_dictionary(dictionary.get('snapshotManagerParams')) if dictionary.get('snapshotManagerParams') else None
        sql_backup_job_params = cohesity_management_sdk.models.sql_backup_job_params.SqlBackupJobParams.from_dictionary(dictionary.get('sqlBackupJobParams')) if dictionary.get('sqlBackupJobParams') else None
        uda_backup_job_params = cohesity_management_sdk.models.uda_backup_job_params.UdaBackupJobParams.from_dictionary(dictionary.get('udaBackupJobParams')) if dictionary.get('udaBackupJobParams') else None
        vmware_backup_params = cohesity_management_sdk.models.vmware_backup_env_params.VmwareBackupEnvParams.from_dictionary(dictionary.get('vmwareBackupParams')) if dictionary.get('vmwareBackupParams') else None

        # Return an object of this model
        return cls(
            acropolis_backup_job_params,
            aws_native_env_params,
            exchange_backup_job_params,
            externally_triggered_job_params,
            file_stubbing_params,
            file_uptiering_params,
            gcp_native_job_params,
            hyperv_backup_params,
            isilon_env_params,
            kubernetes_env_params,
            nas_analysis_job_params,
            nas_backup_params,
            nosql_backup_job_params,
            o_365_backup_params,
            oracle_backup_job_params,
            outlook_backup_params,
            physical_backup_params,
            s3_backup_job_params,
            sfdc_backup_job_params,
            snapshot_manager_params,
            sql_backup_job_params,
            uda_backup_job_params,
            vmware_backup_params
)