# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PeriodicityEnum(object):

    """Implementation of the 'Periodicity' enum.

    Specifies how often to start new Job Runs of a Protection Job.
    'kDaily' means new Job Runs start daily.
    'kMonthly' means new Job Runs start monthly.
    'kContinuous' means new Job Runs repetitively start at the
    beginning of the specified time interval (in hours or minutes).
    'kContinuousRPO' means this is an RPO schedule.
    'kCDP' means this is a continuous data protection policy.

    Attributes:
        KCONTINUOUS: TODO: type description here.
        KDAILY: TODO: type description here.
        KMONTHLY: TODO: type description here.
        KCONTINUOUSRPO: TODO: type description here.
        KCDP: TODO: type description here.

    """

    KCONTINUOUS = 'kContinuous'

    KDAILY = 'kDaily'

    KMONTHLY = 'kMonthly'

    KCONTINUOUSRPO = 'kContinuousRPO'

    KCDP = 'kCDP'

