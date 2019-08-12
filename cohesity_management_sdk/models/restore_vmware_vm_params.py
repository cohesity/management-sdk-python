# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class RestoreVmwareVMParams(object):

    """Implementation of the 'RestoreVMwareVMParams' model.

    TODO: type model description here.

    Attributes:
        copy_recovery (bool): Whether to perform copy recovery instead of
            instant recovery.
        datastore_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        preserve_tags_during_clone (bool): Whether to preserve tags for the
            clone op.
        resource_pool_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        target_datastore_folder (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        target_vm_folder (EntityProto): Specifies the attributes and the
            latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_recovery":'copyRecovery',
        "datastore_entity":'datastoreEntity',
        "preserve_tags_during_clone":'preserveTagsDuringClone',
        "resource_pool_entity":'resourcePoolEntity',
        "target_datastore_folder":'targetDatastoreFolder',
        "target_vm_folder":'targetVmFolder'
    }

    def __init__(self,
                 copy_recovery=None,
                 datastore_entity=None,
                 preserve_tags_during_clone=None,
                 resource_pool_entity=None,
                 target_datastore_folder=None,
                 target_vm_folder=None):
        """Constructor for the RestoreVmwareVMParams class"""

        # Initialize members of the class
        self.copy_recovery = copy_recovery
        self.datastore_entity = datastore_entity
        self.preserve_tags_during_clone = preserve_tags_during_clone
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
        copy_recovery = dictionary.get('copyRecovery')
        datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('datastoreEntity')) if dictionary.get('datastoreEntity') else None
        preserve_tags_during_clone = dictionary.get('preserveTagsDuringClone')
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        target_datastore_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetDatastoreFolder')) if dictionary.get('targetDatastoreFolder') else None
        target_vm_folder = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetVmFolder')) if dictionary.get('targetVmFolder') else None

        # Return an object of this model
        return cls(copy_recovery,
                   datastore_entity,
                   preserve_tags_during_clone,
                   resource_pool_entity,
                   target_datastore_folder,
                   target_vm_folder)


