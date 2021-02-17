# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class UpgradeStatusEnum(object):

    """Implementation of the 'UpgradeStatus' enum.

    Specifies the status of the upgrade of the agent on a physical server.
    Specifies the status of the upgrade of the agent on a physical server.
    'kIdle' indicates there is no agent upgrade in progress.
    'kAccepted' indicates the Agent upgrade is accepted.
    'kStarted' indicates the Agent upgrade is in progress.
    'kFinished' indicates the Agent upgrade is completed.

    Attributes:
        KIDLE: TODO: type description here.
        KACCEPTED: TODO: type description here.
        KSTARTED: TODO: type description here.
        KFINISHED: TODO: type description here.

    """

    KIDLE = 'kIdle'

    KACCEPTED = 'kAccepted'

    KSTARTED = 'kStarted'

    KFINISHED = 'kFinished'

