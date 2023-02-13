# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StateEnum(object):

    """Implementation of the 'State' enum.

    Specifies the state of this volume.
    Specifies the state of a NetApp Volume.
    'kOnline' indicates the volume is online. Read and write access to this
    volume is allowed.
    'kRestricted' indicates the volume is restricted. Some operations,
    such as parity reconstruction, are allowed, but data access is not
    allowed.
    'kOffline' indicates the volume is offline. No access to the volume is
    allowed.
    'kMixed' indicates the volume is in mixed state, which means its
    aggregates are not all in the same state.

    Attributes:
        KONLINE: TODO: type description here.
        KRESTRICTED: TODO: type description here.
        KOFFLINE: TODO: type description here.
        KMIXED: TODO: type description here.

    """

    KONLINE = 'kOnline'

    KRESTRICTED = 'kRestricted'

    KOFFLINE = 'kOffline'

    KMIXED = 'kMixed'

