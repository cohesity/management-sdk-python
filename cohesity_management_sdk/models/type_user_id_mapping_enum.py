# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeUserIdMappingEnum(object):

    """Implementation of the 'Type_UserIdMapping' enum.

    Specifies the mapping type used.
    'kRid' indicates the kRid mapping type.
    'kRfc2307' indicates the kRfc2307 mapping type.
    'kSfu30' indicates the kSfu30 mapping type.
    'kCentrify' indicates the mapping type to refer to a centrify zone.
    'kFixed' indicates the mapping from all Active Directory users to a fixed
    Unix uid, and gid.
    'kCustomAttributes' indicates the mapping to derive from custom attributes
    defined in an AD domain.
    'kLdapProvider' indicates the Active Directory to LDAP provider mapping.

    Attributes:
        KRID: TODO: type description here.
        KRFC2307: TODO: type description here.
        KSFU30: TODO: type description here.
        KCENTRIFY: TODO: type description here.
        KFIXED: TODO: type description here.
        KCUSTOMATTRIBUTES: TODO: type description here.
        KLDAPPROVIDER: TODO: type description here.

    """

    KRID = 'kRid'

    KRFC2307 = 'kRfc2307'

    KSFU30 = 'kSfu30'

    KCENTRIFY = 'kCentrify'

    KFIXED = 'kFixed'

    KCUSTOMATTRIBUTES = 'kCustomAttributes'

    KLDAPPROVIDER = 'kLdapProvider'

