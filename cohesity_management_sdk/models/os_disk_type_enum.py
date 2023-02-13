# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OsDiskTypeEnum(object):

    """Implementation of the 'OsDiskType' enum.

    Specifies the disk type used by the OS.
    'kPremiumSSD' is disk type backed by SSDs, delivers high performance, low
    latency disk support for VMs running I/O intensive workloads.
    'kStandardSSD' implies disk type that offers more consistent performance
    and
    reliability than HDD.
    'kStandardHDD' implies disk type backed by HDDs, delivers cost effective
    storage.

    Attributes:
        KPREMIUMSSD: TODO: type description here.
        KSTANDARDSSD: TODO: type description here.
        KSTANDARDHDD: TODO: type description here.

    """

    KPREMIUMSSD = 'kPremiumSSD'

    KSTANDARDSSD = 'kStandardSSD'

    KSTANDARDHDD = 'kStandardHDD'

