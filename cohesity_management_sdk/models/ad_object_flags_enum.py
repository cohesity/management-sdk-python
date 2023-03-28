# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AdObjectFlagsEnum(object):

    """Implementation of the 'AdObjectFlags' enum.
    Specifies the flags related to this AD Object. 'kEqual' indicates all the
    attributes of the AD Object on the Snapshot and Production are equal.
    'kNotEqual' indicates atleast one of the attribute of the AD Object on the
    Snapshot and Production AD are not equal. 'kRestorePasswordRequired'
    indicates the AD Object is of 'User' object class type. when restoring this
    object from Snapshot AD to Priduction AD, a password is required.
    'kMovedOnDestination' indicates the object has moved to another container
    or OU in production AD compared to AD snapshot. In this case, the
    distinguishedName will be different for these objects
    'kDestinationNotFound' indicates the object corresponding to dest_guid
    specified is missing from Production AD. Caller should check this flag and
    empty 'dest_guid' first to find out destination is missing.
    'kDisableSupported' indicates the enable and disable is supported on the AD
    Object. AD Objects of type 'User' and 'Computers' support this operation.


    Attributes:
        KEQUAL: TODO: type description here.
        KNOTEQUAL: TODO: type description here.
        KRESTOREPASSWORDREQUIRED: TODO: type description here.
        KMOVEDONDESTINATION: TODO: type description here.
        KDESTINATIONNOTFOUND: TODO: type description here.
        KDISABLESUPPORTED: TODO: type description here.

    """

    KEQUAL = 'kEqual'

    KNOTEQUAL = 'kNotEqual'

    KRESTOREPASSWORDREQUIRED = 'kRestorePasswordRequired'

    KMOVEDONDESTINATION = 'kMovedOnDestination'

    KDESTINATIONNOTFOUND = 'kDestinationNotFound'

    KDISABLESUPPORTED = 'kDisableSupported'
