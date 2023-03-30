# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExtendedStyleEnum(object):

    """Implementation of the 'ExtendedStyle' enum.
    Specifies the Extended style information of a NetApp volume. Specifies the
    extended style info of a NetApp Volume. 'kFlexGroup' indicates FlexGroup
    volume. A FlexGroup volume contains several constituents (which themselves
    are Netapp volumes) that automatically and transparently share the traffic.
    Cohesity does not need to deal with the individual consituents, just the
    main FlexGroup volume. 'kFlexVol' indicates FlexVol volume. A typical NAS
    share.


    Attributes:
        KFLEXVOL: TODO: type description here.
        KFLEXGROUP: TODO: type description here.

    """

    KFLEXVOL = 'kFlexVol'

    KFLEXGROUP = 'kFlexGroup'
