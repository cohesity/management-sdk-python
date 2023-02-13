# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RemovalReasonEnum(object):

    """Implementation of the 'RemovalReason' enum.

    Specifies the reason for the removal operation if there is a removal
    operation going on.
    'kUnknown' specifies that the removal reason is not known.
    'kAutoHealthCheck' specifies that an internal health check found problems
    with the Node.
    'kUserGracefulRemoval' specifies that the user requested a graceful
    removal.
    'kUserAvoidAccess' specifies that the user requested to avoid access to
    this Node.
    'kUserGracefulNodeRemoval' specifies that the user requested a graceful
    removal for all of the disks in this Node.
    'kUserRemoveDownNode' specifies that the user requested a graceful
    removal
    of the Node while it is down.

    Attributes:
        KUNKNOWN: TODO: type description here.
        KAUTOHEALTHCHECK: TODO: type description here.
        KUSERGRACEFULREMOVAL: TODO: type description here.
        KUSERAVOIDACCESS: TODO: type description here.
        KUSERGRACEFULNODEREMOVAL: TODO: type description here.
        KUSERREMOVEDOWNNODE: TODO: type description here.

    """

    KUNKNOWN = 'kUnknown'

    KAUTOHEALTHCHECK = 'kAutoHealthCheck'

    KUSERGRACEFULREMOVAL = 'kUserGracefulRemoval'

    KUSERAVOIDACCESS = 'kUserAvoidAccess'

    KUSERGRACEFULNODEREMOVAL = 'kUserGracefulNodeRemoval'

    KUSERREMOVEDOWNNODE = 'kUserRemoveDownNode'

