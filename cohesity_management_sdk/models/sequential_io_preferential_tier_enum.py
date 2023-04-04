# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SequentialIOPreferentialTierEnum(object):

    """Implementation of the 'SequentialIOPreferentialTier' enum.
    Specifies the preferred storage tier for sequential IO operations.


    Attributes:
        KPCIESSD: TODO: type description here.
        KSATASSD: TODO: type description here.
        KSATAHDD: TODO: type description here.
        KCLOUD: TODO: type description here.

    """

    KPCIESSD = 'kPcieSsd'

    KSATASSD = 'kSataSsd'

    KSATAHDD = 'kSataHdd'

    KCLOUD = 'kCloud'
