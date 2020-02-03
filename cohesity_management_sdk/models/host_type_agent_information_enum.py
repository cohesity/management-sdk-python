# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class HostTypeAgentInformationEnum(object):

    """Implementation of the 'HostType_AgentInformation' enum.

    Specifies the host type where the agent is running. This is only set for
    persistent agents.
    'kLinux' indicates the Linux operating system.
    'kWindows' indicates the Microsoft Windows operating system.
    'kAix' indicates the IBM AIX operating system.
    'kSolaris' indicates the Oracle Solaris operating system.
    'kSapHana' indicates the Sap Hana database system developed by SAP SE.
    'kOther' indicates the other types of operating system.

    Attributes:
        KLINUX: TODO: type description here.
        KWINDOWS: TODO: type description here.
        KAIX: TODO: type description here.
        KSOLARIS: TODO: type description here.
        KSAPHANA: TODO: type description here.
        KOTHER: TODO: type description here.

    """

    KLINUX = 'kLinux'

    KWINDOWS = 'kWindows'

    KAIX = 'kAix'

    KSOLARIS = 'kSolaris'

    KSAPHANA = 'kSapHana'

    KOTHER = 'kOther'

