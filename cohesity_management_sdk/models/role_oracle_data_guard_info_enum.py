# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RoleOracleDataGuardInfoEnum(object):

    """Implementation of the 'RoleOracleDataGuardInfoEnum' enum.

    Specifies the role of the DataGuard database.
    Specifies the role of the DataGuard database.

    A Data Guard configuration contains one production database, also referred
    to as the primary database, that functions in the primary role.
    The primary database can be either a single-instance Oracle database or an
    Oracle Real Application Clusters database.

    A standby database is a transactionally consistent copy of the primary
    database. Similar to a primary database, a standby database can be either
    a single-instance Oracle database or an Oracle Real Application Clusters
    database.
    'kPrimary' indicates that the current database is primary database.
    'kStandby' indicates that the current database is standby database.

    Attributes:
        KPRIMARY: TODO: type description here.
        KSECONDARY: TODO: type description here.

    """

    KPRIMARY = 'kPrimary'

    KSECONDARY = 'kSecondary'

