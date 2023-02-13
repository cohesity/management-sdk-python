# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UsageTypeEnum(object):

    """Implementation of the 'UsageType' enum.

    Specifies the usage type of the Vault.
    'kArchival' indicates the Vault provides archive storage for backup data.
    'kCloudSpill' indicates the Vault provides additional storage for cold
    data.

    Attributes:
        KARCHIVAL: TODO: type description here.
        KCLOUDSPILL: TODO: type description here.

    """

    KARCHIVAL = 'kArchival'

    KCLOUDSPILL = 'kCloudSpill'

