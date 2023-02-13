# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ResultTypeEnum(object):

    """Implementation of the 'ResultType' enum.

    Specifies the type of the result returned after performing the internal
    host check.
    Specifies the type of the host check result performed internally.
    'kPass' indicates that the respective check was successful.
    'kFail' indicates that the respective check failed as some mandatory
    setting is not met
    'kWarning' indicates that the respective check has warning as certain
    non-mandatory setting is not met.

    Attributes:
        KPASS: TODO: type description here.
        KFAIL: TODO: type description here.
        KWARNING: TODO: type description here.

    """

    KPASS = 'kPass'

    KFAIL = 'kFail'

    KWARNING = 'kWarning'

