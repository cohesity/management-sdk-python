# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class BackupTypeEnum(object):

    """Implementation of the 'BackupType' enum.

    Specifies the type of backup supported by the VM.
    'kRctBackup', 'kVssBackup'
    Specifies the type of an HyperV datastore object.
    'kRctBackup' indicates backup is done using RCT/checkpoints.
    'kVssBackup' indicates backup is done using VSS.

    Attributes:
        KRCTBACKUP: TODO: type description here.
        KVSSBACKUP: TODO: type description here.

    """

    KRCTBACKUP = 'kRctBackup'

    KVSSBACKUP = 'kVssBackup'

