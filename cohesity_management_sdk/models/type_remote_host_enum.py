# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class TypeRemoteHostEnum(object):

    """Implementation of the 'Type_RemoteHost' enum.

    Specifies the OS type of the remote host that will run the script.
    Currently only 'kLinux' is supported.
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

