# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CloneStatusEnum(object):

    """Implementation of the 'CloneStatus' enum.
    Specifies the latest state of the clone. This is only set when this task is
    a clone task.


    Attributes:
        KRUNNING: TODO: type description here.
        KTEARINGDOWN: TODO: type description here.
        KTORNDOWN: TODO: type description here.
        KTEARDOWNFAILED: TODO: type description here.

    """

    KRUNNING = 'kRunning'

    KTEARINGDOWN = 'kTearingDown'

    KTORNDOWN = 'kTornDown'

    KTEARDOWNFAILED = 'kTearDownFailed'
