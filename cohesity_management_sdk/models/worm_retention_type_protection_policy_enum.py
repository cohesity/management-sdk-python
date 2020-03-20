# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class WormRetentionTypeProtectionPolicyEnum(object):

    """Implementation of the 'WormRetentionType_ProtectionPolicy' enum.

    Specifies WORM retention type for the snapshots. When a WORM retention
    type is specified, the snapshots of the Protection Jobs using this policy
    will be kept until the maximum of the snapshot retention time. During
    that time, the snapshots cannot be deleted.
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

