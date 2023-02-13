# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.rename_object_param_proto

class VMwareStandbyResource(object):

    """Implementation of the 'VMwareStandbyResource' model.

    VMware specific resources needed to create a VM entity on the vCenter.

    Attributes:
        datastore_entity_vec (list of EntityProto): Datastore entities where
            the standby VM should be created.
        network_config (RestoredObjectNetworkConfigProto): Network
            configuration for the standby VM.
        parent_source (EntityProto): The vCenter to which the user wants to
            create a standby VM.
        rename_object_params (RenameObjectParamProto): User defined prefix and
            suffix that need to be added to the standby VM.
        resource_pool_entity (EntityProto): Resource pool entity where the
            standby VM should be created.
        target_datastore_folder (EntityProto): Folder where the VM disks
            should be placed.
        target_vm_folder (EntityProto): Folder where the VMs should be created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datastore_entity_vec": 'datastoreEntityVec',
        "network_config": 'networkConfig',
        "parent_source": 'parentSource',
        "rename_object_params":'renameObjectParams',
        "resource_pool_entity":'resourcePoolEntity',
        "target_datastore_folder":'targetDatastoreFolder',
        "target_vm_folder":'targetVmFolder'
    }

    def __init__(self,
                 datastore_entity_vec=None,
                 network_config=None,
                 parent_source=None,
                 rename_object_params=None,
                 resource_pool_entity=None,
                 target_datastore_folder=None,
                 target_vm_folder=None
                 ):
        """Constructor for the VMwareStandbyResource class"""

        # Initialize members of the class
        self.datastore_entity_vec = datastore_entity_vec
        self.network_config = network_config
        self.parent_source = parent_source
        self.rename_object_params = rename_object_params
        self.resource_pool_entity = resource_pool_entity
        self.target_datastore_folder = target_datastore_folder
        self.target_vm_folder = target_vm_folder

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
        datastore_entity_vec = None
        if dictionary.get('datastoreEntityVec') != None:
            datastore_entity_vec = list()
            for structure in dictionary.get('datastoreEntityVec'):
                datastore_entity_vec.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig')else None
        parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        rename_object_params = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameObjectParams')) if dictionary.get('renameObjectParams') else None
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        target_datastore_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetDatastoreFolder')) if dictionary.get('targetDatastoreFolder') else None
        target_vm_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetVmFolder')) if dictionary.get('targetVmFolder') else None

        # Return an object of this model
        return cls(datastore_entity_vec,
                   network_config,
                   parent_source,
                   rename_object_params,
                   resource_pool_entity,
                   target_datastore_folder,
                   target_vm_folder)


