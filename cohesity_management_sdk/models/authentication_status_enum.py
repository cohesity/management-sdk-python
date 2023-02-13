# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthenticationStatusEnum(object):

    """Implementation of the 'AuthenticationStatus' enum.

    Specifies the status of the authenticating to the Protection Source
    when registering it with Cohesity Cluster. If the status is 'kFinished'
    and there is no error, registration is successful.
    Specifies the status of the authentication during the registration of a
    Protection Source.
    'kPending' indicates the authentication is in progress.
    'kScheduled' indicates the authentication is scheduled.
    'kFinished' indicates the authentication is completed.
    'kRefreshInProgress' indicates the refresh is in progres.

    Attributes:
        KPENDING: TODO: type description here.
        KSCHEDULED: TODO: type description here.
        KFINISHED: TODO: type description here.
        KREFRESHINPROGRESS: TODO: type description here.

    """

    KPENDING = 'kPending'

    KSCHEDULED = 'kScheduled'

    KFINISHED = 'kFinished'

    KREFRESHINPROGRESS = 'kRefreshInProgress'

