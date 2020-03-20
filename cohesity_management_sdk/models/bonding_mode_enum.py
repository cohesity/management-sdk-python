# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class BondingModeEnum(object):

    """Implementation of the 'BondingMode' enum.

    Specifies the bonding mode to use when bonding NICs to this Cluster.
    'KActiveBackup' indicates an Active-backup policy bonding mode.
    'K802_3ad' indicates an EEE 802.3ad Dynamic link aggregation bonding
    mode.
    'KBalanceAlb' indicates a Adaptive load balancing bonding mode.

    Attributes:
        ACTIVEBACKUP: TODO: type description here.
        ENUM_802_3AD: TODO: type description here.
        BALANCEALB: TODO: type description here.

    """

    ACTIVEBACKUP = 'ActiveBackup'

    ENUM_802_3AD = '802_3ad'

    BALANCEALB = 'BalanceAlb'

