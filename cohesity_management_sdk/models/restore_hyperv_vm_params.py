# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.uuid_config_proto


class RestoreHyperVVMParams(object):

    """Implementation of the 'RestoreHyperVVMParams' model.

    TODO: type description here.


    Attributes:

        copy_recovery (bool): Whether to perform copy recovery.
        datastore_entity (EntityProto): A datastore entity where the object's
            files should be restored to. This field is optional if object is
            being restored to its original parent source. If not specified, the
            object's files will be restored to their original datastore
            locations. This field is mandatory if object is being restored to a
            different resource entity or to a different parent source.
        power_state_config (PowerStateConfigProto): Semantics for kRecoverVMs
            task: By default, VMs are restored in their original power state. 
            This proto can be used to override the default behavior for the
            restore task.
        rename_restored_object_param (RenameObjectParamProto): By default, VMs
            are restored with their original name. This field can be used to
            specify the transformation ( i.e prefix/suffix) to be applied to
            the source VM name to derive the new name of the restored VM.
        resource_entity (EntityProto): This field is optional for a kRecoverVMs
            task if the VMs are being restored to its original parent source.
            If not specified, restored VMs will be attached to its original
            host. This field is mandatory if the VMs are being restored to a
            different parent source.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            Semantics for kRecoverVMs task: By default, if the VMs are being
            restored to their original location, then original network
            configuration will be preserved. If objects are being restored to
            different location (i.e., different parent source), then network
            will be detached.  Below field can be used to override the default
            network configuration of the restored VMs.  If user want to keep
            the original network setting for kRecoverVMs task, then this proto
            should not be set.
        use_smb_service (bool): Whether to recover via Cohesity SMB service.
        uuid_config (UuidConfigProto): Semantics for kRecoverVMs task: By
            default, recovered VMs have new UUIDs for them.  This proto can be
            used to override the default behavior for the restore task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "copy_recovery":'copyRecovery',
        "datastore_entity":'datastoreEntity',
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "resource_entity":'resourceEntity',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "use_smb_service":'useSmbService',
        "uuid_config":'uuidConfig',
    }
    def __init__(self,
                 copy_recovery=None,
                 datastore_entity=None,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 resource_entity=None,
                 restored_objects_network_config=None,
                 use_smb_service=None,
                 uuid_config=None,
            ):

        """Constructor for the RestoreHyperVVMParams class"""

        # Initialize members of the class
        self.copy_recovery = copy_recovery
        self.datastore_entity = datastore_entity
        self.power_state_config = power_state_config
        self.rename_restored_object_param = rename_restored_object_param
        self.resource_entity = resource_entity
        self.restored_objects_network_config = restored_objects_network_config
        self.use_smb_service = use_smb_service
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
        use_smb_service = dictionary.get('useSmbService')
        uuid_config = cohesity_management_sdk.models.uuid_config_proto.UuidConfigProto.from_dictionary(dictionary.get('uuidConfig')) if dictionary.get('uuidConfig') else None

        # Return an object of this model
        return cls(
            copy_recovery,
            datastore_entity,
            power_state_config,
            rename_restored_object_param,
            resource_entity,
            restored_objects_network_config,
            use_smb_service,
            uuid_config
)