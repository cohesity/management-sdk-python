# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_info_proto_restore_entity
import cohesity_management_sdk.models.script_execution_status


class RestoreInfoProto(object):

    """Implementation of the 'RestoreInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined. The
    extension applies to both RestoreInfoProto as well as RestoreEntity. 
    RestoreInfoProto extension                     Location           
    Extension
    =============================================================================
    vmware::RestoreInfo::vmware_restore_info     vmware/vmware.proto       100
    sql::RestoreInfo::sql_restore_info           sql/sql.proto             101
    pure::RestoreInfo::pure_restore_info         pure/pure.proto           102
    azure::RestoreInfo::azure_restore_info       azure/azure.proto         103
    file::RestoreInfo::file_restore_info         file/file.proto           104
    hyperv::RestoreInfo::hyperv_restore_info     hyperv/hyperv.proto       105
    acropolis::RestoreInfo::acropolis_restore_info acropolis/acropolis.proto
    106 kvm::RestoreInfo::kvm_restore_info           kvm/kvm.proto            
    107 aws::RestoreInfo::aws_restore_info           aws/aws.proto            
    108 physical::RestoreInfo::physical_restore_info physical.proto           
    109 oracle::RestoreInfo::oracle_restore_info     oracle/oracle.proto      
    110 outlook::RestoreInfo::outlook_restore_info   outlook/outlook.proto    
    111 gcp::RestoreInfo::gcp_restore_info           gcp/gcp.proto            
    112 ad::RestoreInfo::ad_restore_info             ad/ad.proto              
    113 kubernetes::RestoreInfo::kubernetes_restore_info
    kubernetes/kubernetes.proto 114
    one_drive::RestoreInfo::one_drive_restore_info ms_graph/graph.proto     
    115 cdp::RestoreInfo::cdp_restore_info           cdp.proto                
    116 exchange::RestoreInfo::exchange_restore_info exchange/exchange.proto  
    117 imanis::RestoreInfo::nosql_recovery_info     imanis/nosql.proto       
    118 o365::RestoreInfo::o365_restore_info o365/o365.proto      119
    o365::RestoreInfo::o365_one_drive_restore_info o365/o365.proto      120
    o365::PublicFolderRestoreInfoProto::public_folder_restore_info
    o365/o365.proto            121 uda::RestoreInfo::uda_recovery_info         
    uda/uda.proto              122 outlook::RestoreInfo::pst_convert_info      
    outlook/outlook.proto      123 o365::GroupRestoreInfo::group_restore_info  
    o365/o365.proto            124
    o365::TeamsRestoreInfoProto::teams_restore_info o365/o365.proto           
    125
    =============================================================================
    RestoreInfoProto.RestoreEntity extension       Location           
    Extension
    =============================================================================
    vmware::RestoreEntityInfo::vmware_restore_entity_info vmware/vmware.proto  
    100 azure::CloudDeployEntityInfo::azure_restore_entity_info
    azure/azure.proto          101
    hyperv::RestoreEntityInfo::hyperv_restore_entity_info hyperv/hyperv.proto  
    102 acropolis::RestoreEntityInfo::acropolis_restore_entity_info
    acropolis/acropolis.proto  103
    kvm::RestoreEntityInfo::kvm_restore_entity_info kvm/kvm.proto             
    104 aws::CloudDeployEntityInfo::aws_restore_entity_info aws/aws.proto      
    105 outlook::RestoreEntityInfo::outlook_restore_entity_info
    outlook/outlook.proto      106
    gcp::CloudDeployEntityInfo::gcp_restore_entity_info gcp/gcp.proto          
    107 kubernetes::RestoreEntityInfo::kubernetes_restore_entity_info
    kuebrnetes/kubernetes.proto 108
    one_drive::RestoreEntityInfo::one_drive_restore_entity_info
    ms_graph/graph.proto       109
    imanis::RestoreEntityInfo::nosql_restore_entity_info imanis/nosql.proto    
    110 site::RestoreEntityInfo::site_restore_entity_info ms_graph/graph.proto 
    111 uda::RestoreEntityInfo::uda_restore_entity_info uda/uda.proto          
    112
    =============================================================================


    Attributes:

        post_script_status (ScriptExecutionStatus): Captures the execution
            status of post script.
        pre_script_status (ScriptExecutionStatus): Captures the execution
            status of pre script.
        restore_entity_vec (list of RestoreInfoProto_RestoreEntity): Contains
            the file paths and the information of the restored entities.
        target_type (int): Specifies the target type for the task. The field is
            only valid if the task has got a permit.
        mtype (int): The type of environment this restore info pertains to.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "post_script_status":'postScriptStatus',
        "pre_script_status":'preScriptStatus',
        "restore_entity_vec":'restoreEntityVec',
        "target_type":'targetType',
        "mtype":'type',
    }
    def __init__(self,
                 post_script_status=None,
                 pre_script_status=None,
                 restore_entity_vec=None,
                 target_type=None,
                 mtype=None,
            ):

        """Constructor for the RestoreInfoProto class"""

        # Initialize members of the class
        self.post_script_status = post_script_status
        self.pre_script_status = pre_script_status
        self.restore_entity_vec = restore_entity_vec
        self.target_type = target_type
        self.mtype = mtype

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
        post_script_status = cohesity_management_sdk.models.script_execution_status.ScriptExecutionStatus.from_dictionary(dictionary.get('postScriptStatus')) if dictionary.get('postScriptStatus') else None
        pre_script_status = cohesity_management_sdk.models.script_execution_status.ScriptExecutionStatus.from_dictionary(dictionary.get('preScriptStatus')) if dictionary.get('preScriptStatus') else None
        restore_entity_vec = None
        if dictionary.get('restoreEntityVec') != None:
            restore_entity_vec = list()
            for structure in dictionary.get('restoreEntityVec'):
                restore_entity_vec.append(cohesity_management_sdk.models.restore_info_proto_restore_entity.RestoreInfoProto_RestoreEntity.from_dictionary(structure))
        target_type = dictionary.get('targetType')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            post_script_status,
            pre_script_status,
            restore_entity_vec,
            target_type,
            mtype
)