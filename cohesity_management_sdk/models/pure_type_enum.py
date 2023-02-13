# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PureTypeEnum(object):

    """Implementation of the 'PureType' enum.

    Specifies the entity type such as 'kStorageArray' if the environment is
    kPure.
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

