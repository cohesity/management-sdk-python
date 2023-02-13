# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AllocationMethodEnum(object):

    """Implementation of the 'AllocationMethod' enum.

    Specifies the enum for IP allocation method.
    'kUnknownAllocMethod' indicates allocation method is unknown.
    'kStaticAllocMethod' indicates static allocation method for IP addresses.
    'kDynamicAllocMethod' indicates dynamic allocation method for IP addresses.

    Attributes:
        KUNKNOWNALLOCMETHOD: TODO: type description here.
        KSTATICALLOCMETHOD: TODO: type description here.
        KDYNAMICALLOCMETHOD: TODO: type description here.

    """
    KUNKNOWNALLOCMETHOD = 'kUnknownAllocMethod'

    KSTATICALLOCMETHOD = 'kStaticAllocMethod'

    KDYNAMICALLOCMETHOD = 'kDynamicAllocMethod'

