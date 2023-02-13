# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileRecoveryMethodEnum(object):

    """Implementation of the 'FileRecoveryMethod'
    enum.

    Specifies the type of method to be used to perform file recovery.
    'kAutoDeploy' indicates that file restore operation wiil be performed
    using an ephemeral agent.
    'kUseExistingAgent' indicates that file restore operation will be
    performed using an persistent agent.
    'kUseHypervisorAPIs' indicates that file restore operation will be
    performed using an hypervisor API's.

    Attributes:
        KAUTODEPLOY: TODO: type description here.
        KUSEEXISTINGAGENT: TODO: type description here.
        KUSEHYPERVISORAPIS: TODO: type description here.

    """

    KAUTODEPLOY = 'kAutoDeploy'

    KUSEEXISTINGAGENT = 'kUseExistingAgent'

    KUSEHYPERVISORAPIS = 'kUseHypervisorAPIs'

