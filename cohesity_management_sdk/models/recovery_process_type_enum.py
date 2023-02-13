# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RecoveryProcessTypeEnum(object):

    """Implementation of the 'RecoveryProcessType' enum.

    Specifies the type of recovery process to be performed. If unspecified,
    then an instant recovery will be performed.
    Specifies the recovery process type to be used..
    'kInstantRecovery' indicates that an instant recovery should be performed.
    'kCopyRecovery' indicates that a copy recovery should be performed.

    Attributes:
        KINSTANTRECOVERY: TODO: type description here.
        KCOPYRECOVERY: TODO: type description here.

    """

    KINSTANTRECOVERY = 'kInstantRecovery'

    KCOPYRECOVERY = 'kCopyRecovery'

