# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class BondingModeEnum(object):

    """Implementation of the 'BondingMode' enum.

    Specifies the bonding mode to use for this bond. If not specified,
    this value will default to 'kActiveBackup'.
    'kActiveBackup' indicates active backup bonding mode.
    'k802_3ad' indicates 802.3ad bonding mode.

    Attributes:
        KACTIVEBACKUP: TODO: type description here.
        K802_3AD: TODO: type description here.

    """

    KACTIVEBACKUP = 'kActiveBackup'

    K802_3AD = 'k802_3ad'

