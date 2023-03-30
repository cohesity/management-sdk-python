# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_backup_source_params
import cohesity_management_sdk.models.aws_native_backup_source_params
import cohesity_management_sdk.models.aws_snapshot_manager_backup_source_params
import cohesity_management_sdk.models.hyperv_backup_source_params
import cohesity_management_sdk.models.oracle_source_params
import cohesity_management_sdk.models.physical_backup_source_params
import cohesity_management_sdk.models.sfdc_backup_source_params_proto
import cohesity_management_sdk.models.sharepoint_backup_source_params
import cohesity_management_sdk.models.vmware_backup_source_params


class BackupSourceParams(object):

    """Implementation of the 'BackupSourceParams' model.

    Message to capture any additional backup params at the source level.


    Attributes:

        acropolis_params (AcropolisBackupSourceParams): This is applicable to
            sources of type kVirtualMachine (kAcropolis environment).
        app_entity_id_vec (list of long|int): If we are backing up an
            application (such as SQL), this contains the entity ids of the app
            entities (such as SQL instances and databases) that will be
            protected on the backup source.  If this vector is empty, it
            implies that we are protecting all app entities on the source.
        aws_native_params (AWSNativeBackupSourceParams): This is applicable to
            sources of type kAWS with native backup.
        aws_snapshot_manager_params (AWSSnapshotManagerBackupSourceParams):
            This is applicable to sources of type kAWS with snapshot manager
            backup.
        hyperv_params (HyperVBackupSourceParams): This is applicable to sources
            of type kVirtualMachine (kHyperV environment).
        oracle_params (OracleSourceParams): This is applicable to sources of
            type kOracle databases. These are additional backup parameters for
            kOracle. NOTE: For logging this proto use
            GetProtoString(oracle_params); to remove credentials from DB
            information.
        physical_params (PhysicalBackupSourceParams): This is applicable to
            sources of type kHost (kPhysical environment).
        sfdc_params (SfdcBackupSourceParamsProto): This is applicable to
            sources of type kSfdc.
        sharepoint_params (SharepointBackupSourceParams): This is applicable to
            sources of type kSite in o365 domain.
        skip_indexing (bool): Set to true, if indexing is not required for
            given source.
        source_id (long|int): Source entity id. NOTE: This is expected to point
            to a leaf-level entity.
        vmware_params (VMwareBackupSourceParams): This is applicable to sources
            of type kVirtualMachine (kVMware environment).
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "acropolis_params":'acropolisParams',
        "app_entity_id_vec":'appEntityIdVec',
        "aws_native_params":'awsNativeParams',
        "aws_snapshot_manager_params":'awsSnapshotManagerParams',
        "hyperv_params":'hypervParams',
        "oracle_params":'oracleParams',
        "physical_params":'physicalParams',
        "sfdc_params":'sfdcParams',
        "sharepoint_params":'sharepointParams',
        "skip_indexing":'skipIndexing',
        "source_id":'sourceId',
        "vmware_params":'vmwareParams',
    }
    def __init__(self,
                 acropolis_params=None,
                 app_entity_id_vec=None,
                 aws_native_params=None,
                 aws_snapshot_manager_params=None,
                 hyperv_params=None,
                 oracle_params=None,
                 physical_params=None,
                 sfdc_params=None,
                 sharepoint_params=None,
                 skip_indexing=None,
                 source_id=None,
                 vmware_params=None,
            ):

        """Constructor for the BackupSourceParams class"""

        # Initialize members of the class
        self.acropolis_params = acropolis_params
        self.app_entity_id_vec = app_entity_id_vec
        self.aws_native_params = aws_native_params
        self.aws_snapshot_manager_params = aws_snapshot_manager_params
        self.hyperv_params = hyperv_params
        self.oracle_params = oracle_params
        self.physical_params = physical_params
        self.sfdc_params = sfdc_params
        self.sharepoint_params = sharepoint_params
        self.skip_indexing = skip_indexing
        self.source_id = source_id
        self.vmware_params = vmware_params

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
        acropolis_params = cohesity_management_sdk.models.acropolis_backup_source_params.AcropolisBackupSourceParams.from_dictionary(dictionary.get('acropolisParams')) if dictionary.get('acropolisParams') else None
        app_entity_id_vec = dictionary.get("appEntityIdVec")
        aws_native_params = cohesity_management_sdk.models.aws_native_backup_source_params.AWSNativeBackupSourceParams.from_dictionary(dictionary.get('awsNativeParams')) if dictionary.get('awsNativeParams') else None
        aws_snapshot_manager_params = cohesity_management_sdk.models.aws_snapshot_manager_backup_source_params.AWSSnapshotManagerBackupSourceParams.from_dictionary(dictionary.get('awsSnapshotManagerParams')) if dictionary.get('awsSnapshotManagerParams') else None
        hyperv_params = cohesity_management_sdk.models.hyperv_backup_source_params.HyperVBackupSourceParams.from_dictionary(dictionary.get('hypervParams')) if dictionary.get('hypervParams') else None
        oracle_params = cohesity_management_sdk.models.oracle_source_params.OracleSourceParams.from_dictionary(dictionary.get('oracleParams')) if dictionary.get('oracleParams') else None
        physical_params = cohesity_management_sdk.models.physical_backup_source_params.PhysicalBackupSourceParams.from_dictionary(dictionary.get('physicalParams')) if dictionary.get('physicalParams') else None
        sfdc_params = cohesity_management_sdk.models.sfdc_backup_source_params_proto.SfdcBackupSourceParamsProto.from_dictionary(dictionary.get('sfdcParams')) if dictionary.get('sfdcParams') else None
        sharepoint_params = cohesity_management_sdk.models.sharepoint_backup_source_params.SharepointBackupSourceParams.from_dictionary(dictionary.get('sharepointParams')) if dictionary.get('sharepointParams') else None
        skip_indexing = dictionary.get('skipIndexing')
        source_id = dictionary.get('sourceId')
        vmware_params = cohesity_management_sdk.models.vmware_backup_source_params.VMwareBackupSourceParams.from_dictionary(dictionary.get('vmwareParams')) if dictionary.get('vmwareParams') else None

        # Return an object of this model
        return cls(
            acropolis_params,
            app_entity_id_vec,
            aws_native_params,
            aws_snapshot_manager_params,
            hyperv_params,
            oracle_params,
            physical_params,
            sfdc_params,
            sharepoint_params,
            skip_indexing,
            source_id,
            vmware_params
)