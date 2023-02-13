# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VmwareTypeEnum(object):

    """Implementation of the 'VmwareType' enum.

    Specifies the entity type such as 'kVCenter' if the environment is
    kKMware.
    overrideDescription: true
    Examples of VMware Objects include 'kVCenter', 'kFolder', 'kDatacenter',
    'kResourcePool', 'kDatastore', 'kVirtualMachine', etc.
    'kVCenter' indicates the vCenter entity in a VMware protection source
    type.
    'kFolder indicates the folder entity (of any kind) in a VMware protection
    source type.
    'kDatacenter' indicates the datacenter entity in a VMware protection
    source type.
    'kComputeResource' indicates the physical compute resource entity in a
    VMware
    protection source type.
    'kResourcePool' indicates the set of physical resourses within a compute
    resource
    or cloudcompute resource.
    'kDataStore' indicates the datastore entity in a VMware protection source
    type.
    'kHostSystem' indicates the ESXi host entity in a VMware protection source
    type.
    'kVirtualMachine' indicates the virtual machine entity in a VMware
    protection source type.
    'kVirtualApp' indicates the virtual app entity in a VMware protection
    source type.
    'kStandaloneHost' indicates the standalone ESXi host entity (not managed
    by vCenter)
    in a VMware protection source type.
    'kStoragePod' indicates the storage pod entity in a VMware protection
    source type.
    'kNetwork' indicates the standard vSwitch in a VMware protection source
    type.
    'kDistributedVirtualPortgroup' indicates a distributed vSwitch port group
    in a
    VMware protection source type.
    'kTagCategory' indicates a tag category entity in a VMware protection
    source type.
    'kTag' indocates a tag entity in a VMware protection source type.
    'kOpaqueNetwork' indicates a opaque network which is created and managed
    by an
    entity outside of vSphere.
    'kVCloudDirector' indicates a vCloud director entity in a VMware
    protection source type.
    'kOrganization' indicates an Organization under a vCD in a VMware
    protection source type.
    'kVirtualDatacenter' indicates a virtual datacenter entity in a VMware
    protection source type.
    'kCatalog' indocates a VCD catalog entity in a VMware protection source
    type.
    'kOrgMetadata' indicates an VCD organization metadata in a VMware
    protection source type.
    'kStoragePolicy' indicates a storage policy associated with the vApp in a
    VMware protection source type.

    Attributes:
        KVCENTER: TODO: type description here.
        KFOLDER: TODO: type description here.
        KDATACENTER: TODO: type description here.
        KCOMPUTERESOURCE: TODO: type description here.
        KCLUSTERCOMPUTERESOURCE: TODO: type description here.
        KRESOURCEPOOL: TODO: type description here.
        KDATASTORE: TODO: type description here.
        KHOSTSYSTEM: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KVIRTUALAPP: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KSTORAGEPOD: TODO: type description here.
        KNETWORK: TODO: type description here.
        KDISTRIBUTEDVIRTUALPORTGROUP: TODO: type description here.
        KTAGCATEGORY: TODO: type description here.
        KTAG: TODO: type description here.
        KOPAQUENETWORK: TODO: type description here.
        KVCLOUDDIRECTOR: TODO: type description here.
        KORGANIZATION: TODO: type description here.
        KVIRTUALDATACENTER: TODO: type description here.
        KCATALOG: TODO: type description here.
        KORGMETADATA: TODO: type description here.
        KSTORAGEPOLICY: TODO: type description here.

    """

    KVCENTER = 'kVCenter'

    KFOLDER = 'kFolder'

    KDATACENTER = 'kDatacenter'

    KCOMPUTERESOURCE = 'kComputeResource'

    KCLUSTERCOMPUTERESOURCE = 'kClusterComputeResource'

    KRESOURCEPOOL = 'kResourcePool'

    KDATASTORE = 'kDatastore'

    KHOSTSYSTEM = 'kHostSystem'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KVIRTUALAPP = 'kVirtualApp'

    KSTANDALONEHOST = 'kStandaloneHost'

    KSTORAGEPOD = 'kStoragePod'

    KNETWORK = 'kNetwork'

    KDISTRIBUTEDVIRTUALPORTGROUP = 'kDistributedVirtualPortgroup'

    KTAGCATEGORY = 'kTagCategory'

    KTAG = 'kTag'

    KOPAQUENETWORK = 'kOpaqueNetwork'

    K_VCLOUD_DIRECTOR = 'kVCloudDirector'

    KORGANIZATION = 'kOrganization'

    KVIRTUALDATACENTER = 'kVirtualDatacenter'

    KCATALOG = 'kCatalog'

    KORGMETADATA = 'kOrgMetadata'

    KSTORAGEPOLICY = 'kStoragePolicy'

