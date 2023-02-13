# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SqlServerDbStateEnum(object):

    """Implementation of the 'SqlServerDbState' enum.

    The state of the database as returned by SQL Server.
    Indicates the state of the database. The values correspond to the 'state'
    field in the system table sys.databases. See https://goo.gl/P66XqM.
    'kOnline' indicates that database is in online state.
    'kRestoring' indicates that database is in restore state.
    'kRecovering' indicates that database is in recovery state.
    'kRecoveryPending' indicates that database recovery is in pending state.
    'kSuspect' indicates that primary filegroup is suspect and may be
    damaged.
    'kEmergency' indicates that manually forced emergency state.
    'kOffline' indicates that database is in offline state.
    'kCopying' indicates that database is in copying state.
    'kOfflineSecondary' indicates that secondary database is in offline
    state.

    Attributes:
        KONLINE: TODO: type description here.
        KRESTORING: TODO: type description here.
        KRECOVERING: TODO: type description here.
        KRECOVERYPENDING: TODO: type description here.
        KSUSPECT: TODO: type description here.
        KEMERGENCY: TODO: type description here.
        KOFFLINE: TODO: type description here.
        KCOPYING: TODO: type description here.
        KOFFLINESECONDARY: TODO: type description here.

    """

    KONLINE = 'kOnline'

    KRESTORING = 'kRestoring'

    KRECOVERING = 'kRecovering'

    KRECOVERYPENDING = 'kRecoveryPending'

    KSUSPECT = 'kSuspect'

    KEMERGENCY = 'kEmergency'

    KOFFLINE = 'kOffline'

    KCOPYING = 'kCopying'

    KOFFLINESECONDARY = 'kOfflineSecondary'

