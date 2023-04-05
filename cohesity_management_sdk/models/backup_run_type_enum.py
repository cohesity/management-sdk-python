# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class BackupRunTypeEnum(object):

    """Implementation of the 'BackupRunType' enum.
    The backup run type to which this copy policy applies to. If set, this will
    ensure that the first run in scheduled period of given type will be copied.
    If this isn't set, copy tasks will be generated as per other filters in the
    protection policy. Currently, it can only be set to Full. 'kRegular'
    indicates a incremental (CBT) backup. Incremental backups utilizing CBT (if
    supported) are captured of the target protection objects. The first run of
    a kRegular schedule captures all the blocks. 'kFull' indicates a full (no
    CBT) backup. A complete backup (all blocks) of the target protection
    objects are always captured and Change Block Tracking (CBT) is not
    utilized. 'kLog' indicates a Database Log backup. Capture the database
    transaction logs to allow rolling back to a specific point in time.
    'kSystem' indicates a system backup. System backups are used to do bare
    metal recovery of the system to a specific point in time.


    Attributes:
        KREGULAR: TODO: type description here.
        KFULL: TODO: type description here.
        KLOG: TODO: type description here.
        KSYSTEM: TODO: type description here.

    """

    KREGULAR = 'kRegular'

    KFULL = 'kFull'

    KLOG = 'kLog'

    KSYSTEM = 'kSystem'
