# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TileTypesEnum(object):

    """Implementation of the 'TileTypes' enum.

    Specifies the types of the tiles to be returned. If this is not
    specified, all the tiles are returned. This is ignored when allClusters
    is set to true.
    'kHealthTile' is the tile that shows health of the cluster and the alerts
    in
    the past 24 hours.
    'kJobRunsTile' is the tile that shows job runs in the past 24 hours.
    'kRecoveriesTile' is the tile that shows recoveries done in the past 30
    days.
    'kProtectedObjectsTile' is the tile that shows the protected objects
    details.
    'kProtectionTile' is the tile that shows the protection information in the
    past 24 hours.
    'kAuditLogsTile' is the tile that shows the recent audit logs.
    'kIopsTile' is the tile that shows IP performance in the past 24 hours.
    'kThroughputTile' is the tile that shows job runs in the past 24 hours.
    'kStorageEfficiencyTile' is the tile that shows job runs in the past 7
    days.

    Attributes:
        KHOUR: TODO: type description here.
        KJOBRUNSTILE: TODO: type description here.
        KRECOVERIESTILE: TODO: type description here.
        KPROTECTIONTILE: TODO: type description here.
        KAUDITLOGSTILE: TODO: type description here.
        KIOPSTILE: TODO: type description here.
        KTHROUGHPUTTILE: TODO: type description here.
        KSTORAGEEFFICIENCYTILE: TODO: type description here.

    """

    KHOUR = 'kHealthTile'

    KJOBRUNSTILE = 'kJobRunsTile'

    KRECOVERIESTILE = 'kRecoveriesTile'

    KPROTECTEDOBJECTSTILE = 'kProtectedObjectsTile'

    KPROTECTIONTILE = 'kProtectionTile'

    KAUDITLOGSTILE = 'kAuditLogsTile'

    KIOPSTILE = 'kIopsTile'

    KTHROUGHPUTTILE= 'kThroughputTile'

    KSTORAGEEFFICIENCYTILE= 'kStorageEfficiencyTile'

