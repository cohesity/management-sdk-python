# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StateTenantDeletionInfoEnum(object):

    """Implementation of the 'StateTenantDeletionInfo' enum.
    Specifies the deletion completion state of the object category. Completion
    State is captured before any operations are started. Similar to WAL (Write
    Ahead Logging).


    Attributes:
        NOTSTARTED: TODO: type description here.
        INPROGRESS: TODO: type description here.
        FINISHED: TODO: type description here.
        SKIPPED: TODO: type description here.
        WAITING: TODO: type description here.

    """

    NOTSTARTED = 'NotStarted'

    INPROGRESS = 'InProgress'

    FINISHED = 'Finished'

    SKIPPED = 'Skipped'

    WAITING = 'Waiting'
