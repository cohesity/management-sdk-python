# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeOracleDataGuardInfoEnum(object):

    """Implementation of the 'TypeOracleDataGuardInfoEnum' enum.

    Specifies the type of standby database.
    Specifies the type of standby database.
    'kPhysical' indicates that the current database provides a physically
    identical copy of the primary database, with on disk structures identical
    to the primary database on a block-for-block basis. It is kept
    synchronized with the primary database, though Redo Apply, which recovers
    the redo data received from the primary database and applies the redo to
    the physical standby database.
    'kLogical' indicates that the current database provides the same logical
    information as the production database, although the physical structure
    can be different. It is kept synchronized with the primary database
    thorugh SQL Apply, which transforms the data in the redo received from the
    primary database into SQL statements and then executing the SQL statements
    on the standby database.
    'kSnapshot' indicates that the current database is a fully updateable
    standby created by converting a physical standby database into a snasphot
    standby database. It receives and archives but does not apply redo data
    from a primary database.

    Attributes:
        KPHYSICAL: TODO: type description here.
        KLOGICAL: TODO: type description here.
        KSNAPSHOT: TODO: type description here.

    """

    KPHYSICAL = 'kPhysical'

    KLOGICAL = 'kLogical'

    KSNAPSHOT = 'kSnapshot'

