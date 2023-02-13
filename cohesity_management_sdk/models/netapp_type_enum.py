# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NetappTypeEnum(object):

    """Implementation of the 'NetappType' enum.

    Specifies the entity type such as 'kCluster,' if the environment is
    kNetapp.
    'kCluster' indicates a Netapp cluster as a protection source.
    'kVserver' indicates a Netapp vserver in a cluster as a protection
    source.
    'kVolume' indicates  a volume in Netapp vserver as a protection source.

    Attributes:
        KCLUSTER: TODO: type description here.
        KVSERVER: TODO: type description here.
        KVOLUME: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KVSERVER = 'kVserver'

    KVOLUME = 'kVolume'

