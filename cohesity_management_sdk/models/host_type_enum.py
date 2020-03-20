# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class HostTypeEnum(object):

    """Implementation of the 'HostType' enum.

    Specifies the OS type of the Protection Source of type 'kVirtualMachine'
    such as 'kWindows' or 'kLinux'.
    overrideDescription: true
    'kLinux' indicates the Linux operating system.
    'kWindows' indicates the Microsoft Windows operating system.
    'kAix' indicates the IBM AIX operating system.
    'kSolaris' indicates the Oracle Solaris operating system.

    Attributes:
        KLINUX: TODO: type description here.
        KWINDOWS: TODO: type description here.
        KAIX: TODO: type description here.
        KSOLARIS: TODO: type description here.

    """

    KLINUX = 'kLinux'

    KWINDOWS = 'kWindows'

    KAIX = 'kAix'

    KSOLARIS = 'kSolaris'

