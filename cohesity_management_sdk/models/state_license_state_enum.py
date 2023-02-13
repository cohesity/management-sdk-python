# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StateLicenseStateEnum(object):

    """Implementation of the 'State_LicenseState' enum.

    Specifies the current state of licensing workflow.
    LicenseStateType specifies the licenseState type.
    'kInProgressNewCluster' indicates licensing server claim is in progress
    for 'New' Cluster.
    'kInProgressOldCluster' indicates licensing server claim is in progress
    for 'Old' Cluster.
    'kClaimed' indicates licensing server is claimed.
    'kSkipped' indicates licensing workflow has been skipped.
    'kStarted' indicates licensing UI workflow has started.

    Attributes:
        KINPROGRESSNEWCLUSTER: TODO: type description here.
        KINPROGRESSOLDCLUSTER: TODO: type description here.
        KCLAIMED: TODO: type description here.
        KSKIPPED: TODO: type description here.
        KSTARTED: TODO: type description here.

    """

    KINPROGRESSNEWCLUSTER = 'kInProgressNewCluster'

    KINPROGRESSOLDCLUSTER = 'kInProgressOldCluster'

    KCLAIMED = 'kClaimed'

    KSKIPPED = 'kSkipped'

    KSTARTED = 'kStarted'

