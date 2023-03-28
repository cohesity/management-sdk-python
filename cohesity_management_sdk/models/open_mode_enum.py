# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OpenModeEnum(object):

    """Implementation of the 'OpenMode' enum.
    Specifies the OPEN_MODE information. Specifies the OPEN_MODE type for the
    Oracle database. 'kMounted' indicates that the database is open in Mounted
    mode. 'kReadWrite' indicates that the database is open in R/W mode.
    'kReadOnly' indicates that the database is open in ReadOnly mode.
    'kMigrate' inidcates that the database is open in Migrate mode.


    Attributes:
        KMOUNTED: TODO: type description here.
        KREADWRITE: TODO: type description here.
        KREADONLY: TODO: type description here.
        KMIGRATE: TODO: type description here.

    """

    KMOUNTED = 'kMounted'

    KREADWRITE = 'kReadWrite'

    KREADONLY = 'kReadOnly'

    KMIGRATE = 'kMigrate'
