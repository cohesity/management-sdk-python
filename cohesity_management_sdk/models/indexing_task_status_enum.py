# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class IndexingTaskStatusEnum(object):

    """Implementation of the 'IndexingTaskStatus' enum.

    Specifies the status of the indexing Job/task.
    'kJobRunning' indicates that the Job/task is currently running.
    'kJobFinished' indicates that the Job/task completed and finished.
    'kJobFailed' indicates that the Job/task failed and did not complete.
    'kJobCanceled' indicates that the Job/task was canceled.
    'kJobPaused' indicates the Job/task is paused.

    Attributes:
        KJOBRUNNING: TODO: type description here.
        KJOBFINISHED: TODO: type description here.
        KJOBFAILED: TODO: type description here.
        KJOBCANCELED: TODO: type description here.
        KJOBPAUSED: TODO: type description here.

    """

    KJOBRUNNING = 'kJobRunning'

    KJOBFINISHED = 'kJobFinished'

    KJOBFAILED = 'kJobFailed'

    KJOBCANCELED = 'kJobCanceled'

    KJOBPAUSED = 'kJobPaused'

