# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AgentStatusEnum(object):

    """Implementation of the 'AgentStatus' enum.
    Specifies the status of the agent on the Exchange host. Specifies the
    status of agent on Exchange Application Server. 'kSupported' indicates the
    agent is supported for Exchange data protection. 'kUnSupported' indicates
    the agent is not supported for Exchange data protection. 'kUpgrade'
    indicates the agent of server need to be upgraded.


    Attributes:
        KSUPPORTED: TODO: type description here.
        KUPGRADE: TODO: type description here.
        KUNSUPPORTED: TODO: type description here.

    """

    KSUPPORTED = 'kSupported'

    KUPGRADE = 'kUpgrade'

    KUNSUPPORTED = 'kUnsupported'
