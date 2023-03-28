# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AlertStateEnum(object):

    """Implementation of the 'AlertState' enum.
    Specifies the current state of the Alert. kAlertNote - Alerts that are just
    for note. kAlertOpen - Alerts that are unresolved. kAlertResolved - Alerts
    that are already marked as resolved. kAlertSuppressed - Alerts that are
    suppressed due to snooze settings.


    Attributes:
        KNOTE: TODO: type description here.
        KOPEN: TODO: type description here.
        KRESOLVED: TODO: type description here.
        KSUPPRESSED: TODO: type description here.

    """

    KNOTE = 'kNote'

    KOPEN = 'kOpen'

    KRESOLVED = 'kResolved'

    KSUPPRESSED = 'kSuppressed'
