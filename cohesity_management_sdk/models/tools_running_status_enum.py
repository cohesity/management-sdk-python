# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ToolsRunningStatusEnum(object):

    """Implementation of the 'ToolsRunningStatus' enum.

    Specifies the status of VMware Tools for the guest OS on the VM.
    This is only valid for the 'kVirtualMachine' type.
    'kGuestToolsRunning' means the VMware tools are running on the guest OS.
    'kGuestToolsNotRunning' means the VMware tools are not running on the
    guest OS.
    'kUnknown' means the state of the VMware tools on the guest OS is not
    known.
    'kGuestToolsExecutingScripts' means the guest OS is currently executing
    scripts using VMware tools.

    Attributes:
        KUNKNOWN: TODO: type description here.
        KGUESTTOOLSEXECUTINGSCRIPTS: TODO: type description here.
        KGUESTTOOLSNOTRUNNING: TODO: type description here.
        KGUESTTOOLSRUNNING: TODO: type description here.

    """

    KUNKNOWN = 'kUnknown'

    KGUESTTOOLSEXECUTINGSCRIPTS = 'kGuestToolsExecutingScripts'

    KGUESTTOOLSNOTRUNNING = 'kGuestToolsNotRunning'

    KGUESTTOOLSRUNNING = 'kGuestToolsRunning'

