# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.pod_metadata
import cohesity_management_sdk.models.rename_object_param_proto


class RestoreKubernetesNamespacesParams(object):

    """Implementation of the 'RestoreKubernetesNamespacesParams' model.

    TODO: type description here.


    Attributes:

        backup_cluster_id (long|int): Cluster id of the cluster which performed
            the backup.
        backup_job_name (string): Backup job that needs to be used for
            recovering the namespace.
        cluster_entity (EntityProto): This field is optional for a
            kRecoverNamespaces task if the namespace is being restored to its
            original parent source. If not specified, restored namespace will
            be attached to its original cluster. This field is mandatory if the
            namespace is being restored to a different parent source.
        cluster_software_version (string): Cluster software version.
        init_container_image (string): Container image used to mounting PVCs in
            temp pods.
        is_protection_using_datamover_enabled (bool): This indicates if
            magneto_kubernetes_enable_protection_using_datamover is true and
            the flag is enabled in the feature enabler.
        management_namespace (string): Namespace in which restore job will be
            created in K8s cluster.
        pod_metadata_vec (list of PodMetadata): Information about pods in the
            namespace which was backed up.
        rename_restored_object_param (RenameObjectParamProto): By default,
            namespaces are restored with their original name. This field can be
            used to specify the transformation ( i.e prefix/suffix) to be
            applied to the source namespace to derive the new name of the
            restored namespace.
        s3_account_id (string): S3 account ID that was used to register the
            source.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_cluster_id":'backupClusterId',
        "backup_job_name":'backupJobName',
        "cluster_entity":'clusterEntity',
        "cluster_software_version":'clusterSoftwareVersion',
        "init_container_image":'initContainerImage',
        "is_protection_using_datamover_enabled":'isProtectionUsingDatamoverEnabled',
        "management_namespace":'managementNamespace',
        "pod_metadata_vec":'podMetadataVec',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "s3_account_id":'s3AccountId',
    }
    def __init__(self,
                 backup_cluster_id=None,
                 backup_job_name=None,
                 cluster_entity=None,
                 cluster_software_version=None,
                 init_container_image=None,
                 is_protection_using_datamover_enabled=None,
                 management_namespace=None,
                 pod_metadata_vec=None,
                 rename_restored_object_param=None,
                 s3_account_id=None,
            ):

        """Constructor for the RestoreKubernetesNamespacesParams class"""

        # Initialize members of the class
        self.backup_cluster_id = backup_cluster_id
        self.backup_job_name = backup_job_name
        self.cluster_entity = cluster_entity
        self.cluster_software_version = cluster_software_version
        self.init_container_image = init_container_image
        self.is_protection_using_datamover_enabled = is_protection_using_datamover_enabled
        self.management_namespace = management_namespace
        self.pod_metadata_vec = pod_metadata_vec
        self.rename_restored_object_param = rename_restored_object_param
        self.s3_account_id = s3_account_id

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
        backup_cluster_id = dictionary.get('backupClusterId')
        backup_job_name = dictionary.get('backupJobName')
        cluster_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('clusterEntity')) if dictionary.get('clusterEntity') else None
        cluster_software_version = dictionary.get('clusterSoftwareVersion')
        init_container_image = dictionary.get('initContainerImage')
        is_protection_using_datamover_enabled = dictionary.get('isProtectionUsingDatamoverEnabled')
        management_namespace = dictionary.get('managementNamespace')
        pod_metadata_vec = None
        if dictionary.get('podMetadataVec') != None:
            pod_metadata_vec = list()
            for structure in dictionary.get('podMetadataVec'):
                pod_metadata_vec.append(cohesity_management_sdk.models.pod_metadata.PodMetadata.from_dictionary(structure))
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        s3_account_id = dictionary.get('s3AccountId')

        # Return an object of this model
        return cls(
            backup_cluster_id,
            backup_job_name,
            cluster_entity,
            cluster_software_version,
            init_container_image,
            is_protection_using_datamover_enabled,
            management_namespace,
            pod_metadata_vec,
            rename_restored_object_param,
            s3_account_id
)