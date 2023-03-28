# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.tag_attribute


class AzureProtectionSource(object):

    """Implementation of the 'AzureProtectionSource' model.

    Specifies a Protection Source in Azure environment.


    Attributes:

        application_id (string): Specifies Application Id of the active
            directory of Azure account.
        application_key (string): Specifies Application key of the active
            directory of Azure account.
        azure_type (AzureTypeEnum): Specifies the entity type such as
            'kSubscription' if the environment is kAzure. Specifies the type of
            an Azure source entity. 'kSubscription' indicates a billing unit
            within Azure account. 'kResourceGroup' indicates a container that
            holds related resources. 'kVirtualMachine' indicates a Virtual
            Machine in Azure environment. 'kStorageAccount' represents a
            collection of storage containers. 'kStorageKey' indicates a key
            required to access the storage account. 'kStorageContainer'
            represents a storage container within a storage account.
            'kStorageBlob' represents a storage blog within a storage
            container. 'kStorageResourceGroup' indicates a container that holds
            related storage resources. 'kNetworkSecurityGroup' represents a
            network security group. 'kVirtualNetwork' represents a virtual
            network. 'kNetworkResourceGroup' indicates a container that holds
            related network resources. 'kSubnet' represents a subnet within the
            virtual network. 'kComputeOptions' indicates the number of CPU
            cores and memory size available for a type of a Virtual Machine.
            'kAvailabilitySet' indicates the availability set.
        domain_name (string): Specifies Azure stack hub domain name for where
            the given subscription is present.
        host_type (HostTypeEnum): Specifies the OS type of the Protection
            Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'.
            overrideDescription: true 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system. 'kSapHana' indicates
            the Sap Hana database system developed by SAP SE. 'kSapOracle'
            indicates the Sap Oracle database system developed by SAP SE.
            'kCockroachDB' indicates the CockroachDB database system. 'kMySQL'
            indicates the MySQL database system. 'kOther' indicates the other
            types of operating system.
        ip_addresses (list of string): Specifies a list of IP addresses for
            entities of type 'kVirtualMachine'.
        is_managed_vm (bool): Specifies whether VM is managed or not for
            entities of type 'kVirtualMachine'.
        location (string): Specifies the physical location of the resource
            group.
        memory_mbytes (long|int): Specifies the amount of memory in MegaBytes
            of the Azure resource of type 'kComputeOptions'.
        name (string): Specifies the name of the Object set by the Cloud
            Provider. If the provider did not set a name for the object, this
            field is not set.
        num_cores (int): Specifies the number of CPU cores of the Azure
            resource of type 'kComputeOptions'.
        physical_source_id (long|int): Specifies the Protection Source id of
            the registered Physical Host. If the cloud entity is protected
            using a Physical Agent, it must be registered as a physical host.
        region (string): Specifies the region in which the Azure Stack will be
            registered.
        resource_id (string): Specifies the unique Id of the resource given by
            the cloud provider.
        restore_task_id (long|int): Specifies the id of the "convert and
            deploy" restore task that created the entity in the cloud.  It is
            required to support the DR-to-cloud usecase where we replicate an
            on-prem entity to a cluster running in cloud, bring it up using
            "convert and deploy" mechanism, protect it using a cloud job that
            uses physical adapter, and convert it back to the on-prem format
            before replication.  Before replicating, we need to update the
            backup task state of the backed up entity using the on-prem entity
            and on-prem entity's parent. The id is used to lookup the restore
            entity that contains details about the on-prem entity.  It is set
            at the time of refreshing the cloud entity hierarchy if all the
            following conditions are met: Name of the current entity matches
            with name of any cloud entity deployed using the "convert and
            deploy" restore task. Restore entity associated with the above
            matched cloud entity has 'failed_over' flag set to true in its
            cloud extension.
        subscription_id (string): Specifies Subscription id inside a customer's
            Azure account. It represents sub-section within the Azure account
            where a customer allows us to create VMs, storage account etc.
        subscription_type (SubscriptionTypeEnum): Specifies the subscription
            type of Azure such as 'kAzureCommercial', 'kAzureGovCloud',
            'kAzureStackCommercial' or 'kAzureStackADFS'. Specifies the
            subscription type of an Azure source entity. 'kAzureCommercial'
            indicates a standard Azure subscription. 'kAzureGovCloud' indicates
            a govt Azure subscription. 'kAzureStackCommercial' indicates a
            stack commercial Azure subscription. 'kAzureStackADFS' indicates a
            ADFS Azure subbscription.
        tag_attributes (list of TagAttribute): Specifies the list of Azure tag
            attributes.
        tenant_id (string): Specifies Tenant Id of the active directory of
            Azure account.
        mtype (TypeAzureProtectionSourceEnum): Specifies the type of an Azure
            Protection Source Object such as 'kStorageContainer',
            'kVirtualMachine', 'kVirtualNetwork', etc. Specifies the type of an
            Azure source entity. 'kSubscription' indicates a billing unit
            within Azure account. 'kResourceGroup' indicates a container that
            holds related resources. 'kVirtualMachine' indicates a Virtual
            Machine in Azure environment. 'kStorageAccount' represents a
            collection of storage containers. 'kStorageKey' indicates a key
            required to access the storage account. 'kStorageContainer'
            represents a storage container within a storage account.
            'kStorageBlob' represents a storage blog within a storage
            container. 'kStorageResourceGroup' indicates a container that holds
            related storage resources. 'kNetworkSecurityGroup' represents a
            network security group. 'kVirtualNetwork' represents a virtual
            network. 'kNetworkResourceGroup' indicates a container that holds
            related network resources. 'kSubnet' represents a subnet within the
            virtual network. 'kComputeOptions' indicates the number of CPU
            cores and memory size available for a type of a Virtual Machine.
            'kAvailabilitySet' indicates the availability set.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "application_id":'applicationId',
        "application_key":'applicationKey',
        "azure_type":'azureType',
        "domain_name":'domainName',
        "host_type":'hostType',
        "ip_addresses":'ipAddresses',
        "is_managed_vm":'isManagedVm',
        "location":'location',
        "memory_mbytes":'memoryMbytes',
        "name":'name',
        "num_cores":'numCores',
        "physical_source_id":'physicalSourceId',
        "region":'region',
        "resource_id":'resourceId',
        "restore_task_id":'restoreTaskId',
        "subscription_id":'subscriptionId',
        "subscription_type":'subscriptionType',
        "tag_attributes":'tagAttributes',
        "tenant_id":'tenantId',
        "mtype":'type',
    }
    def __init__(self,
                 application_id=None,
                 application_key=None,
                 azure_type=None,
                 domain_name=None,
                 host_type=None,
                 ip_addresses=None,
                 is_managed_vm=None,
                 location=None,
                 memory_mbytes=None,
                 name=None,
                 num_cores=None,
                 physical_source_id=None,
                 region=None,
                 resource_id=None,
                 restore_task_id=None,
                 subscription_id=None,
                 subscription_type=None,
                 tag_attributes=None,
                 tenant_id=None,
                 mtype=None,
            ):

        """Constructor for the AzureProtectionSource class"""

        # Initialize members of the class
        self.application_id = application_id
        self.application_key = application_key
        self.azure_type = azure_type
        self.domain_name = domain_name
        self.host_type = host_type
        self.ip_addresses = ip_addresses
        self.is_managed_vm = is_managed_vm
        self.location = location
        self.memory_mbytes = memory_mbytes
        self.name = name
        self.num_cores = num_cores
        self.physical_source_id = physical_source_id
        self.region = region
        self.resource_id = resource_id
        self.restore_task_id = restore_task_id
        self.subscription_id = subscription_id
        self.subscription_type = subscription_type
        self.tag_attributes = tag_attributes
        self.tenant_id = tenant_id
        self.mtype = mtype

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
        application_id = dictionary.get('applicationId')
        application_key = dictionary.get('applicationKey')
        azure_type = dictionary.get('azureType')
        domain_name = dictionary.get('domainName')
        host_type = dictionary.get('hostType')
        ip_addresses = dictionary.get("ipAddresses")
        is_managed_vm = dictionary.get('isManagedVm')
        location = dictionary.get('location')
        memory_mbytes = dictionary.get('memoryMbytes')
        name = dictionary.get('name')
        num_cores = dictionary.get('numCores')
        physical_source_id = dictionary.get('physicalSourceId')
        region = dictionary.get('region')
        resource_id = dictionary.get('resourceId')
        restore_task_id = dictionary.get('restoreTaskId')
        subscription_id = dictionary.get('subscriptionId')
        subscription_type = dictionary.get('subscriptionType')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes = list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        tenant_id = dictionary.get('tenantId')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            application_id,
            application_key,
            azure_type,
            domain_name,
            host_type,
            ip_addresses,
            is_managed_vm,
            location,
            memory_mbytes,
            name,
            num_cores,
            physical_source_id,
            region,
            resource_id,
            restore_task_id,
            subscription_id,
            subscription_type,
            tag_attributes,
            tenant_id,
            mtype
)