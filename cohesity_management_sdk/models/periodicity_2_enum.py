# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class Periodicity2Enum(object):

    """Implementation of the 'Periodicity2' enum.

    Specifies how often to start new Job Runs of a Protection Job.
    'kDaily' means new Job Runs start daily.
    'kMonthly' means new Job Runs start monthly.
    'kContinuous' means new Job Runs repetitively start at the
    beginning of the specified time interval (in hours or minutes).
    'kOneOff' means this is an additional schedule.

    Attributes:
        KCONTINUOUS: TODO: type description here.
        KDAILY: TODO: type description here.
        KMONTHLY: TODO: type description here.
        KONEOFF: TODO: type description here.

    """

    KCONTINUOUS = 'kContinuous'

    KDAILY = 'kDaily'

    KMONTHLY = 'kMonthly'

    KONEOFF = 'kOneOff'

