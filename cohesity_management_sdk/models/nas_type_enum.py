# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasTypeEnum(object):

    """Implementation of the 'NasType' enum.

    Specifies the type of a NAS Object such as 'kGroup', or 'kHost'.
    Specifies the kind of NAS mount.
    'kGroup' indicates top level node that holds individual NAS hosts.
    'kHost' indicates a single NAS path that can be mounted.
    'kDfsGroup' indicates a DFS group containing top level directories mapped
    to different servers.
    'kDfsTopDir' indicates a top level directory inside a DFS group,
    discovered when registering a DFS group.

    Attributes:
        KGROUP: TODO: type description here.
        KHOST: TODO: type description here.
        KDFSGROUP: TODO: type description here.
        KDFSTOPDIR: TODO: type description here.

    """

    KGROUP = 'kGroup'

    KHOST = 'kHost'

    KDFSGROUP = 'kDfsGroup'

    KDFSTOPDIR = 'kDfsTopDir'

