# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ActionEnum(object):

    """Implementation of the 'Action' enum.

    Specifies the action to take on the specified service.
    'kStop' indicates that the specified services will be stopped.
    'kStart' indicates that the specified services will be started.
    'kRestart' indicates that the specified services will be restarted.

    Attributes:
        KSTOP: TODO: type description here.
        KSTART: TODO: type description here.
        KRESTART: TODO: type description here.

    """

    KSTOP = 'kStop'

    KSTART = 'kStart'

    KRESTART = 'kRestart'

