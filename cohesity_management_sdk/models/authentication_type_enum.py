# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthenticationTypeEnum(object):

    """Implementation of the 'AuthenticationType' enum.

    Specifies the authentication scheme for the cluster.
    'kPasswordOnly' indicates the normal cohesity authentication type.
    'kCertificateOnly' indicates that certificate based authentication has
    been enabled and the password based authentication has been turned off.
    'kPasswordAndCertificate' indicates that both the authenticatio schemes
    are required.

    Attributes:
        KPASSWORDONLY: TODO: type description here.
        KCERTIFICATEONLY: TODO: type description here.
        KPASSWORDANDCERTIFICATE: TODO: type description here.

    """

    KPASSWORDONLY = 'kPasswordOnly'

    KCERTIFICATEONLY = 'kCertificateOnly'

    KPASSWORDANDCERTIFICATE = 'kPasswordAndCertificate'

