# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.azure_managed_disk_params
import cohesity_management_sdk.models.entity_proto

class DeployVMsToAzureParams(object):

    """Implementation of the 'DeployVMsToAzureParams' model.

    Contains Azure specific information needed to identify various resources
    when converting and deploying a VM to Azure.

    Attributes:
        availability_set (EntityProto): Name of the Availability set in which
            the VM is to be restored.
        azure_managed_disk_params (AzureManagedDiskParams): Contains managed
            disk parameters needed to deploy to Azure using managed disk.
        compute_options (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        network_resource_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        network_security_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        resource_group (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        storage_account (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        storage_container (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        storage_key (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        storage_resource_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        subnet (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        temp_vm_resource_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        temp_vm_storage_account (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        temp_vm_storage_container (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        temp_vm_subnet (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        temp_vm_virtual_network (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        virtual_network (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "availability_set":'availabilitySet',
        "azure_managed_disk_params":'azureManagedDiskParams',
        "compute_options":'computeOptions',
        "network_resource_group":'networkResourceGroup',
        "network_security_group":'networkSecurityGroup',
        "resource_group":'resourceGroup',
        "storage_account":'storageAccount',
        "storage_container":'storageContainer',
        "storage_key":'storageKey',
        "storage_resource_group":'storageResourceGroup',
        "subnet":'subnet',
        "temp_vm_resource_group":'tempVmResourceGroup',
        "temp_vm_storage_account":'tempVmStorageAccount',
        "temp_vm_storage_container":'tempVmStorageContainer',
        "temp_vm_subnet":'tempVmSubnet',
        "temp_vm_virtual_network":'tempVmVirtualNetwork',
        "virtual_network":'virtualNetwork'
    }

    def __init__(self,
                 availability_set=None,
                 azure_managed_disk_params=None,
                 compute_options=None,
                 network_resource_group=None,
                 network_security_group=None,
                 resource_group=None,
                 storage_account=None,
                 storage_container=None,
                 storage_key=None,
                 storage_resource_group=None,
                 subnet=None,
                 temp_vm_resource_group=None,
                 temp_vm_storage_account=None,
                 temp_vm_storage_container=None,
                 temp_vm_subnet=None,
                 temp_vm_virtual_network=None,
                 virtual_network=None):
        """Constructor for the DeployVMsToAzureParams class"""

        # Initialize members of the class
        self.availability_set = availability_set
        self.azure_managed_disk_params = azure_managed_disk_params
        self.compute_options = compute_options
        self.network_resource_group = network_resource_group
        self.network_security_group = network_security_group
        self.resource_group = resource_group
        self.storage_account = storage_account
        self.storage_container = storage_container
        self.storage_key = storage_key
        self.storage_resource_group = storage_resource_group
        self.subnet = subnet
        self.temp_vm_resource_group = temp_vm_resource_group
        self.temp_vm_storage_account = temp_vm_storage_account
        self.temp_vm_storage_container = temp_vm_storage_container
        self.temp_vm_subnet = temp_vm_subnet
        self.temp_vm_virtual_network = temp_vm_virtual_network
        self.virtual_network = virtual_network


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
        availability_set = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('availabilitySet')) if dictionary.get('availabilitySet') else None
        azure_managed_disk_params = cohesity_management_sdk.models.azure_managed_disk_params.AzureManagedDiskParams.from_dictionary(dictionary.get('azureManagedDiskParams')) if dictionary.get('azureManagedDiskParams') else None
        compute_options = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('computeOptions')) if dictionary.get('computeOptions') else None
        network_resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('networkResourceGroup')) if dictionary.get('networkResourceGroup') else None
        network_security_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('networkSecurityGroup')) if dictionary.get('networkSecurityGroup') else None
        resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourceGroup')) if dictionary.get('resourceGroup') else None
        storage_account = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageAccount')) if dictionary.get('storageAccount') else None
        storage_container = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageContainer')) if dictionary.get('storageContainer') else None
        storage_key = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageKey')) if dictionary.get('storageKey') else None
        storage_resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('storageResourceGroup')) if dictionary.get('storageResourceGroup') else None
        subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        temp_vm_resource_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('tempVmResourceGroup')) if dictionary.get('tempVmResourceGroup') else None
        temp_vm_storage_account = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('tempVmStorageAccount')) if dictionary.get('tempVmStorageAccount') else None
        temp_vm_storage_container = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('tempVmStorageContainer')) if dictionary.get('tempVmStorageContainer') else None
        temp_vm_subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('tempVmSubnet')) if dictionary.get('tempVmSubnet') else None
        temp_vm_virtual_network = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('tempVmVirtualNetwork')) if dictionary.get('tempVmVirtualNetwork') else None
        virtual_network = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('virtualNetwork')) if dictionary.get('virtualNetwork') else None

        # Return an object of this model
        return cls(availability_set,
                   azure_managed_disk_params,
                   compute_options,
                   network_resource_group,
                   network_security_group,
                   resource_group,
                   storage_account,
                   storage_container,
                   storage_key,
                   storage_resource_group,
                   subnet,
                   temp_vm_resource_group,
                   temp_vm_storage_account,
                   temp_vm_storage_container,
                   temp_vm_subnet,
                   temp_vm_virtual_network,
                   virtual_network)


