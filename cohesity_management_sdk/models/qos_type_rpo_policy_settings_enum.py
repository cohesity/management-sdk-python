# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class QosTypeRpoPolicySettingsEnum(object):

    """Implementation of the 'QosType_RpoPolicySettings' enum.

    Specifies the QoS policy type to use.
    'kBackupHDD' indicates the Cohesity Cluster writes data directly to
    the HDD tier for this Protection Job. This is the recommended setting.
    'kBackupSSD' indicates the Cohesity Cluster writes data directly to
    the SSD tier for this Protection Job. Only specify this policy if
    you need fast ingest speed for a small number of Protection Jobs.

    Attributes:
        KBACKUPHDD: TODO: type description here.
        KBACKUPSSD: TODO: type description here.

    """

    KBACKUPHDD = 'kBackupHDD'

    KBACKUPSSD = 'kBackupSSD'

