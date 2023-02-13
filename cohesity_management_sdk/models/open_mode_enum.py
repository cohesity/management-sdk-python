# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OpenModeEnum(object):

    """Implementation of the 'OpenMode' enum.

    Specifies the OPEN_MODE information.
    Specifies the OPEN_MODE type for the Oracle database.
    'kMounted' indicates that the database is open in Mounted mode.
    'kReadWrite' indicates that the database is open in R/W mode.
    'kReadOnly' indicates that the database is open in ReadOnly mode.
    'kMigrate' indicates that the database is open in Migrate mode.

    """

    KMOUNTED = 'kMounted'

    KREADWRITE = 'kReadWrite'

    KREADONLY = 'kReadOnly'

    KMIGRATE = 'kMigrate'

