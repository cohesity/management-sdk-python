# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeIsilonProtectionSourceEnum(object):

    """Implementation of the 'Type_IsilonProtectionSource' enum.

    Specifies the type of the entity in an Isilon OneFs file system
    like 'kCluster', 'kZone', or, 'kMountPoint'.
    'kCluster' indicates an Isilon OneFs Cluster.
    'kZone' indicates an access zone in an Isilon OneFs Cluster.
    'kMountPoint' indicates a mount point exposed by an Isilon OneFs Cluster.

    Attributes:
        KCLUSTER: TODO: type description here.
        KZONE: TODO: type description here.
        KMOUNTPOINT: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KZONE = 'kZone'

    KMOUNTPOINT = 'kMountPoint'

