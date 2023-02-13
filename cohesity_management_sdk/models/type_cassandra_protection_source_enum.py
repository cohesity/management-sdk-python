# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeCassandraProtectionSourceEnum(object):

    """Implementation of the 'Type_CassandraProtectionSource' enum.

    Specifies the type of the managed Object in Cassandra Protection Source.
    Replication strategy options for a keyspace.
    'kCluster' indicates a Cassandra cluster distributed over several physical
    nodes.
    'kKeyspace' indicates a Keyspace enclosing one or more tables.
    'kTable' indicates a Table in the Cassandra environment.

    Attributes:
        KCLUSTER: TODO: type description here.
        KKEYSPACE: TODO: type description here.
        KTABLE: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KKEYSPACE = 'kKeyspace'

    KTABLE = 'kTable'

