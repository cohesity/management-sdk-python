# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RunStatusEnum(object):

    """Implementation of the 'RunStatus' enum.

    Filter by a list of run statuses such as 'kRunning',
    'kSuccess', 'kFailure' etc.
    Snapshots of Job Runs with the specified run statuses are reported.
    'kSuccess' indicates that the Job Run was successful.
    'kRunning' indicates that the Job Run is currently running.
    'kWarning' indicates that the Job Run was successful but warnings were
    issued.
    'kCancelled' indicates that the Job Run was canceled.
    'kError' indicates the Job Run encountered an error and did not run to
    completion.

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
