# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.cloud_deploy_info_proto_cloud_deploy_entity
import cohesity_management_sdk.models.restore_info_proto

class CloudDeployInfoProto(object):

    """Implementation of the 'CloudDeployInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined. The
    extension applies to both CloudDeployInfoProto as well as
    CloudDeployEntity.
    CloudDeployInfoProto extension                  Location
    Extension
    ===========================================================================
    ==
    aws::CloudDeployInfo::aws_cloud_deploy_info     aws/aws.proto
    100
    azure::CloudDeployInfo::azure_cloud_deploy_info azure/azure.proto
    101
    gcp::CloudDeployInfo::gcp_cloud_deploy_info     gcp/gcp.proto
    102
    aws::ReplicationInfo::aws_replication_info      aws/aws.proto
    103
    azure::ReplicationInfo::azure_replication_info  azure/azure.proto
    104
    ===========================================================================
    ==
    CloudDeployInfoProto.CloudDeployEntity extension  Location
    Extension
    ===========================================================================
    ==
    aws::CloudDeployEntityInfo::aws_cloud_deploy_entity_info
    aws/aws.proto          100
    vmware::RestoreEntityInfo::vmware_cloud_deploy_entity_info
    vmware/vmware.proto    101
    azure::CloudDeployEntityInfo::azure_cloud_deploy_entity_info
    azure/azure.proto      102
    gcp::CloudDeployEntityInfo::gcp_cloud_deploy_entity_info
    gcp/gcp.proto          103
    hyperv::RestoreEntityInfo::hyperv_cloud_deploy_entity_info
    hyperv/hyperv.proto    104
    aws::ReplicationEntityInfo::aws_replication_entity_info
    aws/aws.proto          105
    aws::ReplicationEntityInfo::azure_replication_entity_info
    azure/azure.proto      106
    ===========================================================================
    ==

    Attributes:
        cloud_deploy_entity_vec (list of
            CloudDeployInfoProtoCloudDeployEntity): Contains the file paths
            and the information of the entities deployed to cloud.
        is_incremental (bool): Whether this Cloud deploy info is for
            incremental cloudspin.
        restore_info (RestoreInfoProto): Each available extension is listed
            below along with the location of the proto file (relative to
            magneto/connectors) where it is defined. The extension applies to
            both RestoreInfoProto as well as RestoreEntity.  RestoreInfoProto
            extension                     Location            Extension
            ===================================================================
            ========== vmware::RestoreInfo::vmware_restore_info
            vmware/vmware.proto       100 sql::RestoreInfo::sql_restore_info
            sql/sql.proto             101 pure::RestoreInfo::pure_restore_info
            pure/pure.proto           102
            azure::RestoreInfo::azure_restore_info       azure/azure.proto
            103 file::RestoreInfo::file_restore_info         file/file.proto
            104 hyperv::RestoreInfo::hyperv_restore_info
            hyperv/hyperv.proto       105
            acropolis::RestoreInfo::acropolis_restore_info
            acropolis/acropolis.proto 106 kvm::RestoreInfo::kvm_restore_info
            kvm/kvm.proto             107 aws::RestoreInfo::aws_restore_info
            aws/aws.proto             108
            physical::RestoreInfo::physical_restore_info physical.proto
            109 oracle::RestoreInfo::oracle_restore_info
            oracle/oracle.proto       110
            outlook::RestoreInfo::outlook_restore_info   outlook/outlook.proto
            111 gcp::RestoreInfo::gcp_restore_info           gcp/gcp.proto
            112 ad::RestoreInfo::ad_restore_info             ad/ad.proto
            113 kubernetes::RestoreInfo::kubernetes_restore_info
            kubernetes/kubernetes.proto 114
            one_drive::RestoreInfo::one_drive_restore_info
            ms_graph/graph.proto      115
            ===================================================================
            ==========  RestoreInfoProto.RestoreEntity extension
            Location            Extension
            ===================================================================
            ========== vmware::RestoreEntityInfo::vmware_restore_entity_info
            vmware/vmware.proto        100
            azure::RestoreEntityInfo::azure_restore_entity_info
            azure/azure.proto          101
            hyperv::RestoreEntityInfo::hyperv_restore_entity_info
            hyperv/hyperv.proto        102
            acropolis::RestoreEntityInfo::acropolis_restore_entity_info
            acropolis/acropolis.proto  103
            kvm::RestoreEntityInfo::kvm_restore_entity_info kvm/kvm.proto
            104 aws::RestoreEntityInfo::aws_restore_entity_info aws/aws.proto
            105 outlook::RestoreEntityInfo::outlook_restore_entity_info
            outlook/outlook.proto      106
            gcp::RestoreEntityInfo::gcp_restore_entity_info gcp/gcp.proto
            107 kubernetes::RestoreEntityInfo::kubernetes_restore_entity_info
            kuebrnetes/kubernetes.proto 108
            one_drive::RestoreEntityInfo::one_drive_restore_entity_info
            ms_graph/graph.proto       109
            ===================================================================
            ==========
        target_type (int): Specifies the target type for the task. The field
            is only valid if the task has got a permit.
        total_bytes_transferred_to_source (long|int): Total bytes transferred
            to source.
        mtype (int): The type of environment this cloud deploy info pertains
            to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_deploy_entity_vec":'cloudDeployEntityVec',
        "is_incremental":'isIncremental',
        "restore_info":'restoreInfo',
        "target_type":'targetType',
        "total_bytes_transferred_to_source":'totalBytesTransferredToSource',
        "mtype":'type'
    }

    def __init__(self,
                 cloud_deploy_entity_vec=None,
                 is_incremental=None,
                 restore_info=None,
                 target_type=None,
                 total_bytes_transferred_to_source=None,
                 mtype=None):
        """Constructor for the CloudDeployInfoProto class"""

        # Initialize members of the class
        self.cloud_deploy_entity_vec = cloud_deploy_entity_vec
        self.is_incremental = is_incremental
        self.restore_info = restore_info
        self.target_type = target_type
        self.total_bytes_transferred_to_source = total_bytes_transferred_to_source
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
        cloud_deploy_entity_vec = None
        if dictionary.get('cloudDeployEntityVec') != None:
            cloud_deploy_entity_vec = list()
            for structure in dictionary.get('cloudDeployEntityVec'):
                cloud_deploy_entity_vec.append(cohesity_management_sdk.models.cloud_deploy_info_proto_cloud_deploy_entity.CloudDeployInfoProtoCloudDeployEntity.from_dictionary(structure))
        is_incremental = dictionary.get('isIncremental')
        restore_info = cohesity_management_sdk.models.restore_info_proto.RestoreInfoProto.from_dictionary(dictionary.get('restoreInfo')) if dictionary.get('restoreInfo') else None
        target_type = dictionary.get('targetType')
        total_bytes_transferred_to_source = dictionary.get('totalBytesTransferredToSource')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cloud_deploy_entity_vec,
                   is_incremental,
                   restore_info,
                   target_type,
                   total_bytes_transferred_to_source,
                   mtype)


