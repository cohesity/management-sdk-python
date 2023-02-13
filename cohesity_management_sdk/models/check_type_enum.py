# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CheckTypeEnum(object):

    """Implementation of the 'CheckType' enum.

    Specifies the type of the check internally performed.
    Specifies the type of the host check performed internally.
    'kIsAgentPortAccessible' indicates the check for agent port access.
    'kIsAgentRunning' indicates the status for the Cohesity agent service.
    'kIsSQLWriterRunning' indicates the status for SQLWriter service.
    'kAreSQLInstancesRunning' indicates the run status for all the SQL
    instances in the host.
    'kCheckServiceLoginsConfig' checks the privileges and sysadmin status
    of the logins used by the SQL instance services, Cohesity agent service
    and the SQLWriter service.
    'kCheckSQLFCIVIP' checks whether the SQL FCI is registered with a valid
    VIP or FQDN.
    'kCheckSQLDiskSpace' checks whether volumes containing SQL DBs have at
    least 10% free space.

    Attributes:
        KISAGENTPORTACCESSIBLE: TODO: type description here.
        KISAGENTRUNNING: TODO: type description here.
        KISSQLWRITERRUNNING: TODO: type description here.
        KARESQLINSTANCESRUNNING: TODO: type description here.
        KCHECKSERVICELOGINSCONFIG: TODO: type description here.
        KCHECKSQLFCIVIP: TODO: type description here.

    """

    KISAGENTPORTACCESSIBLE = 'kIsAgentPortAccessible'

    KISAGENTRUNNING = 'kIsAgentRunning'

    KISSQLWRITERRUNNING = 'kIsSQLWriterRunning'

    KARESQLINSTANCESRUNNING = 'kAreSQLInstancesRunning'

    KCHECKSERVICELOGINSCONFIG = 'kCheckServiceLoginsConfig'

    KCHECKSQLFCIVIP = 'kCheckSQLFCIVIP'

    KCHECKSQLDISKSPACE = 'kCheckSQLDiskSpace'

