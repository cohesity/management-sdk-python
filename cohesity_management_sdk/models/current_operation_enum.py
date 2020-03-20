# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class CurrentOperationEnum(object):

    """Implementation of the 'CurrentOperation' enum.

    Specifies the current Cluster-level operation in progress.
    'kUpgrade' indicates the Cohesity Cluster is upgrading to a new release.
    'kRemoveNode' indicates the Cohesity Cluster is removing a Node
    from the Cluster.
    'kNone' indicates no action is occurring on the Cohesity Cluster.
    'kDestroy' indicates the Cohesity Cluster is getting destoryed.
    'kClean' indicates the Cohesity Cluster is getting cleaned.
    'kRestartServices' indicates the Cohesity Cluster is restarting the
    services.

    Attributes:
        KREMOVENODE: TODO: type description here.
        KUPGRADE: TODO: type description here.
        KNONE: TODO: type description here.
        KDESTROY: TODO: type description here.
        KCLEAN: TODO: type description here.
        KRESTARTSERVICES: TODO: type description here.

    """

    KREMOVENODE = 'kRemoveNode'

    KUPGRADE = 'kUpgrade'

    KNONE = 'kNone'

    KDESTROY = 'kDestroy'

    KCLEAN = 'kClean'

    KRESTARTSERVICES = 'kRestartServices'

