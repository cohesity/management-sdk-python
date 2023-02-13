# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AppsModeEnum(object):

    """Implementation of the 'AppsMode' enum.

    Specifies the various modes for running apps.
    'kDisabled' specifies that apps are disabled.
    'kBareMetal' specifies that apps could only run in containers
    on the node (no VM).
    'kVmOnly' specifies that apps could only run in containers on a VM
    hosted by the node.

    Attributes:
        KDISABLED: TODO: type description here.
        KBAREMETAL: TODO: type description here.
        KVMONLY: TODO: type description here.

    """

    KDISABLED = 'kDisabled'

    KBAREMETAL = 'kBareMetal'

    KVMONLY = 'kVmOnly'

