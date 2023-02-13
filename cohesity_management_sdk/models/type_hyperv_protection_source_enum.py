# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeHypervProtectionSourceEnum(object):

    """Implementation of the 'Type_HypervProtectionSource' enum.

    Specifies the type of an HyperV Protection Source Object such as
    'kSCVMMServer', 'kStandaloneHost', 'kNetwork', etc.
    overrideDescription: true
    Specifies the type of an HyperV Protection Source.
    'kSCVMMServer' indicates a collection of root folders clusters.
    'kStandaloneHost' indicates a single Nutanix cluster.
    'kStandaloneCluster' indicates a single Nutanix cluster.
    'kHostGroup' indicates a Nutanix cluster manageed by a Prism Central.
    'kHypervHost' indicates an HyperV host.
    'kHostCluster' indicates a Nutanix cluster manageed by a Prism Central.
    'kVirtualMachine' indicates a Virtual Machine.
    'kNetwork' indicates a Virtual Machine network object.
    'kDatastore' represents a storage container object.
    'kTag' indicates a tag type object.
    'kCustomProperty' indciates a custom property including tag type.

    Attributes:
        KSCVMMSERVER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KSTANDALONECLUSTER: TODO: type description here.
        KHOSTGROUP: TODO: type description here.
        KHYPERVHOST: TODO: type description here.
        KHOSTCLUSTER: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KNETWORK: TODO: type description here.
        KDATASTORE: TODO: type description here.
        KTAG: TODO: type description here.
        KCUSTOMPROPERTY: TODO: type description here.

    """

    KSCVMMSERVER = 'kSCVMMServer'

    KSTANDALONEHOST = 'kStandaloneHost'

    KSTANDALONECLUSTER = 'kStandaloneCluster'

    KHOSTGROUP = 'kHostGroup'

    K_HYPERV_HOST = 'kHypervHost'

    KHOSTCLUSTER = 'kHostCluster'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KNETWORK = 'kNetwork'

    KDATASTORE = 'kDatastore'

    KTAG = 'kTag'

    KCUSTOMPROPERTY = 'kCustomProperty'

