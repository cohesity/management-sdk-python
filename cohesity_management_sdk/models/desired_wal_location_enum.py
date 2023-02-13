# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DesiredWalLocationEnum(object):

    """Implementation of the 'DesiredWalLocation' enum.

    Desired location for write ahead logs(wal).
    'kHomePartition' indicates desired wal location to be the home partition.
    'kDisk' indicates desired wal location to be the same disk as chunk repo.
    'kScribe' indicates desired wal location to be scribe.
    'kScribeTable' indicates chunk repository state is kept as key-value
    pairs in scribe.

    Attributes:
        KHOMEPARTITION: TODO: type description here.
        KDISK: TODO: type description here.
        KSCRIBE: TODO: type description here.
        KSCRIBETABLE: TODO: type description here.

    """

    KHOMEPARTITION = 'kHomePartition'

    KDISK = 'kDisk'

    KSCRIBE = 'kScribe'

    KSCRIBETABLE = 'kScribeTable'

