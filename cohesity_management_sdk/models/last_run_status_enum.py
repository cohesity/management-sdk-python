# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LastRunStatusEnum(object):

    """Implementation of the 'LastRunStatus' enum.
    Specifies the Job Run status of the last Job Run protecting this Protection
    Source Object. 'kSuccess' indicates that the Job Run was successful.
    'kRunning' indicates that the Job Run is currently running. 'kWarning'
    indicates that the Job Run was successful but warnings were issued.
    'kCancelled' indicates that the Job Run was canceled. 'kError' indicates
    the Job Run encountered an error and did not run to completion.


    Attributes:
        KSUCCESS: TODO: type description here.
        KRUNNING: TODO: type description here.
        KWARNING: TODO: type description here.
        KCANCELLED: TODO: type description here.
        KERROR: TODO: type description here.

    """

    KSUCCESS = 'kSuccess'

    KRUNNING = 'kRunning'

    KWARNING = 'kWarning'

    KCANCELLED = 'kCancelled'

    KERROR = 'kError'
