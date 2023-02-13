# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UserDatabasePreferenceEnum(object):

    """Implementation of the 'UserDatabasePreference' enum.

    Specifies the preference for backing up user databases on the host.
    kBackupAllDatabases implies to backup all databases.
    kBackupAllExceptAAGDatabases implies not to backup AAG databases.
    kBackupOnlyAAGDatabases implies to backup only AAG databases.

    Attributes:
        KBACKUPALLDATABASES: TODO: type description here.
        KBACKUPALLEXCEPTAAGDATABASES: TODO: type description here.
        KBACKUPONLYAAGDATABASES: TODO: type description here.

    """

    KBACKUPALLDATABASES = 'kBackupAllDatabases'

    KBACKUPALLEXCEPTAAGDATABASES = 'kBackupAllExceptAAGDatabases'

    KBACKUPONLYAAGDATABASES = 'kBackupOnlyAAGDatabases'

