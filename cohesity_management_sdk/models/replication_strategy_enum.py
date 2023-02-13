# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ReplicationStrategyEnum(object):

    """Implementation of the 'ReplicationStrategy' enum.

    Replication stragegy for the keyspace.
    Specifies the type of an Cassandra source entity.

    Attributes:
        KSIMPLE: TODO: type description here.
        KNETWORK: TODO: type description here.
        KUNSUPPORTED: TODO: type description here.

    """

    KSIMPLE = 'kSimple'

    KNETWORK = 'kNetwork'

    KUNSUPPORTED = 'kUnsupported'

