# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_deploy_info_proto_cloud_deploy_entity
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.restore_info_proto


class CloudDeployInfoProto(object):

    """Implementation of the 'CloudDeployInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined. The
    extension applies to both CloudDeployInfoProto as well as
    CloudDeployEntity.  CloudDeployInfoProto extension                 
    Location           Extension
    =============================================================================
    aws::CloudDeployInfo::aws_cloud_deploy_info     aws/aws.proto           
    100 azure::CloudDeployInfo::azure_cloud_deploy_info azure/azure.proto      
    101 gcp::CloudDeployInfo::gcp_cloud_deploy_info     gcp/gcp.proto          
    102 aws::ReplicationInfo::aws_replication_info      aws/aws.proto          
    103 azure::ReplicationInfo::azure_replication_info  azure/azure.proto      
    104
    =============================================================================
    CloudDeployInfoProto.CloudDeployEntity extension  Location        
    Extension
    =============================================================================
    aws::CloudDeployEntityInfo::aws_cloud_deploy_entity_info aws/aws.proto     
    100 vmware::RestoreEntityInfo::vmware_cloud_deploy_entity_info
    vmware/vmware.proto    101
    azure::CloudDeployEntityInfo::azure_cloud_deploy_entity_info
    azure/azure.proto      102
    gcp::CloudDeployEntityInfo::gcp_cloud_deploy_entity_info gcp/gcp.proto     
    103 hyperv::RestoreEntityInfo::hyperv_cloud_deploy_entity_info
    hyperv/hyperv.proto    104
    aws::ReplicationEntityInfo::aws_replication_entity_info aws/aws.proto      
    105 aws::ReplicationEntityInfo::azure_replication_entity_info
    azure/azure.proto      106
    =============================================================================


    Attributes:

        cloud_deploy_entity_vec (list of
            CloudDeployInfoProto_CloudDeployEntity): Contains the file paths
            and the information of the entities deployed to cloud.
        is_incremental (bool): Whether this Cloud deploy info is for
            incremental cloudspin.
        restore_info (RestoreInfoProto): This will be filled by some restore
            ops to checkpoint their restore state.
        target_type (int): Specifies the target type for the task. The field is
            only valid if the task has got a permit.
        total_bytes_transferred_to_source (long|int): Total bytes transferred
            to source.
        mtype (int): The type of environment this cloud deploy info pertains
            to.
        warnings (list of ErrorProto): Warnings if any. These warnings will be
            propogated to the UI by master.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_deploy_entity_vec":'cloudDeployEntityVec',
        "is_incremental":'isIncremental',
        "restore_info":'restoreInfo',
        "target_type":'targetType',
        "total_bytes_transferred_to_source":'totalBytesTransferredToSource',
        "mtype":'type',
        "warnings":'warnings',
    }
    def __init__(self,
                 cloud_deploy_entity_vec=None,
                 is_incremental=None,
                 restore_info=None,
                 target_type=None,
                 total_bytes_transferred_to_source=None,
                 mtype=None,
                 warnings=None,
            ):

        """Constructor for the CloudDeployInfoProto class"""

        # Initialize members of the class
        self.cloud_deploy_entity_vec = cloud_deploy_entity_vec
        self.is_incremental = is_incremental
        self.restore_info = restore_info
        self.target_type = target_type
        self.total_bytes_transferred_to_source = total_bytes_transferred_to_source
        self.mtype = mtype
        self.warnings = warnings

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
        cloud_deploy_entity_vec = None
        if dictionary.get('cloudDeployEntityVec') != None:
            cloud_deploy_entity_vec = list()
            for structure in dictionary.get('cloudDeployEntityVec'):
                cloud_deploy_entity_vec.append(cohesity_management_sdk.models.cloud_deploy_info_proto_cloud_deploy_entity.CloudDeployInfoProto_CloudDeployEntity.from_dictionary(structure))
        is_incremental = dictionary.get('isIncremental')
        restore_info = cohesity_management_sdk.models.restore_info_proto.RestoreInfoProto.from_dictionary(dictionary.get('restoreInfo')) if dictionary.get('restoreInfo') else None
        target_type = dictionary.get('targetType')
        total_bytes_transferred_to_source = dictionary.get('totalBytesTransferredToSource')
        mtype = dictionary.get('type')
        warnings = None
        if dictionary.get('warnings') != None:
            warnings = list()
            for structure in dictionary.get('warnings'):
                warnings.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cloud_deploy_entity_vec,
            is_incremental,
            restore_info,
            target_type,
            total_bytes_transferred_to_source,
            mtype,
            warnings
)