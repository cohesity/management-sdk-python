# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthenticationTypeUserEnum(object):

    """Implementation of the 'AuthenticationType_User' enum.

    Specifies the authentication type of the user.
    'kAuthLocal' implies authenticated user is a local user.
    'kAuthAd' implies authenticated user is an Active Directory user.
    'kAuthSalesforce' implies authenticated user is a Salesforce user.
    'kAuthGoogle' implies authenticated user is a Google user.
    'kAuthSso' implies authenticated user is an SSO user.

    Attributes:
        KAUTHLOCAL: TODO: type description here.
        KAUTHAD: TODO: type description here.
        KAUTHSALESFORCE: TODO: type description here.
        KAUTHGOOGLE: TODO: type description here.
        KAUTHSSO: TODO: type description here.

    """

    KAUTHLOCAL = 'kAuthLocal'

    KAUTHAD = 'kAuthAd'

    KAUTHSALESFORCE = 'kAuthSalesforce'

    KAUTHGOOGLE = 'kAuthGoogle'

    KAUTHSSO = 'kAuthSso'

