# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SecurityModeEnum(object):

    """Implementation of the 'SecurityMode' enum.

    Specifies the security mode used for this view.
    Currently we support the following modes: Native, Unified and NTFS style.
    'kNativeMode' indicates a native security mode.
    'kUnifiedMode' indicates a unified security mode.
    'kNtfsMode' indicates a NTFS style security mode.

    Attributes:
        KNATIVEMODE: TODO: type description here.
        KUNIFIEDMODE: TODO: type description here.
        KNTFSMODE: TODO: type description here.

    """

    KNATIVEMODE = 'kNativeMode'

    KUNIFIEDMODE = 'kUnifiedMode'

    KNTFSMODE = 'kNtfsMode'

