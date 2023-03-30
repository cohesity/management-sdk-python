# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StatusBackupRunEnum(object):

    """Implementation of the 'StatusBackupRun' enum.
    Specifies the status of Backup task such as 'kRunning', 'kSuccess',
    'kFailure' etc. kWarning, kOnHold, kMissed, kFinalizing, kWaitingToRetry.


    Attributes:
        KACCEPTED: TODO: type description here.
        KRUNNING: TODO: type description here.
        KCANCELING: TODO: type description here.
        KCANCELED: TODO: type description here.
        KSUCCESS: TODO: type description here.
        KFAILURE: TODO: type description here.

    """

    KACCEPTED = 'kAccepted'

    KRUNNING = 'kRunning'

    KCANCELING = 'kCanceling'

    KCANCELED = 'kCanceled'

    KSUCCESS = 'kSuccess'

    KFAILURE = 'kFailure'
