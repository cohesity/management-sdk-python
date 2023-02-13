# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CombineMethodEnum(object):

    """Implementation of the 'CombineMethod' enum.

    Specifies how to combine the children of this node.
    The combining strategy for child devices. Some of these strategies imply
    constraint on the number of child devices. e.g. RAID5 will have 5
    children.
    'LINEAR' indicates children are juxtaposed to form this device.
    'STRIPE' indicates children are striped.
    'MIRROR' indicates children are mirrored.
    'RAID5'
    'RAID6'
    'ZERO'
    'THIN'
    'THINPOOL'
    'SNAPSHOT'
    'CACHE'
    'CACHEPOOL'

    Attributes:
        LINEAR: TODO: type description here.
        STRIPE: TODO: type description here.
        MIRROR: TODO: type description here.
        RAID5: TODO: type description here.
        RAID6: TODO: type description here.
        ZERO: TODO: type description here.
        THIN: TODO: type description here.
        THINPOOL: TODO: type description here.
        SNAPSHOT: TODO: type description here.
        CACHE: TODO: type description here.
        CACHEPOOL: TODO: type description here.

    """

    LINEAR = 'LINEAR'

    STRIPE = 'STRIPE'

    MIRROR = 'MIRROR'

    RAID5 = 'RAID5'

    RAID6 = 'RAID6'

    ZERO = 'ZERO'

    THIN = 'THIN'

    THINPOOL = 'THINPOOL'

    SNAPSHOT = 'SNAPSHOT'

    CACHE = 'CACHE'

    CACHEPOOL = 'CACHEPOOL'

