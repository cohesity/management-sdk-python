# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LockingProtocolEnum(object):

    """Implementation of the 'LockingProtocol' enum.

    Specifies the supported mechanisms to explicity lock a file from NFS/SMB
    interface. Supported locking protocols: kSetReadOnly, kSetAtime.
    'kSetReadOnly' is compatible with Isilon/Netapp behaviour. This locks the
    file and the retention duration is determined in this order:
    1) atime, if set by user/application and within min and max retention
    duration.
    2) Min retention duration, if set.
    3) Otherwise, file is switched to expired data automatically.
    'kSetAtime' is compatible with Data Domain behaviour.

    Attributes:
        KSETREADONLY: TODO: type description here.
        KSETATIME: TODO: type description here.

    """

    KSETREADONLY = 'kSetReadOnly'

    KSETATIME = 'kSetAtime'

