# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto

class RestoreKVMVMsParams(object):

    """Implementation of the 'RestoreKVMVMsParams' model.

    TODO: type model description here.

    Attributes:
        cluster_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        datacenter_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        power_state_config (PowerStateConfigProto): TODO: type description
            here.
        rename_restored_object_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            TODO: type description here.
        storagedomain_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_entity":'clusterEntity',
        "datacenter_entity":'datacenterEntity',
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "storagedomain_entity":'storagedomainEntity'
    }

    def __init__(self,
                 cluster_entity=None,
                 datacenter_entity=None,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 restored_objects_network_config=None,
                 storagedomain_entity=None):
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
        return cls(cluster_entity,
                   datacenter_entity,
                   power_state_config,
                   rename_restored_object_param,
                   restored_objects_network_config,
                   storagedomain_entity)


