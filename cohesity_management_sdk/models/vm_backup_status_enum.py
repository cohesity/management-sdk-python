# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VmBackupStatusEnum(object):

    """Implementation of the 'VmBackupStatus' enum.

    Specifies the status of the VM for backup purpose.
    overrideDescription: true
    Specifies the backup status of a HyperV Virtual Machine object.
    'kSupported' indicates the agent on the VM can do backup.
    'kUnsupportedConfig' indicates the agent on the VM cannot do backup.
    'kMissing' indicates the VM is not found in SCVMM.

    Attributes:
        KSUPPORTED: TODO: type description here.
        KUNSUPPORTEDCONFIG: TODO: type description here.
        KMISSING: TODO: type description here.

    """

    KSUPPORTED = 'kSupported'

    KUNSUPPORTEDCONFIG = 'kUnsupportedConfig'

    KMISSING = 'kMissing'

