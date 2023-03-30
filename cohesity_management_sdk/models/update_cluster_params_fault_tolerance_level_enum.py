# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UpdateClusterParamsFaultToleranceLevelEnum(object):

    """Implementation of the 'UpdateClusterParams_FaultToleranceLevel' enum.

    Specifies the level which 'MetadataFaultToleranceFactor' applies to.
    'kNode' indicates 'MetadataFaultToleranceFactor' applies to Node level.
    'kChassis' indicates 'MetadataFaultToleranceFactor' applies to Chassis
    level.
    'kRack' indicates 'MetadataFaultToleranceFactor' applies to Rack level.

    Attributes:
        KNODE: TODO: type description here.
        KCHASSIS: TODO: type description here.
        KRACK: TODO: type description here.

    """

    KNODE = 'kNode'

    KCHASSIS = 'kChassis'

    KRACK = 'kRack'

