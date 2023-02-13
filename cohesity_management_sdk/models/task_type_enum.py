# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TaskTypeEnum(object):

    """Implementation of the 'TaskType' enum.

    Task type denotes which type of task this notification is for.
    This param is used to reflect the taskType.
    'Restore' notification type is generated upon completion of Restore
    tasks.
    'Clone' notification type is generated upon completion of Clone tasks.
    'BackupNow' notification type is generated upon completion of Backup
    tasks.
    'FieldMessage' notification type is generated when field message from
    Cohesity support is created.
    'bulkInstallApp' notification type is generated from bulk install app
    'tiering' notification type is generated upon completion of tiering tasks.
    'analysis' notification type is generated upon completion of analysis tasks.

    Attributes:
        RESTORE: TODO: type description here.
        CLONE: TODO: type description here.
        BACKUPNOW: TODO: type description here.
        FIELDMESSAGE: TODO: type description here.
        BULKINSTALLAPP: TODO: type description here.
        TIERING: TODO: type description here.
        ANALYSIS: TODO: type description here.

    """

    RESTORE = 'restore'

    CLONE = 'clone'

    BACKUPNOW = 'backupNow'

    FIELDMESSAGE = 'fieldMessage'

    BULKINSTALLAPP = 'bulkInstallApp'

    TIERING = 'tiering'

    ANALYSIS = 'analysis'

