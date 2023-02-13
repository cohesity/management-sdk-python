# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RemovalStateEnum(object):

    """Implementation of the 'RemovalState' enum.

    Specifies the current healing state of the Cluster.
    'kNoRemoval' indicates that there are no removal operations currently
    happening on the Cluster.
    'kNodeRemoval' indicates that there is a Node being removed from the
    Cluster.
    'kDiskRemoval' indicates that there is a Disk being removed from the
    Cluster.
    'kNodeAndDiskRemoval' indicates that there is a Node and a Disk being
    removed from the Cluster.

    Attributes:
        KNOREMOVAL: TODO: type description here.
        KNODEREMOVAL: TODO: type description here.
        KDISKREMOVAL: TODO: type description here.
        KNODEANDDISKREMOVAL: TODO: type description here.

    """

    KNOREMOVAL = 'kNoRemoval'

    KNODEREMOVAL = 'kNodeRemoval'

    KDISKREMOVAL = 'kDiskRemoval'

    KNODEANDDISKREMOVAL = 'kNodeAndDiskRemoval'

