# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PartitionTableFormatEnum(object):

    """Implementation of the 'PartitionTableFormat' enum.

    Specifies partition table format on a disk.
    'kNoPartition' indicates missing partition table.
    'kMBRPartition' indicates partition table is in Master Boot Record
    format.
    'kGPTPartition' indicates partition table is in Guid Partition Table
    format.
    'kSGIPartition' indicates partition table uses SGI scheme.
    'kSUNPartition' indicates partition table uses SUN scheme.

    Attributes:
        KNOPARTITION: TODO: type description here.
        KMBRPARTITION: TODO: type description here.
        KGPTPARTITION: TODO: type description here.
        KSGIPARTITION: TODO: type description here.
        KSUNPARTITION: TODO: type description here.

    """

    KNOPARTITION = 'kNoPartition'

    KMBRPARTITION = 'kMBRPartition'

    KGPTPARTITION = 'kGPTPartition'

    KSGIPARTITION = 'kSGIPartition'

    KSUNPARTITION = 'kSUNPartition'

