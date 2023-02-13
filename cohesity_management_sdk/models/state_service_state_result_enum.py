# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StateServiceStateResultEnum(object):

    """Implementation of the 'State_ServiceStateResult' enum.

    Specifies the state of the service.
    'kServiceStopped' indicates that the service has been stopped.
    'kServiceRunning' indicates that the service is currently running.
    'kServiceRestarting' indicates that the service is in the queue to be
    restarted.

    Attributes:
        KSERVICESTOPPED: TODO: type description here.
        KSERVICERUNNING: TODO: type description here.
        KSERVICERESTARTING: TODO: type description here.

    """

    KSERVICESTOPPED = 'kServiceStopped'

    KSERVICERUNNING = 'kServiceRunning'

    KSERVICERESTARTING = 'kServiceRestarting'

