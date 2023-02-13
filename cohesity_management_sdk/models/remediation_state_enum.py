# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RemediationStateEnum(object):

    """Implementation of the 'RemediationState' enum.

    Specifies the remediation state of the file.
    Remediation State.
    'kQuarantine' indicates 'Quarantine' state of the file. This state blocks
    the client access. The administrator will have to manually delete, rescan
    or
    unquarantine the file.
    'kUnquarantine' indicates 'Unquarantine' state of the file.
    The administrator has manually moved files from quarantined to the
    unquarantined state to allow client access. Unquarantined files are
    not scanned for virus until manually reset.

    Attributes:
        KQUARANTINE: TODO: type description here.
        KUNQUARANTINE: TODO: type description here.

    """

    KQUARANTINE = 'kQuarantine'

    KUNQUARANTINE = 'kUnquarantine'

