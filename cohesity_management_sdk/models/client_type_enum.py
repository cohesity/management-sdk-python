# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ClientTypeEnum(object):

    """Implementation of the 'ClientType' enum.

    Specifies the client type of the externally triggered job
    kGeneric implies generic externally triggered backups.
    kSbt implies externally triggered backups for SBT.

    Attributes:
        KGENERIC: TODO: type description here.
        KSBT: TODO: type description here.

    """

    KGENERIC = 'kGeneric'

    KSBT = 'kSbt'
