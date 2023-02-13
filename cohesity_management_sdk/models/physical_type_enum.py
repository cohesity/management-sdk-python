# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PhysicalTypeEnum(object):

    """Implementation of the 'PhysicalType' enum.

    Specifies the entity type such as 'kPhysicalHost' if the environment is
    kPhysical.
    overrideDescription: true
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

