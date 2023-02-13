# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class BackupTypeSqlEnvJobParametersEnum(object):

    """Implementation of the 'BackupType_SqlEnvJobParameters' enum.

    Specifies the type of the 'kFull' backup job. Specifies whether it is
    Volume level backup or individual files level backup.
    kSqlVSSVolume implies volume based VSS full backup.
    kSqlVSSFile implies file based VSS full backup.

    Attributes:
        KSQLVSSVOLUME: TODO: type description here.
        KSQLVSSFILE: TODO: type description here.
        KSQLNATIVE: TODO: type description here.

    """

    KSQLVSSVOLUME = 'kSqlVSSVolume'

    KSQLVSSFILE = 'kSqlVSSFile'

    KSQLNATIVE = 'kSqlNative'

