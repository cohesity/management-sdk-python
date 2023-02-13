# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PriorityEnum(object):

    """Implementation of the 'Priority' enum.

    Specifies the priority of execution for a Protection Job.
    Cohesity supports concurrent backups but if the number of Jobs exceeds
    the ability to process Jobs, the specified priority determines the
    execution Job priority.
    This field also specifies the replication priority.
    'kLow' indicates lowest execution priority for a Protection job.
    'kMedium' indicates medium execution priority for a Protection job.
    'kHigh' indicates highest execution priority for a Protection job.

    Attributes:
        KLOW: TODO: type description here.
        KMEDIUM: TODO: type description here.
        KHIGH: TODO: type description here.

    """

    KLOW = 'kLow'

    KMEDIUM = 'kMedium'

    KHIGH = 'kHigh'

