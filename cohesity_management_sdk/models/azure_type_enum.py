# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AzureTypeEnum(object):

    """Implementation of the 'AzureType' enum.
    Specifies the entity type such as 'kSubscription' if the environment is
    kAzure. Specifies the type of an Azure source entity. 'kSubscription'
    indicates a billing unit within Azure account. 'kResourceGroup' indicates a
    container that holds related resources. 'kVirtualMachine' indicates a
    Virtual Machine in Azure environment. 'kStorageAccount' represents a
    collection of storage containers. 'kStorageKey' indicates a key required to
    access the storage account. 'kStorageContainer' represents a storage
    container within a storage account. 'kStorageBlob' represents a storage
    blog within a storage container. 'kStorageResourceGroup' indicates a
    container that holds related storage resources. 'kNetworkSecurityGroup'
    represents a network security group. 'kVirtualNetwork' represents a virtual
    network. 'kNetworkResourceGroup' indicates a container that holds related
    network resources. 'kSubnet' represents a subnet within the virtual
    network. 'kComputeOptions' indicates the number of CPU cores and memory
    size available for a type of a Virtual Machine. 'kAvailabilitySet'
    indicates the availability set.


    Attributes:
        KSUBSCRIPTION: TODO: type description here.
        KRESOURCEGROUP: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KSTORAGEACCOUNT: TODO: type description here.
        KSTORAGEKEY: TODO: type description here.
        KSTORAGECONTAINER: TODO: type description here.
        KSTORAGEBLOB: TODO: type description here.
        KSTORAGERESOURCEGROUP: TODO: type description here.
        KNETWORKSECURITYGROUP: TODO: type description here.
        KVIRTUALNETWORK: TODO: type description here.
        KNETWORKRESOURCEGROUP: TODO: type description here.
        KSUBNET: TODO: type description here.
        KCOMPUTEOPTIONS: TODO: type description here.
        KAVAILABILITYSET: TODO: type description here.

    """

    KSUBSCRIPTION = 'kSubscription'

    KRESOURCEGROUP = 'kResourceGroup'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KSTORAGEACCOUNT = 'kStorageAccount'

    KSTORAGEKEY = 'kStorageKey'

    KSTORAGECONTAINER = 'kStorageContainer'

    KSTORAGEBLOB = 'kStorageBlob'

    KSTORAGERESOURCEGROUP = 'kStorageResourceGroup'

    KNETWORKSECURITYGROUP = 'kNetworkSecurityGroup'

    KVIRTUALNETWORK = 'kVirtualNetwork'

    KNETWORKRESOURCEGROUP = 'kNetworkResourceGroup'

    KSUBNET = 'kSubnet'

    KCOMPUTEOPTIONS = 'kComputeOptions'

    KAVAILABILITYSET = 'kAvailabilitySet'
