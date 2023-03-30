# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ServiceStateEnum(object):

    """Implementation of the 'ServiceState' enum.
    Specifies the status of the cbt driver. Specifies the service state of the
    cbt driver. 'kRunning' indicates the cbt driver is running. 'kStopped'
    indicates the service is stopped. 'kPaused' indicates the service is paused
    (it is a Windows-specific state). 'kUnknown' indicates the service with the
    specified name is not known on the system.


    Attributes:
        KRUNNING: TODO: type description here.
        KSTOPPED: TODO: type description here.
        KPAUSED: TODO: type description here.
        KUNKNOWN: TODO: type description here.

    """

    KRUNNING = 'kRunning'

    KSTOPPED = 'kStopped'

    KPAUSED = 'kPaused'

    KUNKNOWN = 'kUnknown'
