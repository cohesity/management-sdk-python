# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypePhysicalProtectionSourceEnum(object):

    """Implementation of the 'Type_PhysicalProtectionSource' enum.

    Specifies the type of managed Object in a Physical Protection Source.
    'kGroup' indicates the EH container.
    'kHost' indicates a single physical server.
    'kWindowsCluster' indicates a Microsoft Windows cluster.
    'kOracleRACCluster' indicates an Oracle Real Application Cluster(RAC).
    'kOracleAPCluster' indicates an Oracle Active-Passive Cluster.

    Attributes:
        KGROUP: TODO: type description here.
        KHOST: TODO: type description here.
        KWINDOWSCLUSTER: TODO: type description here.
        KORACLERACCLUSTER: TODO: type description here.
        KORACLEAPCLUSTER: TODO: type description here.

    """

    KGROUP = 'kGroup'

    KHOST = 'kHost'

    KWINDOWSCLUSTER = 'kWindowsCluster'

    KORACLERACCLUSTER = 'kOracleRACCluster'

    KORACLEAPCLUSTER = 'kOracleAPCluster'

