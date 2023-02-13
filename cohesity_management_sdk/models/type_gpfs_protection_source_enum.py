# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeGpfsProtectionSourceEnum(object):

    """Implementation of the 'Type_GpfsProtectionSource' enum.

    Specifies the type of the entity in an GPFS file system
    like 'kCluster', 'kFilesystem', or, 'kFileset'.
    'kCluster' indicates an GPFS Cluster.
    'kFilesystem' indicates a top level filesystem on GPFS cluster.
    'kFileset' indicates a fileset within a filesystem.

    Attributes:
        KCLUSTER: TODO: type description here.
        KFILESYSTEM: TODO: type description here.
        KFILESET: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KFILESYSTEM = 'kFilesystem'

    KFILESET = 'kFileset'

