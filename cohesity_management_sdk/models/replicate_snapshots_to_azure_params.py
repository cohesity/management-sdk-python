# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class ReplicateSnapshotsToAzureParams(object):

    """Implementation of the 'ReplicateSnapshotsToAzureParams' model.

    This is populated for Azure snapshot manager replication.

    Attributes:
        resource_group (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        storage_account (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        storage_container (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        storage_resource_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resource_group":'resourceGroup',
        "storage_account":'storageAccount',
        "storage_container":'storageContainer',
        "storage_resource_group":'storageResourceGroup'
    }

    def __init__(self,
                 resource_group=None,
                 storage_account=None,
                 storage_container=None,
                 storage_resource_group=None):
        """Constructor for the ReplicateSnapshotsToAzureParams class"""

        # Initialize members of the class
        self.resource_group = resource_group
        self.storage_account = storage_account
        self.storage_container = storage_container
        self.storage_resource_group = storage_resource_group


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
        resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourceGroup')) if dictionary.get('resourceGroup') else None
        storage_account = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageAccount')) if dictionary.get('storageAccount') else None
        storage_container = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageContainer')) if dictionary.get('storageContainer') else None
        storage_resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageResourceGroup')) if dictionary.get('storageResourceGroup') else None

        # Return an object of this model
        return cls(resource_group,
                   storage_account,
                   storage_container,
                   storage_resource_group)


