# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MarketplaceAppsModeEnum(object):

    """Implementation of the 'MarketplaceAppsMode' enum.

    Specifies the various modes for running marketplace apps.
    'kDisabled' specifies that marketplace apps are disabled.
    'kBareMetal' specifies that marketplace apps could only run in containers
    on the node (no VM).
    'kVmOnly' specifies that marketplace apps could only run in containers
    on a VM hosted by the node.

    Attributes:
        KDISABLED: TODO: type description here.
        KBAREMETAL: TODO: type description here.
        KVMONLY: TODO: type description here.

    """

    KDISABLED = 'kDisabled'

    KBAREMETAL = 'kBareMetal'

    KVMONLY = 'kVmOnly'
