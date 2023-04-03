# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RandomIOPreferentialTierEnum(object):

    """Implementation of the 'RandomIOPreferentialTier' enum.
    Specifies the order of perferred storage tiers for random IO operations.


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
