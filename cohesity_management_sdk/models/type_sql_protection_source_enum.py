# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeSqlProtectionSourceEnum(object):

    """Implementation of the 'Type_SqlProtectionSource' enum.

    Specifies the type of the managed Object in a SQL Protection Source.
    Examples of SQL Objects include 'kInstance' and 'kDatabase'.
    'kInstance' indicates that SQL server instance is being protected.
    'kDatabase' indicates that SQL server database is being protected.
    'kAAG' indicates that SQL AAG (AlwaysOn Availability Group) is being
    protected.
    'kAAGRootContainer' indicates that SQL AAG's root container is being
    protected.
    'kRootContainer' indicates root container for SQL sources.

    Attributes:
        KINSTANCE: TODO: type description here.
        KDATABASE: TODO: type description here.
        KAAG: TODO: type description here.
        KAAGROOTCONTAINER: TODO: type description here.
        KROOTCONTAINER: TODO: type description here.

    """

    KINSTANCE = 'kInstance'

    KDATABASE = 'kDatabase'

    KAAG = 'kAAG'

    KAAGROOTCONTAINER = 'kAAGRootContainer'

    KROOTCONTAINER = 'kRootContainer'

