# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ModeFileLockStatusEnum(object):

    """Implementation of the 'Mode_FileLockStatus' enum.

    Specifies the mode of the file lock. 'kCompliance', 'kEnterprise'.
    A lock mode of a file in a view can be in one of the following:
    'kCompliance': Default mode of datalock, in this mode, Data Security
    Admin
    cannot modify/delete this view when datalock is in effect. Data Security
    Admin can delete this view when datalock is expired.
    'kEnterprise' : In this mode, Data Security Admin can change view name or
    delete view when datalock is in effect. Datalock in this mode can be
    upgraded to 'kCompliance' mode.

    Attributes:
        KCOMPLIANCE: TODO: type description here.
        KENTERPRISE: TODO: type description here.

    """

    KCOMPLIANCE = 'kCompliance'

    KENTERPRISE = 'kEnterprise'

