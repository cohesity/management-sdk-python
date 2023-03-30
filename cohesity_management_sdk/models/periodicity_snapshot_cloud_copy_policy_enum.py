# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PeriodicitySnapshotCloudCopyPolicyEnum(object):

    """Implementation of the 'Periodicity_SnapshotCloudCopyPolicy' enum.

    Specifies the frequency that Snapshots should be copied to the
    specified target. Used in combination with multipiler.
    'kEvery' means that the Snapshot copy occurs after the number of
    Job Runs equals the number specified in the multiplier.
    'kHour' means that the Snapshot copy occurs hourly at the frequency
    set in the multiplier, for example if multiplier is 2, the copy occurs
    every 2 hours.
    'kDay' means that the Snapshot copy occurs daily at the frequency
    set in the multiplier.
    'kWeek' means that the Snapshot copy occurs weekly at the frequency
    set in the multiplier.
    'kMonth' means that the Snapshot copy occurs monthly at the frequency
    set in the multiplier.
    'kYear' means that the Snapshot copy occurs yearly at the frequency
    set in the multiplier.

    Attributes:
        KEVERY: TODO: type description here.
        KHOUR: TODO: type description here.
        KDAY: TODO: type description here.
        KWEEK: TODO: type description here.
        KMONTH: TODO: type description here.
        KYEAR: TODO: type description here.

    """

    KEVERY = 'kEvery'

    KHOUR = 'kHour'

    KDAY = 'kDay'

    KWEEK = 'kWeek'

    KMONTH = 'kMonth'

    KYEAR = 'kYear'

