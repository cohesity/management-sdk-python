# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthTypeEnum(object):

    """Implementation of the 'AuthType' enum.

    Specifies the authentication type used while connecting to LDAP servers.
    Authentication level.
    'kAnonymous' indicates LDAP authentication type 'Anonymous'
    'kSimple' indicates LDAP authentication type 'Simple'

    Attributes:
        KANONYMOUS: TODO: type description here.
        KSIMPLE: TODO: type description here.

    """

    KANONYMOUS = 'kAnonymous'

    KSIMPLE = 'kSimple'

