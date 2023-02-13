# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeSmbPermissionEnum(object):

    """Implementation of the 'Type_SmbPermission' enum.

    Specifies the type of permission.
    'kAllow' indicates access is allowed.
    'kDeny' indicates access is denied.
    'kSpecialType' indicates a type defined in the Access Control Entry (ACE)
    does not map to 'kAllow' or 'kDeny'.

    Attributes:
        KALLOW: TODO: type description here.
        KDENY: TODO: type description here.
        KSPECIALTYPE: TODO: type description here.

    """

    KALLOW = 'kAllow'

    KDENY = 'kDeny'

    KSPECIALTYPE = 'kSpecialType'

