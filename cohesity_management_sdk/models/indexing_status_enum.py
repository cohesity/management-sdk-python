# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class IndexingStatusEnum(object):

    """Implementation of the 'IndexingStatus' enum.

    Specifies the indexing status of the snapshot.
    'kStarted' indicates that indexing has started.
    'kDone' indicates that indexing has been completed according to the type
    of object.
    'kNoIndex' indicates that the snapshot cannot be indexed. This is the case
    during archival restore.
    'kIceboxRestoreStarted' indicates that indexing is started from an
    archive.
    'kIceboxRestoreError' indicates that an error occurred during restore
    from archiveand there is no index present.
    'kSkipped' indicates that indexing is skipped due to indexing backlog.

    Attributes:
        KSTARTED: TODO: type description here.
        KDONE: TODO: type description here.
        KNOINDEX: TODO: type description here.
        KICEBOXRESTORESTARTED: TODO: type description here.
        KICEBOXRESTOREERROR: TODO: type description here.
        KSKIPPED: TODO: type description here.

    """

    KSTARTED = 'kStarted'

    KDONE = 'kDone'

    KNOINDEX = 'kNoIndex'

    KICEBOXRESTORESTARTED = 'kIceboxRestoreStarted'

    KICEBOXRESTOREERROR = 'kIceboxRestoreError'

    KSKIPPED = 'kSkipped'

