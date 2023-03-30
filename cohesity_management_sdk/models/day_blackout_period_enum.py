# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DayBlackoutPeriodEnum(object):

    """Implementation of the 'Day_BlackoutPeriod' enum.

    Blackout Day.
    Specifies a day in the week when no new Job Runs should be started
    such as 'kSunday'.
    If not set, the time range applies to all days.
    Specifies a day in a week such as 'kSunday', 'kMonday', etc.

    Attributes:
        KSUNDAY: TODO: type description here.
        KMONDAY: TODO: type description here.
        KTUESDAY: TODO: type description here.
        KWEDNESDAY: TODO: type description here.
        KTHURSDAY: TODO: type description here.
        KFRIDAY: TODO: type description here.
        KSATURDAY: TODO: type description here.

    """

    KSUNDAY = 'kSunday'

    KMONDAY = 'kMonday'

    KTUESDAY = 'kTuesday'

    KWEDNESDAY = 'kWednesday'

    KTHURSDAY = 'kThursday'

    KFRIDAY = 'kFriday'

    KSATURDAY = 'kSaturday'

