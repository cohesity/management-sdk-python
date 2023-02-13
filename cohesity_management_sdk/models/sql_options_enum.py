# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SqlOptionsEnum(object):

    """Implementation of the 'SqlOptions' enum.

    Specifies the sql options to update the Restore Task with.
    Specifies the action type of multi stage SQL restore.
    'kCreate' specifies the create action for a restore.
    'kUpdate' specifies the user action to update an ongoing restore.
    'kFinalize' specifies the user action to finalize a restore.

    Attributes:
        KCREATE: TODO: type description here.
        KUPDATE: TODO: type description here.
        KFINALIZE: TODO: type description here.

    """

    KCREATE = 'kCreate'

    KUPDATE = 'kUpdate'

    KFINALIZE = 'kFinalize'

