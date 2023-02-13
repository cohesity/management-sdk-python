# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class IntervalUnitEnum(object):

    """Implementation of the 'IntervalUnit' enum.

    Specifies an RPO policy interval unit which will be used along with the
    multiplier to calculate the interval for the RPO policy execution.
    this can be kHours, kDays, KWeeks, kMonths
    RPOIntervalUnit.
    Specifies an RPO Schedule interval unit.
    kMinutes specifies that the rpo interval unit is hours.
    kHours specifies that the rpo interval unit is hours.
    kDays specifies that the rpo interval unit is days.
    kWeeks specifies that the rpo interval unit is weeks.
    kMonths specifies that the rpo interval unit is months.

    Attributes:
        KMINUTES: TODO: type description here.
        KHOURS: TODO: type description here.
        KDAYS: TODO: type description here.
        KWEEKS: TODO: type description here.
        KMONTHS: TODO: type description here.

    """

    KMINUTES = 'kMinutes'

    KHOURS = 'kHours'

    KDAYS = 'kDays'

    KWEEKS = 'kWeeks'

    KMONTHS = 'kMonths'

