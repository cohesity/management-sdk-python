# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class WormRetentionTypeEnum(object):

    """Implementation of the 'WormRetentionType' enum.

    Specifies WORM retention type for the snapshot as given by the policy.
    When a WORM retention type is specified, the snapshot will be kept until
    the maximum of the snapshot retention time. During that time, the
    snapshot cannot be deleted.
    'kNone' implies there is no WORM retention set.
    'kCompliance' implies WORM retention is set for compliance reason.
    'kAdministrative' implies WORM retention is set for administrative
    purposes.

    Attributes:
        KNONE: TODO: type description here.
        KCOMPLIANCE: TODO: type description here.
        KADMINISTRATIVE: TODO: type description here.

    """

    KNONE = 'kNone'

    KCOMPLIANCE = 'kCompliance'

    KADMINISTRATIVE = 'kAdministrative'

