# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

class Type11Enum(object):

    """Implementation of the 'Type11' enum.

    Specifies the type of managed NetApp Object in a NetApp Protection Source
    such as 'kCluster', 'kVserver' or 'kVolume'.
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

