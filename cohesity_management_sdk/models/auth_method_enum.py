# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class AuthMethodEnum(object):

    """Implementation of the 'AuthMethod' enum.

    Specifies the iauth method used for the request
    See the Cohesity online help for the value to specify for this field
    based on the current S3-compatible Vault (External Target) type.
    Specifies the authentication method to be used for API calls.
    'kUseIAMUser' indicates a user based authentication.
    'kUseIAMRole' indicates a role based authentication, used only for AWS CE.

    Attributes:
        KUSEIAMUSER: TODO: type description here.
        KUSEIAMROLE: TODO: type description here.

    """


    KUSEIAMUSER = 'kUseIAMUser'

    KUSEIAMROLE = 'kUseIAMRole'

