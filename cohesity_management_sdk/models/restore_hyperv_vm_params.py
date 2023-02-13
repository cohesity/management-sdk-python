# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.uuid_config_proto

class RestoreHypervVMParams(object):

    """Implementation of the 'RestoreHyperVVMParams' model.

    TODO: type model description here.

    Attributes:
        copy_recovery (bool): Whether to perform copy recovery.
        datastore_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        power_state_config (PowerStateConfigProto): TODO: type description
            here.
        rename_restored_object_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.
        resource_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            TODO: type description here.
        uuid_config (UuidConfigProto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_recovery":'copyRecovery',
        "datastore_entity":'datastoreEntity',
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "resource_entity":'resourceEntity',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "uuid_config":'uuidConfig'
    }

    def __init__(self,
                 copy_recovery=None,
                 datastore_entity=None,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 resource_entity=None,
                 restored_objects_network_config=None,
                 uuid_config=None):
        """Constructor for the RestoreHypervVMParams class"""

        # Initialize members of the class
        self.copy_recovery = copy_recovery
        self.datastore_entity = datastore_entity
        self.power_state_config = power_state_config
        self.rename_restored_object_param = rename_restored_object_param
        self.resource_entity = resource_entity
        self.restored_objects_network_config = restored_objects_network_config
        self.uuid_config = uuid_config


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
        copy_recovery = dictionary.get('copyRecovery')
        datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('datastoreEntity')) if dictionary.get('datastoreEntity') else None
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        resource_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourceEntity')) if dictionary.get('resourceEntity') else None
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        uuid_config = cohesity_management_sdk.models.uuid_config_proto.UuidConfigProto.from_dictionary(dictionary.get('uuidConfig')) if dictionary.get('uuidConfig') else None

        # Return an object of this model
        return cls(copy_recovery,
                   datastore_entity,
                   power_state_config,
                   rename_restored_object_param,
                   resource_entity,
                   restored_objects_network_config,
                   uuid_config)


