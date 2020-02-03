# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.rename_object_param_proto

class RestoreKubernetesNamespacesParams(object):

    """Implementation of the 'RestoreKubernetesNamespacesParams' model.

    TODO: type model description here.

    Attributes:
        backup_job_name (string): Backup job that needs to be used for
            recovering the namespace.
        cluster_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        management_namespace (string): Namespace in which restore job will be
            created in K8s cluster.
        rename_restored_object_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_job_name":'backupJobName',
        "cluster_entity":'clusterEntity',
        "management_namespace":'managementNamespace',
        "rename_restored_object_param":'renameRestoredObjectParam'
    }

    def __init__(self,
                 backup_job_name=None,
                 cluster_entity=None,
                 management_namespace=None,
                 rename_restored_object_param=None):
        """Constructor for the RestoreKubernetesNamespacesParams class"""

        # Initialize members of the class
        self.backup_job_name = backup_job_name
        self.cluster_entity = cluster_entity
        self.management_namespace = management_namespace
        self.rename_restored_object_param = rename_restored_object_param


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
        backup_job_name = dictionary.get('backupJobName')
        cluster_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('clusterEntity')) if dictionary.get('clusterEntity') else None
        management_namespace = dictionary.get('managementNamespace')
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None

        # Return an object of this model
        return cls(backup_job_name,
                   cluster_entity,
                   management_namespace,
                   rename_restored_object_param)


