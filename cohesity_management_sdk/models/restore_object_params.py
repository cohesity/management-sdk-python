# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restored_object_network_config_proto


class RestoreObjectParams(object):

    """Implementation of the 'RestoreObjectParams' model.

    TODO: type description here.


    Attributes:

        action (int): The action to perform.
        datastore_entity (EntityProto): A datastore entity where the object's
            files should be restored to. This field is optional if object is
            being restored to its original parent source. If not specified, the
            object's files will be restored to their original datastore
            locations. This field is mandatory if object is being restored to a
            different resource pool or to a different parent source.
        power_state_config (PowerStateConfigProto): Semantics for kCloneVMs
            task: By default, objects are restored in the powered off state. 
            Semantics for kRecoverVMs task: By default, objects are restored in
            the powered on state.  This proto can be used to override the
            default behavior for kCloneVMs or kRecoverVMs task.
        rename_restored_object_param (RenameObjectParamProto): By default,
            objects are restored with their original name. This field can be
            used to specify the transformation ( i.e prefix/suffix) to be
            applied to the source object name to derive the new name of the
            restored object.
        resource_pool_entity (EntityProto): This field is optional for a
            kRecoverVMs task if the objects are being restored to its original
            parent source. If not specified, restored objects will be attached
            to its original resource entity. This field is mandatory if objects
            are being restored to a different parent source.
        restore_parent_source (EntityProto): An optional registered parent
            source to which objects are to be restored. If not specified,
            objects are restored back to the original source that was managing
            the objects.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            Semantics for kCloneVMs task: By default, if objects are being
            restored to their original location, then network will be disabled.
            If objects are being restored to a different location (i.e., either
            to different resource pool or to different parent source), then
            network will be detached.  Semantics for kRecoverVMs task: By
            default, if objects are being restored to their original location,
            then original network configuration will be preserved. If objects
            are being restored to different location, (i.e., either to
            different resource pool or to different parent source), then
            network will be detached.  Below field can be used to override the
            default network configuration of the restored objects.  If user
            want to keep the original network setting for kRecoverVMs task,
            then this proto should not be set.
        view_name (string): Target view into which the objects are to be
            cloned.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "action":'action',
        "datastore_entity":'datastoreEntity',
        "power_state_config":'powerStateConfig',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "resource_pool_entity":'resourcePoolEntity',
        "restore_parent_source":'restoreParentSource',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "view_name":'viewName',
    }
    def __init__(self,
                 action=None,
                 datastore_entity=None,
                 power_state_config=None,
                 rename_restored_object_param=None,
                 resource_pool_entity=None,
                 restore_parent_source=None,
                 restored_objects_network_config=None,
                 view_name=None,
            ):

        """Constructor for the RestoreObjectParams class"""

        # Initialize members of the class
        self.action = action
        self.datastore_entity = datastore_entity
        self.power_state_config = power_state_config
        self.rename_restored_object_param = rename_restored_object_param
        self.resource_pool_entity = resource_pool_entity
        self.restore_parent_source = restore_parent_source
        self.restored_objects_network_config = restored_objects_network_config
        self.view_name = view_name

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
        action = dictionary.get('action')
        datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('datastoreEntity')) if dictionary.get('datastoreEntity') else None
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        restore_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreParentSource')) if dictionary.get('restoreParentSource') else None
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(
            action,
            datastore_entity,
            power_state_config,
            rename_restored_object_param,
            resource_pool_entity,
            restore_parent_source,
            restored_objects_network_config,
            view_name
)