# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ActiveOperationEnum(object):

    """Implementation of the 'ActiveOperation' enum.

    Specifies the active operation on the Node if there is one.
    'kNone' specifies that there is no active operation on the Node.
    'kDestroyCluster' specifies that the Cluster which the Node is a part of
    is currently being destroyed.
    'kUpgradeCluster' specifies that the Cluster which the Node is a part of
    is currently being upgraded to a new software package.
    'kRestartCluster' specifies that the Cluster which the Node is a part of
    is currently being restarted.
    'kCreateCluster' specifies that the Node is currently being used to
    create
    a new Cluster.
    'kExpandCluster' specifies that the Node is currently being added to a
    Cluster or being used to assist in adding another Node to a Cluster.
    'kUpgradeNode' specifies that the Node is currently being upgraded to a
    new
    software package.
    'kRemoveNode' specifies that the Node is currently being removed from a
    Cluster or that it is assisting in removing another Node from a Cluster.
    'kAddDisks' specifies that the Node is being used to assist in adding
    disks
    to the Cluster.
    'kMarkDiskOffline' specifies that the Node is being use to assist in
    marking a disk in the Cluster as offline.

    Attributes:
        KNONE: TODO: type description here.
        KDESTROYCLUSTER: TODO: type description here.
        KUPGRADECLUSTER: TODO: type description here.
        KRESTARTCLUSTER: TODO: type description here.
        KCREATECLUSTER: TODO: type description here.
        KEXPANDCLUSTER: TODO: type description here.
        KUPGRADENODE: TODO: type description here.
        KREMOVENODE: TODO: type description here.
        KADDDISKS: TODO: type description here.
        KMARKDISKOFFLINE: TODO: type description here.

    """

    KNONE = 'kNone'

    KDESTROYCLUSTER = 'kDestroyCluster'

    KUPGRADECLUSTER = 'kUpgradeCluster'

    KRESTARTCLUSTER = 'kRestartCluster'

    KCREATECLUSTER = 'kCreateCluster'

    KEXPANDCLUSTER = 'kExpandCluster'

    KUPGRADENODE = 'kUpgradeNode'

    KREMOVENODE = 'kRemoveNode'

    KADDDISKS = 'kAddDisks'

    KMARKDISKOFFLINE = 'kMarkDiskOffline'

