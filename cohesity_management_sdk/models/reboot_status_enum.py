# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RebootStatusEnum(object):

    """Implementation of the 'RebootStatus' enum.
    Specifies the reboot status of the host post cbt driver installation. Only
    applicable for volcbt driver. Specifies the reboot status of the source
    post volcbt driver installation. 'kRebooted' indicates the source has been
    rebooted post volcbt driver installation. 'kNeedsReboot' indicates the
    source has not been rebooted post volcbt driver installation.
    'kInternalError' indicates that there was an error while fetching reboot
    status from source.


    Attributes:
        KREBOOTED: TODO: type description here.
        KNEEDSREBOOT: TODO: type description here.
        KINTERNALERROR: TODO: type description here.

    """

    KREBOOTED = 'kRebooted'

    KNEEDSREBOOT = 'kNeedsReboot'

    KINTERNALERROR = 'kInternalError'
