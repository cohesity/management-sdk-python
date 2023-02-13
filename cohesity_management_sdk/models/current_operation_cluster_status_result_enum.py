# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CurrentOperationClusterStatusResultEnum(object):

    """Implementation of the 'CurrentOperation_ClusterStatusResult' enum.

    Specifies the current operation being run on the Cluster.
    'kNone' indicates that there is no current operation taking place.
    'kDestroy' indicates that the Cluster is currently being destroyed.
    'kUpgrade' indicates that the Cluster is currently being upgraded.
    'kClean' indicates that the Cluster is being cleaned.
    'kRemoveNode' indicates that a Node is being removed from the Cluster.
    'kRestartServices' indicates that the services on the Cluster are
    currently
    being restarted.

    Attributes:
        KNONE: TODO: type description here.
        KDESTROY: TODO: type description here.
        KUPGRADE: TODO: type description here.
        KCLEAN: TODO: type description here.
        KREMOVENODE: TODO: type description here.
        KRESTARTSERVICES: TODO: type description here.

    """

    KNONE = 'kNone'

    KDESTROY = 'kDestroy'

    KUPGRADE = 'kUpgrade'

    KCLEAN = 'kClean'

    KREMOVENODE = 'kRemoveNode'

    KRESTARTSERVICES = 'kRestartServices'

