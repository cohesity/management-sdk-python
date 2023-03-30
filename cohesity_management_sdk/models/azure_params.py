# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AzureParams(object):

    """Implementation of the 'AzureParams' model.

    Specifies various resources when converting and deploying a VM to Azure.


    Attributes:

        availability_set_id (long|int): Specifies id of the Availability set in
            which the VM is to be restored.
        data_disk_type (DataDiskTypeEnum): Specifies the disk type used by the
            data. 'kPremiumSSD' is disk type backed by SSDs, delivers high
            performance, low latency disk support for VMs running I/O intensive
            workloads. 'kStandardSSD' implies disk type that offers more
            consistent performance and reliability than HDD. 'kStandardHDD'
            implies disk type backed by HDDs, delivers cost effective storage.
        instance_id (long|int): Specifies Type of VM (e.g. small, medium,
            large) when cloning the VM in Azure.
        network_resource_group_id (long|int): Specifies id of the resource
            group for the selected virtual network.
        os_disk_type (OsDiskTypeEnum): Specifies the disk type used by the OS.
            'kPremiumSSD' is disk type backed by SSDs, delivers high
            performance, low latency disk support for VMs running I/O intensive
            workloads. 'kStandardSSD' implies disk type that offers more
            consistent performance and reliability than HDD. 'kStandardHDD'
            implies disk type backed by HDDs, delivers cost effective storage.
        resource_group (long|int): Specifies id of the Azure resource group.
            Its value is globally unique within Azure.
        storage_account (long|int): Specifies id of the storage account that
            will contain the storage container within which we will create the
            blob that will become the VHD disk for the cloned VM.
        storage_container (long|int): Specifies id of the storage container
            within the above storage account.
        storage_resource_group_id (long|int): Specifies id of the resource
            group for the selected storage account.
        subnet_id (long|int): Specifies Id of the subnet within the above
            virtual network.
        temp_vm_resource_group_id (long|int): Specifies the resource group
            where temporary VM needs to be created.
        temp_vm_storage_account_id (long|int): Specifies the Storage account
            where temporary VM needs to be created.
        temp_vm_storage_container_id (long|int): Specifies the Storage
            container where temporary VM needs to be created.
        temp_vm_subnet_id (long|int): Specifies the Subnet where temporary VM
            needs to be created.
        temp_vm_virtual_network_id (long|int): Specifies the Virtual network
            where temporary VM needs to be created.
        virtual_network_id (long|int): Specifies Id of the Virtual Network.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "availability_set_id":'availabilitySetId',
        "data_disk_type":'dataDiskType',
        "instance_id":'instanceId',
        "network_resource_group_id":'networkResourceGroupId',
        "os_disk_type":'osDiskType',
        "resource_group":'resourceGroup',
        "storage_account":'storageAccount',
        "storage_container":'storageContainer',
        "storage_resource_group_id":'storageResourceGroupId',
        "subnet_id":'subnetId',
        "temp_vm_resource_group_id":'tempVmResourceGroupId',
        "temp_vm_storage_account_id":'tempVmStorageAccountId',
        "temp_vm_storage_container_id":'tempVmStorageContainerId',
        "temp_vm_subnet_id":'tempVmSubnetId',
        "temp_vm_virtual_network_id":'tempVmVirtualNetworkId',
        "virtual_network_id":'virtualNetworkId',
    }
    def __init__(self,
                 availability_set_id=None,
                 data_disk_type=None,
                 instance_id=None,
                 network_resource_group_id=None,
                 os_disk_type=None,
                 resource_group=None,
                 storage_account=None,
                 storage_container=None,
                 storage_resource_group_id=None,
                 subnet_id=None,
                 temp_vm_resource_group_id=None,
                 temp_vm_storage_account_id=None,
                 temp_vm_storage_container_id=None,
                 temp_vm_subnet_id=None,
                 temp_vm_virtual_network_id=None,
                 virtual_network_id=None,
            ):

        """Constructor for the AzureParams class"""

        # Initialize members of the class
        self.availability_set_id = availability_set_id
        self.data_disk_type = data_disk_type
        self.instance_id = instance_id
        self.network_resource_group_id = network_resource_group_id
        self.os_disk_type = os_disk_type
        self.resource_group = resource_group
        self.storage_account = storage_account
        self.storage_container = storage_container
        self.storage_resource_group_id = storage_resource_group_id
        self.subnet_id = subnet_id
        self.temp_vm_resource_group_id = temp_vm_resource_group_id
        self.temp_vm_storage_account_id = temp_vm_storage_account_id
        self.temp_vm_storage_container_id = temp_vm_storage_container_id
        self.temp_vm_subnet_id = temp_vm_subnet_id
        self.temp_vm_virtual_network_id = temp_vm_virtual_network_id
        self.virtual_network_id = virtual_network_id

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
        availability_set_id = dictionary.get('availabilitySetId')
        data_disk_type = dictionary.get('dataDiskType')
        instance_id = dictionary.get('instanceId')
        network_resource_group_id = dictionary.get('networkResourceGroupId')
        os_disk_type = dictionary.get('osDiskType')
        resource_group = dictionary.get('resourceGroup')
        storage_account = dictionary.get('storageAccount')
        storage_container = dictionary.get('storageContainer')
        storage_resource_group_id = dictionary.get('storageResourceGroupId')
        subnet_id = dictionary.get('subnetId')
        temp_vm_resource_group_id = dictionary.get('tempVmResourceGroupId')
        temp_vm_storage_account_id = dictionary.get('tempVmStorageAccountId')
        temp_vm_storage_container_id = dictionary.get('tempVmStorageContainerId')
        temp_vm_subnet_id = dictionary.get('tempVmSubnetId')
        temp_vm_virtual_network_id = dictionary.get('tempVmVirtualNetworkId')
        virtual_network_id = dictionary.get('virtualNetworkId')

        # Return an object of this model
        return cls(
            availability_set_id,
            data_disk_type,
            instance_id,
            network_resource_group_id,
            os_disk_type,
            resource_group,
            storage_account,
            storage_container,
            storage_resource_group_id,
            subnet_id,
            temp_vm_resource_group_id,
            temp_vm_storage_account_id,
            temp_vm_storage_container_id,
            temp_vm_subnet_id,
            temp_vm_virtual_network_id,
            virtual_network_id
)