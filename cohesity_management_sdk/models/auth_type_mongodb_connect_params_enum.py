# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthTypeMongoDBConnectParamsEnum(object):

    """Implementation of the 'AuthType_MongoDBConnectParams' enum.

    Specifies whether authentication is configured on this MongoDB cluster.
    Specifies the type of an MongoDB source entity.
    'SCRAM'
    'LDAP'
    'NONE'

    Attributes:
        SCRAM: TODO: type description here.
        LDAP: TODO: type description here.
        NONE: TODO: type description here.
        KERBEROS: TODO: type description here.

    """

    SCRAM = 'SCRAM'

    LDAP = 'LDAP'

    NONE = 'NONE'

    KERBEROS = 'KERBEROS'

