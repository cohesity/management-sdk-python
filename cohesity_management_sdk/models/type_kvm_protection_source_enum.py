# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeKvmProtectionSourceEnum(object):

    """Implementation of the 'Type_KvmProtectionSource' enum.

    Specifies the type of KVM Protection Source entities such as
    'kDatacenter', 'kCluster', 'kVirtualMachine', etc.
    Specifies the type of an KVM source entity.
    'kOVirtManager' indicates the root entity registerd with Cohesity
    cluster.
    'kStandaloneHost' indicates a host registered with Cohesity cluster.
    'kDatacenter' indicates a KVM datacenter managed by the OVirt manager.
    'kCluster' indicates a KVM cluster managed by the OVirt manager.
    'kHost' indicates a host within the KVM environment.
    'kVirtualMachine' indicates a virtual machine in the KVM enironment.
    'kNetwork' represents a network used by the virtual machine entity.
    'kStorageDomain' represents a storage domain in the KVM environment.
    'kVNicProfile' represents a VNic profile.

    Attributes:
        KOVIRTMANAGER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KDATACENTER: TODO: type description here.
        KCLUSTER: TODO: type description here.
        KHOST: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KNETWORK: TODO: type description here.
        KSTORAGEDOMAIN: TODO: type description here.
        KVNICPROFILE: TODO: type description here.

    """

    KOVIRTMANAGER = 'kOVirtManager'

    KSTANDALONEHOST = 'kStandaloneHost'

    KDATACENTER = 'kDatacenter'

    KCLUSTER = 'kCluster'

    KHOST = 'kHost'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KNETWORK = 'kNetwork'

    KSTORAGEDOMAIN = 'kStorageDomain'

    KVNICPROFILE = 'kVNicProfile'

