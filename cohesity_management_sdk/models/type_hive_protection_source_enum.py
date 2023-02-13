# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeHiveProtectionSourceEnum(object):

    """Implementation of the 'Type_HiveProtectionSource' enum.

    Specifies the type of the managed Object in Hive Protection Source.
    Specifies the type of an Hive source entity.
    'kCluster' indicates a Hive cluster distributed over several physical
    nodes.
    'kDatabase' indicates a Database in the Hive environment.
    'kTable' indicates a Table in the Hive environment.

    Attributes:
        KCLUSTER: TODO: type description here.
        KDATABASE: TODO: type description here.
        KTABLE: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KDATABASE = 'kDatabase'

    KTABLE = 'kTable'

