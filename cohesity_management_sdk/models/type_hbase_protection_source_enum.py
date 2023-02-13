# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeHBaseProtectionSourceEnum(object):

    """Implementation of the 'Type_HBaseProtectionSource' enum.

    Specifies the type of the managed Object in HBase Protection Source.
    Specifies the type of an HBase source entity.
    'kCluster' indicates a HBase cluster distributed over several physical
    nodes.
    'kNamespace' indicates a Namespace in the HBase environment.
    'kTable' indicates a Table in the HBase environment.

    Attributes:
        KCLUSTER: TODO: type description here.
        KNAMESPACE: TODO: type description here.
        KTABLE: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KNAMESPACE = 'kNamespace'

    KTABLE = 'kTable'

