# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class HypervTypeEnum(object):

    """Implementation of the 'HyperVType' enum.

    Specifies the entity type if the environment is kHyperV.
    overrideDescription: true
    Specifies the type of an HyperV Protection Source.
    'kSCVMMServer' indicates a collection of root folders clusters.
    'kStandaloneHost' indicates a single Nutanix cluster.
    'kStandaloneCluster' indicates a single Nutanix cluster.
    'kHostGroup' indicates a Nutanix cluster manageed by a Prism Central.
    'kHost' indicates an HyperV host.
    'kHostCluster' indicates a Nutanix cluster manageed by a Prism Central.
    'kVirtualMachine' indicates a Virtual Machine.
    'kNetwork' indicates a Virtual Machine network object.
    'kDatastore' represents a storage container object.

    Attributes:
        KSCVMMSERVER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KSTANDALONECLUSTER: TODO: type description here.
        KHOSTGROUP: TODO: type description here.
        KHOST: TODO: type description here.
        KHOSTCLUSTER: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KNETWORK: TODO: type description here.
        KDATASTORE: TODO: type description here.

    """

    KSCVMMSERVER = 'kSCVMMServer'

    KSTANDALONEHOST = 'kStandaloneHost'

    KSTANDALONECLUSTER = 'kStandaloneCluster'

    KHOSTGROUP = 'kHostGroup'

    KHOST = 'kHost'

    KHOSTCLUSTER = 'kHostCluster'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KNETWORK = 'kNetwork'

    KDATASTORE = 'kDatastore'

