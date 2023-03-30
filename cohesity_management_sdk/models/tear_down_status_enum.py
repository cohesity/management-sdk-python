# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TearDownStatusEnum(object):

    """Implementation of the 'TearDownStatus' enum.

    Specifies the status of the tear down operation. This is only set when the
    field 'CanTearDown' is set to true.
    'kReadyToSchedule' indicates that the task is waiting to be scheduled.
    'kAdmitted' indicates that the task has been admitted.
    'kFinished' indicates that the task is finished with or without error.

    Attributes:
        KREADYTOSCHEDULE: TODO: type description here.
        KADMITTED: TODO: type description here.
        KFINISHED: TODO: type description here.

    """
    KREADYTOSCHEDULE = 'kReadyToSchedule'

    KADMITTED = 'kAdmitted'

    KFINISHED = 'kFinished'

