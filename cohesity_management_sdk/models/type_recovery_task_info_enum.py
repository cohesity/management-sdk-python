# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeRecoveryTaskInfoEnum(object):

    """Implementation of the 'Type_RecoveryTaskInfo' enum.

    Denotes if the recovery task has an archival target.
    This param is used to reflect if the recovery op has an archival
    target to work with.
    'local' indicates no archival target.
    'archive' indicates that objects restored using an archival target.

    Attributes:
        LOCAL: TODO: type description here.
        ARCHIVE: TODO: type description here.

    """

    LOCAL = 'local'

    ARCHIVE = 'archive'

