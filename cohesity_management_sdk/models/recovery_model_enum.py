# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RecoveryModelEnum(object):

    """Implementation of the 'RecoveryModel' enum.

    Specifies the Recovery Model for the database in SQL environment.
    Only meaningful for the 'kDatabase' SQL Protection Source.
    Specifies the Recovery Model set for the Microsoft SQL Server.
    'kSimpleRecoveryModel' indicates the Simple SQL Recovery Model which
    does not utilize log backups.
    'kFullRecoveryModel' indicates the Full SQL Recovery Model which
    requires log backups and allows recovery to a single point in time.
    'kBulkLoggedRecoveryModel' indicates the Bulk Logged SQL Recovery Model
    which requires log backups and allows high-performance bulk copy
    operations.

    Attributes:
        KSIMPLERECOVERYMODEL: TODO: type description here.
        KFULLRECOVERYMODEL: TODO: type description here.
        KBULKLOGGEDRECOVERYMODEL: TODO: type description here.

    """

    KSIMPLERECOVERYMODEL = 'kSimpleRecoveryModel'

    KFULLRECOVERYMODEL = 'kFullRecoveryModel'

    KBULKLOGGEDRECOVERYMODEL = 'kBulkLoggedRecoveryModel'

