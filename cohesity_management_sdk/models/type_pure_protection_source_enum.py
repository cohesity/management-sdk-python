# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class TypePureProtectionSourceEnum(object):

    """Implementation of the 'Type_PureProtectionSource' enum.

    Specifies the type of managed Object in a pure Protection Source like
    a kStorageArray or kVolume.
    Examples of Pure Objects include 'kStorageArray' and 'kVolume'.
    'kStorageArray' indicates that entire pure storage array is being
    protected.
    'kVolume' indicates that volume within the array is being protected.

    Attributes:
        KSTORAGEARRAY: TODO: type description here.
        KVOLUME: TODO: type description here.

    """

    KSTORAGEARRAY = 'kStorageArray'

    KVOLUME = 'kVolume'

