# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StatusSourceBackupStatusEnum(object):

    """Implementation of the 'Status_SourceBackupStatus' enum.

    Specifies the status of the source object being protected.
    'kAccepted' indicates the task is queued to run but not yet running.
    'kRunning' indicates the task is running.
    'kCanceling' indicates a request to cancel the task has occurred but
    the task is not yet canceled.
    'kCanceled' indicates the task has been canceled.
    'kSuccess' indicates the task was successful.
    'kFailure' indicates the task failed.
    'kWarning' indicates the task has finished with warning.
    'kOnHold' indicates the task is kept onHold.
    'kMissed' indicates the task is missed.

    Attributes:

        KACCEPTED: TODO: type description here.
        KRUNNING: TODO: type description here.
        KCANCELING: TODO: type description here.
        KCANCELED: TODO: type description here.
        KSUCCESS: TODO: type description here.
        KFAILURE: TODO: type description here.
        KWARNING: TODO: type description here.
        KONHOLD: TODO: type description here.
        KMISSED: TODO: type description here.

    """

    KACCEPTED = 'kAccepted'

    KRUNNING = 'kRunning'

    KCANCELING = 'kCanceling'

    KCANCELED = 'kCanceled'

    KSUCCESS = 'kSuccess'

    KFAILURE = 'kFailure'

    KWARNING = 'kWarning'

    KONHOLD = 'kOnHold'

    KMISSED = 'kMissed'

