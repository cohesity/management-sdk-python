# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RunTypeRunProtectionJobParamEnum(object):

    """Implementation of the 'RunType_RunProtectionJobParam' enum.

    Specifies the type of backup. If not specified, 'kRegular' is assumed.
    'kRegular' indicates a incremental (CBT) backup. Incremental backups
    utilizing CBT (if supported) are captured of the target protection
    objects.
    The first run of a kRegular schedule captures all the blocks.
    'kFull' indicates a full (no CBT) backup. A complete backup
    (all blocks) of the target protection objects are always captured and
    Change Block Tracking (CBT) is not utilized.
    'kLog' indicates a Database Log backup. Capture the database
    transaction logs to allow rolling back to a specific point in time.
    'kSystem' indicates a system backup. System backups are used to do
    bare metal recovery of the system to a specific point in time.

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

