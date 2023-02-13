# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TaskStateEnum(object):

    """Implementation of the 'TaskState' enum.

    Specifies the current state of the restore virtual disks task.
    Specifies the current state of the restore virtual disks task.
    'kDetachDisksDone' indicates the detached state of disks.
    'kSetupDisksDone' indicates that disks setup is completed.
    'kMigrateDisksStarted' indicates that disks are being migrated.
    'kMigrateDisksDone' indicates that disk migration is completed.
    'kUnMountDatastoreDone' indicates that disk has unmounted the datastore.

    Attributes:
        KDETACHDISKSDONE: TODO: type description here.
        KSETUPDISKSDONE: TODO: type description here.
        KMIGRATEDISKSSTARTED: TODO: type description here.
        KMIGRATEDISKSDONE: TODO: type description here.
        KUNMOUNTDATASTOREDONE: TODO: type description here.

    """

    KDETACHDISKSDONE = 'kDetachDisksDone'

    KSETUPDISKSDONE = 'kSetupDisksDone'

    KMIGRATEDISKSSTARTED = 'kMigrateDisksStarted'

    KMIGRATEDISKSDONE = 'kMigrateDisksDone'

    KUNMOUNTDATASTOREDONE = 'kUnMountDatastoreDone'

