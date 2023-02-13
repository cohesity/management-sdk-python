# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ActionUpdateProtectionJobsStateRequestBodyEnum(object):

    """Implementation of the 'Action_UpdateProtectionJobsStateRequestBody' enum.

    Specifies the action to be performed on all the specfied Protection Jobs.
    Specifies the type of action to be performed on Protection Job.
    'kActivate' specifies that Protection Job should be activated.
    'kDeactivate' sepcifies that Protection Job should be deactivated.
    'kPause' specifies that Protection Job should be paused.
    'kResume' specifies that Protection Job should be resumed.

    Attributes:
        KACTIVATE: TODO: type description here.
        KDEACTIVATE: TODO: type description here.
        KPAUSE: TODO: type description here.
        KRESUME: TODO: type description here.

    """

    KACTIVATE = 'kActivate'

    KDEACTIVATE = 'kDeactivate'

    KPAUSE = 'kPause'

    KRESUME = 'kResume'

