# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StatusTaskEnum(object):

    """Implementation of the 'Status_Task' enum.

    Specifies the status of the task being queried.
    'kActive' indicates that the task is still active.
    'kFinished' indicates that the task has finished without any errors.
    'kFinishedWithError' indicates that the task has finished, but that there
    was an errror of some kind.
    'kCancelled' indicates that the task was cancelled.
    'kFinishedGarbageCollected' inidcates that the task was garbage collected
    due to its subtasks not finishing within the allotted time.

    Attributes:
        KACTIVE: TODO: type description here.
        KFINISHED: TODO: type description here.
        KFINISHEDWITHERROR: TODO: type description here.
        KCANCELLED: TODO: type description here.
        KFINISHEDGARBAGECOLLECTED: TODO: type description here.

    """

    KACTIVE = 'kActive'

    KFINISHED = 'kFinished'

    KFINISHEDWITHERROR = 'kFinishedWithError'

    KCANCELLED = 'kCancelled'

    KFINISHEDGARBAGECOLLECTED = 'kFinishedGarbageCollected'

