# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class QosTierAppInstanceSettingsEnum(object):

    """Implementation of the 'QosTier_AppInstanceSettings' enum.

    Specifies QoSTier of the app instance.
    Specifies QoS Tier for an app instance. App instances are allocated
    resources such as memory, CPU and IO based on their QoS Tier.
    kLow - Low QoS Tier.
    kMedium - Medium QoS Tier.
    kHigh - High QoS Tier.
    kMax - Max QoS Tier.

    Attributes:
        KLOW: TODO: type description here.
        KMEDIUM: TODO: type description here.
        KHIGH: TODO: type description here.
        KMAX: TODO: type description here.

    """

    KLOW = 'kLow'

    KMEDIUM = 'kMedium'

    KHIGH = 'kHigh'

    KMAX = 'kMax'
