# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VaultTypeEnum(object):

    """Implementation of the 'VaultType' enum.

    Specifies the type of the Archival External Target such as 'kCloud',
    'kTape' or 'kNas'.
    'kCloud' indicates the archival location as Cloud.
    'kTape' indicates the archival location as Tape.
    'kNas' indicates the archival location as Network Attached Storage (Nas).

    Attributes:
        KCLOUD: TODO: type description here.
        KTAPE: TODO: type description here.
        KNAS: TODO: type description here.

    """

    KCLOUD = 'kCloud'

    KTAPE = 'kTape'

    KNAS = 'kNas'

