# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeOracleProtectionSourceEnum(object):

    """Implementation of the 'Type_OracleProtectionSource' enum.

    Specifies the type of the managed Object in Oracle Protection Source.
    'kRACRootContainer' indicates the entity is a root container to an Oracle
    Real Application clusters(Oracle RAC).
    'kRootContainer' indicates the entity is a root container to an Oracle
    standalone server.
    'kHost' indicates the entity is an Oracle host.
    'kDatabase' indicates the entity is an Oracle Database.
    'kTableSpace' indicates the entity is an Oracle table space.
    'kTable' indicates the entity is an Oracle table.

    Attributes:
        KRACROOTCONTAINER: TODO: type description here.
        KROOTCONTAINER: TODO: type description here.
        KHOST: TODO: type description here.
        KDATABASE: TODO: type description here.
        KTABLESPACE: TODO: type description here.
        KTABLE: TODO: type description here.

    """

    KRACROOTCONTAINER = 'kRACRootContainer'

    KROOTCONTAINER = 'kRootContainer'

    KHOST = 'kHost'

    KDATABASE = 'kDatabase'

    KTABLESPACE = 'kTableSpace'

    KTABLE = 'kTable'

