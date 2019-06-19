# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class PhysicalTypeEnum(object):

    """Implementation of the 'PhysicalType' enum.

    Specifies the entity type such as 'kPhysicalHost' if the environment is
    kPhysical. overrideDescription: true 'kHost' indicates a single physical
    server. 'kWindowsCluster' indicates a Microsoft Windows cluster.

    Attributes:
        KHOST: TODO: type description here.
        KWINDOWSCLUSTER: TODO: type description here.

    """

    KHOST = 'kHost'

    KWINDOWSCLUSTER = 'kWindowsCluster'

