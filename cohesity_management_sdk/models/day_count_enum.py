# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DayCountEnum(object):

    """Implementation of the 'DayCount' enum.

    Specifies the day count in the month (such as 'kThird') to start
    the Job Run.
    Used in combination with day to define the day in the month to start
    the Job Run.
    Specifies the day count in the month to start the backup.
    For example if day count is set to 'kThird' and day is set to 'kMonday',
    a backup is performed on the third Monday of every month.
    'kFirst' indicates that the first week should be choosen for specified
    day of every month.
    'kSecond' indicates that the second week should be choosen for specified
    day of every month.
    'kThird' indicates that the third week should be choosen for specified
    day of every month.
    'kFourth' indicates that the fourth week should be choosen for specified
    day of every month.
    'kLast' indicates that the last week should be choosen for specified
    day of every month.

    Attributes:
        KFIRST: TODO: type description here.
        KSECOND: TODO: type description here.
        KTHIRD: TODO: type description here.
        KFOURTH: TODO: type description here.
        KLAST: TODO: type description here.

    """

    KFIRST = 'kFirst'

    KSECOND = 'kSecond'

    KTHIRD = 'kThird'

    KFOURTH = 'kFourth'

    KLAST = 'kLast'

