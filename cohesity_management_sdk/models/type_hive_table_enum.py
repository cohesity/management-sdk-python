# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeHiveTableEnum(object):

    """Implementation of the 'Type_HiveTable' enum.

    Specifies the type of table ex. MANAGED,VIRTUAL etc.
    Specifies the type of an Hive table.
    'kManaged' indicates a MANAGED Hive table.
    'kExternal' indicates a EXTERNAL Hive table.
    'kVirtual' indicates a VIRTUAL Hive tablet.
    'kIndex' indicates a INDEX Hive table.

    Attributes:
        KMANAGER: TODO: type description here.
        KEXTERNAL: TODO: type description here.
        KVIRTUAL: TODO: type description here.
        KINDEX: TODO: type description here.

    """

    KMANAGER = 'kManaged'

    KEXTERNAL = 'kExternal'

    KVIRTUAL = 'kVirtual'

    KINDEX = 'kIndex'


