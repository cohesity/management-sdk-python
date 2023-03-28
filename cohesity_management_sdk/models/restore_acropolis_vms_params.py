# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.uuid_config_proto


class RestoreAcropolisVMsParams(object):

    """Implementation of the 'RestoreAcropolisVMsParams' model.

    TODO: type description here.


    Attributes:

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
        storage_container (EntityProto): A storage container where the VM's
            files should be restored to. This field is optional if the VM is
            being restored to its original parent source. If not specified, the
            VM's files will be restored to their original storage container(s).
            This field is mandatory if the VMs are being restored to a
            different parent source.
        uuid_config (UuidConfigProto): Semantics for kRecoverVMs task: By
            default, recovered VMs have new UUIDs for them.  This proto can be
            used to override the default behavior for the restore task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "storage_container":'storageContainer',
        "uuid_config":'uuidConfig',
    }
    def __init__(self,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 restored_objects_network_config=None,
                 storage_container=None,
                 uuid_config=None,
            ):

        """Constructor for the RestoreAcropolisVMsParams class"""

        # Initialize members of the class
        self.power_state_config = power_state_config
        self.rename_restored_object_param = rename_restored_object_param
        self.restored_objects_network_config = restored_objects_network_config
        self.storage_container = storage_container
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
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        storage_container = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageContainer')) if dictionary.get('storageContainer') else None
        uuid_config = cohesity_management_sdk.models.uuid_config_proto.UuidConfigProto.from_dictionary(dictionary.get('uuidConfig')) if dictionary.get('uuidConfig') else None

        # Return an object of this model
        return cls(
            power_state_config,
            rename_restored_object_param,
            restored_objects_network_config,
            storage_container,
            uuid_config
)