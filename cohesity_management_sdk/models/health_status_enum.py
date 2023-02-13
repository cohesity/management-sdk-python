# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class HealthStatusEnum(object):

    """Implementation of the 'HealthStatus' enum.

    Specifies the health status of the Cohesity agent.
    Specifies the status of the agent running on a physical source.
    'kUnknown' indicates the Agent is not known. No attempt to connect
    to the Agent has occurred.
    'kUnreachable' indicates the Agent is not reachable.
    'kHealthy' indicates the Agent is healthy.
    'kDegraded' indicates the Agent is running but in a degraded state.

    Attributes:
        KUNKNOWN: TODO: type description here.
        KUNREACHABLE: TODO: type description here.
        KHEALTHY: TODO: type description here.
        KDEGRADED: TODO: type description here.

    """

    KUNKNOWN = 'kUnknown'

    KUNREACHABLE = 'kUnreachable'

    KHEALTHY = 'kHealthy'

    KDEGRADED = 'kDegraded'

