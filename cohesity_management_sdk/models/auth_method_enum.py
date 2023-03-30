# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuthMethodEnum(object):

    """Implementation of the 'AuthMethod' enum.
    Specifies the authentication method to be used for API calls. Specifies the
    authentication method to be used for API calls. 'kUseIAMUser' indicates a
    user based authentication. 'kUseIAMRole' indicates a role based
    authentication, used only for AWS CE. 'kUseHelios' indicates a Helios based
    authentication.


    Attributes:
        KUSEIAMUSER: TODO: type description here.
        KUSEIAMROLE: TODO: type description here.
        KUSEHELIOS: TODO: type description here.

    """

    KUSEIAMUSER = 'kUseIAMUser'

    KUSEIAMROLE = 'kUseIAMRole'

    KUSEHELIOS = 'kUseHelios'
