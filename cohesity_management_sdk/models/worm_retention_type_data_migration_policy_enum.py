# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class WormRetentionTypeDataMigrationPolicyEnum(object):

    """Implementation of the 'WormRetentionType_DataMigrationPolicy' enum.

    Specifies WORM retention type for the files. When a WORM retention
    type is specified, the files will be kept until the maximum of the
    retention time. During that time, the files cannot be deleted.
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

