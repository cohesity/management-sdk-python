# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SearchResultFlagsEnum(object):

    """Implementation of the 'SearchResultFlags' enum.
    Specifies the SearchResultFlags of the AD object. 'kEqual' indicates the AD
    Object from Snapshot and Production AD are equal. 'kNotEqual' indicates the
    AD Object from snapshot and production AD are not equal.
    'kRestorePasswordRequired' indicates when restoring this AD Object from
    Snapshot AD to Production AD, a password is required. 'kMovedOnDestination'
    indicates the object has moved to another container or OU in Production AD
    compared to  Snapshot AD. 'kDisableSupported' indicates the enable and
    disable is supported on the AD Object. AD Objects of type 'User' and
    'Computers' support this operation.


    Attributes:
        KEQUAL: TODO: type description here.
        KNOTEQUAL: TODO: type description here.
        KRESTOREPASSWORDREQUIRED: TODO: type description here.
        KMOVEDONDESTINATION: TODO: type description here.
        KDISABLESUPPORTED: TODO: type description here.

    """

    KEQUAL = 'kEqual'

    KNOTEQUAL = 'kNotEqual'

    KRESTOREPASSWORDREQUIRED = 'kRestorePasswordRequired'

    KMOVEDONDESTINATION = 'kMovedOnDestination'

    KDISABLESUPPORTED = 'kDisableSupported'
