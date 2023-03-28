# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AzureCredentials(object):

    """Implementation of the 'AzureCredentials' model.

    Specifies the credentials to authenticate with Azure Cloud Platform.


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
        region (string): Specifies the region in which the Azure Stack will be
            registered.
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
        tenant_id (string): Specifies Tenant Id of the active directory of
            Azure account.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "application_id":'applicationId',
        "application_key":'applicationKey',
        "azure_type":'azureType',
        "domain_name":'domainName',
        "region":'region',
        "subscription_id":'subscriptionId',
        "subscription_type":'subscriptionType',
        "tenant_id":'tenantId',
    }
    def __init__(self,
                 application_id=None,
                 application_key=None,
                 azure_type=None,
                 domain_name=None,
                 region=None,
                 subscription_id=None,
                 subscription_type=None,
                 tenant_id=None,
            ):

        """Constructor for the AzureCredentials class"""

        # Initialize members of the class
        self.application_id = application_id
        self.application_key = application_key
        self.azure_type = azure_type
        self.domain_name = domain_name
        self.region = region
        self.subscription_id = subscription_id
        self.subscription_type = subscription_type
        self.tenant_id = tenant_id

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
        region = dictionary.get('region')
        subscription_id = dictionary.get('subscriptionId')
        subscription_type = dictionary.get('subscriptionType')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(
            application_id,
            application_key,
            azure_type,
            domain_name,
            region,
            subscription_id,
            subscription_type,
            tenant_id
)