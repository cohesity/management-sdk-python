# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StatusExchangeHostInfoEnum(object):

    """Implementation of the 'Status_ExchangeHostInfo' enum.

    Specifies the status of the registration of the Exchange Host.
    Specifies the status of registration of Exchange Application Server.
    'kUnknown' indicates the status is not known.
    'kHealthy' indicates the status is healty and is registered as
    Exchange Server.
    'kUnHealthy' indicates the exchange application is registered on the
    physical server but it is unreachable now.
    'kUnregistered' indicates the server is not registered as physical source.
    'kUnreachable' indicates the server is not reachable from the cohesity
    cluster or the cohesity protection server is not installed on the exchange
    server.
    'kDetached' indicates the server is removed from the ExchangeDAG.

    Attributes:
        KUNKNOWN: TODO: type description here.
        KHEALTHY: TODO: type description here.
        KUNHEALTHY: TODO: type description here.
        KUNREGISTERED: TODO: type description here.
        KUNREACHABLE: TODO: type description here.
        KDETACHED: TODO: type description here.

    """

    KUNKNOWN = 'kUnknown'

    KHEALTHY = 'kHealthy'

    KUNHEALTHY = 'kUnHealthy'

    KUNREGISTERED = 'kUnregistered'

    KUNREACHABLE = 'kUnreachable'

    KDETACHED = 'kDetached'

