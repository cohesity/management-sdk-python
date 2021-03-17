# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class TypeEnum(object):

    """Implementation of the 'Type' enum.

    Specifies the type of an Acropolis Protection Source Object such as
    'kPrismCentral', 'kHost', 'kNetwork', etc.
    Specifies the type of an Acropolis source entity.
    'kPrismCentral' indicates a collection of multiple Nutanix clusters.
    'kStandaloneCluster' indicates a single Nutanix cluster.
    'kCluster' indicates a Nutanix cluster manageed by a Prism Central.
    'kHost' indicates an Acropolis host.
    'kVirtualMachine' indicates a Virtual Machine.
    'kNetwork' indicates a Virtual Machine network object.
    'kStorageContainer' represents a storage container object.

    Attributes:
        KPRISMCENTRAL: TODO: type description here.
        KSTANDALONECLUSTER: TODO: type description here.
        KCLUSTER: TODO: type description here.
        KHOST: TODO: type description here.
        KVIRTUALMACHINE: TODO: type description here.
        KNETWORK: TODO: type description here.
        KSTORAGECONTAINER: TODO: type description here.

    """

    KPRISMCENTRAL = 'kPrismCentral'

    KSTANDALONECLUSTER = 'kStandaloneCluster'

    KCLUSTER = 'kCluster'

    KHOST = 'kHost'

    KVIRTUALMACHINE = 'kVirtualMachine'

    KNETWORK = 'kNetwork'

    KSTORAGECONTAINER = 'kStorageContainer'

