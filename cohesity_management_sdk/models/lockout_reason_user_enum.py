# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LockoutReasonUserEnum(object):

    """Implementation of the 'LockoutReasonUser' enum.

    Specifies the lockout reason of the user if it is locked.
    'NotLocked' implies the user is not locked.
    'FailedLoginAttempts' the account is locked due to
    many failed login attempts.
    'LockedByAdmin' implies the account is locked by the admin user.
    'Inactivity' implies the account is locked due to long time of
    inactivity.

    Attributes:

        NOTLOCKED: TODO: type description here.
        FAILEDLOGINATTEMPTS: TODO: type description here.
        LOCKEDBYADMIN: TODO: type description here.
        INACTIVITY: TODO: type description here.

    """
    NOTLOCKED = 'NotLocked'

    FAILEDLOGINATTEMPTS = 'FailedLoginAttempts'

    LOCKEDBYADMIN = 'LockedByAdmin'

    INACTIVITY = 'Inactivity'

