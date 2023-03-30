# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto


class RestoreKVMVMsParams(object):

    """Implementation of the 'RestoreKVMVMsParams' model.

    TODO: type description here.


    Attributes:

        cluster_entity (EntityProto): This field is optional for a kRecoverVMs
            task if the VMs are being restored to its original parent source.
            If not specified, restored VMs will be attached to its original
            host. This field is mandatory if the VMs are being restored to a
            different parent source.
        datacenter_entity (EntityProto): A datacenter where the VM's files
            should be restored to. This field is optional if VM is being
            restored to its original parent source. If not specified, the VM's
            files will be restored to their original datacenter locations. This
            field is mandatory if VM is being restored to a different
            datacenter entity or to a different parent source.
        power_state_config (PowerStateConfigProto): Semantics for kRecoverVMs
            task: By default, VMs are restored in their original power state. 
            This proto can be used to override the default behavior for the
            restore task.
        rename_restored_object_param (RenameObjectParamProto): By default, VMs
            are restored with their original name. This field can be used to
            specify the transformation ( i.e prefix/suffix) to be applied to
            the source VM name to derive the new name of the restored VM.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            Semantics for kRecoverVMs task: By default, if the VMs are being
            restored to their original location, then original network
            configuration will be preserved. If objects are being restored to
            different location (i.e., different parent source), then network
            will be detached.  Below field can be used to override the default
            network configuration of the restored VMs.  If user want to keep
            the original network setting for kRecoverVMs task, then this proto
            should not be set.
        storagedomain_entity (EntityProto): A storagedomain where the VM's disk
            should be restored to. This field is optional if VM is being
            restored to its original parent source. If not specified, the VM's
            disk will be restored to their original storagedomain. This field
            is mandatory if VM is being restored to a different resource entity
            or to a different parent source.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_entity":'clusterEntity',
        "datacenter_entity":'datacenterEntity',
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "storagedomain_entity":'storagedomainEntity',
    }
    def __init__(self,
                 cluster_entity=None,
                 datacenter_entity=None,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 restored_objects_network_config=None,
                 storagedomain_entity=None,
            ):

        """Constructor for the RestoreKVMVMsParams class"""

        # Initialize members of the class
        self.cluster_entity = cluster_entity
        self.datacenter_entity = datacenter_entity
        self.power_state_config = power_state_config
        self.rename_restored_object_param = rename_restored_object_param
        self.restored_objects_network_config = restored_objects_network_config
        self.storagedomain_entity = storagedomain_entity

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
        cluster_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('clusterEntity')) if dictionary.get('clusterEntity') else None
        datacenter_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('datacenterEntity')) if dictionary.get('datacenterEntity') else None
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        storagedomain_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storagedomainEntity')) if dictionary.get('storagedomainEntity') else None

        # Return an object of this model
        return cls(
            cluster_entity,
            datacenter_entity,
            power_state_config,
            rename_restored_object_param,
            restored_objects_network_config,
            storagedomain_entity
)