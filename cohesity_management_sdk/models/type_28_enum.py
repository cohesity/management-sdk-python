# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class Type28Enum(object):

    """Implementation of the 'Type28' enum.

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

