# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LockoutReasonEnum(object):

    """Implementation of the 'LockoutReason' enum.
    Specifies the lockout reason of the user if it is locked. 'NotLocked'
    implies the user is not locked. 'FailedLoginAttempts' the account is locked
    due to many failed login attempts. 'LockedByAdmin' implies the account is
    locked by the admin user. 'Inactivity' implies the account is locked due to
    long time of inactivity. 'OtherReasons' implied the account is loced for
    other reasons.


    Attributes:
        NOTLOCKED: TODO: type description here.
        FAILEDLOGINATTEMPTS: TODO: type description here.
        LOCKEDBYADMIN: TODO: type description here.
        INACTIVITY: TODO: type description here.
        OTHERREASONS: TODO: type description here.

    """

    NOTLOCKED = 'NotLocked'

    FAILEDLOGINATTEMPTS = 'FailedLoginAttempts'

    LOCKEDBYADMIN = 'LockedByAdmin'

    INACTIVITY = 'Inactivity'

    OTHERREASONS = 'OtherReasons'
