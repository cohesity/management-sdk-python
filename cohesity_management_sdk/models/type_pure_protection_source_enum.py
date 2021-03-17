# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class TypePureProtectionSourceEnum(object):

    """Implementation of the 'Type_PureProtectionSource' enum.

    Specifies the type of managed Object in a SAN/Pure Protection
    Source like a kStorageArray or kVolume.
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

