# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NimbleTypeEnum(object):

    """Implementation of the 'NimbleType' enum.

    Specifies the entity type such as 'kStorageArray' if the environment is
    kNimble.
    overrideDescription: true
    Examples of SAN Objects include 'kStorageArray' and 'kVolume'.
    'kStorageArray' indicates that entire SAN storage array is being
    protected.
    'kVolume' indicates that volume within the array is being protected.

    Attributes:
        KSTORAGEARRAY: TODO: type description here.
        KVOLUME: TODO: type description here.

    """

    KSTORAGEARRAY = 'kStorageArray'

    KVOLUME = 'kVolume'

