# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TagEnum(object):

    """Implementation of the 'Tag' enum.

    Specifies use of the nodeport
    kDefault - No specific service.
    kHttp - HTTP server.
    kHttps -  Secure HTTP server.
    kSsh - Secure shell server.

    Attributes:
        KDEFAULT: TODO: type description here.
        KHTTP: TODO: type description here.
        KHTTPS: TODO: type description here.
        KSSH: TODO: type description here.

    """

    KDEFAULT = 'kDefault'

    KHTTP = 'kHttp'

    KHTTPS = 'kHttps'

    KSSH = 'kSsh'

