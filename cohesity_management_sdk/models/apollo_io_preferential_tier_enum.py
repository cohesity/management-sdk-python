# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ApolloIOPreferentialTierEnum(object):

    """Implementation of the 'ApolloIOPreferentialTier' enum.

    Specifies the preferred storage tier used by Apollo as its actions WAL.

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

